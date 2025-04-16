from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from Linked_Queue import LinkedQueue
from Exceptions import OwnEmpty

app = FastAPI()
lista_vuelos = LinkedQueue() # Instancia de Lista Vuelos
# stack = ArrayStack()  # Instancia global

class VueloBase(BaseModel):
    codigo: str
    destino: str
    aerolinea: str

class VueloCreate(VueloBase):
    pass

class VueloOut(VueloBase):
    id: int

    class Config:
        orm_mode = True