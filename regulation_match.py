import requests
import json
from prompt.regulation_prompt import make_regulation_prompt

def query_ollama(prompt, model="llama3.2:latest"):
    """
    Envoie une requête au modèle Ollama et retourne sa réponse
    """
    url = "http://localhost:11434/api/generate"
    
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        print(f"Erreur lors de la requête: {e}")
        return None

def main():
    # Test simple avec un prompt
    test_prompt = "c'est quoi l'intelligence artificielle ?"
    
    response = query_ollama(test_prompt)
    
    if response:
        print("\nRéponse du modèle:")
        print(response)
    else:
        print("Impossible d'obtenir une réponse du modèle.")

if __name__ == "__main__":
    main()
