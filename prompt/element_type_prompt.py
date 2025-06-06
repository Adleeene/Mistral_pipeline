from .prompt_wrap_tags import prompt_wrap_tags
from typing import get_args
from classes.response_classes import (
    ascenseurs_et_monte_charges, chauffage_et_climatisation, echelles_et_echafaudages,
    equipements_de_protection_individuelle, equipements_sous_pression, exposition_des_travailleurs,
    installations_electriques, levage, machines_et_equipements, materiels_d_aspiration,
    metrologie, pmii, portes_et_portails, rampes_d_acces, rayonnages, rayonnements,
    reseaux_de_distribution, securite_incendie, stockage_corrosif, transport_routier
)

# Mapping des noms de réglementation vers leurs classes correspondantes
REGULATION_CLASSES = {
    "ascenseurs_et_monte_charges": ascenseurs_et_monte_charges,
    "chauffage_et_climatisation": chauffage_et_climatisation,
    "echelles_et_echafaudages": echelles_et_echafaudages,
    "equipements_de_protection_individuelle": equipements_de_protection_individuelle,
    "equipements_sous_pression": equipements_sous_pression,
    "exposition_des_travailleurs": exposition_des_travailleurs,
    "installations_electriques": installations_electriques,
    "levage": levage,
    "machines_et_equipements": machines_et_equipements,
    "materiels_d_aspiration": materiels_d_aspiration,
    "metrologie": metrologie,
    "pmii": pmii,
    "portes_et_portails": portes_et_portails,
    "rampes_d_acces": rampes_d_acces,
    "rayonnages": rayonnages,
    "rayonnements": rayonnements,
    "reseaux_de_distribution": reseaux_de_distribution,
    "securite_incendie": securite_incendie,
    "stockage_corrosif": stockage_corrosif,
    "transport_routier": transport_routier
}

def make_element_type_prompt(regulation: str, element_name: str):
    """
    Crée un prompt pour déterminer le type d'élément spécifique en fonction de la réglementation.
    
    Args:
        regulation (str): La catégorie de réglementation (ex: "ascenseurs_et_monte_charges")
        element_name (str): Le nom de l'élément à analyser
    """
    
    # Récupérer la classe correspondante à la réglementation
    regulation_class = REGULATION_CLASSES.get(regulation)
    if not regulation_class:
        raise ValueError(f"Réglementation inconnue: {regulation}")
    
    # Récupérer les options possibles depuis la classe
    # field_info = regulation_class.model_fields["element_type"]
    # options = field_info.annotation.__args__

    annotation = regulation_class.__annotations__["element_type"]
    options = get_args(annotation)


    
    # Créer la liste des options avec leurs descriptions
    options_list = "\n".join([f'   - "{option}"' for option in options])
    
    # Créer le prompt
    prompt = f"""
Tu es un expert en classification d'équipements. Ton objectif est de déterminer le type spécifique d'équipement parmi les options suivantes, en fonction du nom de l'équipement fourni.

### Instructions :
1. Analyse le nom de l'équipement avec attention
2. Choisis UNIQUEMENT parmi les types suivants :
{options_list}

### Nom de l'équipement à analyser :
{element_name}

Réponds UNIQUEMENT avec le type exact, sans commentaire ni explication supplémentaire.
"""
    
    return prompt_wrap_tags(user_prompt=prompt)