from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# Partie 2 : première app
@app.get("/")
def hello_fastapi():
    return {"message" : "API FastAPI opérationnelle"}

# Partie 3 : Routage et paramètres
@app.get("/users")
def user ():
    u = [
        {"id" : 1, "login" : "alice"},
        {"id" : 2, "login" : "bob"},
        {"id" : 3, "login" : "charlie"},
        {"id" : 4, "login" : "diana"},
        {"id" : 5, "login" : "edward"},
        {"id" : 6, "login" : "fatima"},
        {"id" : 7, "login" : "guillaume"},
        {"id" : 8, "login" : "hana"},
        {"id" : 9, "login" : "ismael"},
        {"id" : 10, "login" : "julien"},
    ]
    return u

    
# Partie 4 : Typage et validation automatique

@app.get("/users/{user_id}")
def get_user (user_id: int):
    return {"id" : user_id}

@app.get("/search")
def search(name:str or None = None):
    return {"search" : name}




