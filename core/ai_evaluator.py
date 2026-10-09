import os
import time
import streamlit as st
from google import genai

def obtener_cliente_gemini():
    api_key = None
    
    # 1. Leer de secrets de Streamlit Cloud
    try:
        if hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
            api_key = str(st.secrets["GEMINI_API_KEY"]).strip()
    except Exception:
        pass

    # 2. Leer de variables de entorno si existe
    if not api_key:
        api_key = os.getenv("GEMINI_API_KEY", "").strip()

    if not api_key:
        raise ValueError("Clave GEMINI_API_KEY no encontrada en Secrets ni en variables de entorno.")

    os.environ["GEMINI_API_KEY"] = api_key
    return genai.Client(api_key=api_key)


def peritar_evaluacion_con_gemini(datos_evaluacion: dict) -> str:
    """
    Genera el dictamen pericial psicológico mediante Gemini con respaldo ante fallos.
    """
    cliente = obtener_cliente_gemini()
    
    # Construcción de la instrucción pericial para la IA
    candidato = datos_evaluacion.get("nombre", "Aspirante")
    cedula = datos_evaluacion.get("cedula", "S/D")
    cargo = datos_evaluacion.get("perfil", "General")
    sucursal = datos_evaluacion.get("sucursal", "N/A")
    p_fase1 = datos_evaluacion.get("puntaje_fase1", 0)
    p_fase2 = datos_evaluacion.get("puntaje_fase2", 0)
    total = datos_evaluacion.get("puntaje_total", 0)
    respuestas = datos_evaluacion.get("respuestas_detalle", "Sin detalles.")

    prompt = f"""
    Actúa como un Perito Evaluador Psicométrico Senior y Psicólogo Organizacional Forense.
    Genera un Dictamen Pericial exhaustivo, objetivo y formal para el siguiente aspirante:

    DATOS GENERALES:
    - Nombre del Candidato: {candidato}
    - Documento de Identidad: {cedula}
    - Cargo Postulado: {cargo}
    - Sucursal: {sucursal}
    - Puntuación Psicométrica Fase 1 (Aptitudinal): {p_fase1}%
    - Puntuación Psicométrica Fase 2 (Conductual): {p_fase2}%
    - Promedio Ponderado Total: {total}%

    DETALLE DE RESPUESTAS DEL TEST:
    {respuestas}

    ESTRUCTURA DEL INFORME REQUERIDA (Usa subtítulos en negrita y viñetas):
    1. RESUMEN EJECUTIVO Y CONGRUENCIA DEL PERFIL
    2. ANÁLISIS DE COMPETENCIAS CRÍTICAS (Aptitud, apego a normas, trabajo bajo presión)
    3. FACTORES DE RIESGO O DISTORSIÓN (Sinceridad y consistencia en respuestas)
    4. RECOMENDACIÓN FINAL Y DICTAMEN (APTO, APTO CON OBSERVACIONES o NO RECOMENDADO)
    """

    modelos = ["gemini-2.5-flash", "gemini-1.5-flash", "gemini-1.5-pro"]
    ultimo_error = None

    for modelo in modelos:
        try:
            respuesta = cliente.models.generate_content(
                model=modelo,
                contents=prompt
            )
            if respuesta and respuesta.text:
                return respuesta.text
        except Exception as e:
            ultimo_error = e
            time.sleep(1)
            continue

    raise RuntimeError(f"Error procesando el peritaje con IA: {ultimo_error}")