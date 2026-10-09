import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base
import bcrypt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "disys_system.db")

DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    rol = Column(String)

class Evaluacion(Base):
    __tablename__ = "evaluaciones"
    id = Column(Integer, primary_key=True, index=True)
    codigo_expediente = Column(String, unique=True, index=True)
    candidato_nombre = Column(String)
    candidato_cedula = Column(String)
    perfil_evaluado = Column(String)
    evaluador_username = Column(String)
    sucursal = Column(String)
    puntaje_fase1 = Column(Float)
    puntaje_fase2 = Column(Float)
    puntaje_total_ponderado = Column(Float)
    sinceridad_distorsion = Column(Integer)
    alerta_roja = Column(Integer)
    detalle_alerta = Column(String)
    dictamen_final = Column(String)
    fecha_evaluacion = Column(String)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    if not hashed_password:
        return False
    try:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception:
        return plain_password == hashed_password

Base.metadata.create_all(bind=engine)