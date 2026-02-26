import os
from dotenv import load_dotenv

class Settings:
    def __init__(self) -> None:
        # Charge le fichier .env s'il existe
        load_dotenv()
        # Lecture de la variable d'environnement USERS_JSON_PATH
        # Valeur par défaut utilisée si la variable n'exista pas
        self.users_json_path = os.getenv(
            "USERS_JSON_PATH", 
            "data/users/json"
        )