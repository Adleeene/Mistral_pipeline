import os
import base64
import json
from mistralai import Mistral
from typing import Optional, Dict, Any, List
from classes.pydantic_model import Report, Element, Document, InterventionControl, Observation
from prompt.general_json import make_general_prompt_no_attributes, make_general_prompt, make_general_prompt_no_attributes_french, make_simple_prompt
from schema_selector import SchemaSelector


class PDFProcessor:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the PDF processor with Mistral API key."""
        self.api_key = api_key or os.getenv("MISTRAL_API_KEY") or "bi78LN9q7kO3MmNlzmzlvDOjjieuod4j"
        self.client = Mistral(api_key=self.api_key)
        self.schema_selector = SchemaSelector()
        # Store schema selection info for console display only
        self.schema_selections = []
    
    def encode_pdf(self, pdf_path: str) -> str:
        """Encode PDF file to base64 string."""
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found at: {pdf_path}")
        
        file_size = os.path.getsize(pdf_path)
        print(f"PDF file size: {file_size / (1024*1024):.2f} MB")
        
        if file_size > 50 * 1024 * 1024:  # 50MB limit
            raise ValueError(f"PDF file too large: {file_size / (1024*1024):.2f} MB. Maximum: 50MB")
        
        try:
            with open(pdf_path, "rb") as pdf_file:
                return base64.b64encode(pdf_file.read()).decode('utf-8')
        except Exception as e:
            raise IOError(f"Failed to read PDF file: {str(e)}")
    
    def process_ocr(self, pdf_path: str) -> Dict[str, Any]:
        """Process PDF with Mistral OCR."""
        print("\n=== OCR PROCESSING ===")

        print("Encoding PDF to base64...")
        base64_pdf = self.encode_pdf(pdf_path)
        print(f"Base64 string length: {len(base64_pdf)} characters")
        
        try:
            print("Sending OCR request to Mistral API...")
            ocr_response = self.client.ocr.process(
                model="mistral-ocr-latest",
                document={
                    "type": "document_url", 
                    "document_url": f"data:application/pdf;base64,{base64_pdf}"
                },
                include_image_base64=True
            )
            print("OCR request completed")
            return ocr_response
        except Exception as e:
            raise RuntimeError(f"OCR processing failed: {str(e)}")
    
    def _analyze_schema_selections(self, report_data: Dict[str, Any]) -> None:
        """Analyze and log schema selections (for console display only - doesn't modify JSON)"""
        print("\n=== SMART SCHEMA ANALYSIS ===")
        
        elements = report_data.get("elements", [])
        if not elements:
            print("No elements found to analyze")
            return
        
        self.schema_selections = []  # Reset for this analysis
        
        for i, element in enumerate(elements):
            equipment_name = element.get("name", "")
            if not equipment_name:
                print(f"Element {i+1}: No name found, skipping")
                continue
                
            print(f"\nAnalyzing element {i+1}: '{equipment_name}'")
            
            # Step 1: Get candidate schemas
            candidate_schemas = self.schema_selector.find_matching_schemas(equipment_name, top_k=5)
            
            if not candidate_schemas:
                print(f"  No candidate schemas found for '{equipment_name}'")
                selection_info = {
                    "element_number": i+1,
                    "equipment_name": equipment_name,
                    "selected_schema": None,
                    "candidate_schemas": [],
                    "confidence": "none"
                }
                self.schema_selections.append(selection_info)
                continue
            
            print(f"  Found {len(candidate_schemas)} candidate schemas:")
            for j, schema in enumerate(candidate_schemas, 1):
                print(f"    {j}. {schema}")
            
            # Step 2: Use LLM to select best schema
            try:
                best_schema = self.schema_selector.select_best_schema_with_llm(
                    equipment_name=equipment_name,
                    element_data=element,
                    candidate_schemas=candidate_schemas,
                    mistral_client=self.client
                )
                
                if best_schema:
                    print(f"  ✓ Selected schema: {best_schema}")
                    confidence = "high"
                else:
                    best_schema = candidate_schemas[0]
                    print(f"  ⚠ Fallback to first candidate: {best_schema}")
                    confidence = "medium"
                    
            except Exception as e:
                print(f"  ✗ Schema selection failed: {e}")
                best_schema = candidate_schemas[0] if candidate_schemas else None
                confidence = "low"
            
            # Store selection info for console display (not in JSON)
            selection_info = {
                "element_number": i+1,
                "equipment_name": equipment_name,
                "selected_schema": best_schema,
                "candidate_schemas": candidate_schemas,
                "confidence": confidence
            }
            self.schema_selections.append(selection_info)
    
    def get_schema_selection_summary(self) -> List[Dict]:
        """Get schema selection summary for console display"""
        return self.schema_selections
    
    def analyze_report(self, ocr_response: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze report from OCR response to produce structured output."""
        print("\n=== REPORT ANALYSIS ===")

        # Build full text with page numbers
        full_text = ""
        for i, page in enumerate(ocr_response.pages):
            full_text += f"Page {i+1}:\n{page.markdown}\n\n"

        print(f"Full text length: {len(full_text)} characters")
        
        # Limit text size
        max_chars = 15000
        if len(full_text) > max_chars:
            full_text = full_text[:max_chars]
            print(f"Document truncated to {max_chars} characters")

        # Use existing system prompt
        system_prompt = make_simple_prompt()

        # Messages for Mistral API
        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": full_text
            }
        ]
        
        try:
            print("Sending analysis request to Mistral API...")
            chat_response = self.client.chat.parse(
                model="mistral-large-latest",
                messages=messages,
                response_format=Report,  # Use existing Report model
                temperature=0,
                max_tokens=3000
            )
            print("✓ Analysis completed")
            
            # Extract JSON from response
            response_content = chat_response.choices[0].message.content
            json_data = json.loads(response_content)
            
            # Analyze schema selections (for console display only)
            self._analyze_schema_selections(json_data)
            
            return json_data
            
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {str(e)}")
            raise RuntimeError(f"Failed to parse JSON response: {str(e)}")
        except Exception as e:
            print(f"Analysis error: {str(e)}")
            raise RuntimeError(f"Report analysis failed: {str(e)}")