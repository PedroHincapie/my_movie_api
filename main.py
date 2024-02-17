from fastapi import FastAPI

app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"

@app.get('/', tags=["Home"])
def message():
    return "Hola Mundo!"