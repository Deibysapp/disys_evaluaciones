import os
import time
import streamlit as st
from google import genai
from google.genai import types

def obtener_cliente_gemini():
    api_key = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))
    if not api_key:
        raise ValueError("No se encontró la clave GEMINI_API_KEY en st.secrets ni en el entorno.")
    return genai.Client(api_key=api_key)

def analizar_test_con_gemini(pdf_bytes: bytes) -> str:
    client = obtener_cliente_gemini()

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

    # Lista de modelos ordenados por prioridad en caso de saturación 503
    modelos_candidatos = [
        "gemini-3.8-flash",
        "gemini-2.5-flash",
        "gemini-2.0-flash",
        "gemini-1.5-flash"
    ]

    ultimo_error = None

    for modelo in modelos_candidatos:
        for intento in range(2):  # 2 intentos por modelo
            try:
                response = client.models.generate_content(
                    model=modelo,
                    contents=[
                        types.Part.from_bytes(
                            data=pdf_bytes,
                            mime_type="application/pdf",
                        ),
                        prompt_instrucciones
                    ]
                )
                if response.text:
                    return response.text
            except Exception as e:
                ultimo_error = e
                # Si está ocupado (503) espera 2 segundos antes de reintentar
                time.sleep(2)
                continue

    raise RuntimeError(f"No fue posible procesar la evaluación tras consultar los modelos disponibles. Detalle: {ultimo_error}")