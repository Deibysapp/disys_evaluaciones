CATALOGO_PERFILES = {
    "11_ASESOR_DE_VENTAS": {
        "nombre": "Asesor de Ventas",
        "departamento": "VENTAS_Y_COMERCIAL",
        "dimensiones": ["Gestión y Cierre Comercial", "Cobranza y Apego a Políticas", "Disciplina en Ruta y Cobertura", "Manejo de Objeciones y Ética"],
        "claves": {
            1: "B", 2: "B", 3: "C", 4: "B", 5: "C", 6: "B", 7: "B", 8: "B", 9: "B", 10: "B",
            11: "B", 12: "A", 13: "B", 14: "B", 15: "B", 16: "B", 17: "B", 18: "B", 19: "B", 20: "B",
            21: "B", 22: "B", 23: "B", 24: "B", 25: "B", 26: "B", 27: "B", 28: "B", 29: "B", 30: "B"
        },
        "sinceridad": {
            2: {"trampa": "A", "sincero": "B"}, 7: {"trampa": "A", "sincero": "B"},
            10: {"trampa": "A", "sincero": "B"}, 16: {"trampa": "A", "sincero": "B"},
            20: {"trampa": "A", "sincero": "B"}, 24: {"trampa": "A", "sincero": "B"},
            29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": ["3D", "4A", "5D", "6C", "8D", "11D", "12D", "15A", "17D", "19A", "25C", "26C", "27A", "27C"]
    },
    "12_ASISTENTE_ADMINISTRATIVO": {
        "nombre": "Asistente Administrativo",
        "departamento": "ADMINISTRACION",
        "dimensiones": ["Soporte de Oficina", "Gestión Documental", "Atención Interna", "Procedimientos Administrativos"],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "B", 7: "A", 8: "A", 10: "D",
            11: "C", 12: "B", 13: "A", 15: "B", 16: "D", 17: "A", 18: "B", 20: "C",
            21: "C", 22: "B", 23: "A", 25: "D", 26: "B", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": ["1A", "10A", "10B", "16A", "19A", "19D", "25A", "30A", "30D"]
    },
    "13_ASISTENTE_ADMINISTRATIVO_CONTABLE": {
        "nombre": "Asistente Administrativo Contable",
        "departamento": "CONTABILIDAD_Y_FINANZAS",
        "dimensiones": ["Cierres Cata Suite", "Libros Fiscales Compras/Ventas", "Retenciones ISLR/SAMAT", "Conciliaciones y Provisiones"],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "C", 7: "A", 8: "A", 10: "D",
            11: "C", 12: "B", 13: "A", 15: "C", 16: "D", 17: "A", 18: "B", 20: "C",
            21: "A", 22: "B", 23: "C", 25: "D", 26: "B", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": ["1A", "1B", "10A", "10B", "11D", "16A", "16C", "19A", "19D", "25A", "30A", "30D"]
    },
    "14_AYUDANTE_ALMACEN": {
        "nombre": "Ayudante de Almacén",
        "departamento": "ALMACEN_OPERACIONES",
        "dimensiones": ["Recepción y Estiba", "Preparación de Pedidos (Picking)", "Rotación FIFO/FIFE", "Seguridad y Cuidados Físicos"],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "B", 7: "A", 8: "A", 10: "D",
            11: "C", 12: "B", 13: "A", 15: "B", 16: "D", 17: "A", 18: "B", 20: "C",
            21: "A", 22: "B", 23: "A", 25: "D", 26: "B", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": ["1A", "2D", "10A", "16A", "19A", "19D", "21C", "25A", "30A"]
    },
    "15_AYUDANTE_DESPACHO": {
        "nombre": "Ayudante de Despacho",
        "departamento": "DESPACHO_Y_TRANSPORTE",
        "dimensiones": ["Carga y Distribución Vial", "Entrega Segura en Cliente", "Custodia de Mercancía en Ruta", "Apego a Normas Viales"],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "B", 7: "A", 8: "A", 10: "D",
            11: "C", 12: "B", 13: "A", 15: "B", 16: "D", 17: "A", 18: "B", 20: "C",
            21: "C", 22: "B", 23: "A", 25: "D", 26: "B", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": ["1A", "2C", "7D", "10A", "16A", "19A", "19D", "23C", "25A", "30A"]
    },
    "17_CONTADOR": {
        "nombre": "Contador Público",
        "departamento": "CONTABILIDAD_Y_FINANZAS",
        "dimensiones": ["Estados Financieros VEN-NIF", "Auditoría Fiscal (SENIAT)", "Control Bancario y Pasivos", "Exactitud de Asientos y Costos"],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "C", 7: "A", 8: "A", 10: "D",
            11: "C", 12: "B", 13: "A", 15: "C", 16: "D", 17: "A", 18: "B", 20: "C",
            21: "A", 22: "B", 23: "C", 25: "D", 26: "B", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": ["1A", "1B", "8C", "10A", "10B", "10C", "11D", "16A", "16C", "19A", "19D", "20D", "22C", "25A", "30A", "30D"]
    },
    "18_COORDINADOR_DE_VENTAS": {
        "nombre": "Coordinador de Ventas",
        "departamento": "DIRECCION_COMERCIAL",
        "dimensiones": ["Estrategia Territorial", "Planes de Negocio y Crecimiento", "Reposición de Inventarios", "Salud de Cartera y Cobranzas"],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "B", 7: "A", 8: "A", 10: "D",
            11: "C", 12: "B", 13: "A", 15: "B", 16: "D", 17: "A", 18: "B", 20: "C",
            21: "C", 22: "B", 23: "A", 25: "D", 26: "B", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": ["1A", "1B", "10A", "10B", "16A", "16B", "19A", "19D", "23B", "25A", "30A", "30D"]
    },
    "19_SUPERVISOR_DE_VENTAS": {
        "nombre": "Supervisor de Ventas",
        "departamento": "DIRECCION_COMERCIAL",
        "dimensiones": ["Auditoría de Campo y Coaching", "Acompañamiento en Negociación", "Asignación de Activos Comerciales", "Gestión y Control de Cobranzas"],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "B", 7: "A", 8: "A", 10: "D",
            11: "C", 12: "B", 13: "A", 15: "B", 16: "D", 17: "A", 18: "B", 20: "C",
            21: "C", 22: "B", 23: "A", 25: "D", 26: "B", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": ["1A", "1B", "10A", "10B", "16A", "16B", "19A", "19D", "23B", "25A", "30A", "30D"]
    },
    "20_COORDINADOR_DE_PROCESOS": {
        "nombre": "Coordinador de Procesos",
        "departamento": "CONTROL_DE_GESTION_Y_PROCESOS",
        "dimensiones": ["Verificación de Procesos en Curso", "Auditoría de Devoluciones y Notas Débito", "Arqueos de Caja y Moneda Extranjera", "Diseño de Flujos y Capacitación"],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "C", 7: "A", 8: "A", 10: "D",
            11: "C", 12: "B", 13: "A", 15: "B", 16: "A", 17: "C", 18: "B", 20: "C",
            21: "A", 22: "B", 23: "A", 25: "D", 26: "B", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": ["2A", "3B", "7D", "10A", "10B", "17D", "19A", "19D", "25A", "25B", "26A", "26C", "27C", "30A", "30D"]
    },
    "22_COORDINADOR_DE_OPERACIONES": {
        "nombre": "Coordinador de Operaciones",
        "departamento": "OPERACIONES_Y_LOGISTICA",
        "dimensiones": ["Efectividad y Demanda Insatisfecha", "Gestión Presupuestaria y Desviaciones", "Seguridad Industrial y Normas 5S", "Permisologías y Deberes Fiscales"],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "B", 7: "A", 8: "A", 10: "D",
            11: "C", 12: "B", 13: "A", 15: "B", 16: "D", 17: "A", 18: "B", 20: "C",
            21: "D", 22: "B", 23: "A", 25: "D", 26: "B", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": ["1A", "2A", "3C", "10A", "10B", "12A", "17B", "19A", "19D", "23D", "25A", "25B", "30A", "30D"]
    },
    "24_SUPERVISOR_DE_COBRANZA": {
        "nombre": "Supervisor de Cobranza",
        "departamento": "ADMINISTRACION_Y_COBRANZAS",
        "dimensiones": ["Análisis de Solvencia y Desbloqueos", "Auditoría de Cartera (>31 días)", "Rutas Especiales P50 y P60", "Conciliación Bancaria y Cheques"],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "B", 7: "A", 8: "A", 10: "D",
            11: "C", 12: "B", 13: "A", 15: "B", 16: "D", 17: "A", 18: "B", 20: "C",
            21: "A", 22: "B", 23: "A", 25: "D", 26: "B", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": ["1A", "1B", "3C", "10A", "10B", "12A", "18C", "19A", "19D", "25A", "26A", "30A", "30D"]
    },
    "26_JEFE_DE_LOGISTICA": {
        "nombre": "Jefe de Logística",
        "departamento": "CADENA_DE_SUMINISTRO",
        "dimensiones": ["Flota y Mantenimiento Mecánico", "Carpetas Vehiculares y RCV", "Planta Eléctrica y Combustible", "Seguridad Integral de Sede"],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "B", 7: "A", 8: "A", 10: "D",
            11: "C", 12: "B", 13: "A", 15: "B", 16: "D", 17: "A", 18: "B", 20: "C",
            21: "A", 22: "B", 23: "A", 25: "D", 26: "B", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": ["1A", "1B", "10A", "10B", "12C", "13B", "16A", "16B", "19A", "19D", "25A", "30A", "30D"]
    },
    "27_SUPERVISOR_DE_ALMACEN": {
        "nombre": "Supervisor de Almacén",
        "departamento": "ALMACEN_OPERACIONES",
        "dimensiones": ["Control de Stocks y Ubicación", "Recepción y Fechas de Caducidad", "Rotación FIFO/FIFE", "Mantenimiento y Devoluciones"],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "B", 7: "A", 8: "A", 10: "D",
            11: "C", 12: "B", 13: "A", 15: "B", 16: "D", 17: "A", 18: "B", 20: "C",
            21: "A", 22: "B", 23: "A", 25: "D", 26: "B", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": ["1A", "2D", "10A", "10B", "13B", "16A", "19A", "19D", "25A", "25B", "30A", "30D"]
    },
    "28_SUPERVISOR_DE_DESPACHO": {
        "nombre": "Supervisor de Despacho",
        "departamento": "DESPACHO_Y_TRANSPORTE",
        "dimensiones": ["Equilibrio y Estiba en Camiones", "Ruteo Inteligente y Entregas", "Sinergia Almacén-Flota", "Apoyo en Cobranzas"],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "B", 7: "A", 8: "A", 10: "D",
            11: "C", 12: "B", 13: "A", 15: "B", 16: "D", 17: "A", 18: "B", 20: "C",
            21: "A", 22: "B", 23: "A", 25: "D", 26: "B", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": ["1A", "3B", "10A", "10B", "13B", "16A", "19A", "19D", "23D", "25A", "30A", "30D"]
    },
    # =========================================================================
    # 01. ADMINISTRADOR DE VENTAS / ANALÍTICA COMERCIAL (CJS-ADV)
    # =========================================================================
    "01_ADMINISTRADOR_DE_VENTAS": {
        "nombre": "Administrador de Ventas",
        "departamento": "VENTAS_Y_ANALITICA",
        "dimensiones": [
            "Integridad de Datos y Contingencias",
            "Soporte Analítico y Modelado Comercial",
            "Gestión de Procesos y Automatización",
            "Liderazgo Funcional y Ética Comercial"
        ],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "C", 7: "B",
            8: "A", 10: "D", 11: "C", 12: "B", 13: "A", 15: "C",
            16: "D", 17: "A", 18: "B", 20: "C", 21: "D", 22: "B",
            23: "A", 25: "D", 26: "D", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": [
            "1A", "1B", "2A", "2C", "2D", "3B", "3C", "5A", "5B",
            "9B", "10A", "10B", "11A", "11D", "12D", "13B", "13C",
            "15D", "16B", "17D", "18C", "18D", "19A", "19D", "20A",
            "20B", "22A", "22D", "25A", "25B", "25C", "26C", "27A",
            "27C", "27D", "30A", "30B", "30D"
        ]
    },

    # =========================================================================
    # 02. ADMINISTRADORA GENERAL / GESTIÓN ADMINISTRATIVA Y FINANCIERA (CJS-ADM)
    # =========================================================================
    "02_ADMINISTRADORA": {
        "nombre": "Administradora General",
        "departamento": "ADMINISTRACION_Y_FINANZAS",
        "dimensiones": [
            "Control Financiero y Conciliación Bancaria",
            "Cumplimiento Fiscal, Legal y Laboral",
            "Liderazgo Organizacional y Resolución de Conflictos",
            "Planificación Presupuestaria y Auditoría Interna"
        ],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "C", 7: "B",
            8: "A", 10: "D", 11: "C", 12: "B", 13: "A", 15: "C",
            16: "D", 17: "A", 18: "B", 20: "C", 21: "D", 22: "A",
            23: "A", 25: "D", 26: "B", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": [
            "1B", "2A", "2D", "3B", "3D", "5B", "5C", "7A", "7C",
            "8C", "10A", "10C", "11A", "13B", "13C", "15A", "17B",
            "17D", "19A", "19D", "20A", "20B", "21B", "21C", "22C",
            "22D", "25A", "26A", "27A", "27C", "30A", "30D"
        ]
    },

    # =========================================================================
    # 03. ALMACENISTA (CJS-ALM)
    # =========================================================================
    "03_ALMACENISTA": {
        "nombre": "Almacenista",
        "departamento": "ALMACEN_OPERACIONES",
        "dimensiones": [
            "Recepción, Estiba y Rotación FIFO/PEPS",
            "Seguridad Industrial y Manejo de Herramientas",
            "Exactitud de Inventarios y Control de Averías",
            "Disciplina Laboral y Trabajo en Cuadrilla"
        ],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "C", 7: "B",
            8: "A", 10: "D", 11: "C", 12: "B", 13: "A", 15: "C",
            16: "D", 17: "A", 18: "B", 20: "C", 21: "D", 22: "B",
            23: "A", 25: "C", 26: "D", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": [
            "1A", "1B", "2A", "3B", "3C", "5A", "6A", "7A", "7C", "7D",
            "8C", "10A", "10B", "10C", "11B", "12A", "13C", "15A", "17B",
            "17C", "18A", "18D", "19A", "19D", "20A", "20B", "22C", "23C",
            "25A", "25D", "26A", "26B", "27A", "28A", "28B", "28C", "30B", "30D"
        ]
    },

    # =========================================================================
    # 04. ANALISTA DE COBRANZA (CJS-COB)
    # =========================================================================
    "04_ANALISTA_DE_COBRANZA": {
        "nombre": "Analista de Cobranza",
        "departamento": "COBRANZAS_Y_CREDITO",
        "dimensiones": [
            "Validación Bancaria y Detección de Fraude",
            "Apego a Políticas de Crédito y Desbloqueos",
            "Recuperación de Cartera Vencida y Negociación",
            "Auditoría de Recaudación y Custodia de Valores"
        ],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "C", 7: "A",
            8: "A", 10: "D", 11: "C", 12: "B", 13: "A", 15: "C",
            16: "D", 17: "A", 18: "B", 20: "C", 21: "D", 22: "B",
            23: "C", 25: "D", 26: "B", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": [
            "1A", "1C", "2A", "2C", "2D", "3B", "3C", "5A", "5C",
            "6A", "6D", "7B", "7C", "8B", "8C", "10A", "10C", "12A",
            "12D", "13B", "13D", "15A", "15B", "15D", "16A", "17C",
            "19A", "19D", "20A", "20B", "20D", "21A", "23A", "23B",
            "25A", "25C", "27A", "27C", "28B", "28C", "28D", "30D"
        ]
    },

    # =========================================================================
    # 05. ANALISTA DE COMPRAS (CJS-COM)
    # =========================================================================
    "05_ANALISTA_DE_COMPRAS": {
        "nombre": "Analista de Compras",
        "departamento": "COMPRAS_Y_ABASTECIMIENTO",
        "dimensiones": [
            "Planificación de Reposición y Control de Costos",
            "Ética en Negociación y Cero Corrupción",
            "Gestión de No Conformidades, Devoluciones y Fletes",
            "Abastecimiento Estratégico y Auditoría de Proveedores"
        ],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "C", 7: "B",
            8: "A", 10: "D", 11: "C", 12: "B", 13: "A", 15: "C",
            16: "D", 17: "A", 18: "B", 20: "C", 21: "D", 22: "B",
            23: "A", 25: "D", 26: "B", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": [
            "1A", "1C", "2A", "2C", "2D", "3B", "3C", "3D", "5A", "5C",
            "6A", "6B", "6D", "7A", "7D", "8B", "8D", "10B", "11B", "11D",
            "12C", "14B", "15A", "15B", "15D", "16B", "17B", "17D", "18A",
            "19A", "19D", "20A", "20B", "21A", "21C", "24A", "25A", "25B",
            "26A", "27A", "28B", "28C", "30A", "30D"
        ]
    },

    # =========================================================================
    # 06. ANALISTA DE CONCILIACIÓN BANCARIA Y CONTABLE
    # =========================================================================
    "06_ANALISTA_DE_CONCILIACION": {
        "nombre": "Analista de Conciliación",
        "departamento": "CONTABILIDAD_Y_FINANZAS",
        "dimensiones": [
            "Conciliación Bancaria y Detección de Partidas en Tránsito",
            "Rigor en Asientos de Ajuste y Control de Comisiones",
            "Auditoría de Egresos y Verificación de Soportes",
            "Cierre Mensual y Transparencia en Balances"
        ],
        "claves": {
            1: "B", 2: "D", 3: "A", 5: "C", 6: "B", 7: "D",
            8: "A", 10: "B", 11: "D", 12: "A", 13: "C", 15: "B",
            16: "D", 17: "A", 18: "C", 20: "B", 21: "D", 22: "A",
            23: "C", 25: "B", 26: "D", 27: "A", 28: "C", 30: "B"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": [
            "1A", "2A", "2C", "3C", "5A", "6D", "7C", "8C", "10A", "10C",
            "11A", "13B", "15D", "17D", "18A", "19A", "20A", "22C", "25A",
            "26A", "27C", "30A", "30D"
        ]
    },

    # =========================================================================
    # 07. ANALISTA DE FACTURACIÓN
    # =========================================================================
    "07_ANALISTA_DE_FACTURACION": {
        "nombre": "Analista de Facturación",
        "departamento": "ADMINISTRACION_VENTAS",
        "dimensiones": [
            "Emisión Fiscal y Cumplimiento Normativo SENIAT",
            "Control de Listas de Precios y Escalas de Descuento",
            "Validación de Pedidos vs. Crédito y Stock Físico",
            "Soporte Inmediato al Despacho y Cuadre de Guías"
        ],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "C", 6: "D", 7: "B",
            8: "A", 10: "C", 11: "D", 12: "B", 13: "A", 15: "D",
            16: "B", 17: "C", 18: "A", 20: "D", 21: "B", 22: "C",
            23: "A", 25: "D", 26: "B", 27: "C", 28: "A", 30: "D"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": [
            "1A", "2A", "2C", "3B", "5A", "6A", "7C", "8D", "10A", "11A",
            "11C", "13B", "15A", "17A", "18C", "19A", "20A", "22A", "25A",
            "25C", "27A", "30A", "30C"
        ]
    },

    # =========================================================================
    # 08. ANALISTA DE LOGÍSTICA
    # =========================================================================
    "08_ANALISTA_DE_LOGISTICA": {
        "nombre": "Analista de Logística",
        "departamento": "OPERACIONES_LOGISTICAS",
        "dimensiones": [
            "Optimización de Rutas y Capacidad de Carga",
            "Monitoreo Satelital (GPS) y Tiempos de Entrega",
            "Gestión de Fletes y Control de Combustible",
            "Coordinación Interdepartamental Almacén-Ruta"
        ],
        "claves": {
            1: "C", 2: "A", 3: "D", 5: "B", 6: "C", 7: "A",
            8: "D", 10: "B", 11: "C", 12: "A", 13: "D", 15: "B",
            16: "C", 17: "A", 18: "D", 20: "B", 21: "C", 22: "A",
            23: "D", 25: "B", 26: "C", 27: "A", 28: "D", 30: "B"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": [
            "1A", "2C", "3B", "5A", "6D", "7B", "8B", "10A", "11A", "12C",
            "13B", "15A", "17C", "18A", "19A", "20C", "22B", "25A", "26A",
            "27C", "30A", "30D"
        ]
    },

    # =========================================================================
    # 09. ANALISTA DE SISTEMA SADA / CONTROL AGROALIMENTARIO
    # =========================================================================
    "09_ANALISTA_DE_SISTEMA_SADA": {
        "nombre": "Analista de Sistema SADA",
        "departamento": "REGULACION_Y_SISTEMAS",
        "dimensiones": [
            "Gestión y Descarga Oportuna de Guías SICA/SADA",
            "Apego a Cupos y Conciliación de Volúmenes Regulados",
            "Auditoría Preventiva y Blindaje ante Inspecciones",
            "Resguardo de Claves Institucionales y Legalidad"
        ],
        "claves": {
            1: "A", 2: "C", 3: "B", 5: "D", 6: "A", 7: "C",
            8: "B", 10: "D", 11: "A", 12: "C", 13: "B", 15: "D",
            16: "A", 17: "C", 18: "B", 20: "D", 21: "A", 22: "C",
            23: "B", 25: "D", 26: "A", 27: "C", 28: "B", 30: "D"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": [
            "1B", "2A", "3C", "5B", "6C", "7A", "8C", "10A", "11B", "12A",
            "13A", "15A", "17B", "18C", "19A", "20A", "22B", "25A", "26B",
            "27A", "30A", "30C"
        ]
    },

    # =========================================================================
    # 10. ANALISTAS DE LIQUIDACIÓN
    # =========================================================================
    "10_ANALISTAS_DE_LIQUIDACION": {
        "nombre": "Analistas de Liquidación",
        "departamento": "LIQUIDACION_Y_CAJA",
        "dimensiones": [
            "Recepción y Cuadre de Facturas vs. Cobranzas de Ruta",
            "Custodia de Valores (Efectivo, Divisas y Cheques)",
            "Tratamiento de Rechazos, Devoluciones y Mermas",
            "Cierre de Ruta y Auditoría Inmediata de Diferencias"
        ],
        "claves": {
            1: "B", 2: "D", 3: "A", 5: "C", 6: "B", 7: "D",
            8: "A", 10: "C", 11: "B", 12: "D", 13: "A", 15: "C",
            16: "B", 17: "D", 18: "A", 20: "C", 21: "B", 22: "D",
            23: "A", 25: "C", 26: "B", 27: "D", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": [
            "1A", "2A", "3B", "5A", "6A", "7B", "8C", "10A", "10B", "11A",
            "12B", "13B", "15A", "17A", "18C", "19A", "20A", "22A", "25A",
            "26A", "27A", "28C", "30A", "30D"
        ]
    },

    # =========================================================================
    # 16. AYUDANTE DE ALMACÉN Y DESPACHO (POLIVALENTE)
    # =========================================================================
    "16_AYUDANTES_ALMACEN_Y_DESPACHO_POLIVALENTE": {
        "nombre": "Ayudante Almacén y Despacho (Polivalente)",
        "departamento": "OPERACIONES_LOGISTICAS",
        "dimensiones": [
            "Carga, Descarga y Cuidado de la Mercancía",
            "Picking, Armado de Pedidos y Verificación de Cajas",
            "Apego a Normas de Seguridad Física y Ergonomía",
            "Trabajo en Equipo, Apoyo al Chofer y Respeto"
        ],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "C", 7: "B",
            8: "A", 10: "D", 11: "C", 12: "B", 13: "A", 15: "C",
            16: "D", 17: "A", 18: "B", 20: "C", 21: "D", 22: "B",
            23: "A", 25: "C", 26: "D", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": [
            "1A", "1B", "2A", "3C", "5A", "6A", "7A", "7C", "8C", "10A",
            "10B", "11B", "12A", "13C", "15A", "17B", "18A", "19A", "20A",
            "20B", "22A", "23C", "25A", "26A", "27A", "28B", "30A", "30D"
        ]
    },

    # =========================================================================
    # 20. COORDINACIÓN Y SUPERVISIÓN DE VENTAS (INTEGRADO)
    # =========================================================================
    "20_COORDINACION_Y_SUPERVISION_DE_VENTAS_INTEGRADO": {
        "nombre": "Coordinación y Supervisión de Ventas (Integrado)",
        "departamento": "VENTAS_COMERCIAL",
        "dimensiones": [
            "Liderazgo en Campo y Cumplimiento de Cuotas de Venta",
            "Auditoría de Rutas, Efectividad y Cobertura Real",
            "Supervisión de Cobranzas y Disciplina de Crédito",
            "Desarrollo de Vendedores y Ética Comercial"
        ],
        "claves": {
            1: "C", 2: "A", 3: "D", 5: "B", 6: "C", 7: "A",
            8: "D", 10: "B", 11: "C", 12: "A", 13: "D", 15: "B",
            16: "C", 17: "A", 18: "D", 20: "B", 21: "C", 22: "A",
            23: "D", 25: "B", 26: "C", 27: "A", 28: "D", 30: "B"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": [
            "1A", "2C", "3A", "3D", "5A", "5D", "6C", "7B", "8D", "10C",
            "11D", "12D", "13A", "15A", "17D", "18A", "19A", "20A", "22B",
            "25C", "26A", "27A", "28C", "30A", "30C"
        ]
    },

    # =========================================================================
    # 21. COORDINADOR ADMINISTRATIVO
    # =========================================================================
    "21_COORDINADOR_ADMINISTRATIVO": {
        "nombre": "Coordinador Administrativo",
        "departamento": "ADMINISTRACION_CENTRAL",
        "dimensiones": [
            "Supervisión de Facturación, Caja y Cobranzas",
            "Control Interno, Arqueos y Auditoría Operativa",
            "Gestión de Suministros, Servicios y Cuentas por Pagar",
            "Liderazgo Administrativo y Cumplimiento Normativo"
        ],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "C", 7: "B",
            8: "A", 10: "D", 11: "C", 12: "B", 13: "A", 15: "C",
            16: "D", 17: "A", 18: "B", 20: "C", 21: "D", 22: "A",
            23: "A", 25: "D", 26: "B", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": [
            "1A", "2A", "2D", "3B", "5B", "7A", "7C", "8C", "10A", "11A",
            "13B", "15A", "17B", "17D", "19A", "20A", "21C", "22C", "25A",
            "26A", "27A", "28C", "30A", "30D"
        ]
    },

    # =========================================================================
    # 23. COORDINADOR DE TALENTO HUMANO
    # =========================================================================
    "23_COORDINADOR_DE_TALENTO_HUMANO": {
        "nombre": "Coordinador de Talento Humano",
        "departamento": "TALENTO_HUMANO",
        "dimensiones": [
            "Apego a Normativa Laboral (LOTTT, Inpsasel, Seguro Social)",
            "Gestión Disciplinaria y Resolución Neutral de Conflictos",
            "Auditoría y Supervisión de Nómina e Incidencias",
            "Reclutamiento Técnico, Clima Laboral y Retención"
        ],
        "claves": {
            1: "B", 2: "D", 3: "A", 5: "C", 6: "B", 7: "D",
            8: "A", 10: "C", 11: "B", 12: "D", 13: "A", 15: "C",
            16: "B", 17: "D", 18: "A", 20: "C", 21: "B", 22: "D",
            23: "A", 25: "C", 26: "B", 27: "D", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": [
            "1C", "2B", "3B", "5A", "6A", "7B", "8C", "10B", "11A", "12A",
            "13C", "15A", "16A", "16C", "19A", "20A", "21A", "22B", "25B",
            "26C", "27A", "30A", "30D"
        ]
    },

    # =========================================================================
    # 25. DESPACHADOR
    # =========================================================================
    "25_DESPACHADOR": {
        "nombre": "Despachador",
        "departamento": "DESPACHO_Y_TRANSPORTE",
        "dimensiones": [
            "Cotejo de Mercancía Física vs. Guía/Factura Legal",
            "Auditoría de Carga y Amarre Seguro de Unidades",
            "Atención a Choferes y Prevención de Mermas/Sobrantes",
            "Despacho a Tiempo y Custodia del Precinto de Seguridad"
        ],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "C", 7: "B",
            8: "A", 10: "D", 11: "C", 12: "B", 13: "A", 15: "C",
            16: "D", 17: "A", 18: "B", 20: "C", 21: "D", 22: "B",
            23: "A", 25: "C", 26: "D", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": [
            "1A", "1B", "2A", "3B", "5A", "6A", "6D", "7A", "8C", "10A",
            "10B", "11A", "12A", "13C", "15A", "17B", "18A", "19A", "20B",
            "22C", "23C", "25A", "25D", "27A", "28B", "30A", "30D"
        ]
    },

    # =========================================================================
    # 29. SUPERVISOR LOGÍSTICA, ALMACÉN Y DESPACHO (INTEGRADO)
    # =========================================================================
    "29_SUPERVISOR_LOGISTICA_ALMACEN_DESPACHO_INTEGRADO": {
        "nombre": "Supervisor Logística, Almacén, Despacho (Integrado)",
        "departamento": "CADENA_DE_SUMINISTRO",
        "dimensiones": [
            "Liderazgo Integral de la Operación y Cuadrillas",
            "Control y Auditoría de Stock, Mermas y Diferencias",
            "Sincronización de Salida y Retorno de Flota Primaria/Secundaria",
            "Seguridad Industrial, Disciplina y Cero Pérdidas"
        ],
        "claves": {
            1: "C", 2: "A", 3: "D", 5: "B", 6: "C", 7: "A",
            8: "D", 10: "B", 11: "C", 12: "A", 13: "D", 15: "B",
            16: "C", 17: "A", 18: "D", 20: "B", 21: "C", 22: "A",
            23: "D", 25: "B", 26: "C", 27: "A", 28: "D", 30: "B"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": [
            "1A", "2C", "3B", "5A", "6A", "7D", "8B", "10A", "11B", "12A",
            "13B", "15A", "17B", "18A", "19A", "20A", "22C", "25A", "26A",
            "27A", "28C", "30A", "30D"
        ]
    },

    # =========================================================================
    # 30. MANTENIMIENTO Y LIMPIEZA
    # =========================================================================
    "30_MANTENIMIENTO_Y_LIMPIEZA": {
        "nombre": "Mantenimiento y Limpieza",
        "departamento": "SERVICIOS_GENERALES",
        "dimensiones": [
            "Diligencia en Higiene, Sanitización y Desinfección",
            "Uso Responsable y Cuidadoso de Productos Químicos",
            "Cuidado y Resguardo de Instalaciones y Bienes",
            "Puntualidad, Discreción y Trabajo sin Supervisión"
        ],
        "claves": {
            1: "A", 2: "C", 3: "B", 5: "D", 6: "A", 7: "C",
            8: "B", 10: "D", 11: "A", 12: "C", 13: "B", 15: "D",
            16: "A", 17: "C", 18: "B", 20: "D", 21: "A", 22: "C",
            23: "B", 25: "D", 26: "A", 27: "C", 28: "B", 30: "D"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": [
            "1C", "2A", "3A", "5B", "6C", "7A", "8A", "10A", "11B", "12B",
            "13C", "15A", "17A", "18C", "19A", "20B", "22A", "25A", "26C",
            "27A", "28B", "30A"
        ]
    },

    # =========================================================================
    # 31. MERCADERISTA / TRADE MARKETING
    # =========================================================================
    "31_MERCADERISTA": {
        "nombre": "Mercaderista",
        "departamento": "TRADE_MARKETING",
        "dimensiones": [
            "Exhibición Estratégica, Planometría y Espacios en Anaquel",
            "Rotación FIFO/PEPS y Alerta Temprana de Vencimientos",
            "Relación Comercial con Encargados de Supermercados",
            "Reporte Fidedigno de Precios y Acciones de Competencia"
        ],
        "claves": {
            1: "B", 2: "D", 3: "A", 5: "C", 6: "B", 7: "D",
            8: "A", 10: "C", 11: "B", 12: "D", 13: "A", 15: "C",
            16: "B", 17: "D", 18: "A", 20: "C", 21: "B", 22: "D",
            23: "A", 25: "C", 26: "B", 27: "D", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": [
            "1A", "2A", "3C", "5A", "6A", "7C", "8B", "10A", "11A", "12B",
            "13C", "15A", "17B", "17C", "18C", "19A", "20A", "22A", "25A",
            "26C", "27C", "30A", "30C"
        ]
    },

    # =========================================================================
    # 32. MONTACARGUISTA
    # =========================================================================
    "32_MONTACARGA": {
        "nombre": "Montacarguista",
        "departamento": "ALMACEN_OPERACIONES",
        "dimensiones": [
            "Operación Segura de Maquinaria y Prevención de Accidentes",
            "Inspección Diaria (Checklist: Batería, Frenos, Hidráulica)",
            "Estiba en Altura, Capacidad de Carga y Amarre de Paletas",
            "Cuidado de la Carga, Cero Averías y Disciplina Operativa"
        ],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "C", 7: "B",
            8: "A", 10: "D", 11: "C", 12: "B", 13: "A", 15: "C",
            16: "D", 17: "A", 18: "B", 20: "C", 21: "D", 22: "B",
            23: "A", 25: "C", 26: "D", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": [
            "1A", "1B", "2A", "3D", "5A", "6A", "7A", "7C", "8C", "10A",
            "11B", "12A", "13C", "15A", "17B", "18A", "19A", "20B", "22C",
            "23B", "23C", "23D", "25A", "26A", "26B", "27A", "28A", "30A"
        ]
    },
    "34_VIGILANTE": {
        "nombre": "Vigilante de Seguridad",
        "departamento": "SEGURIDAD_INTEGRAL",
        "dimensiones": ["Control de Accesos y Facturas", "Rondas Perimétricas y Brequeras", "Custodia de Llaves y Flota", "Disciplina y Relevo de Guardia"],
        "claves": {
            1: "D", 2: "B", 3: "A", 5: "D", 6: "B", 7: "A", 8: "A", 10: "D",
            11: "C", 12: "B", 13: "A", 15: "C", 16: "D", 17: "A", 18: "B", 20: "C",
            21: "D", 22: "A", 23: "A", 25: "D", 26: "B", 27: "B", 28: "A", 30: "C"
        },
        "sinceridad": {
            4: {"trampa": "C", "sincero": "B"}, 9: {"trampa": "A", "sincero": "C"},
            14: {"trampa": "D", "sincero": "A"}, 19: {"trampa": "B", "sincero": "C"},
            24: {"trampa": "C", "sincero": "B"}, 29: {"trampa": "A", "sincero": "B"}
        },
        "alertas_rojas": ["1A", "1B", "5A", "5B", "6D", "10A", "10B", "16A", "18A", "19A", "19D", "25B", "27A", "30A", "30D"]
    }
}

