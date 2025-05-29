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

def make_general_prompt_no_attributes_french():

    prompt = (
                    "Tu es un expert en analyse de documents techniques. Extrait les détails du document, "
                    "les informations de contrôle d'intervention et la liste des éléments selon la structure suivante :\n"
                    "{\n"
                    "  \"document\": {\"nom\": \"string\", \"numero\": integer, \"date\": \"YYYY-MM-DD\", \"nombre_de_pages\": integer},\n"
                    "  \"intervention_control\": {\"nom\": \"string\", \"date_de_debut\": \"YYYY-MM-DD\", \"date_de_fin\": \"YYYY-MM-DD\", "
                    "\"entreprise_inspecteur\": \"string\", \"agence_inspecteur\": \"string\", \"nom_inspecteur\": \"string\", "
                    "\"entreprise_client\": \"string\", \"adresse_client\": \"string\", \"usine_client\": \"string\", "
                    "\"nombre_d_elements\": integer, \"nombre_de_taches\": integer},\n"
                    "  \"elements\": [{\n"
                    "    \"numero\": integer,\n"
                    "    \"page\": integer,\n"
                    "    \"inspecteur\": \"string\",\n"
                    "    \"nom\": \"string\",\n"
                    "    \"numero_identification_interne\": integer,\n"
                    "    \"usine\": \"string\",\n"
                    "    \"batiment\": \"string\",\n"
                    "  }]\n"
                    "}\n"
                    "Retourne UNIQUEMENT un objet JSON valide correspondant à cette structure. N'inclue aucun texte supplémentaire."
                )
    


    return prompt_wrap_tags(user_prompt=prompt)