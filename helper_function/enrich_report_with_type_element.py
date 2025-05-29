from regulation_match import query_ollama
from prompt.element_type_prompt import make_element_type_prompt

def enrich_report_with_type_element(report_data):

    if not report_data or "elements" not in report_data:
        print("Données de rapport invalides ou vides")
        return report_data
    
    print("\n=== ENRICHISSEMENT DES TYPES D'ÉLÉMENTS ===")
    
    for element in report_data["elements"]:
        element_name = element.get("name", "")
        regulation = element.get("regulation")
        
        if not element_name:
            print(f"Élément sans nom trouvé, ignoré")
            continue
            
        if not regulation:
            print(f"Élément {element_name} sans Régulation, ignoré")
            continue
            
        print(f"\nAnalyse de l'élément: {element_name}")
        print(f"Régulation: {regulation}")
        
        # Création du prompt pour la catégorisation
        prompt = make_element_type_prompt(regulation, element_name)
        
        # Appel à Ollama pour obtenir le type d'élément
        element_type = query_ollama(prompt)
        
        if element_type:
            # Nettoyage de la réponse (enlever les espaces et retours à la ligne)
            element_type = element_type.strip()
            print(f"Type d'élément trouvé: {element_type}")
            # Ajout du type d'élément
            element["element_type"] = element_type
        else:
            print(f"Impossible de déterminer le type d'élément pour {element_name}")
            element["element_type"] = None
    
    return report_data 