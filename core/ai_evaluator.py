import os
import io
import time
import streamlit as st
from google import genai

def obtener_cliente_gemini():
    api_key = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))
    if not api_key:
        raise ValueError("No se encontró la clave GEMINI_API_KEY en st.secrets ni en el entorno.")
    return genai.Client(api_key=api_key)

def analizar_test_con_gemini(pdf_bytes: bytes) -> str:
    client = obtener_cliente_gemini()

    # 1. Subir el archivo de 23MB de forma controlada a la API de Google
    archivo_stream = io.BytesIO(pdf_bytes)
    archivo_subido = client.files.upload(
        file=archivo_stream,
        mime_type="application/pdf"
    )

    # Esperar brevemente a que el archivo esté en estado ACTIVE
    while archivo_subido.state.name == "PROCESSING":
        time.sleep(2)
        archivo_subido = client.files.get(name=archivo_subido.name)

    prompt_instrucciones = """
    Eres un perito experto en psicometría aplicada y auditoría operativa de talento humano.
    Analiza este documento PDF escaneado correspondiente a una evaluación psicotécnica situacional:

    1. DATOS DE IDENTIFICACIÓN:
       - Nombre completo del postulante, Cédula de Identidad, Cargo postulado y Fecha.

    2. EXTRACCIÓN DE RESPUESTAS:
       - Extrae con total precisión la opción marcada con (X) en cada uno de los 30 reactivos.
       - Lista ordenada de respuestas detectadas (ejemplo: 1. D, 2. B, ...).

    3. EVALUACIÓN Y BALANCE:
       - Porcentaje de aciertos operativos y consistencia interna.
       - Dimensiones evaluadas (Rigor Analítico, Integridad Ética, Soporte Comercial, Procesos).
       - Escala de sinceridad y autocrítica (L-Scale).

    4. DICTAMEN FINAL:
       - Recomendación pericial de contratación (Apto / No Apto) y conclusiones ejecutivas.
    """

    try:
        # Llamada directa al modelo vigente indicado por la API
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=[archivo_subido, prompt_instrucciones]
        )
        return response.text
    finally:
        # Limpieza del archivo temporal en los servidores de Google
        try:
            client.files.delete(name=archivo_subido.name)
        except Exception:
            pass