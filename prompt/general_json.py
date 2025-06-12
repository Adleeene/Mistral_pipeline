from .prompt_wrap_tags import prompt_wrap_tags



def make_general_prompt():

    prompt = (
                    "Tu es un expert en analyse de documents techniques. Extrait les détails du document, "
                    "les informations de contrôle d'intervention et la liste des éléments selon la structure suivante :\n"
                    "{\n"
                    "  \"document\": {\"name\": \"string\", \"number\": integer, \"date\": \"YYYY-MM-DD\", \"pages_number\": integer},\n"
                    "  \"intervention_control\": {\"name\": \"string\", \"start_date\": \"YYYY-MM-DD\", \"end_date\": \"YYYY-MM-DD\", "
                    "\"inspector_company\": \"string\", \"inspector_agency\": \"string\", \"inspector_name\": \"string\", "
                    "\"customer_company\": \"string\", \"customer_adress\": \"string\", \"customer_factory\": \"string\", "
                    "\"elements_number\": integer, \"tasks_number\": integer},\n"
                    "  \"elements\": [{\n"
                    "    \"number\": integer,\n"
                    "    \"page\": integer,\n"
                    "    \"inspector\": \"string\",\n"
                    "    \"name\": \"string\",\n"
                    "    \"n_internal\": integer,\n"
                    "    \"factory\": \"string\",\n"
                    "    \"building\": \"string\",\n"
                    "    \"type_de_traction_electrique\": {\"choices\": [\"Entraînement par adhérence\", \"Entraînement attelé\"]},\n"
                    "    \"modification_importante\": {\"choices\": [\"Oui\", \"Non\"]},\n"
                    "    \"societe_de_maintenance\": \"string\",\n"
                    "    \"type_de_traction_hydraulique\": {\"choices\": [\"Entraînement direct\", \"Entraînement indirect\"]},\n"
                    "    \"fabricant\": \"string\",\n"
                    "    \"charge_maximale_kg_var\": integer,\n"
                    "    \"date_de_fabrication\": \"YYYY-MM-DD\",\n"
                    "    \"date_de_mise_en_service\": \"YYYY-MM-DD\",\n"
                    "    \"parachute\": {\"choices\": [\"Oui\", \"Non\"]},\n"
                    "    \"nombre_d_etages\": integer,\n"
                    "    \"machinerie\": {\"choices\": [\"Basse\", \"Haute\", \"Latérale\", \"Latérale basse\", \"Latérale haute\", \"Sans\"]},\n"
                    "    \"nombre_de_personnes\": integer,\n"
                    "    \"motorisation\": {\"choices\": [\"Une vitesse\", \"Deux vitesses\", \"Variateur de fréquence\", \"Hydraulique\"]},\n"
                    "    \"type_de_traction\": {\"choices\": [\"Électrique\", \"Hydraulique\"]},\n"
                    "    \"type_d_ouverture\": {\"choices\": [\"Automatique\", \"Manuelle\"]},\n"
                    "    \"type_de_porte\": {\"choices\": [\"Porte Coulissante\", \"Porte battante\", \"Porte pliante\", \"Porte à ouverture centrale\", \"Porte à guillotine\"]},\n"
                    "    \"en_location\": {\"choices\": [\"Oui\", \"Non\"]},\n"
                    "    \"status\": {\"choices\": [\"Actif\", \"Au chômage\", \"Au rebut\", \"En stock\", \"Au brouillon\"]},\n"
                    "    \"vitesse_nominale_en_m_s_var\": decimal,\n"
                    "    \"certification_ce\": {\"choices\": [\"Oui\", \"Non\"]},\n"
                    "    \"type_de_control\": {\"choices\": [\"Contrôle technique\", \"Vérification périodique\"]}\n"
                    "  }]\n"
                    "}\n"
                    "Retourne UNIQUEMENT un objet JSON valide correspondant à cette structure. N'inclue aucun texte supplémentaire. et Conserve l'ordre dans lequel les éléments apparaissent dans le document."
                )
    


    return prompt_wrap_tags(user_prompt=prompt)


def make_general_prompt_no_attributes():

    prompt = (
                    "Tu es un expert en analyse de documents techniques. Extrait les détails du document, "
                    "les informations de contrôle d'intervention et la liste des éléments selon la structure suivante :\n"
                    "{\n"
                    "  \"document\": {\"name\": \"string\", \"number\": integer, \"date\": \"YYYY-MM-DD\", \"pages_number\": integer},\n"
                    "  \"intervention_control\": {\"name\": \"string\", \"start_date\": \"YYYY-MM-DD\", \"end_date\": \"YYYY-MM-DD\", "
                    "\"inspector_company\": \"string\", \"inspector_agency\": \"string\", \"inspector_name\": \"string\", "
                    "\"customer_company\": \"string\", \"customer_adress\": \"string\", \"customer_factory\": \"string\", "
                    "\"elements_number\": integer, \"tasks_number\": integer},\n"
                    "  \"elements\": [{\n"
                    "    \"number\": integer,\n"
                    "    \"page\": integer,\n"
                    "    \"inspector\": \"string\",\n"
                    "    \"name\": \"string\",\n"
                    "    \"n_internal\": integer,\n"
                    "    \"factory\": \"string\",\n"
                    "    \"building\": \"string\",\n"
                    "  }]\n"
                    "}\n"
                    "Retourne UNIQUEMENT un objet JSON valide correspondant à cette structure. N'inclue aucun texte supplémentaire."
                )
    


    return prompt_wrap_tags(user_prompt=prompt)


# NAME OF KEY IN FRENCH 

def make_general_prompt1():

    prompt = (
                    "Tu es un expert en analyse de documents techniques. Extrait les détails du document, "
                    "les informations de contrôle d'intervention et la liste des éléments selon la structure suivante :\n"
                    "{\n"
                    "  \"document\": {\n"
                    "    \"name\": \"string\",\n"
                    "    \"number\": integer,\n"
                    "    \"date\": \"YYYY-MM-DD\",\n"
                    "    \"pages_number\": integer\n"
                    "  },\n"
                    "  \"intervention_control\": {\n"
                    "    \"name\": \"string\",\n"
                    "    \"start_date\": \"YYYY-MM-DD\",\n"
                    "    \"end_date\": \"YYYY-MM-DD\",\n"
                    "    \"inspector_company\": \"string\",\n"
                    "    \"inspector_agency\": \"string\",\n"
                    "    \"inspector_name\": \"string\",\n"
                    "    \"customer_company\": \"string\",\n"
                    "    \"customer_adress\": \"string\",\n"
                    "    \"customer_factory\": \"string\",\n"
                    "    \"elements_number\": integer,\n"
                    "    \"tasks_number\": integer\n"
                    "  },\n"
                    "  \"elements\": [\n"
                    "    {\n"
                    "      \"number\": string,\n"
                    "      \"pages\": [integer],\n"
                    "      \"inspector\": \"string\",\n"
                    "      \"name\": \"string\",\n"
                    "      \"n_internal\": string,\n"
                    "      \"factory\": \"string\",\n"
                    "      \"building\": \"string\"\n"
                    "    }\n"
                    "  ],\n"
                    "  \"observations\": [\n"
                    "    {\n"
                    "      \"element_number\": integer,\n"
                    "      \"n_serie\": \"string\",\n"
                    "      \"element_name\": \"string\",\n"
                    "      \"verified_point\": \"string\",\n"
                    "      \"description\": \"string\",\n"
                    "      \"detailed_description\": \"string\",\n"
                    "      \"observation_type\": \"string\",\n"
                    "      \"suggested_priority\": \"string\",\n"
                    "      \"first_emission_date\": \"string\",\n"
                    "      \"predicted_criticality\": boolean,\n"
                    "      \"observation_number\": \"string\"\n"
                    "    }\n"
                    "  ]\n"
                    "}\n"
                    "Retourne UNIQUEMENT un objet JSON valide correspondant à cette structure. N'inclue aucun texte supplémentaire."
                )
    


    return prompt_wrap_tags(user_prompt=prompt)


def make_simple_prompt():

    prompt = (
                    "Tu es un expert en analyse de documents techniques. Extrait les informations du document " 
                    "Fait bien attention, si deux éléments on le même nom, ce n'est pas forcément qu'ils sont identiques, si ils "
                    "ont un numéro de série différent, ils sont différent et il faut prendre en compte les deux éléments distincts. "          
                                )
    


    return prompt_wrap_tags(user_prompt=prompt)

def make_attribute_prompt(n_internal : int):

    if n_internal : 
        prompt = (
                        f"""Tu es un expert en analyse de documents techniques. Extrait les attributs spécifiques de l'élément dont le n_internal(ou numero de series) est {n_internal} """
                    
                    )
    else : 
         prompt = (
                    "Tu es un expert en analyse de documents techniques. Extrait les informations du document " 
                    
                    )

    


    return prompt_wrap_tags(user_prompt=prompt)




 