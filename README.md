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

J'ai créer un fichier main.py dans lequel je retourne un message, puis j'ai lancer le serveur uvicorn avec "uvicorn main:app". Enfin j'affiche un message à l'url de base (http://127.0.0.1:8000) et je teste la route avec swagger (http://127.0.0.1:8000/docs)

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

<h2> Partie 5 </h2>

5.1) Exemple de modèle Pydantic

Field sert à configurer un champ d'un model, dans user_model.py j'utilise field pour fixer les limites de l'age (minimum 1 et maximum 120).

1) Le champ id n'est pas présent dans le modèle userCreate car userCreate sert de consommable à l'API c'est-à-dire qu'il valide le format des données entrantes et sortantes.

2)Il doit être attribué par user_model au moment où on insère dans la base de données car c'est cette classe qui a pour but la persistance.

5.2) Création de la factory d'utilisateurs

1) Car on souhaite séparer les responsabilités. L'un va servir de consommable à L'API et l'autre va permettre la persistance.
2) Car c'est un schéma de données formel, il sert à valider le format des données.
3) Il est attribé par la bdd lorsqu'on y ajoute un objet.
4) Tout d'abord l'api ne sera pas documenter correctement, et je ne respecterai pas le principe SOLID.

5) 

5.3) Créer la factory UsersFactory

La méthode create_users a pour rôle de charger et de convertir des données brutes en objets. Elle prend en paramètre le chemin d'un fichier JSON, l'ouvre, et charge son contenu dans un dictionnaire Python. Après s'être assurée que la clé principale "users" est bien présente dans ce dictionnaire, la méthode parcourt la liste des utilisateurs. Chaque entrée est alors transformée en une instance de la classe UserModel, puis ajoutée à une liste qui est finalement retournée par la fonction.

1) Elle ne doit pas importer fastAPI car sa seul responsabilité est de créer des utilisateurs.
2) Je ne respecterai pas le principe de responsabilité unique et si je souhaite réutiliser la factory dans un autre contexte je serai obliger de lancer un serveur web.
3) Si je souhaite ajouter les utilisateurs du fichier json directement dans une bdd.

5.5)  Tests unitaires de la factory

1) Le cas où la clé n'est pas dans le fichier, le cas avec la bonne clé et le bon format de données et le cas avec le mauvais format de données.

<h2>Partie 8</h2>

8.3) création de l'interface du service avec 3 méthodes : list_users() qui retourne une liste de UserModel, get_user_by_id(user_id : int) qui retourne un UserModel ou rien et create_user(payload : UserModelCreate) qui retourne un UserModel.

8.4) Le service implémente l'interface ce qui garantit le respect du contrat des méthodes que l'on a définis.
Le constructeur du service reçoit une factory et un objet settings en paramètre. Ensuite il charge les données une seule fois au démarrage dans une liste sans avoir directement accès au variables d'environnement. De plus, la méthode list_users retourne une copie de la liste afin de protéger l'intégrité des données du service contre toute modification accidentelle à l'extérieur.
Enfin, la méthode create_user calcul l'id suivant à l'aide de max() ou l'initialise à 1 si la liste users est vide. Puis transforme le payload UserModelCreate reçu en paramètre en UserModel. J'ai utilisé model_dump() et ** pour fusionner les attributs. J'ajoute ensuite le nouvel objet dans la liste puis je le retourne.