
import json
import os

TOKENS_FILE = os.path.join(os.path.dirname(__file__), "jetons.json")


def obtenir_utilisateur(jeton):
    """Retourne les informations de l'utilisateur si le jeton est valide."""
    if not jeton:
        return None

    try:
        with open(TOKENS_FILE, "r", encoding="utf-8") as fichier:
            jetons = json.load(fichier)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

    utilisateur = jetons.get(jeton)
    if not isinstance(utilisateur, dict):
        return None

    return utilisateur

