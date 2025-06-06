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


def split_report_extraction(self, messages: List[Dict[str, str]]):
        """Extraction en plusieurs étapes pour Report"""
        

        # Étape 2: Extraire les éléments (sans attributs complexes)
        elements_basic = self._extract_elements_basic(messages)


        return elements_basic


# Utilisation des différentes stratégies
def main_extraction_strategies():
    """Exemple d'utilisation des stratégies de division"""

    # Stratégie 1
    pdf_processor = PDFProcessor()
    message = pdf_processor.process_ocr("/Users/adlenemeraga/Documents/GitHub/OCR_mistral/test_PDF/apave_13.pdf")

    report_data = pdf_processor.analyze_report(message)

    print("\nRésultat formaté :")
    print(json.dumps(report_data, indent=2, ensure_ascii=False, sort_keys=False))
    print("--------------------------------")

        # Enrich report with regulations
    report_data = enrich_report_with_regulations(report_data)

    # Enrich report with element type
    report_data = enrich_report_with_type_element(report_data)
    
    
    # on va parcourir les elements et on va extraire les pages ou cet element est present
    for element in report_data["elements"]:
        element_pages = element["pages"]
        # Récupérer le texte des pages concernées
        pages_text = ""
        for page_num in element_pages:
            # Les index de pages sont probablement 1-based dans report_data, mais 0-based dans ocr_response.pages
            page_index = page_num - 1
            if 0 <= page_index < len(message.pages):
                pages_text += f"Page {page_num}:\n{message.pages[page_index].markdown}\n\n"
                
        
        result = pdf_processor.analyze_attributes(report_data,pages_text,element["element_type"], element["n_internal"])
        element["attribut"] = result

        # print("resultat pour l'element ",element["n_internal"],":",result)


    

    
    # print("type of report_data : ",type(report_data))



        # print("pages_text pour l'element ",element['number']," :\n ",pages_text)
        # print("--------------------------------")
    print("\nRésultat final apres ajout des attributs:")
    print(json.dumps(report_data, indent=2, ensure_ascii=False, sort_keys=False))
    print("--------------------------------")


        # print("pages_text pour l'element : ",element['number']," : ",pages_text)



        

  


if __name__ == "__main__":
    main_extraction_strategies()