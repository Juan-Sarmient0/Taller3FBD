from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from datetime import datetime
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

#os.environ para despliegue. Descomente cuando ya probó todo local.
#client = MongoClient(os.environ["MONGO_URI"])
# TODO: conectarse al cluster Admonsis  
#client = MongoClient("mongodb://<ISIS2304C24202620>:<M4hE7Vz2iaT2>@157.253.236.88:8087")

client = MongoClient(os.environ["MONGO_URI"])
db = client["ISIS2304C24202620"]

@app.get("/")
def inicio():
    return {"estado": "API funcionando correctamente"}

@app.get('/bares/{bar_id}/comentarios')
def get_comentarios(bar_id: int):
    comentarios = list(db["comentarios_bares"].find({"bar_id": bar_id}, {"_id": 0}))
    return comentarios
 
@app.post('/bares/{bar_id}/comentarios')
def post_comentario(bar_id: int, datos: dict):
    datos['bar_id'] = bar_id
    datos['fecha'] = datetime.now().isoformat()
    db["comentarios_bares"].insert_one(datos)
    return {'mensaje': 'Comentario guardado'}
 
@app.get('/bares/{bar_id}/eventos')
def get_eventos(bar_id: int):
    eventos = list(db["eventos"].find({"bar_id": bar_id}, {"_id": 0}))
    return eventos
 
 
@app.post('/bares/{bar_id}/eventos')
def post_evento(bar_id: int, datos: dict):
    evento = {k: v for k, v in datos.items() if v not in (None, "")}
    evento['bar_id'] = bar_id
    evento['fecha_creacion'] = datetime.now().isoformat()
    db["eventos"].insert_one(evento)
    return {'mensaje': 'Evento guardado'}