from fastapi import FastAPI

app = FastAPI()

@app.get("/{name}")
def read_root(name):
    return "Hi it is gokul iof",name

@app.post("/")
def change():
    return "it is gokul"
