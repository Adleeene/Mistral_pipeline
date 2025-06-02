import os
import importlib
import re
import sys
from typing import Dict, List, Type, Union
from difflib import SequenceMatcher
from pydantic import BaseModel

class SchemaSelector:
    def __init__(self):
        self.all_schemas = self._get_available_schemas()
    
    def _get_available_schemas(self) -> Dict[str, Type[BaseModel]]:
        """Dynamically discover all available attribute schemas"""
        schemas = {}
        
        # Correct path: classes/element_json_models
        element_models_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'classes', 'element_json_models')
        
        if element_models_path not in sys.path:
            sys.path.insert(0, element_models_path)
        
        # Also add the classes directory for imports
        classes_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'classes')
        if classes_path not in sys.path:
            sys.path.insert(0, classes_path)
        
        # Scan the element_json_models directory
        if not os.path.exists(element_models_path):
            print(f"ERROR: {element_models_path} directory not found")
            return schemas
            
        for file in os.listdir(element_models_path):
            if file.endswith(".py") and not file.startswith("__"):
                module_name = file[:-3]  # Remove .py
                try:
                    # Import from element_json_models
                    module = importlib.import_module(f"element_json_models.{module_name}")
                    
                    # Get all classes ending with _0, _1, etc.
                    for attr_name in dir(module):
                        if re.match(r".*_\d+$", attr_name):  # Ends with underscore + number
                            attr_class = getattr(module, attr_name)
                            # Make sure it's actually a BaseModel class
                            if isinstance(attr_class, type) and issubclass(attr_class, BaseModel):
                                schemas[attr_name] = attr_class
                                
                except ImportError as e:
                    print(f"Could not import {module_name}: {e}")
                except Exception as e:
                    print(f"Error processing {module_name}: {e}")
                    
        print(f"Found {len(schemas)} available schemas")
        return schemas
    
    def find_matching_schemas(self, equipment_name: str, top_k: int = 5) -> List[str]:
        """Find schemas that best match the equipment name"""
        
        equipment_name_clean = equipment_name.lower().strip()
        # Remove numbers and extra words like "1", "2", "ABC" etc.
        equipment_base = re.sub(r'\s+\d+.*$', '', equipment_name_clean)  # "Ascenseur 1" -> "Ascenseur"
        equipment_base = re.sub(r'\s+[A-Z]+.*$', '', equipment_base, flags=re.IGNORECASE)  # Remove codes
        
        candidates = []
        
        for schema_name in self.all_schemas.keys():
            # Extract keywords from schema name
            schema_keywords = re.findall(r'[a-z]+', schema_name.lower())
            schema_text = " ".join(schema_keywords)
            
            # Calculate similarity scores
            similarity_scores = []
            
            # 1. Direct substring match with base name (highest priority)
            if equipment_base in schema_text:
                similarity_scores.append(0.95)
            
            # 2. Direct substring match with full name
            if equipment_name_clean in schema_text:
                similarity_scores.append(0.9)
            
            # 3. Fuzzy string similarity with base name
            fuzzy_score = SequenceMatcher(None, equipment_base, schema_text).ratio()
            similarity_scores.append(fuzzy_score * 0.8)  # Weight down fuzzy matching
            
            # 4. Individual word matches
            equipment_words = equipment_base.split()
            word_matches = sum(1 for word in equipment_words if word in schema_keywords)
            word_score = word_matches / len(equipment_words) if equipment_words else 0
            similarity_scores.append(word_score * 0.7)  # Weight down word matching
            
            # Final score (take the best)
            final_score = max(similarity_scores) if similarity_scores else 0
            
            candidates.append((schema_name, final_score))
        
        # Sort by score and return top K
        candidates.sort(key=lambda x: x[1], reverse=True)
        return [name for name, score in candidates[:top_k] if score > 0.1]  # Lower threshold
    
    def select_best_schema_with_llm(self, equipment_name: str, element_data: Dict, candidate_schemas: List[str], mistral_client) -> str:
        """Use LLM to select the best schema from candidates using full equipment context"""
        
        if not candidate_schemas:
            return None
            
        if len(candidate_schemas) == 1:
            return candidate_schemas[0]
        
        # Build detailed element context
        element_context = f"""
Equipment Name: {equipment_name}
Factory: {element_data.get('factory', 'N/A')}
Building: {element_data.get('building', 'N/A')}
Inspector: {element_data.get('inspector', 'N/A')}
Page: {element_data.get('page', 'N/A')}
"""
        
        # Add any existing attributes if available
        existing_attrs = element_data.get('attribut', {})
        if existing_attrs:
            element_context += f"Existing attributes: {existing_attrs}\n"
        
        # Build schema options with human-readable descriptions
        schema_descriptions = []
        for i, schema_name in enumerate(candidate_schemas):
            # Convert schema name to human-readable description
            parts = schema_name.split('_')
            readable_parts = []
            
            for part in parts[:-1]:  # Skip the final number
                if part in ['et', 'de', 'du', 'des', 'a', 'au']:
                    readable_parts.append(part)
                else:
                    readable_parts.append(part.capitalize())
            
            readable = ' '.join(readable_parts)
            schema_descriptions.append(f"{i+1}. {schema_name} ({readable})")
        
        prompt = f"""Given this equipment from an inspection report:

{element_context}

Select the most appropriate schema from these {len(candidate_schemas)} options:
{chr(10).join(schema_descriptions)}

Consider the equipment's specific type, function, and context. Choose the schema that best matches the equipment category.

Return ONLY the number (1-{len(candidate_schemas)}) of your choice."""
        
        try:
            # Simple LLM call for schema selection
            response = mistral_client.chat.complete(
                model="mistral-large-latest",
                messages=[
                    {
                        "role": "system", 
                        "content": "You are an expert in industrial equipment classification. Select the most appropriate schema based on equipment type and context."
                    },
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ],
                temperature=0,
                max_tokens=10
            )
            
            # Parse the response
            choice_text = response.choices[0].message.content.strip()
            
            # Extract number from response
            import re
            numbers = re.findall(r'\d+', choice_text)
            if numbers:
                choice_num = int(numbers[0])
                if 1 <= choice_num <= len(candidate_schemas):
                    selected_schema = candidate_schemas[choice_num - 1]
                    print(f"LLM selected schema {choice_num}: {selected_schema} for '{equipment_name}'")
                    return selected_schema
            
            # Fallback to first candidate
            print(f"Could not parse LLM choice '{choice_text}', using first candidate for '{equipment_name}'")
            return candidate_schemas[0]
            
        except Exception as e:
            print(f"LLM schema selection failed for '{equipment_name}': {e}")
            # Fallback to first candidate
            return candidate_schemas[0]
    
    def get_best_schema_for_equipment(self, equipment_name: str) -> str:
        """Get the best schema for a given equipment name (fallback method)"""
        matching_schemas = self.find_matching_schemas(equipment_name, top_k=1)
        return matching_schemas[0] if matching_schemas else None
    
    def get_schema_classes_for_names(self, equipment_names: List[str]) -> List[Type[BaseModel]]:
        """Get the actual schema classes for equipment names"""
        schema_classes = []
        for name in equipment_names:
            schema_name = self.get_best_schema_for_equipment(name)
            if schema_name and schema_name in self.all_schemas:
                schema_classes.append(self.all_schemas[schema_name])
        return schema_classes

# Test the schema selector
if __name__ == "__main__":
    selector = SchemaSelector()
    
    # Test with some equipment names
    test_names = ["Ascenseur 1", "Extincteur ABC", "Chaudière", "Monte charge 2"]
    for name in test_names:
        candidates = selector.find_matching_schemas(name, top_k=5)
        print(f"\n{name} -> Top 5 candidates:")
        for i, candidate in enumerate(candidates, 1):
            print(f"  {i}. {candidate}")