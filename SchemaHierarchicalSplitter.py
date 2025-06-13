from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional, Union, Literal
import json
from mistralai import Mistral
import os
import base64
from typing import Optional, Dict, Any
from prompt.general_json import make_simple_prompt
from Mistral_OCR import PDFProcessor
from helper_function.enrich_report_with_regulations import enrich_report_with_regulations
from helper_function.enrich_report_with_type_element import enrich_report_with_type_element
# attribut_model_map
import time

# class Page:
#     def __init__(self, markdown):
#         self.markdown = markdown

# class OCRResponse:
#     def __init__(self, pages):
#         self.pages = pages


# # Utilisation des différentes stratégies
def main_extraction_strategies():

    # Start timing
    start_time = time.time()
    
    # Stratégie 1
    pdf_processor = PDFProcessor()
    message = pdf_processor.process_ocr("/Users/adlenemeraga/Documents/GitHub/OCR_mistral/test_PDF/apave_13_1obs.pdf")
    # message = pdf_processor.process_ocr("/Users/adlenemeraga/Documents/GitHub/OCR_mistral/test_PDF/apave_13.pdf")
    

    # # Lecture du fichier texte
    # with open("extracted_text.txt", 'r', encoding='utf-8') as f:
    #     text_content = f.read()
    # # Création d'un objet OCRResponse avec le texte lu
    # message = OCRResponse([Page(text_content)])

    # print(f"Waiting 60 seconds before processing the FIRST element...")
    # time.sleep(60)


    report_data = pdf_processor.analyze_report(message)


    print("\nRésultat formaté :")
    print(json.dumps(report_data, indent=2, ensure_ascii=False, sort_keys=False))
    print("--------------------------------")

        # Enrich report with regulations
    report_data = enrich_report_with_regulations(report_data)

    # Enrich report with element type
    report_data = enrich_report_with_type_element(report_data)
    

    # on va parcourir les elements et on va extraire les pages ou cet element est present pour ajouter les attributs
    print("\n=== ENRICHISSEMENT DES ATTRIBUTS POUR CHAQUE ELEMENT ===")
    
    print(f"Waiting 60 seconds before processing the FIRST element...")
    time.sleep(60)

    for i, element in enumerate(report_data["elements"]):
        element_pages = element["pages"]
        # Récupérer le texte des pages concernées
        pages_text = ""
        for page_num in element_pages:
            # Les index de pages sont probablement 1-based dans report_data, mais 0-based dans ocr_response.pages
            page_index = page_num - 1
            if 0 <= page_index < len(message.pages):
                pages_text += f"Page {page_num}:\n{message.pages[page_index].markdown}\n\n"
                
        
        result = pdf_processor.analyze_attributes(pages_text,element["element_type"], element["n_internal"],element["name"],element["number"] )
        element["attribut"] = result

        # # Add 30 second delay between each analyze_attributes call, except for the last element
        # if i < len(report_data["elements"]) - 1:
        #     print(f"Waiting 60 seconds before processing next element...")
        #     time.sleep(60)



    # Calculate execution time
    execution_time = time.time() - start_time
    report_data["total_time"] = round(execution_time, 2)

    

    print("\nRésultat final apres ajout des attributs:")
    print(json.dumps(report_data, indent=2, ensure_ascii=False, sort_keys=False))
    print("--------------------------------")

    # Convert null to None in report_data
    def convert_null_to_none(obj):
        if isinstance(obj, dict):
            return {k: convert_null_to_none(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_null_to_none(item) for item in obj]
        elif obj is None or obj == "null":
            return None
        return obj

    report_data = convert_null_to_none(report_data)
        

     # Save to file
    output_file = "report_analysis.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=2, ensure_ascii=False)
    print(f"✓ Results saved to {output_file}")


        # print("pages_text pour l'element : ",element['number']," : ",pages_text)



        

  


if __name__ == "__main__":
    main_extraction_strategies()