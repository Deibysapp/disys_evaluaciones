import os
import streamlit as st
from google import genai

def obtener_cliente_gemini():
    api_key = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))
    if not api_key:
        raise ValueError("No se encontró la clave GEMINI_API_KEY en st.secrets ni en el entorno.")
    return genai.Client(api_key=api_key)

def peritar_evaluacion_con_gemini(cargo: str, datos_candidato: dict, respuestas_marcadas: dict, preguntas_contexto: list) -> str:
    """
    Analiza cualquier cargo de forma dinámica enviando un payload liviano de texto.
    Elimina por completo el error 503 por subida de archivos pesados.
    """
    client = obtener_cliente_gemini()

    # Formatear el cuestionario con las preguntas y las opciones marcadas
    detalle_cuestionario = []
    for num, item in enumerate(preguntas_contexto, start=1):
        pregunta_txt = item.get("pregunta", item.get("enunciado", f"Reactivo {num}"))
        opciones_txt = item.get("opciones", {})
        resp_candidato = respuestas_marcadas.get(num, "No contestada")
        
        texto_item = f"Pregunta {num}: {pregunta_txt}\n"
        if isinstance(opciones_txt, dict):
            for letra, desc in opciones_txt.items():
                texto_item += f"  [{letra}] {desc}\n"
        texto_item += f"  -> OPCIÓN MARCADA POR EL POSTULANTE: {resp_candidato}\n"
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
    1. Evalúa la idoneidad situacional de cada respuesta basándote estrictamente en las responsabilidades operativas, control interno, manejo de datos o inventario del cargo: {cargo}.
    2. Identifica los reactivos de sinceridad y autocrítica (L-Scale) y dictamina si el postulante muestra apertura honesta o deseabilidad social fingida.
    3. Detecta alertas críticas, riesgos operacionales o faltas éticas si las hubiere.
    4. Emite el informe pericial estructurado:
       - Resumen Cuantitativo (% de efectividad situacional y conteo de aciertos idóneos).
       - Desglose por Dimensiones Competenciales relevantes al cargo evaluado.
       - Auditoría de la Escala de Sinceridad (L-Scale).
       - Dictamen Ejecutivo y Recomendación Definitiva de Contratación (Apto Sobresaliente, Apto con Observaciones o No Apto).
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text