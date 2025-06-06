import requests
import json
from prompt.regulation_prompt import make_regulation_prompt
from prompt.general_json import make_general_prompt_no_attributes
import time
from Mistral_OCR import PDFProcessor


def query_ollama(user_prompt, system_prompt="", model="mistral-small:24b"):
    """
    Envoie une requête au modèle Ollama et retourne sa réponse
    
    Args:
        user_prompt (str): Le prompt utilisateur
        system_prompt (str): Le prompt système (optionnel)
        model (str): Le modèle à utiliser
    """
    url = "http://localhost:11434/api/generate"
    
    # Construction du prompt complet avec les balises système et utilisateur
    if system_prompt:
        full_prompt = f"<s>[INST] <<SYS>>\n{system_prompt}\n<</SYS>>\n\n{user_prompt} [/INST]"
    else:
        full_prompt = f"<s>[INST] {user_prompt} [/INST]"
    
    data = {
        "model": model,
        "prompt": full_prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        print(f"Erreur lors de la requête: {e}")
        return None


