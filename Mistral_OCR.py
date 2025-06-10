import os
import base64
import json
from mistralai import Mistral
from typing import Optional, Dict, Any
from classes.pydantic_model import Report
from prompt.general_json import make_general_prompt_no_attributes, make_general_prompt, make_general_prompt_no_attributes_french, make_simple_prompt
from ollama import chat

from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional, Union, Literal
from classes.element_json_models import * 



class PDFProcessor:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the PDF processor with Mistral API key."""
        self.api_key = api_key or os.getenv("MISTRAL_API_KEY") or "bi78LN9q7kO3MmNlzmzlvDOjjieuod4j"
        self.client = Mistral(api_key=self.api_key)
    
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
    
    def analyze_report(self, ocr_response: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze report from OCR response to produce structured output."""
        print("\n=== REPORT ANALYSIS ===")

        # Build full text with page numbers
        full_text = ""
        for i, page in enumerate(ocr_response.pages):
            full_text += f"Page {i+1}:\n{page.markdown}\n\n"

        print(full_text)
        
        # Limit text size
        max_chars = 15000
        print(f"Full text length: {len(full_text)} characters") 
        if len(full_text) > max_chars:
            full_text = full_text[:max_chars]
            print(f"Document truncated to {max_chars} characters")


        #--------------------------------SYSTEM PROMPT--------------------------------
        
        system_prompt = make_simple_prompt()

        #--------------------------------MISTRAL LARGE API--------------------------------
        
        #Define messages for Mistral API
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
                #response_format={"type": "json_object"},
                response_format=Report,
                #je crois que schema dynamique  n'est pas supporté par l'api , faut que j'essaye avec les fonctions tools 

                temperature=0,
                max_tokens=4096
            )
            print("Analysis request completed")
            
            # Extract JSON from response
            response_content = chat_response.choices[0].message.content

            # print("type(response_content) : ",type(response_content))

            json_data = json.loads(response_content)

        #--------------------------------OLLAMA MISTRAL SMALL 24B--------------------------------

        # try : 
        #     response = chat(
        #     messages=[
        #         {
        #             'role': 'system',
        #             'content': system_prompt,
        #         },
        #         {
        #             'role': 'user',
        #             'content': full_text,
        #         }
        #         ],
        #         model='mistral-small:24b',
        #         format=Report.model_json_schema(),
        #         options={'temperature': 0},  # Set temperature to 0 for more deterministic output
        #     )

        #     Rapport = Report.model_validate_json(response.message.content)
        #     json_data = Rapport.model_dump_json()
            
        #     # Convertir la chaîne JSON en dictionnaire Python
        #     json_data = json.loads(json_data)


        #----------------------------POST PROCESSING----------------------------------------------
            
            # print("-----------------json_data-----------------")
            # print(json_data)
            # print("-----------------json_data-----------------")

            # Validate with Pydantic
            #report = Report.model_validate(json_data)


            # Convert to dictionary
           # return report.model_dump()
            return json_data
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {str(e)}")
            raise RuntimeError(f"Failed to parse JSON response: {str(e)}")
        except Exception as e:
            print(f"Analysis error: {str(e)}")
            raise RuntimeError(f"Report analysis failed: {str(e)}")
        


        
    def analyze_attributes(self,report_data: Dict[str, Any], pages_text_specific_element: str,element_type: str,n_internal: int) -> Dict[str, Any]:
        """Analyze the attributes of each element by an adequate response format"""

        attribut_model_map = {
            # Ascenseurs et monte-charges
            "ascenseur": ascenseurs_et_monte_charges_ascenseur.ascenseurs_et_monte_charges_ascenseur_0,
            "monte_charge": ascenseurs_et_monte_charges_monte_charge.ascenseurs_et_monte_charges_monte_charge_0,
            
            # Chauffage et climatisation
            "chaudiere": chauffage_et_climatisation_chaudiere.chauffage_et_climatisation_chaudiere_0,
            "tour_aerorefrigerante_tar_var": chauffage_et_climatisation_tour_aerorefrigerante_tar_var.chauffage_et_climatisation_tour_aerorefrigerante_tar_var_0,
            "climatisations_pac_et_fluides_frigorigenes": chauffage_et_climatisation_climatisations_pac_et_fluides_frigorigenes.chauffage_et_climatisation_climatisations_pac_et_fluides_frigorigenes_0,
            "cheminee": chauffage_et_climatisation_cheminee.chauffage_et_climatisation_cheminee_0,
            
            # Échelles et échafaudages
            "echelles": echelles_et_echafaudages_echelles.echelles_et_echafaudages_echelles_0,
            "echafaudage": echelles_et_echafaudages_echafaudage.echelles_et_echafaudages_echafaudage_0,
            
            # Équipements de protection individuelle
            "appareils_de_protection_respiratoire": equipements_de_protection_individuelle_appareils_de_protection_respiratoire.equipements_de_protection_individuelle_appareils_de_protection_respiratoire_0,
            "lignes_de_vie": equipements_de_protection_individuelle_lignes_de_vie.equipements_de_protection_individuelle_lignes_de_vie_0,
            "stock_de_cartouche_pour_appareil_respiratoire": equipements_de_protection_individuelle_stock_de_cartouche_pour_appareil_respiratoire.equipements_de_protection_individuelle_stock_de_cartouche_pour_appareil_respiratoire_0,
            "travail_en_hauteur": equipements_de_protection_individuelle_travail_en_hauteur.equipements_de_protection_individuelle_travail_en_hauteur_0,
            "equipements_de_travail": equipements_de_protection_individuelle_equipements_de_travail.equipements_de_protection_individuelle_equipements_de_travail_0,
            "detecteur_portatif": equipements_de_protection_individuelle_detecteur_portatif.equipements_de_protection_individuelle_detecteur_portatif_0,
            "detecteur_fixe": equipements_de_protection_individuelle_detecteur_fixe.equipements_de_protection_individuelle_detecteur_fixe_0,
            "materiel_d_urgence": equipements_de_protection_individuelle_materiel_d_urgence.equipements_de_protection_individuelle_materiel_d_urgence_0,
            
            # Équipements sous pression
            "accessoire_de_securite": equipements_sous_pression_accessoire_de_securite.equipements_sous_pression_accessoire_de_securite_0,
            "accessoire_sous_pression": equipements_sous_pression_accessoire_sous_pression.equipements_sous_pression_accessoire_sous_pression_0,
            "recipient": equipements_sous_pression_recipient.equipements_sous_pression_recipient_0,
            "canalisation": equipements_sous_pression_canalisation.equipements_sous_pression_canalisation_0,
            "transportable": equipements_sous_pression_transportable.equipements_sous_pression_transportable_0,
            "generateur_de_vapeur": equipements_sous_pression_generateur_de_vapeur.equipements_sous_pression_generateur_de_vapeur_0,
            "tuyauterie": equipements_sous_pression_tuyauterie.equipements_sous_pression_tuyauterie_0,
            
            # Exposition des travailleurs
            "bruit": exposition_des_travailleurs_bruit.exposition_des_travailleurs_bruit_0,
            "risque_chimique": exposition_des_travailleurs_risque_chimique.exposition_des_travailleurs_risque_chimique_0,
            "vibration_mecanique": exposition_des_travailleurs_vibration_mecanique.exposition_des_travailleurs_vibration_mecanique_0,
            "eclairage": exposition_des_travailleurs_eclairage.exposition_des_travailleurs_eclairage_0,
            
            # Installations électriques
            "installation_classique": installations_electriques_installation_classique.installations_electriques_installation_classique_0,
            "foudre": installations_electriques_foudre.installations_electriques_foudre_0,
            "eclairage_de_securite": installations_electriques_eclairage_de_securite.installations_electriques_eclairage_de_securite_0,
            
            # Levage
            "accessoire": levage_accessoire.levage_accessoire_0,
            "appareil": levage_appareil.levage_appareil_0,
            
            # Machines et équipements
            "machines_industrielles": machines_et_equipements_machines_industrielles.machines_et_equipements_machines_industrielles_0,
            "outillage": machines_et_equipements_outillage.machines_et_equipements_outillage_0,
            
            # Matériels d'aspiration
            "hotte_aspirante": materiels_d_aspiration_hotte_aspirante.materiels_d_aspiration_hotte_aspirante_0,
            "sorbonne_de_laboratoire": materiels_d_aspiration_sorbonne_de_laboratoire.materiels_d_aspiration_sorbonne_de_laboratoire_0,
            "paillasse_aspirante": materiels_d_aspiration_paillasse_aspirante.materiels_d_aspiration_paillasse_aspirante_0,
            "armoire_ventilee": materiels_d_aspiration_armoire_ventilee.materiels_d_aspiration_armoire_ventilee_0,
            "locaux_a_pollution_non_specifiques": materiels_d_aspiration_locaux_a_pollution_non_specifiques.materiels_d_aspiration_locaux_a_pollution_non_specifiques_0,
            "installation_a_pollution_specifique": materiels_d_aspiration_installation_a_pollution_specifique.materiels_d_aspiration_installation_a_pollution_specifique_0,
            
            # Métrologie
            "appareil_de_mesure": metrologie_appareil_de_mesure.metrologie_appareil_de_mesure_0,
            "instrument_de_pesage": metrologie_instrument_de_pesage.metrologie_instrument_de_pesage_0,
            
            # PMII
            "rack_de_tuyauterie": pmii_rack_de_tuyauterie.pmii_rack_de_tuyauterie_0,
            "cuvette_de_retention": pmii_cuvette_de_retention.pmii_cuvette_de_retention_0,
            "massif_de_reservoir": pmii_massif_de_reservoir.pmii_massif_de_reservoir_0,
            "caniveaux_en_beton": pmii_caniveaux_en_beton.pmii_caniveaux_en_beton_0,
            "fosses_humides": pmii_fosses_humides.pmii_fosses_humides_0,
            "accessoire_de_securite": pmii_accessoire_de_securite.pmii_accessoire_de_securite_0,
            "mmri": pmii_mmri.pmii_mmri_0,
            "reservoir_de_stockage": pmii_reservoir_de_stockage.pmii_reservoir_de_stockage_0,
            "reservoir_cryogenique": pmii_reservoir_cryogenique.pmii_reservoir_cryogenique_0,
            "bac_de_stockage": pmii_bac_de_stockage.pmii_bac_de_stockage_0,
            "tuyauterie": pmii_tuyauterie.pmii_tuyauterie_0,
            "capacite": pmii_capacite.pmii_capacite_0,
            
            # Portes et portails
            "portes": portes_et_portails_portes.portes_et_portails_portes_0,
            "portails": portes_et_portails_portails.portes_et_portails_portails_0,
            "tourniquet": portes_et_portails_tourniquet.portes_et_portails_tourniquet_0,
            
            # Rampes d'accès
            "quai_niveleur": rampes_d_acces_quai_niveleur.rampes_d_acces_quai_niveleur_0,
            
            # Rayonnages
            "rayonnage_metallique": rayonnages_rayonnage_metallique.rayonnages_rayonnage_metallique_0,
            
            # Rayonnements
            "ionisant": rayonnements_ionisant.rayonnements_ionisant_0,
            "non_ionisant": rayonnements_non_ionisant.rayonnements_non_ionisant_0,
            "instrument_de_radioprotection": rayonnements_instrument_de_radioprotection.rayonnements_instrument_de_radioprotection_0,
            
            # Réseaux de distribution
            "systeme_anti_pollution": reseaux_de_distribution_systeme_anti_pollution.reseaux_de_distribution_systeme_anti_pollution_0,
            "eau_a_consommation_humaine": reseaux_de_distribution_eau_a_consommation_humaine.reseaux_de_distribution_eau_a_consommation_humaine_0,
            "rejet_aqueux": reseaux_de_distribution_rejet_aqueux.reseaux_de_distribution_rejet_aqueux_0,
            "eau_chaude_sanitaire": reseaux_de_distribution_eau_chaude_sanitaire.reseaux_de_distribution_eau_chaude_sanitaire_0,
            
            # Sécurité incendie
            "porte_coupe_feu": securite_incendie_porte_coupe_feu.securite_incendie_porte_coupe_feu_0,
            "installation_d_extinction_a_gaz": securite_incendie_installation_d_extinction_a_gaz.securite_incendie_installation_d_extinction_a_gaz_0,
            "sprinkler": securite_incendie_sprinkler.securite_incendie_sprinkler_0,
            "extincteur": securite_incendie_extincteur.securite_incendie_extincteur_0,
            "dispositif_de_desenfumage": securite_incendie_dispositif_de_desenfumage.securite_incendie_dispositif_de_desenfumage_0,
            "robinet_incendie_arme_ria_var": securite_incendie_robinet_incendie_arme_ria_var.securite_incendie_robinet_incendie_arme_ria_var_0,
            "installation_de_detection_automatique": securite_incendie_installation_de_detection_automatique.securite_incendie_installation_de_detection_automatique_0,
            "installation_de_point_d_eau_incendie": securite_incendie_installation_de_point_d_eau_incendie.securite_incendie_installation_de_point_d_eau_incendie_0,
            "signaux_de_securite": securite_incendie_signaux_de_securite.securite_incendie_signaux_de_securite_0,
            
            # Stockage corrosif
            "cuve": stockage_corrosif_cuve.stockage_corrosif_cuve_0,
            "bassin": stockage_corrosif_bassin.stockage_corrosif_bassin_0,
            "reservoir": stockage_corrosif_reservoir.stockage_corrosif_reservoir_0,
            
            # Transport routier
            "vehicule_leger": transport_routier_vehicule_leger.transport_routier_vehicule_leger_0,
            "vehicule_lourd": transport_routier_vehicule_lourd.transport_routier_vehicule_lourd_0
        }

        if element_type not in attribut_model_map:
            raise ValueError(f"Invalid element_type: {element_type}")

        attributes_class = attribut_model_map[element_type]

        #--------------------------------SYSTEM PROMPT--------------------------------
        
        system_prompt = make_simple_prompt()

        #--------------------------------MISTRAL LARGE API--------------------------------
        
        #Define messages for Mistral API
        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": pages_text_specific_element
            }
        ]
        
        try:
            print("Sending analysis request to Mistral API...")
            chat_response = self.client.chat.parse(
                model="mistral-large-latest",
                messages=messages,
                response_format=attributes_class,
                temperature=0,
                max_tokens=3000
            )
            print("Analysis request completed")
            
            # Extract JSON from response
            response_content = chat_response.choices[0].message.content
            json_data = json.loads(response_content)
            return json_data

            # Add the response content to the report_data for the specific element
            # for element in report_data.get("elements", []):
            #     if element.get("element_type") == n_internal:
            #         element.update(json_data)
            #         break

        # try : 
        #     response = chat(
        #     messages=[
        #         {
        #             'role': 'system',
        #             'content': system_prompt,
        #         },
        #         {
        #             'role': 'user',
        #             'content': full_text,
        #         }
        #         ],
        #         model='mistral-small:24b',
        #         format=Report.model_json_schema(),
        #         options={'temperature': 0},  # Set temperature to 0 for more deterministic output
        #     )

        #     Rapport = Report.model_validate_json(response.message.content)
        #     json_data = Rapport.model_dump_json()
            
        #     # Convertir la chaîne JSON en dictionnaire Python
        #     json_data = json.loads(json_data)


        #----------------------------POST PROCESSING----------------------------------------------
            
            # print("-----------------json_data-----------------")
            # print(json_data)
            # print("-----------------json_data-----------------")

            # Validate with Pydantic
            #report = Report.model_validate(json_data)


            
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {str(e)}")
            raise RuntimeError(f"Failed to parse JSON response: {str(e)}")
        except Exception as e:
            print(f"Analysis error: {str(e)}")
            raise RuntimeError(f"Report analysis failed: {str(e)}")

