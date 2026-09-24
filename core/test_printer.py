import io
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from core.questions_bank import obtener_datos_test

class CuadernilloNumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFillColor(colors.HexColor("#0E1E38"))
        self.rect(20, 762, 10, 10, fill=1, stroke=0)
        self.rect(582, 762, 10, 10, fill=1, stroke=0)
        self.rect(20, 20, 10, 10, fill=1, stroke=0)
        self.rect(582, 20, 10, 10, fill=1, stroke=0)

        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawString(36, 25, "DiSys 2026 | Sistema Integrado de Evaluación Técnica y Psicométrica")
        self.drawRightString(576, 25, f"Página {self._pageNumber} de {page_count}")
        self.restoreState()

def generar_cuadernillo_test_pdf(perfil_key: str, perfil_nombre: str) -> io.BytesIO:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=42
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'TestTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        alignment=1,
        textColor=colors.HexColor("#0E1E38")
    )
    
    instr_style = ParagraphStyle(
        'InstrStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#FF6B00")
    )
    
    q_num_style = ParagraphStyle(
        'QNumStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#0E1E38")
    )

    opt_style = ParagraphStyle(
        'OptStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#1E293B")
    )

    story = []
    
    datos_test = obtener_datos_test(perfil_key)
    if not datos_test:
        story.append(Paragraph(f"<b>DiSys 2026 | INSTRUMENTO PENDIENTE POR CARGAR</b>", title_style))
        story.append(Spacer(1, 10))
        story.append(Paragraph(f"El perfil <b>{perfil_nombre}</b> aún no tiene reactivos cargados en el banco oficial.", opt_style))
        doc.build(story)
        buffer.seek(0)
        return buffer

    codigo_instrumento = datos_test.get("codigo", "CJS")
    titulo_test = datos_test.get("titulo", f"EVALUACIÓN: {perfil_nombre.upper()}")
    instrucciones = datos_test.get("instrucciones", "Marque con una equis [X] una sola opción por pregunta.")
    preguntas_dict = datos_test.get("preguntas", {})

    story.append(Paragraph(f"<b>DiSys 2026 | {titulo_test} ({codigo_instrumento})</b>", title_style))
    story.append(Spacer(1, 4))

    ficha_data = [
        [Paragraph("<b>Nombres y Apellidos:</b> ___________________________________________________________", opt_style),
         Paragraph("<b>Fecha:</b> _____ / _____ / 2026", opt_style)],
        [Paragraph("<b>Cédula de Identidad:</b>  [  ] V   [  ] E   - __________________", opt_style),
         Paragraph(f"<b>Cargo:</b> {perfil_nombre}", opt_style)]
    ]
    t_ficha = Table(ficha_data, colWidths=[360, 180])
    t_ficha.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_ficha)
    story.append(Spacer(1, 4))

    story.append(Paragraph(f"<b>INSTRUCCIONES:</b> {instrucciones}", instr_style))
    story.append(Spacer(1, 6))

    for i in range(1, 31):
        q_info = preguntas_dict.get(i, {})
        enunciado = q_info.get("enunciado", f"Pregunta {i}")
        opciones = q_info.get("opciones", {})

        q_block = [
            [Paragraph(f"<b>{i}.</b> {enunciado}", q_num_style), ""]
        ]
        
        for letra in ["A", "B", "C", "D"]:
            texto_opc = opciones.get(letra, "")
            casilla_txt = f"<b>[&nbsp;&nbsp;&nbsp;&nbsp;] {letra}.</b>"
            q_block.append([
                Paragraph(casilla_txt, q_num_style),
                Paragraph(f"{texto_opc}", opt_style)
            ])

        t_q = Table(q_block, colWidths=[38, 502])
        t_q.setStyle(TableStyle([
            ('SPAN', (0,0), (1,0)),
            ('TOPPADDING', (0,0), (-1,-1), 1),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))
        
        story.append(KeepTogether([t_q, Spacer(1, 4)]))

    doc.build(story, canvasmaker=CuadernilloNumberedCanvas)
    buffer.seek(0)
    return buffer