from regulation_match import query_ollama
from prompt.regulation_prompt import make_regulation_prompt

def enrich_report_with_regulations(report_data):
    
    print("\n=== ENRICHISSEMENT DES Regulations ===")
    
    for element in report_data["elements"]:
        element_name = element.get("name", "")
        if not element_name:
            print(f"Élément sans nom trouvé, ignoré")
            continue
            
        print(f"\nAnalyse de l'élément: {element_name}")
        
        # Création du prompt pour la catégorisation
        prompt = make_regulation_prompt(element_name)
        
        # Appel à Ollama pour obtenir la catégorie
        regulation = query_ollama(prompt)
        
        if regulation:
            # Nettoyage de la réponse (enlever les espaces et retours à la ligne)
            regulation = regulation.strip()
            print(f"Catégorie trouvée: {regulation}")
            # Ajout de la catégorie à l'élément
            element["regulation"] = regulation
        else:
            print(f"Impossible de déterminer la catégorie pour {element_name}")
            element["regulation"] = None
    
    return report_data 