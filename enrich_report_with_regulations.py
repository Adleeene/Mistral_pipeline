import os
import json
from mistralai import Mistral

def query_mistral_for_regulation(element_name):
    """
    Query Mistral API for regulation categorization instead of Ollama
    """
    # Initialize Mistral client
    api_key = os.getenv("MISTRAL_API_KEY") or "bi78LN9q7kO3MmNlzmzlvDOjjieuod4j"
    client = Mistral(api_key=api_key)
    
    # Create prompt for regulation classification
    prompt = f"""
Vous êtes un expert en réglementation des équipements mécaniques.

Classifiez l'équipement suivant selon la réglementation française applicable:

Équipement: {element_name}

Répondez avec UNE SEULE catégorie réglementaire parmi:
- Code du travail
- Code de la construction
- Réglementation ascenseurs
- Réglementation ERP
- Autre

Répondez UNIQUEMENT avec le nom de la catégorie, sans explication.
"""
    
    try:
        response = client.chat.complete(
            model="mistral-large-latest",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=50
        )
        
        regulation = response.choices[0].message.content.strip()
        return regulation
        
    except Exception as e:
        print(f"Erreur lors de la requête Mistral: {e}")
        return None

def enrich_report_with_regulations(report_data):
    """
    Enrich report with regulations using Mistral API instead of Ollama
    """
    print("\n=== ENRICHISSEMENT DES Regulations (Mistral API) ===")
    
    for element in report_data["elements"]:
        element_name = element.get("name", "")
        if not element_name:
            print(f"Élément sans nom trouvé, ignoré")
            continue
            
        print(f"\nAnalyse de l'élément: {element_name}")
        
        # Call Mistral API instead of Ollama
        regulation = query_mistral_for_regulation(element_name)
        
        if regulation:
            regulation = regulation.strip()
            print(f"Catégorie trouvée: {regulation}")
            element["regulation"] = regulation
        else:
            print(f"Impossible de déterminer la catégorie pour {element_name}")
            element["regulation"] = None
    
    return report_data