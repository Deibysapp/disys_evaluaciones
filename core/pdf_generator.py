from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
import io
import os

def generar_pdf_dictamen_ia(datos_candidato: dict, dictamen_texto: str, cargo: str) -> bytes:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    
    # Estilos corporativos DiSys
    estilo_titulo = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.HexColor('#0E1E38'),
        alignment=TA_CENTER
    )
    estilo_sub = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#FF6B00'),
        alignment=TA_CENTER
    )
    estilo_campo_lbl = ParagraphStyle(
        'LabelField',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#0E1E38')
    )
    estilo_campo_val = ParagraphStyle(
        'ValField',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#333333')
    )
    estilo_cuerpo = ParagraphStyle(
        'BodyDictamen',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#1E293B'),
        alignment=TA_JUSTIFY,
        spaceAfter=6
    )
    estilo_subtitulo_peritaje = ParagraphStyle(
        'H2Dictamen',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#0E1E38'),
        spaceBefore=8,
        spaceAfter=4
    )

    story = []

    # Encabezado
    story.append(Paragraph("DISYS 2026 - SISTEMA DE AUDITORÍA Y PERITAJE TÉCNICO", estilo_titulo))
    story.append(Spacer(1, 2))
    story.append(Paragraph("DICTAMEN PERICIAL PSICOTÉCNICO SITUACIONAL", estilo_sub))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#FF6B00'), spaceAfter=10))

    # Ficha técnica del aspirante
    tabla_data = [
        [
            Paragraph("<b>Postulante:</b>", estilo_campo_lbl),
            Paragraph(datos_candidato.get("nombre", ""), estilo_campo_val),
            Paragraph("<b>Cédula:</b>", estilo_campo_lbl),
            Paragraph(datos_candidato.get("cedula", ""), estilo_campo_val),
        ],
        [
            Paragraph("<b>Cargo Postulado:</b>", estilo_campo_lbl),
            Paragraph(cargo, estilo_campo_val),
            Paragraph("<b>Fecha:</b>", estilo_campo_lbl),
            Paragraph(datos_candidato.get("fecha", ""), estilo_campo_val),
        ],
        [
            Paragraph("<b>Sede / Sucursal:</b>", estilo_campo_lbl),
            Paragraph(datos_candidato.get("sucursal", "Planta Central"), estilo_campo_val),
            Paragraph("<b>Evaluador:</b>", estilo_campo_lbl),
            Paragraph(datos_candidato.get("evaluador", "Auditoría"), estilo_campo_val),
        ]
    ]

    t_info = Table(tabla_data, colWidths=[85, 200, 75, 180])
    t_info.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8F9FA')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.3, colors.HexColor('#E2E8F0')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_info)
    story.append(Spacer(1, 12))

    # Parsear texto del informe generado
    lineas = dictamen_texto.split('\n')
    for linea in lineas:
        txt = linea.strip()
        if not txt:
            story.append(Spacer(1, 3))
            continue
        # Limpieza básica de Markdown
        txt_limpio = txt.replace("**", "<b>").replace("__", "<b>")
        if "<b>" in txt_limpio and not "</b>" in txt_limpio:
            txt_limpio += "</b>"

        if txt.startswith("#") or txt.isupper() and len(txt) < 60:
            txt_tit = txt.lstrip("#").strip().replace("*", "")
            story.append(Paragraph(txt_tit, estilo_subtitulo_peritaje))
        elif txt.startswith(("*", "-", "•")):
            item_txt = txt.lstrip("*-•").strip()
            story.append(Paragraph(f"• {item_txt}", estilo_cuerpo))
        else:
            story.append(Paragraph(txt_limpio, estilo_cuerpo))

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()