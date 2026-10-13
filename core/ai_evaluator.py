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


def _generar_dictamen_contingencia(datos: dict, metricas: dict) -> str:
    """Plantilla que refleja con precisión matemática el desempeño real."""
    candidato = datos.get("nombre") or datos.get("candidato_nombre") or "Aspirante"
    cedula = datos.get("cedula") or datos.get("candidato_cedula") or "S/D"
    cargo = datos.get("cargo") or datos.get("perfil") or "General"
    sucursal = datos.get("sucursal") or "Corporativo"
    fecha = datos.get("fecha") or "13/10/2026"
    evaluador = datos.get("evaluador") or "Administrador Maestro DiSys"

    p_f1 = metricas.get("puntaje_fase1", 0)
    p_f2 = metricas.get("puntaje_fase2", 0)
    total = metricas.get("puntaje_total", 0)
    aciertos = metricas.get("aciertos_totales", 0)
    preguntas = metricas.get("total_preguntas", 30)
    distorsion = metricas.get("distorsion", 0)
    es_azar = metricas.get("es_azar", False)

    # Lógica de dictamen pericial forense
    if es_azar or total < 45.0:
        veredicto = "NO RECOMENDADO"
        conclusion = f"El aspirante NO CALIFICA para el cargo de {cargo}. El rendimiento situacional ({total}%) es crítico e insuficiente para asumir responsabilidades operativas o de cobranza."
        analisis_distorsion = "SE DETECTA PATRÓN DE RESPUESTA POR AZAR O DISPERSIÓN SEVERA. Las elecciones carecen de congruencia técnica, denotando falta de criterio o desinterés en la prueba."
    elif distorsion >= 4:
        veredicto = "APTO CON OBSERVACIONES (DISTORSIÓN DETECTADA)"
        conclusion = f"El aspirante obtiene un puntaje técnico de {total}%, pero muestra una tendencia deliberada a falsear respuestas hacia la deseabilidad social. Se recomienda entrevista presencial de confrontación."
        analisis_distorsion = f"Índice de distorsión elevado ({distorsion}/6 puntos). El candidato intentó proyectar una imagen irrealmente perfecta en situaciones de presión y error humano."
    elif total < 70.0:
        veredicto = "APTO CON OBSERVACIONES"
        conclusion = f"El aspirante reúne competencias básicas ({total}%), pero requiere supervisión estricta en gestión de conflictos y apego a normas de crédito/operaciones."
        analisis_distorsion = "Índice de sinceridad aceptable, sin alertas rojas de manipulación."
    else:
        veredicto = "APTO"
        conclusion = f"El evaluado reúne plenamente el perfil de competencias, madurez y criterio situacional requerido para {cargo}."
        analisis_distorsion = "Respuestas coherentes y consistentes con los baremos institucionales."

    return f"""DICTAMEN PERICIAL PSICOTÉCNICO SITUACIONAL Y FORENSE
Expediente Técnico: EXP-{cedula}
Fecha de Emisión: {fecha}
Perito Evaluador Responsable: {evaluador}

1. RESUMEN EJECUTIVO Y CONGRUENCIA DEL PERFIL
- Evaluado: {candidato} | Cédula: {cedula}
- Cargo Postulado: {cargo} | Centro Operativo / Sede: {sucursal}
- Rendimiento Cuantitativo: {aciertos} de {preguntas} reactivos correctos ({total}%).
- Fase 1 (Aptitud y Criterio Técnico): {p_f1}% | Fase 2 (Gestión Situacional y Presión): {p_f2}%.

2. ANÁLISIS DE COMPETENCIAS CRÍTICAS Y CONDUCTUALES
- Criterio de Decisión y Procedimientos: El aspirante obtuvo un rendimiento de {p_f1}% en apego normativo. {"Presenta lagunas severas de juicio frente a situaciones de conflicto." if total < 50 else "Demuestra criterio acorde a las exigencias."}
- Tolerancia a la Frustración y Trabajo bajo Presión: {"Baja capacidad de contención; patrón errático o reactivo frente a escenarios de alta exigencia." if total < 50 else "Capacidad adecuada de autorregulación emocional en ruta y cobranza."}
- Defensa de Políticas Corporativas: {"Alto riesgo de indulgencia o vulneración de límites crediticios." if total < 50 else "Alineación consistente con las directrices de control interno."}

3. EVALUACIÓN DE INTEGRIDAD, SINCERIDAD Y FACTORES DE RIESGO
- Indicador de Deseabilidad Social: {distorsion} puntos acumulados.
- Análisis de Validez del Protocolo: {analisis_distorsion}

4. CONCLUSIONES Y RECOMENDACIÓN FINAL
DICTAMEN: {veredicto}
{conclusion}"""


def peritar_evaluacion_con_gemini(*args, **kwargs) -> str:
    datos = {}
    if args and isinstance(args[0], dict):
        datos.update(args[0])
    datos.update(kwargs)

    dc = datos.get("datos_candidato") or {}
    if not isinstance(dc, dict):
        dc = {}

    metricas = datos.get("metricas_evaluacion") or {}
    if not isinstance(metricas, dict):
        metricas = {
            "puntaje_fase1": dc.get("puntaje_fase1", 0),
            "puntaje_fase2": dc.get("puntaje_fase2", 0),
            "puntaje_total": dc.get("puntaje_total", 0),
            "distorsion": dc.get("distorsion", 0),
            "alerta_roja": dc.get("alerta_roja", False),
            "es_azar": dc.get("es_azar", False)
        }

    candidato = dc.get("nombre") or datos.get("candidato_nombre") or "Aspirante"
    cedula = dc.get("cedula") or datos.get("candidato_cedula") or "S/D"
    cargo = datos.get("cargo") or dc.get("cargo") or "General"
    sucursal = dc.get("sucursal") or "Corporativo"
    fecha = dc.get("fecha") or "13/10/2026"
    evaluador = dc.get("evaluador") or "Administrador Maestro DiSys"
    respuestas = str(datos.get("respuestas_marcadas") or "")

    prompt = f"""
    Actúa como Perito Psicólogo Organizacional Forense de la Distribuidora.
    Tu trabajo es evaluar con RIGOR CIENTÍFICO y TOTAL OBJETIVIDAD los resultados reales del aspirante.
    NUNCA emitas dictamen APTO si el aspirante respondió al azar o sacó mala puntuación.

    DATOS CUANTITATIVOS REALES DEL TEST:
    - Aspirante: {candidato} (C.I.: {cedula})
    - Cargo Postulado: {cargo} | Sucursal: {sucursal}
    - Puntaje Total Obtenido: {metricas.get('puntaje_total')}%
    - Aciertos Fase 1: {metricas.get('puntaje_fase1')}%
    - Aciertos Fase 2: {metricas.get('puntaje_fase2')}%
    - Aciertos Totales: {metricas.get('aciertos_totales')}/{metricas.get('total_preguntas')}
    - Índice de Distorsión / Mentira: {metricas.get('distorsion')} puntos.
    - Patrón de Azar Detectado: {'SÍ (RESPONDIÓ AL AZAR O CON REPETICIÓN MONÓTONA)' if metricas.get('es_azar') else 'NO'}
    - Respuestas Marcadas: {respuestas}

    REGLAS ESTRICTAS DE DICTAMEN:
    - Si el puntaje total es inferior al 50% o respondió al azar: DICTAMEN: NO RECOMENDADO. Critica la falta de criterio técnico, el patrón de respuestas y el riesgo operativo.
    - Si el puntaje está entre 50% y 69%: DICTAMEN: APTO CON OBSERVACIONES. Señala las fallas en normas, cobros y ventas.
    - Si la distorsión es >= 4: DICTAMEN: APTO CON OBSERVACIONES (DISTORSIÓN DETECTADA). Señala que intentó mentir fingiendo perfección.
    - Solo si el puntaje es >= 70% y distorsión baja: DICTAMEN: APTO.

    FORMATO REQUERIDO OBLIGATORIO:
    DICTAMEN PERICIAL PSICOTÉCNICO SITUACIONAL Y FORENSE
    Expediente Técnico: EXP-{cedula}
    Fecha de Emisión: {fecha}
    Perito Evaluador Responsable: {evaluador}

    1. RESUMEN EJECUTIVO Y CONGRUENCIA DEL PERFIL
    [Detalla los puntajes reales obtenidos y la validez de la prueba]

    2. ANÁLISIS DE COMPETENCIAS CRÍTICAS Y CONDUCTUALES
    - Criterio de Decisión y Procedimientos: [Análisis técnico real según su puntaje]
    - Tolerancia a la Frustración y Trabajo bajo Presión: [Análisis de estabilidad]
    - Apego a Políticas y Cobranza: [Riesgo de fraude o permisividad]

    3. EVALUACIÓN DE INTEGRIDAD, SINCERIDAD Y FACTORES DE RIESGO
    - Índice de Distorsión Psicométrica: [Evalúa la deseabilidad social o azar]
    - Factores Críticos / Alertas: [Señala si hay alerta roja]

    4. CONCLUSIONES Y RECOMENDACIÓN FINAL
    DICTAMEN: [APTO / APTO CON OBSERVACIONES / NO RECOMENDADO]
    [Fundamentación directa y sin ambigüedades]
    """

    modelos = ["gemini-3.8-flash", "gemini-2.5-flash"]
    try:
        cliente = obtener_cliente_gemini()
        for mod in modelos:
            try:
                res = cliente.models.generate_content(
                    model=mod, 
                    contents=prompt
                )
                if res and res.text and len(res.text.strip()) > 100:
                    return str(res.text).strip()
            except Exception:
                time.sleep(1)
                continue
    except Exception:
        pass

    return _generar_dictamen_contingencia(datos, metricas)