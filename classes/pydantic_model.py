from typing import Optional, Dict, Any, List, Literal, Union, Type
from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from pydantic import Field,validator,create_model,root_validator,model_validator,AfterValidator,ValidationInfo
from .element_json_models import *
from typing_extensions import Self,TypeVar,override,Annotated


# class BaseAttributes(BaseModel):
#     regulation_type: Literal["ascenseurs", "mont_charge","chaudiere"]
    
    

# class chauffage_et_climatisation_chaudiere_0(BaseAttributes):

#     regulation_type : Literal["chaudiere" ]= "chaudiere"

#     type_de_control : Optional[Literal["Contrôle de l'efficacité énergétique", 'Entretien annuel', 'Calcul du rendement']] = None
#     date_de_mise_en_service : Optional[str] = None
#     date_de_fabrication_du_bruleur : Optional[str] = None
#     date_de_fabrication_du_generateur : Optional[str] = None
#     marque_du_bruleur : Optional[str] = None
#     puissance_nominale_du_generateur_kw_var : Optional[int] = None
#     numero_de_serie_du_generateur : Optional[str] = None
#     combustible : Optional[Literal['Gazeux', 'Liquide', 'Solide', '']] = None
#     temperature_de_consigne_du_fluide_caloporteur : Optional[int] = None
#     fluide_caloporteur : Optional[str] = None
#     numero_du_bruleur : Optional[str] = None
#     pression_de_consigne_du_fluide_caloporteur_bar_var : Optional[float] = None
#     puissance_du_bruleur : Optional[int] = None
#     marque_du_generateur : Optional[str] = None
#     pci_du_combustible_kwh_nm3_var : Optional[float] = None
#     en_location : Optional[bool] = None
#     status : Optional[Literal['Actif', 'Au chômage', 'Au rebut', 'En stock', 'Au brouillon', '']] = None
#     est_ce_une_chaudiere_de_recuperation_de_gaz_var : Optional[bool] = None
#     avez_vous_un_contrat_de_performance_energetique_sur_cette_installation_var : Optional[bool] = None
#     l_installation_est_elle_classee_dans_la_rubrique_2910_a_et_situe_dans_un_etablissement_soumis_a_declaration_dc_var : Optional[bool] = None
#     somme_des_puissances_nominales_des_chaudieres_en_reseau_en_kw_var : Optional[int] = None
#     la_chaudiere_est_elle_mise_en_reseau_avec_d_autres_chaudieres_dans_un_meme_local_var : Optional[bool] = None
#     type_de_bruleur : Optional[str] = None
#     type_de_generateur : Optional[str] = None
#     type_de_combustible_solide : Optional[str] = None


# class ascenseurs_et_monte_charges_ascenseur_0(BaseAttributes):
#     regulation_type : Literal["ascenseur" ]= "ascenseur"
#     type_de_control : Optional[Literal['Contrôle technique', 'Vérification périodique']] = None
#     date_de_mise_en_service : Optional[str] = None
#     date_de_fabrication : Optional[str] = None
#     modification_importante : Optional[bool] = None
#     societe_de_maintenance : Optional[str] = None
#     fabricant : Optional[str] = None
#     charge_maximale_kg_var : Optional[int] = None
#     parachute : Optional[bool] = None
#     nombre_d_etages : Optional[int] = None
#     machinerie : Optional[Literal['Basse', 'Haute', 'Latérale', 'Latérale basse', 'Latérale haute', 'Sans', '']] = None
#     nombre_de_personnes : Optional[int] = None
#     motorisation : Optional[Literal['Une vitesse', 'Deux vitesses', 'Variateur de fréquence', 'Hydraulique', '']] = None
#     en_location : Optional[bool] = None
#     status : Optional[Literal['Actif', 'Au chômage', 'Au rebut', 'En stock', 'Au brouillon', '']] = None
#     vitesse_nominale_en_m_s_var : Optional[float] = None
#     certification_ce : Optional[bool] = None
#     type_de_traction_electrique : Optional[Literal['Entraînement par adhérence', 'Entraînement attelé', '']] = None
#     type_de_traction_hydraulique : Optional[Literal['Entraînement direct', 'Entraînement indirect', '']] = None
#     type_de_traction : Optional[Literal['Électrique', 'Hydraulique', '']] = None
#     type_d_ouverture : Optional[Literal['Automatique', 'Manuelle', '']] = None
#     type_de_porte : Optional[Literal['Porte Coulissante', 'Porte battante', 'Porte pliante', 'Porte à ouverture centrale', 'Porte à guillotine', '']] = None



# class ascenseurs_et_monte_charges_monte_charge_0(BaseAttributes):
#     regulation_type : Literal["monte_charge" ]= "monte_charge"
#     type_de_control : Optional[Literal['Vérification périodique']] = None
#     date_de_mise_en_service : Optional[str] = None
#     date_de_fabrication : Optional[str] = None
#     certification_ce : Optional[bool] = None
#     nombre_d_etages : Optional[int] = None
#     fabricant : Optional[str] = None
#     charge_maximale_kg_var : Optional[int] = None
#     a_t_il_subi_une_modification_importante_var : Optional[bool] = None
#     parachute : Optional[bool] = None
#     societe_de_maintenance : Optional[str] = None
#     motorisation : Optional[Literal['Une vitesse', 'Deux vitesses', 'Variateur de fréquence', 'Hydraulique', '']] = None
#     machinerie : Optional[Literal['Basse', 'Haute', 'Latérale', 'Sans', '']] = None
#     vitesse_nominale_en_m_s_var : Optional[float] = None
#     en_location : Optional[bool] = None
#     status : Optional[Literal['Actif', 'Au chômage', 'Au rebut', 'En stock', 'Au brouillon', '']] = None
#     type_de_traction_electrique : Optional[Literal['Entraînement par adhérence', 'Entraînement attelé', '']] = None
#     type_de_traction_hydraulique : Optional[Literal['Entraînement direct', 'Entraînement indirect', '']] = None
#     type_de_traction : Optional[Literal['Électrique', 'Hydraulique', '']] = None
#     type_d_ouverture : Optional[Literal['Automatique', 'Manuelle', '']] = None
#     type_de_porte : Optional[Literal['Porte Coulissante', 'Porte battante', 'Porte pliante', 'Porte à ouverture centrale', 'Porte à guillotine', '']] = None
# # def auto_assign_attribut_from_regulation(value: str, info: ValidationInfo) -> str:
#     """Assigne automatiquement attribut basé sur regulation, ignore la valeur d'entrée"""
#     # Récupère la valeur du champ 'regulation'
#     regulation = info.data.get('regulation') if info.data else None
    
#     if regulation == "ascenseurs":
#         return "ascenseurs"  # Force la valeur
#     elif regulation == "mont_charge":
#         return "mont_charge"  # Force la valeur
#     else:
#         # Si regulation inconnue, retourne la valeur originale
#         return value

# # Type annoté qui force l'assignation (comme EvenNumber mais qui transforme)
# AutoAssignedAttribut = Annotated[str, AfterValidator(auto_assign_attribut_from_regulation)]



# FIXED: Make fields optional for OCR step
class Observation(BaseModel):
    element_number: int = Field(description="Index de l'élément concerné")
    n_serie: str = Field(description="Numéro de l'élément concerné, peut etre un string par exemple : 1137/45SHZ568 ")
    element_name: str = Field(description="Nom de l'élément concerné")
    verified_point: Optional[str] = Field(default=None, description="Point vérifié où l'observation a été faite")
    description: str = Field(description="Description courte de l'observation")
    detailed_description: Optional[str] = Field(default=None, description="Description détaillée complète")
    observation_type: Optional[str] = Field(default=None, description="Type d'observation: anomalie, défaut, action, etc.")
    suggested_priority: Optional[str] = Field(default=None, description="Priorité suggérée")
    first_emission_date: Optional[str] = Field(default=None, description="Date d'émission au format YYYY-MM-DD")
    predicted_criticality: bool = Field(default=None, description="Criticité prédite pour la sécurité")
    observation_number: str = Field(description="Numéro de l'observation")
    


class Element(BaseModel,extra="allow" ):
    number: str
    pages: list[int] = Field(description="Toutes les pages ou cet element precis est present")
    inspector: str
    name: str
    n_internal: Optional[str] = Field(description="Numéro d'identification de l'élément")
    factory: str
    building: str
    regulation: Literal["ascenseurs", "mont_charge"]

    # attribut: Union[
    #     ascenseurs_et_monte_charges_ascenseur.ascenseurs_et_monte_charges_ascenseur_0,
    #     ascenseurs_et_monte_charges_monte_charge.ascenseurs_et_monte_charges_monte_charge_0        

    #     # ascenseurs_et_monte_charges_ascenseur_0,
    #     # ascenseurs_et_monte_charges_monte_charge_0  ,
    #     # chauffage_et_climatisation_chaudiere_0
    #      ] 
    # = Field(discriminator="regulation_type")

    
    # test: AutoAssignedAttribut
    

    # @model_validator(mode="after")
    # def set_admin_status(self):

    #     attribut_model_map = {
    #         "ascenseurs": ascenseurs_et_monte_charges_ascenseur.ascenseurs_et_monte_charges_ascenseur_0,
    #         "mont_charge": ascenseurs_et_monte_charges_monte_charge.ascenseurs_et_monte_charges_monte_charge_0
    #     }
    #     self.attribut = attribut_model_map[self.regulation]
    #     print(self)
        
    #     return self
    
    # @override
    # def model_dump(self, include_extra: bool = True, **kwargs):
    #     # On force l'inclusion des champs extra si include_extra=True
    #     data = super().model_dump(**kwargs)
    #     if include_extra and hasattr(self, "is_admin"):
    #         data.update(self.is_admin)
    #     return data

    # def to_dict(self):
    #     return self.model_dump(by_alias=True, include_extra=True)

    # attribut: Optional[Union[
    #     ascenseurs_et_monte_charges_ascenseur.ascenseurs_et_monte_charges_ascenseur_0,
    #     ascenseurs_et_monte_charges_monte_charge.ascenseurs_et_monte_charges_monte_charge_0
    # ]] = None
    

    # @root_validator(pre=True)
    # def set_attribut_by_regulation(cls, values):
        # attribut_model_map = {
        #     "ascenseurs": ascenseurs_et_monte_charges_ascenseur.ascenseurs_et_monte_charges_ascenseur_0,
        #     "mont_charge": ascenseurs_et_monte_charges_monte_charge.ascenseurs_et_monte_charges_monte_charge_0
        # }
        # reg = values.get("regulation")
        # attribut_data = values.get("attribut")
        # if reg in attribut_model_map and attribut_data is not None and not isinstance(attribut_data, attribut_model_map[reg]):
        #     values["attribut"] = attribut_model_map[reg](**attribut_data) if isinstance(attribut_data, dict) else attribut_data
        # return values



    
    # is_admin: bool = Field(
    #     default=False,
    #     description="Défini automatiquement selon le type de régulation",
       
    # )

   


    
    


    

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
    observations: List[Observation]
    # elements: List[Element]





# ---------------------attributs_elements_json_models---------------------



    