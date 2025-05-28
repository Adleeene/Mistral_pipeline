from .prompt_wrap_tags import prompt_wrap_tags



def make_regulation_prompt(element_name: str):
    """
    Compose the prompt for the regulation model (model 2 part 1).

    Parameters
    ----------
    text : str
        The text to be analysed.
    model_type : str
        The type of model for which the prompt is created.

    Returns
    -------
    str
        The complete prompt for the regulation model.


    If the text contains acronyms, the prompt will include the meanings of these acronyms.
    """

    prompt = f"""
Tu es un expert en catégorisation d'équipements. Ton objectif est de sélectionner la catégorie **la plus précise** et appropriée à partir des options ci-dessous, en fonction du nom de l'équipement fourni. Réponds uniquement par le nom exact de la catégorie, sans commentaire ou explication supplémentaire.

### Instructions :
1. **Analyse chaque catégorie** et ses exemples avec attention.
2. Si le nom de l'équipement contient un mot ou une expression qui correspond à un exemple d'une catégorie, choisis cette catégorie.
3. **Assure-toi que la catégorie choisie est la plus spécifique possible** et qu'elle correspond bien aux exemples fournis.
4. **Évite les catégories trop générales** si une correspondance exacte est disponible.

### Catégories disponibles avec exemples :
ascenseurs_et_monte_charges : ascenseur, monte-charge.
chauffage_et_climatisation : chaudière, radiateur, climatiseur, ventilateur, extracteur, filtre, gaine, conduit, thermostat, vanne.
echelles_et_echafaudages : échelle, échafaudage.
equipements_de_protection_individuelle : appareil de protection respiratoire, ligne de vie, détecteur portatif, matériel pour travail en hauteur.
equipements_sous_pression : réservoir, tuyauterie, vanne.
exposition_des_travailleurs : dispositif et conditions relatives à l'exposition des travailleurs à des risques.
installations_electriques : installation et équipement électrique.
levage : chariot élévateur, chariot de manutention, nacelle, palan, élingue, plateforme élévatrice, chariot élévateur à conducteur porté, gerbeur, élévateur de personnes, grue, transpalette.
machines_et_equipements : presse, massicot, centrifugeuse, compacteur, perceuse, poste à souder, touret.
materiels_d_aspiration : aspirateur industriel, système de dépoussiérage, hotte aspirante.
metrologie : équipement et dispositif de métrologie, ou si le nom se termine par 'mètre'.
pmii : plan de modernisation des installations industrielles.
portes_et_portails : porte, portail de tout type, rideau métallique.
rampes_d_acces : rampe d'accès, quai niveleur.
rayonnages : étagère, rack, palettier, cantilever.
rayonnements : équipement ou dispositif lié aux rayonnements.
reseaux_de_distribution : réseau d'eau, système anti-pollution, rejet aqueux, eau chaude sanitaire.
securite_incendie : extincteur, alarme, détecteur de fumée, porte coupe-feu, issue de secours, plan d'évacuation.
stockage_corrosif : cuve, bassin, réservoir.
transport_routier : équipement ou dispositif lié au transport routier.

### Nom de l'équipement :
***
{element_name.lower()}
***

Sélectionne toujours la **catégorie la plus précise** en fonction des exemples, et évite les catégories trop générales si une correspondance exacte est trouvée.
"""
    


    return prompt_wrap_tags(user_prompt=prompt)




# Tu es un expert en catégorisation d'équipements. Ton objectif est de sélectionner la catégorie **la plus précise** et appropriée à partir des options ci-dessous, en fonction du nom de l'équipement fourni. Réponds uniquement par le nom exact de la catégorie, sans commentaire ou explication supplémentaire.

# ### Instructions :
# 1. **Analyse chaque catégorie** et ses exemples avec attention.
# 2. Si le nom de l'équipement contient un mot ou une expression qui correspond à un exemple d'une catégorie, choisis cette catégorie.
# 3. **Assure-toi que la catégorie choisie est la plus spécifique possible** et qu'elle correspond bien aux exemples fournis.
# 4. **Évite les catégories trop générales** si une correspondance exacte est disponible.

# ### Catégories disponibles avec exemples :
# ascenseurs_et_monte_charges : ascenseur, monte-charge.
# chauffage_et_climatisation : chaudière, radiateur, climatiseur, ventilateur, extracteur, filtre, gaine, conduit, thermostat, vanne.
# echelles_et_echafaudages : échelle, échafaudage.
# equipements_de_protection_individuelle : appareil de protection respiratoire, ligne de vie, détecteur portatif, matériel pour travail en hauteur.
# equipements_sous_pression : réservoir, tuyauterie, vanne.
# exposition_des_travailleurs : dispositif et conditions relatives à l'exposition des travailleurs à des risques.
# installations_electriques : installation et équipement électrique.
# levage : chariot élévateur, chariot de manutention, nacelle, palan, élingue, plateforme élévatrice, chariot élévateur à conducteur porté, gerbeur, élévateur de personnes, grue, transpalette.
# machines_et_equipements : presse, massicot, centrifugeuse, compacteur, perceuse, poste à souder, touret.
# materiels_d_aspiration : aspirateur industriel, système de dépoussiérage, hotte aspirante.
# metrologie : équipement et dispositif de métrologie, ou si le nom se termine par 'mètre'.
# pmii : plan de modernisation des installations industrielles.
# portes_et_portails : porte, portail de tout type, rideau métallique.
# rampes_d_acces : rampe d'accès, quai niveleur.
# rayonnages : étagère, rack, palettier, cantilever.
# rayonnements : équipement ou dispositif lié aux rayonnements.
# reseaux_de_distribution : réseau d'eau, système anti-pollution, rejet aqueux, eau chaude sanitaire.
# securite_incendie : extincteur, alarme, détecteur de fumée, porte coupe-feu, issue de secours, plan d'évacuation.
# stockage_corrosif : cuve, bassin, réservoir.
# transport_routier : équipement ou dispositif lié au transport routier.

# ### Nom de l'équipement :