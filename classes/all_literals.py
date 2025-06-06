from typing import Literal
from pydantic import BaseModel

class AllLiterals(BaseModel):
    element_type: Literal[
        # Régulations
        "ascenseurs", "mont_charge", "chaudiere",
        
        # Types d'éléments - Ascenseurs
        "ascenseur", "monte_charge",
        
        # Types d'éléments - Échelles
        "echelles", "echafaudage",
        
        # Types d'éléments - EPI
        "appareils_de_protection_respiratoire",
        "lignes_de_vie",
        "stock_de_cartouche_pour_appareil_respiratoire",
        "travail_en_hauteur",
        "equipements_de_travail",
        "detecteur_portatif",
        "detecteur_fixe",
        "materiel_d_urgence",
        
        # Types d'éléments - ESP
        "accessoire_de_securite",
        "accessoire_sous_pression",
        "recipient",
        "canalisation",
        "transportable",
        "generateur_de_vapeur",
        "tuyauterie",
        
        # Types d'éléments - Exposition
        "bruit",
        "risque_chimique",
        "vibration_mecanique",
        "eclairage",
        
        # Types d'éléments - Électrique
        "installation_classique",
        "foudre",
        "eclairage_de_securite",
        
        # Types d'éléments - Levage
        "accessoire", "appareil",
        
        # Types d'éléments - Machines
        "machines_industrielles", "outillage",
        
        # Types d'éléments - Métrologie
        "appareil_de_mesure", "instrument_de_pesage",
        
        # Types d'éléments - PMII
        "rack_de_tuyauterie",
        "cuvette_de_retention",
        "massif_de_reservoir",
        "caniveaux_en_beton",
        "fosses_humides",
        "mmri",
        "reservoir_de_stockage",
        "reservoir_cryogenique",
        "bac_de_stockage",
        "capacite",
        
        # Types d'éléments - Portes
        "portes", "portails", "tourniquet",
        
        # Types d'éléments - Rampes
        "quai_niveleur",
        
        # Types d'éléments - Rayonnages
        "rayonnage_metallique",
        
        # Types d'éléments - Sécurité
        "porte_coupe_feu",
        "installation_d_extinction_a_gaz",
        "sprinkler",
        "extincteur",
        "dispositif_de_desenfumage",
        "robinet_incendie_arme_ria_var",
        "installation_de_detection_automatique",
        "installation_de_point_d_eau_incendie",
        "signaux_de_securite",
        
        # Types d'éléments - Stockage
        "cuve", "bassin", "reservoir",
        
        # Types d'éléments - Transport
        "vehicule_leger", "vehicule_lourd",
        
        # Types de contrôles
        "Vérification périodique",
        "Vérification générale périodique",
        "Vérification semestrielle",
        "Vérification annuelle",
        "Vérification",
        "Remise en conformité",
        
        # Types spécifiques aux équipements
        "Monogaz",
        "Multigaz",
        "Dispositif d'Alarme pour Travailleur Isolé (DATI)",
        "Autre",
        "",
        "Simple",
        "Articulé",
        "A crochets",
        "A ventouses",
        "Lyre",
        "Droite",
        "Classique",
        "En S",
        "Câble",
        "Chaîne",
        "Textile",
        "Aimant",
        "Anneau",
        "Clé de levage",
        "Crochet",
        "Elingue",
        "Griffe",
        "Lève palette",
        "Manille",
        "Palonnier",
        "Pince",
        "Poulie de puits",
        "Ventouse",
        "Douche de sécurité",
        "Rince-œil",
        "Combiné douche et rince-œil",
        "Lavage d'urgence",
        "Défibrillateur",
        "Trousse de secours",
        "Gilet de sauvetage",
        "Lumineux",
        "Acoustique",
        "Intermittent",
        "Continu",
        "Type 2a",
        "Type 2b",
        "Type 3",
        "Type 4",
        "Actif",
        "Au chômage",
        "Au rebut",
        "En stock",
        "Au brouillon",
        "Modulaire",
        "Centralisée",
        "Directionnelle",
        "Gaz inhibiteurs",
        "Gaz inertes",
        "CSPRS",
        "Disque de rupture",
        "DSDCS",
        "Pompe",
        "Pressostat de sécurité",
        "Soupape",
        "SRMCR",
        "Arrête-flamme",
        "Anti-déflagration en bout de ligne",
        "Anti-déflagration en ligne",
        "Anti-détonation",
        "Mono ou bidirectionnel",
        "Longe",
        "Sangle",
        "Mousqueton",
        "Harnais",
        "Descendeur",
        "Absorbeur",
        "Poulie",
        "Perche",
        "Corde",
        "Antichute",
        "Bloqueur",
        "Stop-chute",
        "Porte-outils"
    ] 