import streamlit as st
import os
import uuid
from datetime import datetime
from core.database import SessionLocal, Usuario, Evaluacion, verify_password, get_password_hash
from core.profiles_data import CATALOGO_PERFILES
from core.test_printer import generar_cuadernillo_test_pdf
from core.questions_bank import BANCO_PREGUNTAS
from core.ai_evaluator import peritar_evaluacion_con_gemini

st.set_page_config(
    page_title="DiSys 2026 - Plataforma de Selección Técnica",
    page_icon="assets/logo.png" if os.path.exists("assets/logo.png") else "🏢",
    layout="wide"
)

st.markdown("""
<style>
    :root {
        --disys-blue: #0E1E38;
        --disys-orange: #FF6B00;
        --disys-light: #F8F9FA;
    }
    .main-header {
        background-color: #0E1E38;
        padding: 15px 25px;
        border-radius: 8px;
        color: white;
        margin-bottom: 20px;
        border-left: 6px solid #FF6B00;
    }
    .stButton>button {
        background-color: #FF6B00 !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 6px !important;
        border: none !important;
        height: 50px;
        font-size: 16px !important;
    }
</style>
""", unsafe_allow_html=True)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.user = None

def login(username, password):
    db = SessionLocal()
    try:
        user = db.query(Usuario).filter(Usuario.username == username).first()
        if user and user.activo:
            if verify_password(password, user.password_hash):
                st.session_state.authenticated = True
                st.session_state.user = {
                    "id": user.id,
                    "username": user.username,
                    "nombre": user.nombre_completo,
                    "rol": user.rol,
                    "sucursal": user.sucursal
                }
                user.intentos_fallidos = 0
                db.commit()
                return True
            else:
                user.intentos_fallidos += 1
                db.commit()
        return False
    finally:
        db.close()

def logout():
    st.session_state.authenticated = False
    st.session_state.user = None
    st.rerun()

# -------------------------------------------------------------
# LOGIN
# -------------------------------------------------------------
if not st.session_state.authenticated:
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<br/><br/>", unsafe_allow_html=True)
        if os.path.exists("assets/logo.png"):
            st.image("assets/logo.png", width=320)
        else:
            st.title("DiSys 2026")
            st.caption("Tecnología para la distribución eficiente")
            
        st.markdown("### Acceso al Sistema de Auditoría y Evaluación")
        with st.form("form_login"):
            u_input = st.text_input("Usuario")
            p_input = st.text_input("Contraseña", type="password")
            btn_login = st.form_submit_button("INGRESAR AL SISTEMA")
            if btn_login:
                if login(u_input, p_input):
                    st.success("Acceso autorizado.")
                    st.rerun()
                else:
                    st.error("Credenciales incorrectas o usuario suspendido.")
    st.stop()

# -------------------------------------------------------------
# BARRA LATERAL
# -------------------------------------------------------------
with st.sidebar:
    if os.path.exists("assets/logo.png"):
        st.image("assets/logo.png", use_container_width=True)
    st.markdown(f"**Usuario:** {st.session_state.user['nombre']}")
    st.markdown(f"**Rol:** `{st.session_state.user['rol']}` | **Sede:** {st.session_state.user['sucursal']}")
    st.markdown("---")
    
    opciones_menu = ["Nueva Evaluación (Auditoría Pericial)", "Historial de Expedientes"]
    if st.session_state.user["rol"] == "MASTER":
        opciones_menu.append("Panel Master (Gestión de Usuarios)")
        
    menu_seleccionado = st.radio("Navegación:", opciones_menu)
    st.markdown("---")
    if st.button("Cerrar Sesión"):
        logout()

# -------------------------------------------------------------
# NUEVA EVALUACIÓN (PERITAJE DINÁMICO UNIVERSAL CON IA)
# -------------------------------------------------------------
if menu_seleccionado == "Nueva Evaluación (Auditoría Pericial)":
    st.markdown("""
    <div class="main-header">
        <h2 style='margin:0;'>Auditoría Pericial Psicotécnica con Inteligencia Artificial</h2>
        <p style='margin:0; font-size:13px; opacity:0.9;'>Selecciona el perfil, registra las opciones marcadas por el postulante y genera el dictamen oficial DiSys</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 1. Datos y Selección del Perfil
    with st.expander("1. DATOS DEL POSTULANTE Y PERFIL A EVALUAR", expanded=True):
        c1, c2, c3 = st.columns(3)
        with c1:
            candidato_nombre = st.text_input("Nombres y Apellidos")
            candidato_cedula = st.text_input("Cédula de Identidad (ej. V-12345678)")
        with c2:
            perfiles_keys = sorted(list(BANCO_PREGUNTAS.keys()))
            def formatear_perfil(k):
                datos = BANCO_PREGUNTAS.get(k, {})
                cod = datos.get("codigo", "")
                tit = datos.get("titulo", k)
                nombre_limpio = tit.replace("EVALUACIÓN PSICOTÉCNICA SITUACIONAL EN ", "").replace("EVALUACIÓN PSICOTÉCNICA COMERCIAL EN ", "").strip()
                return f"{nombre_limpio.title()} ({cod})"

            perfil_sel = st.selectbox("Seleccione Perfil Organizacional:", perfiles_keys, format_func=formatear_perfil)
            sucursal_eval = st.text_input("Sede / Sucursal", value=st.session_state.user["sucursal"])
        with c3:
            fecha_eval = st.date_input("Fecha de Aplicación", datetime.now())
            evaluador_nom = st.text_input("Evaluador Responsable", value=st.session_state.user["nombre"])

        cfg_perfil = CATALOGO_PERFILES.get(perfil_sel, {"nombre": perfil_sel, "departamento": "GENERAL"})
        preguntas_actuales = BANCO_PREGUNTAS.get(perfil_sel, {}).get("preguntas", [])

        st.markdown("---")
        col_dl1, col_dl2 = st.columns([2, 1])
        with col_dl1:
            st.info(f"Instrumento seleccionado: **{cfg_perfil['nombre']}** ({len(preguntas_actuales)} reactivos cargados)")
        with col_dl2:
            pdf_cuadernillo = generar_cuadernillo_test_pdf(perfil_sel, cfg_perfil['nombre'])
            st.download_button(
                label="📄 IMPRIMIR TEST EN BLANCO",
                data=pdf_cuadernillo,
                file_name=f"Test_{perfil_sel}_{cfg_perfil['nombre'].replace(' ', '_')}.pdf",
                mime="application/pdf"
            )

    # 2. Captura Rápida de Respuestas del Aspirante
    with st.expander("2. RESPUESTAS MARCADAS POR EL CANDIDATO (1 al 30)", expanded=True):
        st.caption("Seleccione las alternativas marcadas por el aspirante en su hoja de examen:")
        
        # Grilla organizada de 5 columnas para marcar en 15 segundos
        respuestas_ingresadas = {}
        cols = st.columns(5)
        total_items = len(preguntas_actuales) if preguntas_actuales else 30
        
        for i in range(1, total_items + 1):
            col_idx = (i - 1) % 5
            with cols[col_idx]:
                opcion = st.selectbox(
                    f"Ítem {i:02d}",
                    ["A", "B", "C", "D"],
                    key=f"item_{i}",
                    index=0
                )
                respuestas_ingresadas[i] = opcion

        # Tira resumen compacta
        tira_txt = " | ".join([f"<b>{k:02d}:</b> {v}" for k, v in respuestas_ingresadas.items()])
        st.markdown(f"<div style='background-color:#F1F5F9; padding:10px; border-radius:5px; font-family:monospace; margin-top:10px;'><b>Tira de respuestas:</b> {tira_txt}</div>", unsafe_allow_html=True)

    # Botón de Peritaje
    st.markdown("<br/>", unsafe_allow_html=True)
    if st.button("ANALIZAR EVALUACIÓN Y GENERAR DICTAMEN PERICIAL CON IA", use_container_width=True):
        if not candidato_nombre or not candidato_cedula:
            st.error("Debe ingresar el nombre y la cédula de identidad del aspirante.")
        else:
            with st.spinner("Procesando auditoría técnica y redactando informe pericial con IA..."):
                try:
                    datos_aspirante = {
                        "nombre": candidato_nombre,
                        "cedula": candidato_cedula,
                        "cargo": cfg_perfil["nombre"],
                        "sucursal": sucursal_eval,
                        "fecha": fecha_eval.strftime("%d/%m/%Y"),
                        "evaluador": evaluador_nom
                    }

                    informe_resultado = peritar_evaluacion_con_gemini(
                        cargo=cfg_perfil["nombre"],
                        datos_candidato=datos_aspirante,
                        respuestas_marcadas=respuestas_ingresadas,
                        preguntas_contexto=preguntas_actuales
                    )

                    codigo_exp = f"EXP-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"

                    # Guardar registro en BD
                    db = SessionLocal()
                    try:
                        nueva_eval = Evaluacion(
                            codigo_expediente=codigo_exp,
                            candidato_nombre=candidato_nombre,
                            candidato_cedula=candidato_cedula,
                            perfil_evaluado=cfg_perfil["nombre"],
                            evaluador_username=st.session_state.user["username"],
                            sucursal=sucursal_eval,
                            puntaje_fase1=100.0,
                            puntaje_fase2=0.0,
                            puntaje_total_ponderado=100.0,
                            sinceridad_distorsion=0,
                            alerta_roja=False,
                            detalle_alerta="Peritaje dinámico completado.",
                            dictamen_final="Auditado por IA"
                        )
                        db.add(nueva_eval)
                        db.commit()
                    finally:
                        db.close()

                    st.success("Dictamen pericial emitido con éxito.")
                    st.markdown("---")
                    st.markdown(informe_resultado)

                    st.download_button(
                        label="📥 DESCARGAR INFORME PERICIAL OFICIAL (.TXT)",
                        data=informe_resultado,
                        file_name=f"Dictamen_{candidato_cedula}_{cfg_perfil['nombre'].replace(' ', '_')}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )

                except Exception as e:
                    st.error(f"Error procesando el peritaje: {str(e)}")

# -------------------------------------------------------------
# HISTORIAL
# -------------------------------------------------------------
elif menu_seleccionado == "Historial de Expedientes":
    st.markdown("""
    <div class="main-header">
        <h2 style='margin:0;'>Historial y Auditoría de Expedientes Evaluados</h2>
        <p style='margin:0; font-size:13px; opacity:0.9;'>Consulta de evaluaciones procesadas por sede</p>
    </div>
    """, unsafe_allow_html=True)
    
    db = SessionLocal()
    try:
        query = db.query(Evaluacion)
        if st.session_state.user["rol"] != "MASTER":
            query = query.filter(Evaluacion.sucursal == st.session_state.user["sucursal"])
        registros = query.order_by(Evaluacion.fecha_evaluacion.desc()).all()
        
        if registros:
            tabla = []
            for r in registros:
                tabla.append({
                    "Expediente": r.codigo_expediente,
                    "Fecha": r.fecha_evaluacion.strftime("%d/%m/%Y"),
                    "Candidato": r.candidato_nombre,
                    "Cédula": r.candidato_cedula,
                    "Perfil": r.perfil_evaluado,
                    "Puntaje": f"{r.puntaje_total_ponderado} pts",
                    "Dictamen": r.dictamen_final,
                    "Evaluador": r.evaluador_username
                })
            st.dataframe(tabla, use_container_width=True)
        else:
            st.info("No hay evaluaciones registradas en el historial.")
    finally:
        db.close()

# -------------------------------------------------------------
# PANEL MASTER
# -------------------------------------------------------------
elif menu_seleccionado == "Panel Master (Gestión de Usuarios)":
    st.markdown("""
    <div class="main-header">
        <h2 style='margin:0;'>Panel Master - Gestión de Usuarios y Accesos</h2>
        <p style='margin:0; font-size:13px; opacity:0.9;'>Creación, asignación de sedes y revocación inmediata de cuentas</p>
    </div>
    """, unsafe_allow_html=True)
    
    tab_crear, tab_listar = st.tabs(["Crear Evaluador", "Evaluadores Activos y Suspender"])
    
    with tab_crear:
        with st.form("form_alta_usuario"):
            c_u1, c_u2 = st.columns(2)
            with c_u1:
                nuevo_nom = st.text_input("Nombre y Apellido")
                nuevo_user = st.text_input("Nombre de Usuario (Login)")
                nuevo_pass = st.text_input("Contraseña", type="password")
            with c_u2:
                nuevo_rol = st.selectbox("Rol", ["EVALUADOR", "MASTER"])
                nueva_suc = st.text_input("Sucursal / Sede", value="Planta Central")
                
            if st.form_submit_button("REGISTRAR EVALUADOR"):
                if not nuevo_user or not nuevo_pass or not nuevo_nom:
                    st.error("Todos los datos son obligatorios.")
                else:
                    db = SessionLocal()
                    try:
                        existe = db.query(Usuario).filter(Usuario.username == nuevo_user).first()
                        if existe:
                            st.error(f"El usuario '{nuevo_user}' ya existe.")
                        else:
                            u_obj = Usuario(
                                nombre_completo=nuevo_nom,
                                username=nuevo_user,
                                password_hash=get_password_hash(nuevo_pass),
                                rol=nuevo_rol,
                                sucursal=nueva_suc,
                                activo=True
                            )
                            db.add(u_obj)
                            db.commit()
                            st.success(f"Evaluador '{nuevo_user}' registrado exitosamente.")
                    finally:
                        db.close()
                        
    with tab_listar:
        db = SessionLocal()
        try:
            usuarios_bd = db.query(Usuario).all()
            for usr in usuarios_bd:
                col_u1, col_u2, col_u3, col_u4 = st.columns([2, 2, 1.5, 1.5])
                col_u1.markdown(f"**{usr.nombre_completo}** (`{usr.username}`)")
                col_u2.markdown(f"Rol: `{usr.rol}` | Sede: {usr.sucursal}")
                col_u3.markdown(f"{'🟢 Activo' if usr.activo else '🔴 Suspendido'}")
                if usr.username != st.session_state.user["username"]:
                    btn_label = "Suspender" if usr.activo else "Activar"
                    if col_u4.button(btn_label, key=f"btn_usr_{usr.id}"):
                        usr.activo = not usr.activo
                        db.commit()
                        st.rerun()
                else:
                    col_u4.caption("Sesión Activa")
                st.markdown("---")
        finally:
            db.close()