import os
import streamlit as st
from google import genai

def obtener_cliente_gemini():
    api_key = None
    
    # 1. Intentar desde Streamlit Secrets
    try:
        if hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
            api_key = str(st.secrets["GEMINI_API_KEY"]).strip()
    except Exception:
        pass

    # 2. Intentar desde variable de entorno
    if not api_key:
        api_key = os.getenv("GEMINI_API_KEY", "").strip()

    if not api_key:
        raise ValueError("Clave GEMINI_API_KEY no encontrada en secrets ni en variables de entorno.")

    # Establecer la variable de entorno global para que las llamadas internas no fallen
    os.environ["GEMINI_API_KEY"] = api_key

    # Inicializar el cliente
    return genai.Client(api_key=api_key)