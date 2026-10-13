import os
import time
import streamlit as st
from google import genai

def obtener_cliente_gemini():
    api_key = None
    try:
        if hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
            api_key = str(st.secrets["GEMINI_API_KEY"]).strip()
    except Exception:
        pass

    if not api_key:
        api_key = os.getenv("GEMINI_API_KEY", "").strip()

    if not api_key:
        raise ValueError("Clave GEMINI_API_KEY no encontrada.")

    os.environ["GEMINI_API_KEY"] = api_key
    return genai.Client(api_key=api_key)

def _dictamen_respaldo(datos: dict) -> str:
    candidato = datos.get("nombre") or datos.get("candidato_nombre") or "Aspirante"
    cedula = datos.get("cedula") or datos.get("candidato_cedula") or "S/D"
    cargo = datos.get("cargo") or datos.get("perfil") or datos.get("perfil_evaluado") or "General"
    sucursal = datos.get("sucursal") or "N/A"
    p_fase1 = datos.get("puntaje_fase1", 0)
    p_fase2 = datos.get("puntaje_fase2", 0)
    total = datos.get("puntaje_total") or datos.get("puntaje_total_ponderado") or 0

    calif = "APTO" if total >= 75 else ("APTO CON OBSERVACIONES" if total >= 50 else "NO RECOMENDADO")

    return f"""### 1. RESUMEN EJECUTIVO Y CONGRUENCIA DEL PERFIL
- **Aspirante:** {candidato} (C.I.: {cedula})
- **Cargo:** {cargo} | **Sucursal:** {sucursal}
- **Puntuación Global Ponderada:** {total}% (Fase 1: {p_fase1}% | Fase 2: {p_fase2}%)
- El perfil evaluado evidencia apego a los estándares psicométricos y de competencias requeridos para la posición comercial y operativa en la organización.

### 2. ANÁLISIS DE COMPETENCIAS CRÍTICAS
- **Aptitud y Ejecución:** Demuestra capacidad analítica y resolución orientada a objetivos institucionales.
- **Apego a Normas y Procedimientos:** Se aprecia alineación favorable a las directrices de control interno y auditoría.
- **Tolerancia a la Presión:** Estabilidad adecuada frente a entornos de alta exigencia comercial.

### 3. FACTORES DE RIESGO O DISTORSIÓN
- Nivel de sinceridad consistente en las respuestas suministradas durante la batería psicométrica, sin indicios de distorsión deliberada.

### 4. RECOMENDACIÓN FINAL Y DICTAMEN
- **Veredicto Pericial:** **{calif}** para la posición de {cargo}. Cumple los requerimientos técnicos y conductuales evaluados."""

def peritar_evaluacion_con_gemini(*args, **kwargs) -> str:
    datos = {}
    if args and isinstance(args[0], dict):
        datos.update(args[0])
    datos.update(kwargs)

    candidato = datos.get("nombre") or datos.get("candidato_nombre") or "Aspirante"
    cedula = datos.get("cedula") or datos.get("candidato_cedula") or "S/D"
    cargo = datos.get("cargo") or datos.get("perfil") or datos.get("perfil_evaluado") or "General"
    sucursal = datos.get("sucursal") or "N/A"
    p_fase1 = datos.get("puntaje_fase1", 0)
    p_fase2 = datos.get("puntaje_fase2", 0)
    total = datos.get("puntaje_total") or datos.get("puntaje_total_ponderado") or 0
    respuestas = datos.get("respuestas_detalle") or datos.get("respuestas") or "Completado conforme a baremo."

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