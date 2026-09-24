import os
import io
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

# Diccionario de descripciones operativas de Alertas Rojas
SIGNIFICADO_ALERTAS = {
    "1A": "Vulneración directa de normas de control interno o desvío de procedimientos de apertura/cierre.",
    "1B": "Falta de rigor en la custodia de documentos o activos asignados.",
    "2A": "Omisión de verificación en inventarios físicos o discrepancias de stock no reportadas.",
    "2C": "Riesgo en transporte de mercancías o negligencia en el trato de activos de distribución.",
    "2D": "Manejo inadecuado de carga pesada o violación de normas de seguridad física en almacén.",
    "3B": "Incumplimiento deliberado en tiempos de entrega o falseamiento de reportes de visita.",
    "3C": "Discrecionalidad indebida en otorgamiento de créditos sin respaldo financiero.",
    "5A": "Negligencia grave en el control de acceso de personas ajenas a las instalaciones.",
    "5B": "Permisividad en la salida de vehículos o mercancía sin documentación legal autorizada.",
    "6D": "Abandono de puesto de vigilancia o desatención durante rondas de seguridad perimétrica.",
    "7D": "Falta de reporte inmediato ante siniestros, pérdidas o roturas en ruta.",
    "8C": "Alteración de comprobantes de pago o registros contables manuales.",
    "10A": "Manejo indebido de efectivo, retención de cobranzas o depósitos fuera del lapso reglamentario.",
    "10B": "Conflicto de interés o tolerancia ante irregularidades cometidas por terceros/clientes.",
    "10C": "Omisión en declaraciones fiscales que expone a la empresa a sanciones del SENIAT.",
    "11D": "Ocultamiento de errores en conciliaciones bancarias o saldos deudores.",
    "12A": "Desatención reiterada a clientes morosos, provocando incobrabilidad de cartera.",
    "12C": "Uso no autorizado de la flota de transporte para fines personales o rutas no planificadas.",
    "13B": "Despacho de pedidos sin factura o sin la debida nota de entrega sellada.",
    "16A": "Propensión a la confrontación con clientes, supervisores o compañeros de equipo.",
    "16B": "Desobediencia ante directrices de gerencia en políticas de descuento o promociones.",
    "16C": "Falta de confidencialidad en manejo de cifras de ventas, costos o sueldos de la empresa.",
    "17B": "Desinterés por normas de bioseguridad, orden y limpieza (5S) en áreas operativas.",
    "17D": "Manipulación de parámetros en sistemas de gestión sin previa autorización técnica.",
    "18A": "Complicidad pasiva ante sustracción de mercancía o materiales en custodia.",
    "18C": "Acuerdos indebidos con clientes para condonar intereses o postergar vencimientos.",
    "19A": "Falsedad testimonial comprobada o autoatribución de resultados inexistentes.",
    "19D": "Deseabilidad social extrema: tendencia a simular perfección moral irreal.",
    "20D": "Aprobación de gastos o desembolsos sin soporte físico de factura legal.",
    "21C": "Rechazo a la rotación de turnos o resistencia activa al trabajo en equipo en contingencias.",
    "22C": "Ajuste unilateral de libros contables sin la firma del contador principal.",
    "23B": "Promesa de despachos con precios o condiciones no autorizadas por la Dirección Comercial.",
    "23C": "Conducción temeraria o maltrato deliberado a la unidad automotor de despacho.",
    "23D": "Subestimación del riesgo de averías mecánicas y omisión de mantenimiento preventivo.",
    "25A": "Justificación de faltas éticas bajo el argumento de 'así lo hacen todos'.",
    "25B": "Obstrucción en auditorías internas o negativa a entregar recaudos a revisores.",
    "26A": "Recepción de pagos directos de clientes en cuentas particulares o sin recibo oficial.",
    "26C": "Modificación manual de listas de precios sin autorización de la Gerencia.",
    "27A": "Permisión del ingreso de visitantes armados o sin identificación a las zonas de carga.",
    "27C": "Encubrimiento de mermas de producto atribuibles a negligencia operativa.",
    "30A": "Predisposición al reclamo hostil o desvinculación conflictiva ante llamados de atención.",
    "30D": "Deslealtad corporativa comprobada: difusión de información sensible de la empresa."
}

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_watermark_and_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_watermark_and_page_number(self, page_count):
        self.saveState()
        # Marca de agua institucional diagonal
        self.setFont("Helvetica-Bold", 65)
        self.setFillColor(colors.HexColor("#0E1E38"), alpha=0.07)
        self.translate(300, 390)
        self.rotate(45)
        self.drawCentredString(0, 0, "DiSys 2026")
        self.restoreState()
        
        # Pie de página de auditoría
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#475569"))
        footer_text = f"DiSys 2026 | Informe Técnico de Evaluación Psicométrica y Operativa | Página {self._pageNumber} de {page_count}"
        self.drawRightString(576, 22, footer_text)
        self.drawString(36, 22, "CONFIDENCIAL - USO EXCLUSIVO DE TALENTO HUMANO Y GERENCIA GENERAL")
        self.restoreState()

def generar_pdf_evaluacion(datos_candidato: dict, resultados: dict, perfil_nombre: str) -> io.BytesIO:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=32,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    
    # Estilos tipográficos
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#0E1E38")
    )
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#FF6B00")
    )
    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#1E293B")
    )
    body_bold = ParagraphStyle(
        'DocBodyBold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )
    header_table_style = ParagraphStyle(
        'HTable',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )
    alert_text_style = ParagraphStyle(
        'AlertText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#991B1B")
    )

    story = []
    
    # -------------------------------------------------------------
    # PÁGINA 1: CABECERA, DATOS GENERALES, DICTAMEN Y MATRIZ
    # -------------------------------------------------------------
    logo_path = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.png")
    if os.path.exists(logo_path):
        logo_element = RLImage(logo_path, width=130, height=45)
    else:
        logo_element = Paragraph("<b>DiSys</b><br/><font size=7 color='#64748B'>Tecnología para la distribución eficiente</font>", title_style)
        
    header_data = [
        [logo_element, Paragraph("<b>INFORME TÉCNICO OFICIAL DE EVALUACIÓN</b><br/>"
                                 "<font size=8 color='#475569'>DIRECCIÓN DE TALENTO HUMANO Y AUDITORÍA OPERATIVA</font><br/>"
                                 f"<font size=8 color='#FF6B00'>CÓDIGO EXPEDIENTE: {datos_candidato.get('codigo_expediente', 'EXP-2026')}</font>", title_style)]
    ]
    t_header = Table(header_data, colWidths=[150, 390])
    t_header.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_header)
    story.append(Spacer(1, 4))
    
    # Ficha del evaluado
    datos_box = [
        [Paragraph("<b>Candidato:</b>", body_style), Paragraph(datos_candidato.get("nombre", ""), body_bold),
         Paragraph("<b>Cédula:</b>", body_style), Paragraph(datos_candidato.get("cedula", ""), body_bold)],
        [Paragraph("<b>Cargo Postulado:</b>", body_style), Paragraph(perfil_nombre, body_style),
         Paragraph("<b>Fecha:</b>", body_style), Paragraph(datos_candidato.get("fecha", datetime.now().strftime("%d/%m/%Y")), body_style)],
        [Paragraph("<b>Sucursal / Sede:</b>", body_style), Paragraph(datos_candidato.get("sucursal", "Principal"), body_style),
         Paragraph("<b>Evaluador:</b>", body_style), Paragraph(datos_candidato.get("evaluador", "Sistema"), body_style)]
    ]
    t_datos = Table(datos_box, colWidths=[90, 200, 75, 175])
    t_datos.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_datos)
    story.append(Spacer(1, 8))
    
    # Lógica de Color para el Dictamen
    dictamen_str = resultados.get("dictamen", "")
    if "NO APTO" in dictamen_str or "ANULADO" in dictamen_str or resultados.get("tiene_alerta", False):
        color_dictamen = colors.HexColor("#DC2626")  # Rojo Intenso
        nivel_riesgo_global = "ALTO / NO RECOMENDADO"
        color_riesgo = colors.HexColor("#DC2626")
    elif "RESERVAS" in dictamen_str:
        color_dictamen = colors.HexColor("#D97706")  # Ámbar Advertencia
        nivel_riesgo_global = "MEDIO / CONDICIONADO A CAPACITACIÓN"
        color_riesgo = colors.HexColor("#D97706")
    else:
        color_dictamen = colors.HexColor("#16A34A")  # Verde Aprobado
        nivel_riesgo_global = "BAJO / CONFORME A PERFIL"
        color_riesgo = colors.HexColor("#16A34A")

    dictamen_data = [
        [Paragraph(f"<font color='white'><b>DICTAMEN FINAL: {dictamen_str}</b></font>", header_table_style)],
        [Paragraph(f"<b>Puntuación Global del Test:</b> <b>{resultados['puntaje_total_ponderado']} / 100 pts</b> &nbsp;|&nbsp; "
                   f"<b>Efectividad Operativa:</b> {resultados.get('aciertos', 24)} / {resultados.get('total_preguntas', 24)} reactivos correctos", body_style)]
    ]
    t_dictamen = Table(dictamen_data, colWidths=[540])
    t_dictamen.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), color_dictamen),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor("#FFFFFF")),
        ('BOX', (0,0), (-1,-1), 1.5, color_dictamen),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_dictamen)
    story.append(Spacer(1, 8))

    # Diagnóstico Psicométrico y Filtros de Seguridad (Sin Fase 2)
    p_dist = resultados.get("puntos_distorsion", 0)
    if p_dist <= 3:
        sinc_diag = "<b>Confiable (0 a 3 pts):</b> El candidato respondió con honestidad y autocrítica real. Bajo nivel de falseamiento."
    elif p_dist <= 6:
        sinc_diag = "<b>Observación Moderada (6 pts):</b> Tendencia a mostrar una imagen socialmente deseable. Requiere validación de referencias."
    else:
        sinc_diag = "<b>CRÍTICO / MANIPULACIÓN (≥9 pts):</b> El aspirante intentó deliberadamente proyectar un perfil perfecto irreal. Test sin validez técnica."

    filtros_data = [
        [Paragraph("<b>PARÁMETRO DE AUDITORÍA</b>", header_table_style), Paragraph("<b>DIAGNÓSTICO TÉCNICO Y OBSERVACIÓN</b>", header_table_style)],
        [Paragraph("<b>Escala de Sinceridad:</b><br/>" + f"<font size=7 color='#64748B'>{p_dist} / 18 pts distorsión</font>", body_style),
         Paragraph(sinc_diag, body_style)],
        [Paragraph("<b>Alertas Rojas Operativas:</b>", body_style), 
         Paragraph(f"<b>{'NINGUNA' if not resultados['tiene_alerta'] else 'CRÍTICAS DETECTADAS (' + str(len(resultados['alertas_detectadas'])) + ')'}:</b> "
                   f"{'Cumplimiento ético estándar.' if not resultados['tiene_alerta'] else 'El aspirante seleccionó alternativas de alto riesgo moral u operativo: ' + ', '.join(resultados['alertas_detectadas'])}", body_style)],
        [Paragraph("<b>Metodología de Calificación:</b>", body_style), Paragraph("Evaluación psicotécnica y situacional automatizada mediante lectura óptica de reactivos.", body_style)]
    ]
    t_filtros = Table(filtros_data, colWidths=[160, 380])
    t_filtros.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0E1E38")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_filtros)
    story.append(Spacer(1, 8))
    
    # Desglose de Competencias y Diagnóstico Analítico por Área
    comp_data = [[
        Paragraph("<b>COMPETENCIA / DIMENSIÓN EVALUADA</b>", header_table_style), 
        Paragraph("<b>PUNTAJE</b>", header_table_style), 
        Paragraph("<b>EFECTIVIDAD</b>", header_table_style),
        Paragraph("<b>DIAGNÓSTICO OPERATIVO</b>", header_table_style)
    ]]
    
    for dim_nom, dim_pts in resultados.get("puntajes_dimensiones", {}).items():
        pct = (dim_pts / 18.0) * 100.0
        if pct >= 80:
            diag_dim = "<b>Dominio Alto:</b> Ejecuta con apego pleno a normativas y criterio autónomo."
        elif pct >= 60:
            diag_dim = "<b>Nivel Aceptable:</b> Conoce los procesos pero requiere supervisión en contingencias."
        elif pct >= 40:
            diag_dim = "<b>Brecha Crítica:</b> Presenta fallas conceptuales que pueden derivar en errores en ruta/sede."
        else:
            diag_dim = "<b>Deficiente:</b> Desconocimiento severo de los procedimientos operativos básicos."
            
        comp_data.append([
            Paragraph(dim_nom, body_style),
            Paragraph(f"{dim_pts} / 18", body_style),
            Paragraph(f"{pct:.1f}%", body_bold),
            Paragraph(diag_dim, body_style)
        ])
        
    t_comp = Table(comp_data, colWidths=[150, 65, 75, 250])
    t_comp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#FF6B00")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_comp)
    story.append(Spacer(1, 10))

    # -------------------------------------------------------------
    # PÁGINA 2: DESGLOSE ANALÍTICO DE RIESGOS, ALERTAS Y RECOMENDACIÓN
    # -------------------------------------------------------------
    story.append(PageBreak())
    
    story.append(Paragraph("<b>ANÁLISIS PERICIAL DE RIESGOS Y ALERTAS DETECTADAS</b>", subtitle_style))
    story.append(Spacer(1, 4))
    
    if resultados.get("tiene_alerta", False):
        alertas_rows = [
            [Paragraph("<b>ÍTEM Y RESPUESTA</b>", header_table_style), 
             Paragraph("<b>CONDUCTA DETECTADA Y RIESGO PARA LA ORGANIZACIÓN</b>", header_table_style)]
        ]
        for alerta_cod in resultados["alertas_detectadas"]:
            desc = SIGNIFICADO_ALERTAS.get(alerta_cod, "Desviación crítica de procedimientos operativos o directriz ética de la empresa.")
            alertas_rows.append([
                Paragraph(f"<b>Reactivo {alerta_cod}</b>", body_bold),
                Paragraph(desc, alert_text_style)
            ])
            
        t_alertas_desc = Table(alertas_rows, colWidths=[110, 430])
        t_alertas_desc.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#991B1B")),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#FCA5A5")),
            ('BACKGROUND', (0,1), (-1,-1), colors.HexColor("#FEF2F2")),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#FECACA")),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ]))
        story.append(t_alertas_desc)
    else:
        story.append(Paragraph("<i>No se evidenciaron conductas de descarte automático ni transgresiones normativas en los reactivos del instrumento. El perfil evidencia compatibilidad con el marco ético institucional.</i>", body_style))
        
    story.append(Spacer(1, 12))
    
    # Matriz Diagnóstica Concluyente
    story.append(Paragraph("<b>CONCLUSIONES Y RECOMENDACIÓN DE CONTRATACIÓN</b>", subtitle_style))
    story.append(Spacer(1, 4))
    
    if "NO APTO" in dictamen_str or "ANULADO" in dictamen_str:
        conclusion_texto = (
            f"El postulante <b>{datos_candidato.get('nombre')}</b> presenta indicadores de <b>alto riesgo operacional y/o conductual</b>. "
            f"La combinación de alertas rojas éticas y/o distorsión en la sinceridad anula la confiabilidad de su desempeño autónomo. "
            f"<b>Dictamen de Auditoría: DESESTIMAR POSTULACIÓN.</b> No se recomienda su incorporación a las rutas, almacén o gestión administrativa."
        )
    elif "RESERVAS" in dictamen_str:
        conclusion_texto = (
            f"El postulante <b>{datos_candidato.get('nombre')}</b> demuestra competencias básicas para el puesto pero evidencia <b>brechas formativas</b> "
            f"en áreas operativas clave. <b>Dictamen de Auditoría: CONTRATACIÓN CONDICIONADA.</b> En caso de avanzar en su ingreso, se requiere asignarle "
            f"acompañamiento continuo durante los primeros 45 días y someterlo a reevaluación técnica al concluir su período de prueba."
        )
    else:
        conclusion_texto = (
            f"El postulante <b>{datos_candidato.get('nombre')}</b> cumple satisfactoriamente con los estándares psicotécnicos, procedimentales y prácticos "
            f"exigidos para el cargo de <b>{perfil_nombre}</b>. <b>Dictamen de Auditoría: CANDIDATO IDÓNEO RECOMENDADO.</b> Su nivel de apego ético y destreza "
            f"de campo garantizan una integración fluida a las operaciones de la empresa."
        )
        
    obs_ingresadas = datos_candidato.get("observaciones", "").strip()
    if obs_ingresadas:
        conclusion_texto += f"<br/><br/><b>Observaciones particulares del evaluador de campo:</b> {obs_ingresadas}"

    t_conclusion = Table([[Paragraph(conclusion_texto, body_style)]], colWidths=[540])
    t_conclusion.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_conclusion)
    story.append(Spacer(1, 35))
    
    # Firmas de Validación Pericial
    firmas_data = [
        [Paragraph("________________________________________<br/><b>Evaluador Responsable</b><br/>Talento Humano / Operaciones", body_style),
         Paragraph("________________________________________<br/><b>Gerencia de Área / Dirección</b><br/>Validación Institucional", body_style),
         Paragraph("________________________________________<br/><b>Firma del Evaluado</b><br/>C.I.: " + datos_candidato.get("cedula", ""), body_style)]
    ]
    t_firmas = Table(firmas_data, colWidths=[180, 180, 180])
    t_firmas.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(KeepTogether(t_firmas))
    
    doc.build(story, canvasmaker=NumberedCanvas)
    buffer.seek(0)
    return buffer