import os
import shutil
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, Text, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
import bcrypt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(BASE_DIR)
LOCAL_DB = os.path.join(REPO_ROOT, "disys_system.db")

# En la nube trabajamos sobre /tmp para permisos garantizados de escritura
if os.name != "nt":
    DB_PATH = "/tmp/disys_system.db"
    if not os.path.exists(DB_PATH) and os.path.exists(LOCAL_DB):
        shutil.copy2(LOCAL_DB, DB_PATH)
        try:
            os.chmod(DB_PATH, 0o666)
        except Exception:
            pass
else:
    DB_PATH = LOCAL_DB

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
    nombre_completo = Column(String, default="Usuario")
    rol = Column(String, default="evaluador")
    sucursal = Column(String, default="DIPACA")
    activo = Column(Boolean, default=True)

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
    dictamen_final = Column(Text)
    fecha_evaluacion = Column(DateTime, default=datetime.utcnow)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    if not hashed_password:
        return False
    try:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception:
        return plain_password == hashed_password

def get_password_hash(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

Base.metadata.create_all(bind=engine)