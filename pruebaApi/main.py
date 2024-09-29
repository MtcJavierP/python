# main.py
from fastapi import FastAPI

# Crear la aplicación FastAPI
app = FastAPI()

# Definir una ruta principal
@app.get("/")
def leer_raiz():
    return {"mensaje": "¡Hola, FastAPI!"}

# Definir una ruta que reciba un parámetro
@app.get("/items/{item_id}")
def leer_item(item_id: int):
    if item_id != 123:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return {"item_id": item_id}