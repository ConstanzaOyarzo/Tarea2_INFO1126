from sqlalchemy import Column, Integer, String, Text, Enum, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
import enum

# Se define la base del modelo ORM
Base = declarative_base()

class EstadoVuelo(enum.Enum):
    programado = "programado"
    emergencia = "emergencia"
    retrasado = "retrasado"

class Vuelo(Base):
    __tablename__ = "vuelos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    codigo = Column(String, unique=True, nullable=False)  # ej: "AV2025"
    estado = Column(Enum(EstadoVuelo), default=EstadoVuelo.programado)
    hora = Column(DateTime, default=datetime.utcnow)
    origen = Column(String, nullable=False)
    destino = Column(String, nullable=False)