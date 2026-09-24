import os
import bcrypt
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Float, Text
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///disys_system.db")
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String(150), nullable=False)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    rol = Column(String(20), default="EVALUADOR", nullable=False)  # 'MASTER' o 'EVALUADOR'
    sucursal = Column(String(100), default="Sede Principal", nullable=False)
    activo = Column(Boolean, default=True, nullable=False)
    intentos_fallidos = Column(Integer, default=0, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

class Evaluacion(Base):
    __tablename__ = "evaluaciones"
    
    id = Column(Integer, primary_key=True, index=True)
    codigo_expediente = Column(String(50), unique=True, index=True, nullable=False)
    candidato_nombre = Column(String(150), nullable=False)
    candidato_cedula = Column(String(30), nullable=False)
    perfil_evaluado = Column(String(100), nullable=False)
    evaluador_username = Column(String(50), nullable=False)
    sucursal = Column(String(100), nullable=False)
    
    # Puntajes y Métricas
    puntaje_fase1 = Column(Float, nullable=False)
    puntaje_fase2 = Column(Float, nullable=False)
    puntaje_total_ponderado = Column(Float, nullable=False)
    sinceridad_distorsion = Column(Integer, nullable=False)
    alerta_roja = Column(Boolean, default=False, nullable=False)
    detalle_alerta = Column(Text, nullable=True)
    
    dictamen_final = Column(String(50), nullable=False)
    fecha_evaluacion = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

def get_password_hash(password: str) -> str:
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception:
        return False

def inicializar_superadmin():
    db = SessionLocal()
    try:
        admin = db.query(Usuario).filter(Usuario.username == "master").first()
        if not admin:
            nuevo_master = Usuario(
                nombre_completo="Administrador Maestro DiSys",
                username="master",
                password_hash=get_password_hash("Master2026.*"),
                rol="MASTER",
                sucursal="Corporativo",
                activo=True
            )
            db.add(nuevo_master)
            db.commit()
    finally:
        db.close()

inicializar_superadmin()