"""
DiSys 2026 - Motor de Calificación Automatizado (100% Test Escaneado)
Calcula el puntaje global sobre 100 puntos directos del test situacional.
"""

def analizar_prueba(cfg_perfil: dict, respuestas_candidato: dict, observaciones: str = "") -> dict:
    claves = cfg_perfil.get("claves", {})
    dimensiones = cfg_perfil.get("dimensiones", ["Dimensión 1", "Dimensión 2", "Dimensión 3", "Dimensión 4"])
    sinceridad_cfg = cfg_perfil.get("sinceridad", {})
    alertas_rojas_cfg = cfg_perfil.get("alertas_rojas", [])

    # 1. Calificación de Reactivos Operativos (24 preguntas clave)
    # Cada acierto vale 4.1667 pts para un total de 100 pts
    total_operativas = len(claves) if len(claves) > 0 else 24
    valor_por_acierto = 100.0 / total_operativas
    
    aciertos = 0
    puntaje_dimensiones = {dim: 0.0 for dim in dimensiones}
    
    # Asignación de reactivos por dimensión (6 por dimensión)
    lista_q = sorted(list(claves.keys()))
    q_por_dim = max(len(lista_q) // len(dimensiones), 1)

    for idx, q_num in enumerate(lista_q):
        resp_candidato = str(respuestas_candidato.get(q_num, "")).strip().upper()
        resp_correcta = str(claves[q_num]).strip().upper()
        
        dim_index = min(idx // q_por_dim, len(dimensiones) - 1)
        dim_nombre = dimensiones[dim_index]

        if resp_candidato == resp_correcta:
            aciertos += 1
            puntaje_dimensiones[dim_nombre] += valor_por_acierto

    puntaje_test = round(aciertos * valor_por_acierto, 2)
    puntaje_global = min(100.0, puntaje_test)

    # 2. Escala de Sinceridad (Distorsión / Deseabilidad Social)
    puntos_distorsion = 0
    for q_num, regla in sinceridad_cfg.items():
        resp_cand = str(respuestas_candidato.get(q_num, "")).strip().upper()
        if resp_cand == regla.get("trampa", "").upper():
            puntos_distorsion += 3

    instrumento_anulado = puntos_distorsion >= 9

    # 3. Detección de Alertas Rojas Éticas/Operativas
    alertas_detectadas = []
    for q_num in range(1, 31):
        resp_cand = str(respuestas_candidato.get(q_num, "")).strip().upper()
        if resp_cand:
            codigo_alerta = f"{q_num}{resp_cand}"
            if codigo_alerta in alertas_rojas_cfg:
                alertas_detectadas.append(codigo_alerta)

    tiene_alerta = len(alertas_detectadas) > 0

    # 4. Dictamen Final Automatizado
    if tiene_alerta:
        dictamen = "NO APTO (Alerta Roja Ética / Descarte Automático)"
    elif instrumento_anulado:
        dictamen = "ANULADO (Manipulación / Distorsión en Sinceridad)"
    elif puntaje_global >= 75.0:
        dictamen = "APTO (Candidato Idóneo Recomendado)"
    elif puntaje_global >= 60.0:
        dictamen = "APTO CON RESERVAS (Requiere Inducción Supervisada)"
    else:
        dictamen = "NO APTO (Puntaje Insuficiente)"

    return {
        "puntaje_total_ponderado": puntaje_global,
        "puntaje_fase1": puntaje_test,
        "aciertos": aciertos,
        "total_preguntas": total_operativas,
        "puntajes_dimensiones": puntaje_dimensiones,
        "puntos_distorsion": puntos_distorsion,
        "instrumento_anulado": instrumento_anulado,
        "tiene_alerta": tiene_alerta,
        "alertas_detectadas": alertas_detectadas,
        "dictamen": dictamen
    }