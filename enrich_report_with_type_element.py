import os
import json
from mistralai import Mistral

def query_mistral_for_element_type(regulation, element_name):
    """
    Query Mistral API for element type classification instead of Ollama
    """
    # Initialize Mistral client
    api_key = os.getenv("MISTRAL_API_KEY") or "bi78LN9q7kO3MmNlzmzlvDOjjieuod4j"
    client = Mistral(api_key=api_key)
    
    # Create prompt for element type classification
    prompt = f"""
Vous êtes un expert en classification d'équipements mécaniques.

Déterminez le type spécifique de cet équipement:

Équipement: {element_name}
Réglementation: {regulation}

Répondez avec UN SEUL type d'équipement parmi:
- Ascenseur électrique
- Ascenseur hydraulique
- Monte-charge
- Élévateur
- Escalier mécanique
- Trottoir roulant
- Autre équipement

Répondez UNIQUEMENT avec le type d'équipement, sans explication.
"""
    
    try:
        response = client.chat.complete(
            model="mistral-large-latest",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=50
        )
        
        element_type = response.choices[0].message.content.strip()
        return element_type
        
    except Exception as e:
        print(f"Erreur lors de la requête Mistral: {e}")
        return None

def enrich_report_with_type_element(report_data):
    """
    Enrich report with element types using Mistral API instead of Ollama
    """
    if not report_data or "elements" not in report_data:
        print("Données de rapport invalides ou vides")
        return report_data
    
    print("\n=== ENRICHISSEMENT DES TYPES D'ÉLÉMENTS (Mistral API) ===")
    
    for element in report_data["elements"]:
        element_name = element.get("name", "")
        regulation = element.get("regulation")
        
        if not element_name:
            print(f"Élément sans nom trouvé, ignoré")
            continue
            
        if not regulation:
            print(f"Élément {element_name} sans Régulation, assignation d'une réglementation par défaut")
            regulation = "Code du travail"  # Default regulation
            
        print(f"\nAnalyse de l'élément: {element_name}")
        print(f"Régulation: {regulation}")
        
        # Call Mistral API instead of Ollama
        element_type = query_mistral_for_element_type(regulation, element_name)
        
        if element_type:
            element_type = element_type.strip()
            print(f"Type d'élément trouvé: {element_type}")
            element["element_type"] = element_type
        else:
            print(f"Impossible de déterminer le type d'élément pour {element_name}")
            element["element_type"] = None
    
    return report_data