import os
import time
import tempfile
import streamlit as st
from google import genai

def obtener_cliente_gemini():
    api_key = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))
    if not api_key:
        raise ValueError("No se encontró la clave GEMINI_API_KEY en st.secrets ni en el entorno.")
    return genai.Client(api_key=api_key)

def analizar_test_con_gemini(pdf_bytes: bytes) -> str:
    client = obtener_cliente_gemini()

    # 1. Guardar temporalmente en disco para subirlo limpiamente a la Files API
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(pdf_bytes)
        tmp_path = tmp_file.name

    try:
        # Subida oficial mediante ruta de archivo
        archivo_subido = client.files.upload(file=tmp_path)

        # Esperar confirmación de procesamiento si aplica
        while getattr(archivo_subido, "state", None) and archivo_subido.state.name == "PROCESSING":
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

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=[archivo_subido, prompt_instrucciones]
        )
        return response.text

    finally:
        # Limpieza del archivo temporal local
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        # Limpieza del archivo en Google Files API
        try:
            client.files.delete(name=archivo_subido.name)
        except Exception:
            pass