import os
import time
import streamlit as st
from google import genai

def obtener_cliente_gemini():
    api_key = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))
    if not api_key:
        raise ValueError("No se encontró la clave GEMINI_API_KEY en st.secrets ni en el entorno.")
    return genai.Client(api_key=api_key)

def peritar_evaluacion_con_gemini(cargo: str, datos_candidato: dict, respuestas_marcadas: dict, preguntas_contexto) -> str:
    client = obtener_cliente_gemini()

    # Formateo de cuestionario universal
    detalle_cuestionario = []
    if isinstance(preguntas_contexto, dict):
        items_preguntas = [(k, v) for k, v in sorted(preguntas_contexto.items(), key=lambda x: int(x[0]) if str(x[0]).isdigit() else str(x[0]))]
    elif isinstance(preguntas_contexto, list):
        items_preguntas = [(idx + 1, item) for idx, item in enumerate(preguntas_contexto)]
    else:
        items_preguntas = [(i, {}) for i in range(1, 31)]

    for num, item in items_preguntas:
        resp_candidato = respuestas_marcadas.get(int(num) if str(num).isdigit() else num, "No contestada")
        if isinstance(item, dict):
            pregunta_txt = item.get("pregunta", item.get("enunciado", f"Situación operativa {num}"))
            opciones_txt = item.get("opciones", {})
            texto_item = f"Pregunta {num}: {pregunta_txt}\n"
            if isinstance(opciones_txt, dict):
                for letra, desc in opciones_txt.items():
                    texto_item += f"  [{letra}] {desc}\n"
        else:
            texto_item = f"Pregunta {num}: {item}\n"
        texto_item += f"  -> RESPUESTA MARCADA: {resp_candidato}\n"
        detalle_cuestionario.append(texto_item)

    bloque_cuestionario = "\n".join(detalle_cuestionario)

    prompt = f"""
    Eres un perito experto en psicometría aplicada y auditoría operativa de talento humano en empresas de distribución comercial y consumo masivo.
    
    Analiza con máxima rigurosidad técnica la siguiente evaluación situacional:
    
    DATOS DEL EVALUADO:
    - Postulante: {datos_candidato.get('nombre', 'No especificado')}
    - Cédula de Identidad: {datos_candidato.get('cedula', 'No especificado')}
    - Cargo Postulado: {cargo}
    - Sucursal / Sede: {datos_candidato.get('sucursal', 'No especificado')}
    - Fecha: {datos_candidato.get('fecha', 'No especificado')}
    
    INSTRUMENTO SITUACIONAL Y RESPUESTAS MARCADAS:
    {bloque_cuestionario}
    
    INSTRUCCIONES PERICIALES:
    1. Evalúa la idoneidad de cada respuesta basándote estrictamente en las responsabilidades operativas y éticas del cargo: {cargo}.
    2. Identifica los reactivos de sinceridad/autocrítica (L-Scale) y dictamina si el postulante muestra autenticidad o deseabilidad social manipulada.
    3. Detecta riesgos operacionales o faltas éticas si las hubiere.
    4. Estructura el informe pericial:
       - Resumen Cuantitativo (% de efectividad situacional y conteo de aciertos idóneos).
       - Desglose por Dimensiones Competenciales relevantes al cargo evaluado.
       - Auditoría de la Escala de Sinceridad (L-Scale).
       - Dictamen Ejecutivo y Recomendación Definitiva de Contratación (Apto Sobresaliente, Apto con Observaciones o No Apto).
    """

    # Obtener modelos disponibles con soporte de generación
    modelos_a_probar = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-2.5-pro"]
    try:
        disponibles = [m.name.replace("models/", "") for m in client.models.list()]
        candidatos = [m for m in disponibles if "flash" in m or "pro" in m]
        if candidatos:
            modelos_a_probar = candidatos + [m for m in modelos_a_probar if m not in candidatos]
    except Exception:
        pass

    ultimo_error = None
    for mod in modelos_a_probar:
        for _ in range(2):
            try:
                res = client.models.generate_content(model=mod, contents=prompt)
                if res.text:
                    return res.text
            except Exception as e:
                ultimo_error = e
                time.sleep(1.5)

    raise RuntimeError(f"Servidores saturados momentáneamente. Detalle: {ultimo_error}")