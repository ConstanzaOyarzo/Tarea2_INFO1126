from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from Linked_Queue import LinkedQueue
from Exceptions import OwnEmpty
from models import Base, EstadoVuelo, Vuelo
from typing import Optional, List

app = FastAPI()
lista_vuelos = LinkedQueue() # Instancia de Lista Vuelos

class VueloCreate(BaseModel):
    id: int
    codigo: str
    estado: Optional[EstadoVuelo] = EstadoVuelo.programado
    origen: str
    destino: str
    aerolinea: str

class VueloOut(VueloCreate):
    id: int

    class Config:
        from_attributes = True

""" POST /vuelos """
@app.post("/vuelos", response_model=VueloOut)
def añadir_vuelo(vuelo: VueloCreate):
    if vuelo.estado == "emergencia":
        lista_vuelos.insertar_al_frente(vuelo)
    else:
        lista_vuelos.enqueue(vuelo)
    return vuelo

""" GET /vuelos/total """
@app.get("/vuelos/total")
def total_vuelos():
    return {"total": lista_vuelos.size}

""" GET /vuelos/próximo """
@app.get("/vuelos/proximo", response_model=VueloOut)
def proximo_vuelo():
    if lista_vuelos.is_empty():
        raise HTTPException(status_code=404, detail="No hay vuelos en la cola")
    return lista_vuelos.first()

""" GET /vuelos/ultimo """
@app.get("/vuelos/ultimo", response_model=VueloOut)
def ultimo_vuelo():
    if lista_vuelos.is_empty():
        raise HTTPException(status_code=404, detail="No hay vuelos en la cola")
    return lista_vuelos.last()

""" POST /vuelos/insertar """
@app.post("/vuelos/insertar", response_model=VueloOut)
def insertar_vuelo(vuelo: VueloCreate, posicion: int):
    lista_vuelos.insertar_en_posicion(vuelo, posicion)
    return vuelo

""" DELETE /vuelos/extraer """
@app.delete("/vuelos/extraer")
def extraer_vuelo(posicion: int):
    vuelo_removido = lista_vuelos.extraer_de_posicion(posicion)
    return {"mensaje": "Vuelo removido", "vuelo": vuelo_removido}

""" GET /vuelos/lista """
@app.get("/vuelos/lista", response_model=List[VueloOut])
def listar_vuelos():
    return lista_vuelos.obtener_lista()  # método que devuelva los vuelos como lista

""" PATCH /vuelos/reordenar """
@app.patch("/vuelos/reordenar")
def reordenar_vuelos():
    if lista_vuelos.is_empty():
        raise HTTPException(status_code=404, detail="No hay vuelos en la cola")

    lista_vuelos.reordenar()  # Usa la lógica de prioridad: emergencia → retrasado → programado
    return lista_vuelos.obtener_lista()