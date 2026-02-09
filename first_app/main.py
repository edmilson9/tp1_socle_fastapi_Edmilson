from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_fastapi():
    return {"message" : "API FastAPI opérationnelle"}

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

    