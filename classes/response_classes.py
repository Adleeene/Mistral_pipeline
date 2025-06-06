from pydantic import BaseModel , Field
from typing import Literal


class RegulationResult(BaseModel):
    regulation : Literal['ascenseurs_et_monte_charges',
                         'chauffage_et_climatisation',
                         'echelles_et_echafaudages',
                         'equipements_de_protection_individuelle',
                         'equipements_sous_pression',
                         'exposition_des_travailleurs',
                         'installations_electriques',
                         'levage',
                         'machines_et_equipements',
                         'materiels_d_aspiration',
                         'metrologie',
                         'pmii',
                         'portes_et_portails',
                         'rampes_d_acces',
                         'rayonnages',
                         'rayonnements',
                         'reseaux_de_distribution',
                         'securite_incendie',
                         'stockage_corrosif',
                         'transport_routier',
                         ] = Field(description="regulation la plus appropriée pour l'élément")


class ascenseurs_et_monte_charges(BaseModel):
    element_type : Literal[
        "ascenseur",
        "monte_charge"
    ] = Field(description="Type d'élément d'ascenseur ou de monte-charge")

class chauffage_et_climatisation(BaseModel):
    element_type : Literal[
        "chaudiere",
        "tour_aerorefrigerante_tar_var",
        "climatisations_pac_et_fluides_frigorigenes",
        "cheminee"
    ] = Field(description="Type d'élément de chauffage ou de climatisation")

class echelles_et_echafaudages(BaseModel):
    element_type : Literal[
        "echelles",
        "echafaudage"
    ] = Field(description="Type d'élément d'échelle ou d'échafaudage")

class equipements_de_protection_individuelle(BaseModel):
    element_type : Literal[
        "appareils_de_protection_respiratoire",
        "lignes_de_vie",
        "stock_de_cartouche_pour_appareil_respiratoire",
        "travail_en_hauteur",
        "equipements_de_travail",
        "detecteur_portatif",
        "detecteur_fixe",
        "materiel_d_urgence"
    ] = Field(description="Type d'équipement de protection individuelle")

class equipements_sous_pression(BaseModel):
    element_type : Literal[
        "accessoire_de_securite",
        "accessoire_sous_pression",
        "recipient",
        "canalisation",
        "transportable",
        "generateur_de_vapeur",
        "tuyauterie"
    ] = Field(description="Type d'élément d'équipement sous pression")

class exposition_des_travailleurs(BaseModel):
    element_type : Literal[
        "bruit",
        "risque_chimique",
        "vibration_mecanique",
        "eclairage"
    ] = Field(description="Type d'élément d'exposition des travailleurs")

class installations_electriques(BaseModel):
    element_type : Literal[
        "installation_classique",
        "foudre",
        "eclairage_de_securite"
    ] = Field(description="Type d'élément d'installation électrique")

class levage(BaseModel):
    element_type : Literal[
        "accessoire",
        "appareil"
    ] = Field(description="Type d'élément de levage")

class machines_et_equipements(BaseModel):
    element_type : Literal[
        "machines_industrielles",
        "outillage"
    ] = Field(description="Type d'élément de machine ou d'équipement")

class materiels_d_aspiration(BaseModel):
    element_type : Literal[
        "hotte_aspirante",
        "sorbonne_de_laboratoire",
        "paillasse_aspirante",
        "armoire_ventilee",
        "locaux_a_pollution_non_specifiques",
        "installation_a_pollution_specifique"
    ] = Field(description="Type d'élément de matériel d'aspiration")

class metrologie(BaseModel):
    element_type : Literal[
        "appareil_de_mesure",
        "instrument_de_pesage"
    ] = Field(description="Type d'élément de métrologie")

class pmii(BaseModel):
    element_type : Literal[
        "rack_de_tuyauterie",
        "cuvette_de_retention",
        "massif_de_reservoir",
        "caniveaux_en_beton",
        "fosses_humides",
        "accessoire_de_securite",
        "mmri",
        "reservoir_de_stockage",
        "reservoir_cryogenique",
        "bac_de_stockage",
        "tuyauterie",
        "capacite"
    ] = Field(description="Type d'élément de PMII")

class portes_et_portails(BaseModel):
    element_type : Literal[
        "portes",
        "portails",
        "tourniquet"
    ] = Field(description="Type d'élément de porte ou de portail")

class rampes_d_acces(BaseModel):
    element_type : Literal[
        "quai_niveleur"
    ] = Field(description="Type d'élément de rampe d'accès")

class rayonnages(BaseModel):
    element_type : Literal[
        "rayonnage_metallique"
    ] = Field(description="Type d'élément de rayonnage")

class rayonnements(BaseModel):
    element_type : Literal[
        "ionisant",
        "non_ionisant",
        "instrument_de_radioprotection"
    ] = Field(description="Type d'élément de rayonnement")

class reseaux_de_distribution(BaseModel):
    element_type : Literal[
        "systeme_anti_pollution",
        "eau_a_consommation_humaine",
        "rejet_aqueux",
        "eau_chaude_sanitaire"
    ] = Field(description="Type d'élément de réseau de distribution")

class securite_incendie(BaseModel):
    element_type : Literal[
        "porte_coupe_feu",
        "installation_d_extinction_a_gaz",
        "sprinkler",
        "extincteur",
        "dispositif_de_desenfumage",
        "robinet_incendie_arme_ria_var",
        "installation_de_detection_automatique",
        "installation_de_point_d_eau_incendie",
        "signaux_de_securite"
    ] = Field(description="Type d'élément de sécurité incendie")

class stockage_corrosif(BaseModel):
    element_type : Literal[
        "cuve",
        "bassin",
        "reservoir"
    ] = Field(description="Type d'élément de stockage corrosif")

class transport_routier(BaseModel):
    element_type : Literal[
        "vehicule_leger",
        "vehicule_lourd"
    ] = Field(description="Type d'élément de transport routier")

