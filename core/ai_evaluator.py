import os
import streamlit as st
from google import genai
from google.genai import types

def obtener_cliente_gemini():
    # Intenta obtener la clave desde Streamlit Secrets o variables de entorno
    api_key = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))
    if not api_key:
        raise ValueError("No se encontró la clave GEMINI_API_KEY en st.secrets ni en el entorno.")
    return genai.Client(api_key=api_key)

def analizar_test_con_gemini(pdf_bytes: bytes) -> str:
    """
    Envía el PDF escaneado a Gemini para extraer las respuestas marcadas,
    verificar la consistencia del evaluado y generar el informe técnico pericial.
    """
    client = obtener_cliente_gemini()

    prompt_instrucciones = """
    Eres un perito experto en psicometría aplicada, auditoría de operaciones comerciales y talento humano.
    Examina minuciosamente este documento PDF escaneado correspondiente a un test psicotécnico situacional:

    1. DATOS DE IDENTIFICACIÓN:
       - Nombre completo del postulante.
       - Cédula de identidad.
       - Cargo postulado.
       - Fecha de aplicación.

    2. EXTRACCIÓN PERICIAL DE RESPUESTAS:
       - Extrae la opción marcada (A, B, C o D) en cada uno de los reactivos del examen.
       - Muestra la lista completa de respuestas detectadas de forma ordenada (ejemplo: 1. D, 2. B, ...).

    3. BALANCE CUANTITATIVO:
       - Total de reactivos y efectividad general porcentual.
       - Nivel de coherencia y consistencia interna de las respuestas.

    4. EVALUACIÓN POR DIMENSIONES COMPETENCIALES:
       - Rigor Analítico, Precisión Numérica y Auditoría de Datos.
       - Integridad Ética, Normativa y Confidencialidad Comercial.
       - Proactividad, Resolución de Contingencias y Orientación a Procesos.
       - Soporte a la Fuerza de Ventas y Relaciones Interdepartamentales.

    5. CONTROL DE SINCERIDAD Y AUTOCRÍTICA (L-SCALE):
       - Evalúa si el postulante muestra apertura honesta reconociendo fatiga, presión o errores involuntarios habituales del trabajo, o si incurrió en deseabilidad social / simulación irreal de perfección.

    6. DICTAMEN PERICIAL Y RECOMENDACIÓN FINAL:
       - Dictamen claro: Apto Recomendado, Apto con Observaciones o No Apto.
       - Conclusiones ejecutivas orientadas a la toma de decisión gerencial.
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[
            types.Part.from_bytes(
                data=pdf_bytes,
                mime_type="application/pdf",
            ),
            prompt_instrucciones
        ]
    )

    return response.text