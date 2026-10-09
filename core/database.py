import os
import shutil
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOCAL_DB = os.path.join(BASE_DIR, "disys_system.db")

# En entornos Linux (Streamlit Cloud), usamos /tmp para garantizar permisos de escritura
if os.name != "nt":
    TMP_DIR = "/tmp"
    DB_PATH = os.path.join(TMP_DIR, "disys_system.db")
    
    # Si la base de datos no está en /tmp pero existe la plantilla del repo, se copia
    if not os.path.exists(DB_PATH) and os.path.exists(LOCAL_DB):
        shutil.copy2(LOCAL_DB, DB_PATH)
        try:
            os.chmod(DB_PATH, 0o666)
        except Exception:
            pass
else:
    # En Windows (entorno local de desarrollo)
    DB_PATH = LOCAL_DB

# Conexión SQLite con soporte para múltiples hilos
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()