from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255))
    rol = Column(String(20))

class Dataset(Base):
    __tablename__ = "dataset"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    ruta = Column(String(255))
    usuario_id = Column(Integer)

class Modelo(Base):
    __tablename__ = "modelo"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    tipo = Column(String(50))
    usuario_id = Column(Integer)

class Entrenamiento(Base):
    __tablename__ = "entrenamiento"

    id = Column(Integer, primary_key=True, index=True)
    dataset_id = Column(Integer)
    modelo_id = Column(Integer)
    accuracy = Column(Float)


class Resultado(Base):
    __tablename__ = "resultado"

    id = Column(Integer, primary_key=True, index=True)
    entrenamiento_id = Column(Integer)
    resultado_json = Column(Text)

