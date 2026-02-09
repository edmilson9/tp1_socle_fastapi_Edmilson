# Rapport et réponses du tp

<h2> Partie 1 </h2>

Cette première partie va servir à installer fastAPI, créer et configurer un environnement virtuel. J'ai utilisé plusieurs commandes sous linux notamment : 

$python3 -m venv tp_fastAPI
$source tp_fastAPI/bin/activate
$pip install fastapi uvicorn pydantic

Puis j'ai geler la configuration avec $pip freeze > requirements.txt

Mais à quoi servent ces dépendances ? 
Elles servent à tout d'abord avoir un environnement virtuel actif avec les dépendances nécessaires à l'utilisation de fastAPI et du serveur uvicorn.


<h2> Partie 2 </h2>

J'ai créer un fichier main.py dans lequel, puis j'ai lancer le serveur uvicorn avec "uvicorn main:app". Enfin j'affiche un message à l'url de base (http://127.0.0.1:8000) et je teste la route avec swagger (http://127.0.0.1:8000/docs)

<h2> Partie 3 </h2>

Je crée une nouvelle route users avec une fonction user où je déclare une liste de dictionnaire avec des champs id et login. Ensuite je retourne le dictionnaire qui sera sérialisé en JSON.

<h2> Partie 4 </h2>
4.2) Validation automatique des paramètres

Cas 1 :  
Oui la route est executée et elle retourne la valeur mis en paramètre si c'est un entier sinon il y a une erreur.

Cas 2 : 
La fonction est exécutée mais le paramètre n'est pas retourné car ce n'est pas un entier.

4.3) Typage des Query Parameters

1. Le paramètre n'est pas obligatoire grâce à "(name:str or None = None)".
2. Toutes les valeurs sont acceptées car elles sont considérées comme des chaînes de caractères.

