import os
import streamlit as st
from google import genai
from google.genai import types

def obtener_cliente_gemini():
    api_key = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))
    if not api_key:
        raise ValueError("No se encontró la clave GEMINI_API_KEY en st.secrets ni en el entorno.")
    return genai.Client(api_key=api_key)

def seleccionar_modelo_disponible(client):
    """Detecta dinámicamente un modelo Flash activo en tu proyecto."""
    try:
        modelos = [m.name for m in client.models.list()]
        # Prioriza modelos flash modernos disponibles
        for m in modelos:
            if "flash" in m.lower() and "generateContent" in getattr(m, "supported_actions", ["generateContent"]):
                return m.replace("models/", "")
        for m in modelos:
            if "flash" in m.lower():
                return m.replace("models/", "")
    except Exception:
        pass
    # Respaldo por defecto
    return "gemini-2.0-flash"

def analizar_test_con_gemini(pdf_bytes: bytes) -> str:
    client = obtener_cliente_gemini()
    modelo_activo = seleccionar_modelo_disponible(client)

    prompt_instrucciones = """
    Eres un perito experto en psicometría aplicada y auditoría operativa de talento humano.
    Analiza este documento PDF escaneado correspondiente a una evaluación psicotécnica situacional:

    1. DATOS DE IDENTIFICACIÓN:
       - Nombre completo del postulante, Cédula de Identidad, Cargo postulado y Fecha.

    2. EXTRACCIÓN DE RESPUESTAS:
       - Extrae con precisión la opción marcada (A, B, C o D) en cada uno de los reactivos (1 al 30).
       - Lista las respuestas detectadas (ej: 1. D, 2. B, ...).

    3. EVALUACIÓN Y BALANCE:
       - Porcentaje de aciertos y consistencia interna.
       - Dimensiones evaluadas (Rigor Analítico, Integridad Ética, Resguardo de Procesos, Soporte Comercial).
       - Escala de sinceridad y autocrítica (L-Scale).

    4. DICTAMEN FINAL:
       - Recomendación pericial de contratación (Apto / No Apto) y conclusiones ejecutivas.
    """

   response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=[
            types.Part.from_bytes(
                data=pdf_bytes,
                mime_type="application/pdf",
            ),
            prompt_instrucciones
        ]
    )

    return response.text