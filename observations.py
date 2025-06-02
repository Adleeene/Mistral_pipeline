import os
import json
from typing import List, Dict, Any, Optional
from mistralai import Mistral


class ObservationExtractor:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the observation extractor with Mistral API."""
        self.api_key = api_key or os.getenv("MISTRAL_API_KEY") or "bi78LN9q7kO3MmNlzmzlvDOjjieuod4j"
        self.client = Mistral(api_key=self.api_key)
        self.model = "mistral-large-latest"
    
    def extract_observations(self, report_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Extract observations from the report data using Mistral API.
        
        Args:
            report_data: The structured report data from pipeline
            
        Returns:
            List of observations extracted from the report
        """
        print("\n=== EXTRACTION DES OBSERVATIONS ===")
        
        if not report_data.get("elements"):
            print("Aucun élément trouvé dans le rapport")
            return []
        
        # Get element names for validation
        elements = [element.get("name", "") for element in report_data.get("elements", [])]
        elements = [elem for elem in elements if elem]  # Remove empty names
        
        if not elements:
            print("Aucun nom d'élément valide trouvé")
            return []
        
        # Create prompt
        prompt = self._create_observation_prompt(report_data, elements)
        
        # Extract observations using Mistral API
        try:
            observations = self._extract_with_mistral(prompt, elements, report_data)
            print(f"✓ {len(observations)} observations extraites")
            return observations
        except Exception as e:
            print(f"Erreur lors de l'extraction: {str(e)}")
            return []
    
    def _create_observation_prompt(self, report_data: Dict[str, Any], elements: List[str]) -> str:
        """Create the prompt for observation extraction."""
        
        # Convert report data to formatted text
        report_text = json.dumps(report_data, indent=2, ensure_ascii=False)
        
        prompt = f"""
Vous êtes un expert en analyse de rapports de vérification d'équipements mécaniques.

Analysez le rapport JSON suivant et extrayez TOUTES les observations, anomalies, défectuosités ou actions à entreprendre mentionnées.

RAPPORT À ANALYSER:
{report_text}

ÉLÉMENTS DISPONIBLES:
{', '.join(elements)}

INSTRUCTIONS:
1. Identifiez toutes les observations, anomalies, défectuosités dans le rapport
2. Pour chaque observation trouvée, extrayez les informations selon la structure demandée
3. Associez chaque observation à l'élément concerné parmi la liste fournie
4. Trouvez le nom du contrôle effectué (généralement le type de vérification)
5. Pour detailed_description: Le détail de l'observation ou de l'action à prendre. Le plus souvent, c'est une phrase ou un paragraphe qui explique le problème ou la tâche à faire.
6. Pour suggested_priority: Évaluez la priorité selon l'urgence (Faible/Normale/Élevée/Critique/À l'arrêt)
7. Pour predicted_criticality: Évaluez si c'est critique pour la sécurité des personnes (true/false)

STRUCTURE DE RÉPONSE REQUISE:
{{
  "observations": [
    {{
      "verified_point": "[Le point vérifié ou observé, sur ce quoi porte l'observation ou l'action à prendre]",
      "description": "[Le titre de l'observation ou de l'action à entreprendre. Le plus souvent, c'est le titre de l'observation, quelques mots qui décrivent le problème ou la partie de l'objet]",
      "detailed_description": "[Le détail de l'observation ou de l'action à prendre. Le plus souvent, c'est une phrase ou un paragraphe qui explique le problème ou la tâche à faire]",
      "observation_number": "[Numéro d'observation comme string]",
      "suggested_priority": "[Priorité: Faible/Normale/Élevée/Critique/À l'arrêt]",
      "first_emission_date": "[Date au format YYYY-MM-DD]",
      "predicted_criticality": [true si critique pour la sécurité, false sinon],
      "element_number": [Numéro de l'élément concerné comme integer],
      "element_name": "[Nom exact de l'élément concerné]",
      "controls_name": "[Nom du type de contrôle/vérification effectué]"
    }}
  ]
}}

IMPORTANT:
- Répondez UNIQUEMENT avec un JSON valide
- Si aucune observation n'est trouvée, retournez {{"observations": []}}
- Utilisez exactement les noms d'éléments de la liste fournie
- Pour first_emission_date, utilisez la date de vérification du rapport
- Pour controls_name, identifiez le type de contrôle (ex: "Vérification générale périodique")
"""
        return prompt
    
    def _extract_with_mistral(self, prompt: str, elements: List[str], report_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract observations using Mistral API with structured output."""
        
        max_retries = 3
        
        for attempt in range(max_retries):
            try:
                print(f"Tentative {attempt + 1}/{max_retries} d'extraction...")
                
                # Call Mistral API
                response = self.client.chat.complete(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    response_format={"type": "json_object"},
                    temperature=0.1,
                    max_tokens=3000
                )
                
                # Parse response
                response_content = response.choices[0].message.content
                
                try:
                    # Parse JSON response
                    json_data = json.loads(response_content)
                    
                    # Get observations list
                    observations = json_data.get("observations", [])
                    
                    # Enhance observations with additional fields
                    enhanced_observations = []
                    for obs in observations:
                        enhanced_obs = self._enhance_observation(obs, report_data)
                        if enhanced_obs:  # Only add if valid
                            enhanced_observations.append(enhanced_obs)
                    
                    return enhanced_observations
                    
                except json.JSONDecodeError as e:
                    print(f"Erreur de parsing JSON (tentative {attempt + 1}): {str(e)}")
                    if attempt == max_retries - 1:
                        print("Réponse brute:", response_content[:500])
                    continue
                    
                except Exception as e:
                    print(f"Erreur de validation (tentative {attempt + 1}): {str(e)}")
                    continue
                    
            except Exception as e:
                print(f"Erreur API Mistral (tentative {attempt + 1}): {str(e)}")
                if attempt == max_retries - 1:
                    raise
                continue
        
        print(f"Échec après {max_retries} tentatives")
        return []
    
    def _enhance_observation(self, obs: Dict[str, Any], report_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Enhance observation with additional fields and null values."""
        
        # Find the element to get n_serie
        element_number = obs.get("element_number")
        n_serie = None
        
        if element_number:
            for element in report_data.get("elements", []):
                if element.get("number") == element_number:
                    n_serie = element.get("n_internal")
                    break
        
        # Create enhanced observation with new structure
        enhanced_obs = {
            "verified_point": obs.get("verified_point"),
            "description": obs.get("description"),
            "detailed_description": obs.get("detailed_description"),  # From LLM
            "observation_number": str(obs.get("observation_number", "")),  # Convert to string
            "suggested_priority": obs.get("suggested_priority"),  # From LLM inference
            "first_emission_date": obs.get("first_emission_date"),
            "predicted_criticality": obs.get("predicted_criticality"),  # From LLM inference
            "element_number": obs.get("element_number"),
            "element_name": obs.get("element_name"),
            "n_serie": n_serie,  # From element's n_internal
            "controls_name": obs.get("controls_name")
        }
        
        return enhanced_obs


def enrich_report_with_observations(report_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Main function to enrich report with observations using Mistral API.
    
    Args:
        report_data: The report data dictionary from pipeline
        
    Returns:
        Updated report data with observations
    """
    try:
        extractor = ObservationExtractor()
        observations = extractor.extract_observations(report_data)
        
        # Add observations to report data
        report_data["observations"] = observations
        
        return report_data
        
    except Exception as e:
        print(f"Erreur lors de l'enrichissement avec observations: {str(e)}")
        # Return original data with empty observations if extraction fails
        report_data["observations"] = []
        return report_data


def main():
    """Test function with sample data."""
    # Load sample report data
    try:
        with open("report_analysis.json", "r", encoding="utf-8") as f:
            test_data = json.load(f)
        
        print("Données de test chargées depuis report_analysis.json")
        
    except FileNotFoundError:
        # Fallback sample data
        test_data = {
            "document": {
                "name": "Test Report",
                "date": "2024-03-07"
            },
            "intervention_control": {
                "inspector_name": "Mr TEST",
                "customer_company": "TEST COMPANY"
            },
            "elements": [
                {
                    "number": 1,
                    "name": "Ascenseur",
                    "n_internal": 12345,
                    "factory": "TEST FACTORY",
                    "building": "Bâtiment A"
                }
            ]
        }
        print("Utilisation de données de test par défaut")
    
    # Extract observations
    result = enrich_report_with_observations(test_data)
    
    # Display results
    print("\n=== RÉSULTATS ===")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()