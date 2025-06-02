from typing import Optional, Dict, Any, List, Literal, Union, Type
from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from pydantic import Field,validator,create_model
from .element_json_models import *




# Define Pydantic models for the desired JSON structure
class Element(BaseModel):
    number: int
    page: int
    inspector: str
    name: str
    #N_Identification: Dict[str, int]  # Assuming string keys and values; change to Dict[str, int] if number_internal is an integer
    n_internal: Optional[int] # Assuming string keys and values; change to Dict[str, int] if number_internal is an integer
    factory: str
    building: str 
    regulation: Literal[
        "ascenseurs", 
        "monte_charge",

        ]
    #----------------------------------ATTRIBUTES----------------------------------

    attribut: Union[
        ascenseurs_et_monte_charges_ascenseur.ascenseurs_et_monte_charges_ascenseur_0,
        ascenseurs_et_monte_charges_monte_charge.ascenseurs_et_monte_charges_monte_charge_0
    ]


    
# class ElementBase(BaseModel):
#     number: int
#     page: int
#     inspector: str
#     name: str
#     n_internal: Optional[int] = Field(None, alias="N_Identification")
#     factory: str
#     building: str 
#     regulation: Literal["ascenseurs", "monte_charge"]

# class Element(ElementBase):
#     attribut: Dict = Field(..., description="Attributs obligatoires")

#     @classmethod
#     def create_element_model(cls, regulation_type: str) -> Type[BaseModel]:
#         attribut_model_map = {
#             "ascenseurs": ascenseurs_et_monte_charges_ascenseur.ascenseurs_et_monte_charges_ascenseur_0,
#             "monte_charge": ascenseurs_et_monte_charges_monte_charge.ascenseurs_et_monte_charges_monte_charge_0
#         }
        
#         if regulation_type not in attribut_model_map:
#             raise ValueError(f"Type de régulation non supporté: {regulation_type}")
        
#         return create_model(
#             f"Element{regulation_type.capitalize()}",
#             __base__=Element,
#             attribut=(attribut_model_map[regulation_type], Field(...))
#         )
    
    # attribut: Union[
    #     transport_routier_vehicule_lourd.transport_routier_vehicule_lourd_0,
    #     transport_routier_vehicule_leger.transport_routier_vehicule_leger_0,
    #     stockage_corrosif_reservoir.stockage_corrosif_reservoir_0,
    #     stockage_corrosif_cuve.stockage_corrosif_cuve_0,
    #     stockage_corrosif_bassin.stockage_corrosif_bassin_0,
    #     securite_incendie_sprinkler.securite_incendie_sprinkler_0,
    #     securite_incendie_signaux_de_securite.securite_incendie_signaux_de_securite_0,
    #     securite_incendie_robinet_incendie_arme_ria_var.securite_incendie_robinet_incendie_arme_ria_var_0,
    #     securite_incendie_porte_coupe_feu.securite_incendie_porte_coupe_feu_0,
    #     securite_incendie_installation_de_point_d_eau_incendie.securite_incendie_installation_de_point_d_eau_incendie_0,
    #     securite_incendie_installation_de_detection_automatique.securite_incendie_installation_de_detection_automatique_0,
    #     securite_incendie_installation_d_extinction_a_gaz.securite_incendie_installation_d_extinction_a_gaz_0,
    #     securite_incendie_extincteur.securite_incendie_extincteur_0,
    #     securite_incendie_dispositif_de_desenfumage.securite_incendie_dispositif_de_desenfumage_0,
    #     reseaux_de_distribution_systeme_anti_pollution.reseaux_de_distribution_systeme_anti_pollution_0,
    #     reseaux_de_distribution_rejet_aqueux.reseaux_de_distribution_rejet_aqueux_0,
    #     reseaux_de_distribution_eau_chaude_sanitaire.reseaux_de_distribution_eau_chaude_sanitaire_0,
    #     reseaux_de_distribution_eau_a_consommation_humaine.reseaux_de_distribution_eau_a_consommation_humaine_0,
    #     rayonnements_non_ionisant.rayonnements_non_ionisant_0,
    #     rayonnements_ionisant.rayonnements_ionisant_0,
    #     rayonnements_instrument_de_radioprotection.rayonnements_instrument_de_radioprotection_0,
    #     rayonnages_rayonnage_metallique.rayonnages_rayonnage_metallique_0,
    #     rampes_d_acces_quai_niveleur.rampes_d_acces_quai_niveleur_0,
    #     portes_et_portails_portes.portes_et_portails_portes_0,
    #     portes_et_portails_tourniquet.portes_et_portails_tourniquet_0,
    #     portes_et_portails_portails.portes_et_portails_portails_0,
    #     pmii_tuyauterie.pmii_tuyauterie_0,
    #     pmii_reservoir_de_stockage.pmii_reservoir_de_stockage_0,
    #     pmii_reservoir_cryogenique.pmii_reservoir_cryogenique_0,
    #     pmii_rack_de_tuyauterie.pmii_rack_de_tuyauterie_0,
    #     pmii_mmri.pmii_mmri_0,
    #     pmii_massif_de_reservoir.pmii_massif_de_reservoir_0,
    #     pmii_fosses_humides.pmii_fosses_humides_0,
    #     pmii_cuvette_de_retention.pmii_cuvette_de_retention_0,
    #     pmii_capacite.pmii_capacite_0,
    #     pmii_caniveaux_en_beton.pmii_caniveaux_en_beton_0,
    #     pmii_bac_de_stockage.pmii_bac_de_stockage_0,
    #     pmii_accessoire_de_securite.pmii_accessoire_de_securite_0,
    #     metrologie_instrument_de_pesage.metrologie_instrument_de_pesage_0,
    #     metrologie_appareil_de_mesure.metrologie_appareil_de_mesure_0,
    #     materiels_d_aspiration_sorbonne_de_laboratoire.materiels_d_aspiration_sorbonne_de_laboratoire_0,
    #     materiels_d_aspiration_paillasse_aspirante.materiels_d_aspiration_paillasse_aspirante_0,
    #     materiels_d_aspiration_locaux_a_pollution_non_specifiques.materiels_d_aspiration_locaux_a_pollution_non_specifiques_0,
    #     materiels_d_aspiration_installation_a_pollution_specifique.materiels_d_aspiration_installation_a_pollution_specifique_0,
    #     materiels_d_aspiration_hotte_aspirante.materiels_d_aspiration_hotte_aspirante_0,
    #     materiels_d_aspiration_armoire_ventilee.materiels_d_aspiration_armoire_ventilee_0,
    #     machines_et_equipements_outillage.machines_et_equipements_outillage_0,
    #     machines_et_equipements_machines_industrielles.machines_et_equipements_machines_industrielles_0,
    #     levage_appareil.levage_appareil_0,
    #     levage_accessoire.levage_accessoire_0,
    #     installations_electriques_installation_classique.installations_electriques_installation_classique_0,
    #     installations_electriques_foudre.installations_electriques_foudre_0,
    #     installations_electriques_eclairage_de_securite.installations_electriques_eclairage_de_securite_0,
    #     exposition_des_travailleurs_risque_chimique.exposition_des_travailleurs_risque_chimique_0,
    #     exposition_des_travailleurs_eclairage.exposition_des_travailleurs_eclairage_0,
    #     exposition_des_travailleurs_bruit.exposition_des_travailleurs_bruit_0,
    #     exposition_des_travailleurs_vibration_mecanique.exposition_des_travailleurs_vibration_mecanique_0,
    #     equipements_sous_pression_tuyauterie.equipements_sous_pression_tuyauterie_0,
    #     equipements_sous_pression_transportable.equipements_sous_pression_transportable_0,
    #     equipements_sous_pression_recipient.equipements_sous_pression_recipient_0,
    #     equipements_sous_pression_generateur_de_vapeur.equipements_sous_pression_generateur_de_vapeur_0,
    #     equipements_sous_pression_canalisation.equipements_sous_pression_canalisation_0,
    #     equipements_sous_pression_accessoire_sous_pression.equipements_sous_pression_accessoire_sous_pression_0,
    #     equipements_sous_pression_accessoire_de_securite.equipements_sous_pression_accessoire_de_securite_0,
    #     equipements_de_protection_individuelle_travail_en_hauteur.equipements_de_protection_individuelle_travail_en_hauteur_0,
    #     equipements_de_protection_individuelle_materiel_d_urgence.equipements_de_protection_individuelle_materiel_d_urgence_0,
    #     equipements_de_protection_individuelle_lignes_de_vie.equipements_de_protection_individuelle_lignes_de_vie_0,
    #     equipements_de_protection_individuelle_equipements_de_travail.equipements_de_protection_individuelle_equipements_de_travail_0,
    #     equipements_de_protection_individuelle_detecteur_portatif.equipements_de_protection_individuelle_detecteur_portatif_0,
    #     equipements_de_protection_individuelle_detecteur_fixe.equipements_de_protection_individuelle_detecteur_fixe_0,
    #     equipements_de_protection_individuelle_appareils_de_protection_respiratoire.equipements_de_protection_individuelle_appareils_de_protection_respiratoire_0,
    #     equipements_de_protection_individuelle_stock_de_cartouche_pour_appareil_respiratoire.equipements_de_protection_individuelle_stock_de_cartouche_pour_appareil_respiratoire_0,
    #     echelles_et_echafaudages_echelles.echelles_et_echafaudages_echelles_0,
    #     echelles_et_echafaudages_echafaudage.echelles_et_echafaudages_echafaudage_0,
    #     chauffage_et_climatisation_tour_aerorefrigerante_tar_var.chauffage_et_climatisation_tour_aerorefrigerante_tar_var_0,
    #     chauffage_et_climatisation_climatisations_pac_et_fluides_frigorigenes.chauffage_et_climatisation_climatisations_pac_et_fluides_frigorigenes_0,
    #     chauffage_et_climatisation_cheminee.chauffage_et_climatisation_cheminee_0,
    #     chauffage_et_climatisation_chaudiere.chauffage_et_climatisation_chaudiere_0,
    #     ascenseurs_et_monte_charges_monte_charge.ascenseurs_et_monte_charges_monte_charge_0,
    #     ascenseurs_et_monte_charges_ascenseur.ascenseurs_et_monte_charges_ascenseur_0
    # ] = Field(description="Les attributs de l'élément, la classe d'attributs à utiliser dependra du nom de d'élément")


class Document(BaseModel):
    name: str
    number: int
    date: str  # Format YYYY-MM-DD
    pages_number: int

class InterventionControl(BaseModel):
    name: str
    start_date: str  # Format YYYY-MM-DD
    end_date: str  # Format YYYY-MM-DD
    inspector_company: str
    inspector_agency: str
    inspector_name: str
    customer_company: str
    customer_adress: str
    customer_factory: str
    elements_number: int
    tasks_number: int

class Report(BaseModel):
    document: Document
    intervention_control: InterventionControl
    elements: List[Element]