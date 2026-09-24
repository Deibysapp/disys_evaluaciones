"""
DiSys 2026 - Banco Centralizado de Reactivos Psicotécnicos.
Perfiles consolidados: 01, 02, 03, 04, 05, 06, 08 y 09.
"""

BANCO_PREGUNTAS = {
    # =========================================================================
    # 01. ADMINISTRADOR DE VENTAS (CJS-ADV)
    # =========================================================================
    "01_ADMINISTRADOR_DE_VENTAS": {
        "codigo": "CJS-ADV",
        "titulo": "EVALUACIÓN PSICOTÉCNICA SITUACIONAL EN ADMINISTRACIÓN DE VENTAS Y ANALÍTICA",
        "instrucciones": "Lea con atención cada situación laboral y comercial. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con honestidad sobre su estilo real de manejo de datos, soporte a la fuerza de ventas y resolución de inconsistencias. Dispone de un máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "A las 8:30 a.m. se detecta que el sistema de facturación no sincronizó las ventas de dos rutas foráneas del día anterior, impidiendo emitir el reporte matutino de volumen de ventas para la Gerencia:",
                "opciones": {
                    "A": "Emite el reporte incompleto sin advertir la falta de datos para cumplir con la hora de entrega.",
                    "B": "Cancela la emisión del reporte diario y espera a que el personal de Sistemas lo resuelva en la tarde.",
                    "C": "Reclama agresivamente a los supervisores de ruta culpándolos por no sincronizar sus dispositivos.",
                    "D": "Identifica las dos rutas faltantes, extrae la data preliminar por contingencia, notifica a Sistemas con ticket prioritario y emite el informe con la salvedad cuantitativa para no frenar la reunión de negocio."
                }
            },
            2: {
                "enunciado": "Un supervisor de ventas le solicita modificar manualmente el cierre de volumen de uno de sus vendedores para que alcance la cuota y no pierda la escala de comisiones:",
                "opciones": {
                    "A": "Modifica la cifra en la hoja de cálculo asumiendo que el supervisor es la máxima autoridad del canal.",
                    "B": "Rechaza la solicitud con firmeza, explica la política de auditoría de datos y emite el reporte con las cifras reales facturadas y liquidadas en el sistema.",
                    "C": "Acepta el cambio a cambio de que el supervisor le otorgue una parte de la comisión comercial.",
                    "D": "Altera el número pero borra el registro de auditoría para que la Gerencia General no lo note."
                }
            },
            3: {
                "enunciado": "Al auditar la base de datos de clientes, detecta que más de 80 clientes aparecen registrados con números de RIF duplicados o direcciones comerciales inexistentes:",
                "opciones": {
                    "A": "Diseña un plan de saneamiento: cruza la data con cobranzas y vendedores de ruta, bloquea temporalmente duplicados y actualiza los expedientes con respaldo físico.",
                    "B": "Borra todos los clientes dudosos del sistema de forma masiva sin consultar a la fuerza comercial.",
                    "C": "Ignora la inconsistencia considerando que mientras los clientes compren no importa la exactitud de los datos.",
                    "D": "Le traslada toda la responsabilidad al departamento de atención al cliente sin brindar apoyo técnico."
                }
            },
            4: {
                "enunciado": "En su trayectoria profesional y manejo de información analítica:",
                "opciones": {
                    "A": "Si un vendedor me cuestiona un número en un reporte, me niego a volver a cruzar la data con él.",
                    "B": "En ocasiones he sentido fatiga mental ante tablas de datos extensas o cierres comerciales complejos, pero verifico las fórmulas antes de publicar.",
                    "C": "Jamás en mi vida profesional me he equivocado en una fórmula, tabla dinámica o celda de cálculo.",
                    "D": "Prefiero no compartir mis plantillas automatizadas con nadie para asegurar mi indispensabilidad."
                }
            },
            5: {
                "enunciado": "Durante el cruce de ventas contra inventario, detecta que un producto en promoción masiva se vendió por encima del stock físico disponible en el almacén:",
                "opciones": {
                    "A": "Modifica el inventario en el sistema para que coincida con las ventas sin revisar la existencia en depósito.",
                    "B": "Oculta el desfase a la Gerencia de Ventas esperando que los despachadores resuelvan el problema en la calle.",
                    "C": "Sugiere anular las ventas de los clientes más pequeños para cuadrar los bultos disponibles.",
                    "D": "Levanta de inmediato una alerta operativa con el Jefe de Almacén y el Gerente de Ventas para frenar facturación adicional y coordinar asignación equitativa o sustitución autorizada."
                }
            },
            6: {
                "enunciado": "Un asesor de ventas se queja formalmente porque asegura que el reporte de cobranzas no le acreditó la recuperación de un cliente clave de su ruta:",
                "opciones": {
                    "A": "Desestima el reclamo del vendedor diciéndole que el sistema administrativo nunca se equivoca.",
                    "B": "Le pide al vendedor que hable directamente con el cliente y que ellos resuelvan la diferencia bancaria.",
                    "C": "Solicita el número de comprobante, valida la fecha de liquidación con la analista de cobranzas y corrige el indicador emitiendo la nota de crédito o rectificación en el tablero.",
                    "D": "Insulta al vendedor acusándolo de llevar un mal control de sus cobranzas en la calle."
                }
            },
            7: {
                "enunciado": "El proceso manual de extracción y consolidación de reportes de ventas por ruta toma 3 horas cada mañana, retrasando la toma de decisiones comerciales:",
                "opciones": {
                    "A": "Se conforma con el proceso manual argumentando que siempre se ha hecho así en la empresa.",
                    "B": "Desarrolla y prueba una plantilla automatizada (macros/Power Query/tablas dinámicas vinculadas) que reduzca la extracción a minutos y garantice reportes inmediatos.",
                    "C": "Pide que le contraten a dos asistentes para que ellos realicen el copiado manual de la información.",
                    "D": "Deja de entregar reportes detallados y solo envía un resumen de tres líneas por mensaje de texto."
                }
            },
            8: {
                "enunciado": "En una reunión de seguimiento de negocio, un supervisor cuestiona con agresividad la veracidad de su reporte de efectividad de visita frente a la Gerencia:",
                "opciones": {
                    "A": "Mantiene la calma, proyecta las trazas de geolocalización (GPS), pedidos cargados y horas de visita del sistema, defendiendo la data con hechos auditables.",
                    "B": "Se altera emocionalmente y le responde a gritos al supervisor interrumpiendo la reunión.",
                    "C": "Se disculpa a ciegas asumiendo que su reporte estaba mal sin haber verificado los números.",
                    "D": "Abandona la sala de juntas de manera intempestiva y se niega a volver a interactuar con ese supervisor."
                }
            },
            9: {
                "enunciado": "Respecto al rigor técnico y la honestidad en el manejo de cifras de la empresa:",
                "opciones": {
                    "A": "Nunca en ninguno de mis trabajos anteriores he sentido presión ni he tenido dudas al presentar indicadores a la alta gerencia.",
                    "B": "Considero que las estadísticas de ventas son relativas y pueden moldearse para dar buena impresión.",
                    "C": "Cuando he detectado un desfase involuntario en un gráfico o KPI, lo he corregido transparentemente notificando a los involucrados.",
                    "D": "Si una fórmula arroja un error en plena presentación, prefiero culpar al proyector o a la versión de Excel."
                }
            },
            10: {
                "enunciado": "La Gerencia Comercial le pide calcular las proyecciones de demanda para la compra de inventario del trimestre siguiente:",
                "opciones": {
                    "A": "Coloca un porcentaje idéntico para todos los rubros al azar sin analizar el historial de consumo.",
                    "B": "Utiliza únicamente los datos del mejor mes del año pasado para inflar las proyecciones de compra.",
                    "C": "Le traslada el cálculo completo a los proveedores para no asumir la responsabilidad técnica.",
                    "D": "Cruza el historial de ventas estacionales por categoría, analiza la rotación por canal comercial y genera escenarios cuantitativos con rangos de desviación controlados."
                }
            },
            11: {
                "enunciado": "Varios vendedores solicitan con urgencia la creación de nuevos códigos de clientes para despachar pedidos el mismo día, pero faltan documentos fiscales requeridos:",
                "opciones": {
                    "A": "Crea los códigos de inmediato sin ningún documento, priorizando la venta sobre la legalidad.",
                    "B": "Rechaza las solicitudes de forma despectiva y bloquea la comunicación con los asesores de venta.",
                    "C": "Revisa qué recaudos indispensables faltan, orienta al asesor para su recolección rápida y tramita la creación bajo el cumplimiento estricto del manual de procedimientos.",
                    "D": "Inventa números de RIF ficticios en el software administrativo para que el sistema permita guardar el pedido."
                }
            },
            12: {
                "enunciado": "Debe presentar a la Gerencia General un informe de rentabilidad por canal de venta (mayoristas, supermercados, bodegas), pero los datos de costos operativos están desordenados:",
                "opciones": {
                    "A": "Entrega un informe superficial basándose solo en volumen de venta bruto sin discriminar margen ni costo.",
                    "B": "Realiza un trabajo minucioso de conciliación de costos, clasifica los márgenes brutos y netos por canal y presenta un análisis comparativo claro con recomendaciones.",
                    "C": "Le solicita a la Gerencia que postergue la presentación indefinidamente hasta que Contabilidad organice todo.",
                    "D": "Copia los márgenes de una empresa competidora y los presenta como si fueran los de la compañía."
                }
            },
            13: {
                "enunciado": "Un asesor de ventas le pide que le filtre información confidencial sobre las ventas y clientes de otro compañero de ruta para ganar una competencia interna:",
                "opciones": {
                    "A": "Niega con cortesía y firmeza la solicitud, recordando que la data de rendimiento individual es confidencial y solo accesible a supervisores y gerencia.",
                    "B": "Le facilita los reportes de su compañero a cambio de un porcentaje de su comisión comercial.",
                    "C": "Le entrega la información pero le pide que no le cuente a nadie para no meterse en problemas.",
                    "D": "Publica la data de todos los vendedores en una cartelera pública para que todos compitan abiertamente."
                }
            },
            14: {
                "enunciado": "En relación con las jefaturas comerciales y los requerimientos imprevistos:",
                "opciones": {
                    "A": "He tenido divergencias de interpretación numérica con gerentes de ventas, pero siempre las dirimimos revisando la fuente de datos con profesionalismo.",
                    "B": "Los gerentes comerciales generalmente no entienden nada de tablas ni análisis de datos.",
                    "C": "No tolero que me pidan informes fuera del formato estándar que yo mismo establecí.",
                    "D": "En todos mis empleos anteriores he tenido jefes comerciales absolutamente perfectos con los que jamás tuve ninguna diferencia."
                }
            },
            15: {
                "enunciado": "Se detecta que un producto estratégico está perdiendo presencia en los anaqueles a pesar de que el reporte de facturación muestra ventas continuas:",
                "opciones": {
                    "A": "No hace nada porque su trabajo se limita únicamente a registrar lo que se factura en el sistema.",
                    "B": "Acusa a los choferes de estar robándose la mercancía sin presentar ninguna evidencia cuantitativa.",
                    "C": "Cruza los datos de venta por cliente y detecta que el producto se está concentrando en solo dos clientes mayoristas en lugar de dispersarse en la ruta minorista, reportándolo a la gerencia.",
                    "D": "Modifica las estadísticas para que parezca que el producto está presente en el 100% de los negocios."
                }
            },
            16: {
                "enunciado": "El Gerente de Ventas le solicita permanecer después de su hora habitual de salida (6:00 p.m.) para cerrar el consolidado mensual de comisiones que debe enviarse a Nómina esa misma noche:",
                "opciones": {
                    "A": "Apaga su estación de trabajo a las 6:00 p.m. exacta argumentando que el cierre no es su problema directo.",
                    "B": "Carga cifras provisionales sin auditar para terminar rápido y marcharse a su casa.",
                    "C": "Manifiesta su molestia quejándose en los pasillos frente a los demás colaboradores.",
                    "D": "Asume el requerimiento con sentido de responsabilidad, revisa los indicadores de liquidación y entrega el consolidado auditado a tiempo para la nómina."
                }
            },
            17: {
                "enunciado": "Al revisar el maestro de clientes, detecta que hay clientes que tienen asignadas rutas de venta que no corresponden a su ubicación geográfica real:",
                "opciones": {
                    "A": "Reordena la asignación territorial en el sistema coordinando previamente con los supervisores de zona, optimizando los tiempos de traslado de los asesores.",
                    "B": "Deja la asignación errónea para no generar descontento en los vendedores que atienden a esos clientes.",
                    "C": "Elimina a los clientes del sistema para que no sigan causando distorsión en las rutas.",
                    "D": "Le cobra una tarifa administrativa a los supervisores por corregir las rutas en la base de datos."
                }
            },
            18: {
                "enunciado": "Se produce una caída de la conexión a internet en la sede principal a mediodía, justo cuando se deben procesar los pedidos de la tarde:",
                "opciones": {
                    "A": "Se cruza de brazos y da la jornada por terminada hasta que el servicio de internet se restablezca solo.",
                    "B": "Activa el protocolo de contingencia (conexión compartida autorizada/módem de respaldo o recolección de pedidos en plantilla local desconectada) para mantener el flujo comercial.",
                    "C": "Empieza a cancelar pedidos de clientes argumentando que la empresa no cuenta con infraestructura.",
                    "D": "Se retira de la oficina sin avisar a sus superiores aprovechando la falla técnica."
                }
            },
            19: {
                "enunciado": "Sobre la custodia y el manejo de información de precios, descuentos y márgenes comerciales:",
                "opciones": {
                    "A": "Comparto las listas de costos y márgenes con amigos externos que trabajan en empresas competidoras.",
                    "B": "Jamás en toda mi carrera he sentido curiosidad ni he mirado un dato corporativo que no me correspondiera directamente.",
                    "C": "Manejo la política de precios y escalas de descuento con absoluta reserva, evitando la fuga de información sensible.",
                    "D": "Si un cliente me cae bien, le revelo el margen de ganancia de la distribuidora para que negocie mejor."
                }
            },
            20: {
                "enunciado": "En el cierre semanal, un supervisor afirma haber cumplido la meta de cobertura de clientes, pero el cruce con el sistema arroja que un 15% de las visitas fueron telefónicas y no presenciales:",
                "opciones": {
                    "A": "Valida las llamadas como visitas físicas presenciales para no perjudicar la evaluación del supervisor.",
                    "B": "Borra los registros telefónicos para que el indicador quede en blanco y nadie se dé cuenta.",
                    "C": "Refleja con precisión técnica en el tablero ambos indicadores: porcentaje de cobertura presencial vs. cobertura telefónica, garantizando transparencia gerencial.",
                    "D": "Envía un memorando sancionatorio al supervisor sin tener la potestad jerárquica para hacerlo."
                }
            },
            21: {
                "enunciado": "La Gerencia le solicita diseñar un nuevo tablero de control (Dashboard) comercial para monitorear el desempeño diario de los vendedores:",
                "opciones": {
                    "A": "Descarga una plantilla genérica de internet sin adaptarla a la realidad ni a los indicadores de la empresa.",
                    "B": "Diseña un tablero con fórmulas tan enredadas que solo usted sea capaz de entender los resultados.",
                    "C": "Se niega a realizarlo argumentando que los tableros visuales son modas innecesarias de la administración.",
                    "D": "Estructura un tablero visual e interactivo centrado en los KPIs clave (volumen, cobranza, efectividad, rechazos), facilitando la lectura ejecutiva a supervisores y gerentes."
                }
            },
            22: {
                "enunciado": "Al consolidar las devoluciones de mercancía del mes, nota una tendencia creciente de rechazos por 'producto vencido o próximo a vencer':",
                "opciones": {
                    "A": "Oculta la tendencia en el reporte consolidado para no alarmar a la Dirección de la empresa.",
                    "B": "Elabora un análisis estadístico específico del impacto de los rechazos, identifica las marcas afectadas y lo presenta al Gerente de Ventas y Jefe de Almacén para tomar acciones preventivas.",
                    "C": "Culpa exclusivamente a los clientes comerciantes por no saber rotar el producto en sus anaqueles.",
                    "D": "Deja de registrar las devoluciones en el sistema administrativo para que las cifras parezcan limpias."
                }
            },
            23: {
                "enunciado": "Un vendedor nuevo en su primera semana de ruta presenta dificultades para cargar los pedidos en la aplicación móvil comercial:",
                "opciones": {
                    "A": "Le brinda soporte técnico paciente, le explica el paso a paso del flujo de pedidos y le suministra una guía rápida para reforzar su autonomía.",
                    "B": "Le dice de forma despectiva que si no sabe manejar un teléfono inteligente no sirve para el cargo de vendedor.",
                    "C": "Hace el trabajo de cargarle todos los pedidos de su ruta durante meses sin enseñarle a usar la herramienta.",
                    "D": "Lo reporta de inmediato a Recursos Humanos solicitando su despido fulminante por ignorancia digital."
                }
            },
            24: {
                "enunciado": "Sobre el manejo del estrés en días de cierre comercial y presión de metas:",
                "opciones": {
                    "A": "Si alguien me habla durante un cierre de mes, le grito para que me deje concentrar en mis tablas.",
                    "B": "He experimentado momentos de alta presión en cierres de ciclo, pero mantengo la concentración y la precisión en el ingreso de datos.",
                    "C": "Poseo un control mental perfecto; jamás nada ni nadie ha logrado generarme la menor sensación de apuro o tensión.",
                    "D": "Cuando me saturo de reportes, apago el computador y me retiro a descansar sin avisar a nadie."
                }
            },
            25: {
                "enunciado": "Se detecta una discrepancia entre la lista de precios aprobada por la Gerencia General y la que está activa en el sistema de ventas:",
                "opciones": {
                    "A": "Espera a que termine el mes para ver si alguien más se da cuenta del error en la facturación.",
                    "B": "Ajusta los precios por su cuenta sin contar con el memorando o documento formal de aprobación gerencial.",
                    "C": "Modifica los reportes de ventas para tapar las diferencias de margen generadas por el error.",
                    "D": "Bloquea preventivamente la facturación errónea, notifica de inmediato a la Gerencia Comercial con el comparativo de listas y aplica la parametrización correcta avalada."
                }
            },
            26: {
                "enunciado": "La empresa implementa un nuevo módulo de auditoría de rutas y clientes en el sistema y requiere capacitar a los supervisores:",
                "opciones": {
                    "A": "Se resiste a utilizar el módulo y continúa entregando sus informes en formatos obsoletos.",
                    "B": "Envía el manual técnico en inglés de 100 páginas a los supervisores sin ofrecer ninguna explicación práctica.",
                    "C": "Cobra una tarifa económica personal a los supervisores por enseñarles a usar la nueva función.",
                    "D": "Prepara una sesión de entrenamiento práctica y dinámica, elabora ejemplos con casos reales de ruta y acompaña a los supervisores en sus primeras consultas."
                }
            },
            27: {
                "enunciado": "Durante la auditoría semanal de cobranzas, observa que se han emitido recibos provisionales manuales que no han sido reportados en el sistema durante más de 72 horas:",
                "opciones": {
                    "A": "Ignora los recibos manuales considerando que el dinero aparecerá tarde o temprano en el banco.",
                    "B": "Emite un informe de alerta sobre los cobros pendientes de ingreso, solicita la validación a la analista de cobranzas y notifica a la supervisión para evitar fugas de custodia.",
                    "C": "Rompe los recibos manuales para no tener diferencias pendientes en el balance de cobranzas.",
                    "D": "Le aconseja a los vendedores que sigan cobrando con recibos manuales sin reportar al sistema."
                }
            },
            28: {
                "enunciado": "La Gerencia le solicita participar activamente en la reunión semanal de análisis de negocio con el equipo de ventas:",
                "opciones": {
                    "A": "Asiste con preparación técnica: expone los indicadores de gestión de cada ruta, resalta desvíos de metas con datos claros y propone acciones de mejora analítica.",
                    "B": "Asiste a la reunión únicamente a escuchar sin emitir comentarios ni aportar ninguna cifra de valor.",
                    "C": "Utiliza la reunión comercial para ventilar conflictos personales con los asesores de venta.",
                    "D": "No se presenta a la reunión argumentando que el trabajo analítico se hace detrás de un escritorio y no conversando con vendedores."
                }
            },
            29: {
                "enunciado": "Respecto a las relaciones con otros analistas y el reconocimiento profesional:",
                "opciones": {
                    "A": "Nunca en mi vida profesional he sentido la menor molestia ni recelo ante el éxito o felicitación de un colega.",
                    "B": "A veces he sentido sana competencia ante el buen trabajo de otros, pero me enfoco en perfeccionar mis habilidades y modelos analíticos.",
                    "C": "Pienso que con frecuencia se premia a alguien por favoritismo.",
                    "D": "Prefiero trabajar de forma aislada porque en el área de sistemas y análisis todos buscan robarse el crédito ajeno."
                }
            },
            30: {
                "enunciado": "Presidencia le encomienda liderar la integración automatizada entre la plataforma de ventas y el sistema administrativo de la distribuidora:",
                "opciones": {
                    "A": "Deja el proyecto en manos de un pasante sin supervisar los resultados ni hacer pruebas de estrés.",
                    "B": "Se opone a la integración porque considera que automatizar los reportes le restará valor a su puesto de trabajo.",
                    "C": "Lidera el cronograma de trabajo: levanta requerimientos de cada área, coordina pruebas de consistencia de datos con Sistemas, valida los reportes piloto y asegura una transición limpia.",
                    "D": "Da por completada la integración sin haber hecho pruebas, generando un colapso en la facturación del día 1."
                }
            }
        }
    },

    # =========================================================================
    # 02. ADMINISTRADORA (CJS-ADM)
    # =========================================================================
    "02_ADMINISTRADORA": {
        "codigo": "CJS-ADM",
        "titulo": "EVALUACIÓN PSICOTÉCNICA SITUACIONAL EN GESTIÓN ADMINISTRATIVA Y FINANCIERA",
        "instrucciones": "Lea atentamente cada situación gerencial y administrativa. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con total honestidad sobre su estilo real de liderazgo, control financiero y toma de decisiones. Dispone de un tiempo máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "A primera hora de la mañana, la analista de cobranzas solicita con urgencia los estados de cuenta bancarios para liberar pedidos retenidos, pero el portal bancario presenta lentitud en la descarga:",
                "opciones": {
                    "A": "Le dice a la analista que espere hasta la tarde sin buscar alternativas de conexión.",
                    "B": "Autoriza la liberación de los pedidos a ciegas sin verificar los fondos reales en cuenta.",
                    "C": "Reclama agresivamente al soporte técnico del banco paralizando el trabajo del departamento.",
                    "D": "Ingresa por canales alternativos (banca móvil/reporte consolidado), emite los saldos preliminares verificados y coordina la validación inmediata para no frenar la facturación."
                }
            },
            2: {
                "enunciado": "Al revisar la conciliación bancaria del cierre mensual, detecta un débito no identificado por un monto relevante que no coincide con ninguna orden de pago autorizada:",
                "opciones": {
                    "A": "Ajusta contablemente la diferencia como un 'gasto administrativo menor' para cuadrar el balance.",
                    "B": "Bloquea preventivamente el instrumento, genera el reclamo formal con el banco y rastrea el origen del comprobante antes de cerrar el informe contable.",
                    "C": "Asume que se trata de una comisión bancaria rutinaria y lo deja sin conciliar para el mes entrante.",
                    "D": "Le traslada la responsabilidad a la cajera y le descuenta el monto sin iniciar investigación previa."
                }
            },
            3: {
                "enunciado": "Un proveedor estratégico exige el pago inmediato de una factura vencida amenazando con suspender despachos clave, pero el flujo de caja del día está comprometido para el pago de nómina:",
                "opciones": {
                    "A": "Prioriza el pago sagrado de nómina, negocia un cronograma de abono parcial inmediato con el proveedor respaldado por cobranzas del día y notifica a Presidencia.",
                    "B": "Desvía los fondos de la nómina para pagar la totalidad al proveedor sin consultar a la gerencia.",
                    "C": "Apaga el teléfono corporativo y evade la comunicación con el proveedor hasta la semana entrante.",
                    "D": "Emite un cheque sin provisión de fondos para ganar tiempo mientras ingresa nueva cobranza."
                }
            },
            4: {
                "enunciado": "En su trayectoria profesional y gestión bajo presión:",
                "opciones": {
                    "A": "Si un colaborador subordinado comete una falta menor, lo sanciono con despido de inmediato.",
                    "B": "He sentido tensión en cierres contables o auditorías exigentes, pero mantengo la serenidad y el rigor numérico.",
                    "C": "Jamás en toda mi vida profesional he experimentado estrés, preocupación o fatiga laboral ante una auditoría.",
                    "D": "Prefiero trabajar en solitario porque delegar en otros siempre termina en errores ajenos."
                }
            },
            5: {
                "enunciado": "Durante una revisión interna de la cartelera fiscal y permisos de la empresa, nota que la solvencia municipal vence en 48 horas y los recaudos no están listos:",
                "opciones": {
                    "A": "Espera a que la empresa sea fiscalizada o multada para justificar la necesidad del trámite.",
                    "B": "Paga una comisión informal a un gestor externo sin soporte legal para obtener un documento dudoso.",
                    "C": "Modifica la fecha de vigencia del documento anterior de manera digital para ganar tiempo ante una inspección.",
                    "D": "Activa de inmediato la recopilación de recaudos, gestiona el pago de tributos pendientes y tramita la constancia de renovación en trámite ante el ente regulador."
                }
            },
            6: {
                "enunciado": "Se presentan roces constantes entre el área de ventas y la analista de cobranzas por pedidos bloqueados debido a deudas no conciliadas:",
                "opciones": {
                    "A": "Toma partido por ventas y ordena desbloquear a todos los clientes sin importar su estatus moroso.",
                    "B": "Respalda a ciegas a cobranzas y prohíbe cualquier diálogo entre los departamentos.",
                    "C": "Reúne a ambas partes, audita las cuentas en disputa, agiliza la validación bancaria y establece un protocolo formal de conciliación diaria para armonizar el flujo.",
                    "D": "Ignora la disputa argumentando que la relación con los clientes es problema exclusivo de la gerencia de ventas."
                }
            },
            7: {
                "enunciado": "Al auditar la caja chica de una sucursal, descubre comprobantes informales o recibos de gastos personales no autorizados por parte de un coordinador de confianza:",
                "opciones": {
                    "A": "Justifica los recibos cargándolos a gastos operativos de representación para proteger al colaborador.",
                    "B": "Levanta un acta de auditoría, frena la reposición del fondo, exige el reembolso inmediato y reporta la anomalía a la Dirección General.",
                    "C": "Destruye los recibos y le pide al involucrado que reponga el dinero poco a poco cuando pueda.",
                    "D": "Cierra la sucursal de forma unilateral paralizando la operación comercial del negocio."
                }
            },
            8: {
                "enunciado": "Presidencia le solicita un reporte estadístico de rentabilidad y gastos departamentales con proyección para una junta directiva imprevista al final de la tarde:",
                "opciones": {
                    "A": "Centraliza la información del sistema administrativo, procesa los indicadores financieros clave y entrega el informe ejecutivo con análisis de desviaciones a tiempo.",
                    "B": "Envía la data cruda sin filtrar ni interpretar diciendo que no tuvo tiempo de generar gráficas.",
                    "C": "Inventa proyecciones aproximadas sin sustento en los libros contables para salir del paso.",
                    "D": "Manifiesta que su horario finaliza a las 6:00 p.m. y que entregará el informe dos días después."
                }
            },
            9: {
                "enunciado": "Respecto a la infalibilidad y el manejo de errores administrativos:",
                "opciones": {
                    "A": "Jamás en ninguno de mis empleos he cometido una sola equivocación en un cálculo, transferencia o reporte.",
                    "B": "Las normas contables son flexibles y no pasa nada grave si un balance tiene inconsistencias menores.",
                    "C": "Cuando he detectado un desfase o error operativo en mi área, lo he asumido con madurez y ejecutado la rectificación inmediata.",
                    "D": "Si el sistema contable falla, prefiero atribuirlo a la incompetencia de los analistas subordinados."
                }
            },
            10: {
                "enunciado": "Un directivo de la empresa le solicita realizar una transferencia bancaria a una cuenta personal sin el debido soporte de orden de pago o factura:",
                "opciones": {
                    "A": "Ejecuta la transferencia de inmediato sin dejar ningún registro en el software administrativo.",
                    "B": "Rechaza la orden de forma grosera y amenaza con denunciar a la directiva en redes sociales.",
                    "C": "Transfiere el monto y altera los libros contables registrándolo a nombre de un proveedor ficticio.",
                    "D": "Solicita respetuosamente el soporte administrativo formal o la instrucción por escrito requerida por auditoría para respaldar el egreso en los libros contables."
                }
            },
            11: {
                "enunciado": "El software administrativo presenta una inconsistencia entre los saldos del inventario teórico y los reportes de almacén:",
                "opciones": {
                    "A": "Realiza un ajuste de inventario manual en el sistema sin investigar las causas de la merma o faltante.",
                    "B": "Culpa al personal de soporte del software y deja el inventario desfasado durante meses.",
                    "C": "Coordina una auditoría de conteo físico selectivo junto al jefe de almacén para conciliar entradas, salidas y corregir la causa raíz.",
                    "D": "Da por bueno el inventario teórico ignorando la existencia física real en los depósitos."
                }
            },
            12: {
                "enunciado": "Debe comunicar a su equipo de trabajo una reestructuración de funciones que implica mayor control de horarios y rotación de tareas:",
                "opciones": {
                    "A": "Impone los cambios mediante un memorando punitivo sin abrir espacio para el diálogo ni la orientación.",
                    "B": "Reúne al equipo, explica con claridad los objetivos estratégicos de la medida, escucha inquietudes y lidera la transición con seguimiento cercano.",
                    "C": "Delega la vocería en un subordinado para evitar asumir el costo emocional de las quejas.",
                    "D": "Informa que no está de acuerdo con los cambios pero que está obligada a aplicarlos por culpa de Presidencia."
                }
            },
            13: {
                "enunciado": "Llega una notificación de fiscalización tributaria (SENIAT / Alcaldía) exigiendo libros de compra y venta al día:",
                "opciones": {
                    "A": "Revisa meticulosamente la integridad de los libros fiscales, constata que los cierres z y retenciones cuadren y atiende la inspección con rigor técnico y solvencia.",
                    "B": "Cierra la oficina y desaloja al personal para fingir que la empresa no está laborando hoy.",
                    "C": "Ofrece un arreglo informal al funcionario fiscal antes de mostrar cualquier libro contable.",
                    "D": "Entrega carpetas incompletas y desordenadas responsabilizando a los auditores externos."
                }
            },
            14: {
                "enunciado": "En relación con las autoridades y directrices corporativas previas:",
                "opciones": {
                    "A": "He tenido divergencias técnicas de criterio con directores, pero siempre defendí mi punto con base en números y respeté la decisión final.",
                    "B": "La alta gerencia rara vez comprende la complejidad del trabajo contable y administrativo.",
                    "C": "No tolero que supervisen mis balances porque mi criterio técnico está por encima de cualquier jefe.",
                    "D": "En todos mis cargos anteriores he trabajado con presidentes y directores absolutamente perfectos y libres de errores."
                }
            },
            15: {
                "enunciado": "Se detecta que un mensajero interno demoró el depósito de cheques de cobro de alto valor durante tres días:",
                "opciones": {
                    "A": "Le resta importancia al asunto considerando que los cheques no pierden vigencia tan rápido.",
                    "B": "Le descuenta el valor de los cheques al mensajero de su sueldo sin investigar los motivos.",
                    "C": "Indaga los motivos de la demora, audita los recibos de entrega, aplica el correctivo disciplinario y rediseña la ruta de entrega bancaria diaria.",
                    "D": "Prohíbe la recepción de cheques en la empresa sin consultar la política comercial de Presidencia."
                }
            },
            16: {
                "enunciado": "Un colaborador clave del departamento administrativo presenta problemas personales que están mermando notablemente su rendimiento en los cierres de mes:",
                "opciones": {
                    "A": "Lo despide de forma fulminante sin evaluar su trayectoria previa en la organización.",
                    "B": "Ignora el bajo rendimiento y absorbe personalmente todo el trabajo atrasado sin decir nada.",
                    "C": "Ridiculiza la situación del colaborador frente al resto de la oficina para presionarlo.",
                    "D": "Sostiene una sesión privada de feedback, acuerda metas de regularización a corto plazo y brinda apoyo dentro de los límites institucionales."
                }
            },
            17: {
                "enunciado": "Al preparar la emisión de pagos a proveedores de la semana, nota que dos facturas presentan duplicidad de conceptos o sobreprecio no acordado en la orden de compra:",
                "opciones": {
                    "A": "Retiene el pago de esas facturas, notifica al departamento de compras para la emisión de notas de crédito y emite el resto de la programación sin demoras.",
                    "B": "Paga el sobreprecio para evitar fricciones con el proveedor y no retrasar la emisión de cheques.",
                    "C": "Cancela la relación comercial con el proveedor de forma unilateral sin consultar a la gerencia general.",
                    "D": "Rompe las facturas y borra la cuenta por pagar del sistema administrativo."
                }
            },
            18: {
                "enunciado": "Se plantea la implementación de un nuevo software ERP para integrar ventas, almacén y contabilidad, generando resistencia en el personal antiguo:",
                "opciones": {
                    "A": "Se une a la resistencia de los empleados para forzar a la empresa a mantener el sistema manual.",
                    "B": "Se capacita a profundidad en la nueva plataforma, lidera con el ejemplo y diseña un plan de inducción progresivo para asegurar la adaptación del equipo.",
                    "C": "Obliga al personal a usar el sistema sin darles manuales ni capacitación previa.",
                    "D": "Utiliza el sistema nuevo solo para contabilidad y deja que las demás áreas sigan trabajando a mano."
                }
            },
            19: {
                "enunciado": "Sobre la confidencialidad de la información financiera y nóminas de sueldos:",
                "opciones": {
                    "A": "Comparto los salarios de la directiva con colaboradores cercanos para fomentar la transparencia.",
                    "B": "Jamás en mi vida he sentido la mínima curiosidad ni he emitido un solo comentario sobre ningún asunto ajeno.",
                    "C": "Resguardo con estricta confidencialidad los datos sensibles, manejando claves de seguridad y restringiendo el acceso a personal no autorizado.",
                    "D": "Si tengo un desacuerdo salarial, utilizo la información de otros sueldos como medida de presión."
                }
            },
            20: {
                "enunciado": "En la verificación de cuentas por cobrar, observa que un cliente antiguo con volumen alto de compras acumula 60 días de mora:",
                "opciones": {
                    "A": "Condona la deuda del cliente por iniciativa propia para mantener una relación comercial amistosa.",
                    "B": "Continúa aprobando pedidos a crédito sin exigir abonos para no perder la comisión de la ruta.",
                    "C": "Bloquea el código en el sistema, elabora un estado de cuenta conciliado y coordina con ventas un plan de pago inmediato antes de nuevos despachos.",
                    "D": "Envía una demanda legal contra el cliente sin notificar previamente a la Dirección General."
                }
            },
            21: {
                "enunciado": "Al procesar la nómina quincenal, se percata de que se calculó un bono de incentivo por error a un trabajador que estuvo de reposo no remunerado:",
                "opciones": {
                    "A": "Paga el bono de todas formas para no generar descontento en el colaborador.",
                    "B": "Modifica manualmente la fórmula de toda la nómina afectando a otros trabajadores para compensar.",
                    "C": "Oculta el descuadre contable registrándolo bajo el rubro de horas extras ficticias.",
                    "D": "Corrige el cálculo antes de emitir la orden de transferencia, notifica con tacto al trabajador y documenta el ajuste para el archivo de nómina."
                }
            },
            22: {
                "enunciado": "La empresa enfrenta una caída temporal de liquidez por retrasos en la cobranza regional y se requiere priorizar compromisos:",
                "opciones": {
                    "A": "Elabora un plan de contingencia financiera, jerarquiza pagos esenciales (nómina, operatividad básica) y presenta escenarios a Presidencia para la toma de decisiones.",
                    "B": "Detiene todos los pagos de la empresa sin excepción hasta que las cuentas bancarias se recuperen solas.",
                    "C": "Solicita un préstamo bancario de alto costo a título corporativo sin la firma de los accionistas.",
                    "D": "Desaparece de la oficina y no responde llamadas de proveedores ni empleados."
                }
            },
            23: {
                "enunciado": "Presidencia le solicita coordinar la logística de suministros y equipos de oficina para la apertura de una nueva sucursal comercial:",
                "opciones": {
                    "A": "Cotiza con al menos tres proveedores calificados, analiza tiempos de entrega, costo-beneficio y ejecuta las compras bajo estricto apego presupuestario.",
                    "B": "Compra los suministros más costosos en el primer establecimiento que encuentra para terminar rápido.",
                    "C": "Delega la compra de equipos en personal subalterno sin fijar límites de gasto ni supervisar facturas.",
                    "D": "Posterga la compra indefinidamente porque considera que la apertura de sucursales no es su función."
                }
            },
            24: {
                "enunciado": "Sobre el control emocional en situaciones de conflicto laboral:",
                "opciones": {
                    "A": "Si alguien me desafía la autoridad en público, le alzo la voz para demostrar quién tiene el mando.",
                    "B": "He tenido situaciones de molestia legítima ante negligencias ajenas, pero canalizo la corrección de forma profesional y privada.",
                    "C": "Poseo una serenidad sobrehumana; jamás ninguna persona ni situación ha logrado incomodarme o disgustarme en lo absoluto.",
                    "D": "Cuando me enojo con un colaborador, le retiro la palabra durante semanas como castigo disciplinario."
                }
            },
            25: {
                "enunciado": "Un cliente exige la devolución de dinero de una factura alegando un error en el pedido, pero la mercancía aún no ha sido recibida en el almacén:",
                "opciones": {
                    "A": "Hace la transferencia de reembolso de inmediato sin comprobar si la mercancía regresó a la empresa.",
                    "B": "Le niega la atención de forma grosera acusándolo de querer estafar a la organización.",
                    "C": "Le pide al cliente que solucione su problema directamente con el chofer que le entregó.",
                    "D": "Explica con cortesía la política de notas de crédito y espera la conformidad de ingreso físico por parte de almacén antes de procesar el ajuste financiero."
                }
            },
            26: {
                "enunciado": "Durante un arqueo sorpresivo, la custodia de la caja chica presenta un faltante de 30 dólares en efectivo:",
                "opciones": {
                    "A": "Pone dinero de su propio bolsillo para tapar el descuadre y no generar problemas en el área.",
                    "B": "Levanta el reporte correspondiente, solicita la justificación documentada a la responsable y aplica la reposición o descuento según la normativa interna.",
                    "C": "Ignora la diferencia asumiendo que 30 dólares no afectan el patrimonio de la compañía.",
                    "D": "Llama a las autoridades policiales de inmediato antes de realizar una verificación de comprobantes."
                }
            },
            27: {
                "enunciado": "Al cierre de la jornada a las 6:00 p.m., el sistema bancario concluye la compensación y requiere validar los créditos recibidos para autorizar los despachos de la madrugada siguiente:",
                "opciones": {
                    "A": "Apaga el computador puntualmente y deja la validación para el mediodía del día siguiente sin importar los camiones.",
                    "B": "Asume la extensión horaria con flexibilidad gerencial, finaliza la conciliación de créditos y deja las órdenes liberadas para el equipo de despacho.",
                    "C": "Aprueba todos los despachos a ciegas sin conciliar para poder marcharse a su hora.",
                    "D": "Se queja formalmente con los choferes acusándolos de ser una carga innecesaria para el personal de oficina."
                }
            },
            28: {
                "enunciado": "Debe redactar el informe mensual de gestión administrativa para la junta directiva:",
                "opciones": {
                    "A": "Presenta un informe ejecutivo consolidando estadísticas de cobranza, gastos, rentabilidad, cumplimiento fiscal y recomendaciones de optimización.",
                    "B": "Envía un correo con tres líneas diciendo que la administración se encuentra marchando con normalidad.",
                    "C": "Copia el informe del mes anterior cambiando solo las fechas sin actualizar ningún número contable.",
                    "D": "Exige que cada jefe de departamento redacte el informe por su cuenta y lo entregue directamente a Presidencia."
                }
            },
            29: {
                "enunciado": "En su relación con otros líderes departamentales y ascensos internos:",
                "opciones": {
                    "A": "Jamás en mi trayectoria he sentido un solo ápice de desacuerdo, recelo o inconformidad ante decisiones de la Dirección.",
                    "B": "En ocasiones he defendido con firmeza el presupuesto de mi área frente a otras gerencias, buscando siempre el consenso institucional.",
                    "C": "Considero que las demás gerencias operativas solo generan gastos inútiles y entorpecen la administración.",
                    "D": "Prefiero no generar vínculos con otras áreas porque cada gerencia debe velar exclusivamente por sus propios intereses."
                }
            },
            30: {
                "enunciado": "Presidencia le encomienda una tarea de auditoría confidencial sobre un área sensible de la organización:",
                "opciones": {
                    "A": "Comenta la asignación con los colaboradores del departamento durante el almuerzo para pedir opiniones.",
                    "B": "Se niega a realizar la auditoría argumentando que eso generará antipatía entre sus compañeros de trabajo.",
                    "C": "Ejecuta la auditoría con absoluto sigilo profesional, recopila evidencias verificables y rinde cuentas exclusivamente a Presidencia.",
                    "D": "Modifica los hallazgos para favorecer a sus colaboradores más cercanos y no perjudicarlos."
                }
            }
        }
    },

    # =========================================================================
    # 03. ALMACENISTA (CJS-ALM)
    # =========================================================================
    "03_ALMACENISTA": {
        "codigo": "CJS-ALM",
        "titulo": "EVALUACIÓN PSICOTÉCNICA SITUACIONAL EN ALMACÉN E INVENTARIO",
        "instrucciones": "Lea atentamente cada situación laboral. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Sea totalmente honesto sobre su forma real de actuar en el trabajo físico y operativo. Dispone de un tiempo máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "Al descargar una gandola de flota primaria, nota que tres bultos de producto vienen rotos por una mala estiba:",
                "opciones": {
                    "A": "Los coloca al fondo del almacén para despacharlos rápido a clientes que no revisen mucho.",
                    "B": "Recibe todo completo para no demorar al chofer y luego le avisa al jefe de almacén si hay tiempo.",
                    "C": "Rechaza la gandola completa sin permitir la descarga de los demás productos intactos.",
                    "D": "Separa la mercancía dañada, notifica de inmediato al supervisor y levanta la nota de rechazo/avería antes de firmar la guía."
                }
            },
            2: {
                "enunciado": "El jefe de almacén le indica que antes de despachar un pedido urgente debe barrer y despejar el pasillo principal por seguridad:",
                "opciones": {
                    "A": "Pasa por alto la orden y monta el pedido para demostrar que el despacho es más prioritario.",
                    "B": "Acata la instrucción, despeja y limpia el pasillo con rapidez y luego procede con la carga.",
                    "C": "Hace la limpieza a regañadientes y se queja con los choferes de la exigencia del jefe.",
                    "D": "Le dice a un compañero de menor rango que barra para usted ocuparse solo de lo importante."
                }
            },
            3: {
                "enunciado": "En el almacén ingresa un lote nuevo del mismo producto con vencimiento a 12 meses, mientras en el anaquel queda stock que vence en 3 meses:",
                "opciones": {
                    "A": "Ubica el lote nuevo detrás o debajo del lote antiguo para garantizar la rotación correcta (FIFO/PEPS).",
                    "B": "Coloca el lote nuevo al frente porque las cajas vienen más limpias y mejor presentadas.",
                    "C": "Mezcla ambos lotes en la misma tarima sin importar la fecha de vencimiento.",
                    "D": "Deja el lote nuevo en el piso del pasillo para despacharlo primero por comodidad de agarre."
                }
            },
            4: {
                "enunciado": "En su rutina de trabajo y relaciones laborales diarias:",
                "opciones": {
                    "A": "Si un compañero no trabaja a mi ritmo, le reclamo fuertemente de inmediato.",
                    "B": "A veces siento cansancio o estrés por la carga física pesada, pero mantengo el ritmo y el cuidado.",
                    "C": "Jamás en mi vida he sentido pereza, fatiga o desánimo al momento de hacer fuerza física.",
                    "D": "Prefiero trabajar solo porque no tolero que nadie opine sobre mi forma de cargar."
                }
            },
            5: {
                "enunciado": "Durante el conteo físico diario, el sistema indica que deben existir 150 cajas de un producto, pero usted cuenta físicamente 148 cajas:",
                "opciones": {
                    "A": "Ajusta el informe escribiendo 150 para evitar llamadas de atención y que el inventario cuadre.",
                    "B": "Asume que se entregaron dos de más por error en despachos anteriores y lo deja pasar sin reportar.",
                    "C": "Le echa la culpa al turno de despacho anterior antes de volver a verificar el lote.",
                    "D": "Realiza un reconteo detallado, verifica la zona de averías/muestras y reporta el faltante real al jefe de almacén."
                }
            },
            6: {
                "enunciado": "Un chofer de despacho le pide apurar la carga ofreciéndole 'un refresco o propina' para que no le revise minuciosamente el camión:",
                "opciones": {
                    "A": "Acepta el refresco y carga rápido sin verificar cantidades exactas ni estado del vehículo.",
                    "B": "Se molesta de forma agresiva y detiene la operación de despacho durante todo el día.",
                    "C": "Rechaza con respeto el ofrecimiento y realiza el chequeo minucioso de cada bulto según la factura.",
                    "D": "Deja que el chofer cargue solo lo que quiera mientras usted llena los papeles en la oficina."
                }
            },
            7: {
                "enunciado": "Al mover una paleta con la transpaleta, tropieza accidentalmente con un estante y abolla dos cajas de mercancía:",
                "opciones": {
                    "A": "Mete las dos cajas abolladas en medio de un pedido grande para que el cliente no lo note.",
                    "B": "Notifica de inmediato al jefe de almacén sobre el accidente para verificar el contenido y registrar la merma.",
                    "C": "Deja las cajas dañadas en el pasillo y se retira fingiendo que no sabe quién causó el golpe.",
                    "D": "Culpa al conductor del montacargas o al chofer que estaba cerca del área."
                }
            },
            8: {
                "enunciado": "Son las 4:45 p.m. (su hora de salida es a las 5:00 p.m.) y llega un camión imprevisto con mercancía crítica que requiere descarga inmediata:",
                "opciones": {
                    "A": "Apoya con disposición al equipo para iniciar la descarga organizada, extendiendo su jornada según la necesidad operativa.",
                    "B": "Se cambia de ropa de inmediato para salir puntual argumentando que no le avisaron con tiempo.",
                    "C": "Se esconde en un área ciega del almacén hasta que den las 5:00 p.m. para poder retirarse.",
                    "D": "Descarga con brusquedad tirando las cajas al piso como muestra de molestia por la hora."
                }
            },
            9: {
                "enunciado": "Respecto al cumplimiento de las normas de seguridad industrial y dotación (botas, fajas, guantes):",
                "opciones": {
                    "A": "Cumplo al pie de la letra el 100% de las normas cada segundo; jamás me he quitado un equipo de protección ni por calor extremo.",
                    "B": "Considero que los equipos de seguridad son estorbos innecesarios que solo retrasan la velocidad del trabajo.",
                    "C": "Procuro usar siempre el equipo de seguridad asignado, aunque en ocasiones el calor o la faena resulten incómodos.",
                    "D": "Solo me coloco las botas y la faja cuando veo entrar al supervisor al almacén."
                }
            },
            10: {
                "enunciado": "Un cliente que vino a retirar mercancía directamente al almacén le pide que le añada 'dos bultos extras' que no están en la factura prometiendo pagarlos luego:",
                "opciones": {
                    "A": "Le entrega los dos bultos de palabra confiando en que el cliente es conocido de la casa.",
                    "B": "Le propone al cliente cobrarle esos dos bultos por mitad de precio para su propio bolsillo.",
                    "C": "Le dice que sí pero le pide al chofer que los saque escondidos debajo del asiento.",
                    "D": "Le informa con firmeza y educación que solo despacha lo facturado y lo orienta a facturar el adicional en administración."
                }
            },
            11: {
                "enunciado": "Debe armar un pedido complejo con 20 renglones distintos y varias referencias son muy parecidas en su empaque:",
                "opciones": {
                    "A": "Se guía únicamente por el color de la caja a simple vista para no perder tiempo leyendo etiquetas.",
                    "B": "Agarra las primeras cajas que ve en el pasillo asumiendo que todas contienen el mismo producto.",
                    "C": "Verifica código por código, descripción y fecha de cada bulto contra el picking list antes de montarlo.",
                    "D": "Arma el pedido al cálculo aproximado para salir rápido del compromiso de carga."
                }
            },
            12: {
                "enunciado": "Su supervisor le llama la atención porque dejó cajas mal apiladas que representan un riesgo de caída:",
                "opciones": {
                    "A": "Le discute al supervisor diciéndole que las cajas no se van a caer y que él sabe cómo hace su trabajo.",
                    "B": "Acepta la corrección, reestiba la paleta garantizando el amarre seguro y cuida la altura reglamentaria.",
                    "C": "Se va del almacén enfadado y deja las cajas tiradas en el piso.",
                    "D": "Reestiba la mercancía pero habla mal del supervisor a espaldas con el resto del personal."
                }
            },
            13: {
                "enunciado": "Durante una jornada de lluvia intensa se produce una filtración imprevista en el techo sobre un lote de harina/azúcar:",
                "opciones": {
                    "A": "Traslada de inmediato la mercancía a una zona seca, cubre los bultos con plástico y reporta la avería.",
                    "B": "Se queda esperando que el jefe de mantenimiento llegue para que tome cartas en el asunto.",
                    "C": "Deja que el agua caiga sobre el producto pensando que la empresa tiene seguro contra pérdidas.",
                    "D": "Se retira del área mojada para evitar resbalarse sin avisar a nadie sobre el riesgo de la mercancía."
                }
            },
            14: {
                "enunciado": "En relación con las autoridades y jefaturas en sus empleos pasados:",
                "opciones": {
                    "A": "He tenido desacuerdos con algunos jefes sobre la forma de organizar la carga, pero siempre los resolví hablando con respeto.",
                    "B": "La mayoría de los jefes no saben nada de cómo se trabaja con el lomo en el almacén.",
                    "C": "No me gusta tener jefes porque prefiero hacer las cosas a mi propio criterio y ritmo.",
                    "D": "En todos mis trabajos anteriores he tenido jefes absolutamente perfectos con quienes jamás tuve la menor diferencia."
                }
            },
            15: {
                "enunciado": "Al momento de chequear una devolución de mercancía que trae un camión de reparto:",
                "opciones": {
                    "A": "Firma la recepción a ciegas confiando en lo que dice el chofer sin contar ni abrir las cajas.",
                    "B": "Recibe únicamente lo que esté en perfecto estado y bota a la basura lo demás sin registrarlo en el sistema.",
                    "C": "Revisa bulto por bulto, verifica sellos, fechas de caducidad, causa de rechazo y firma la nota con el estado real.",
                    "D": "Deja la mercancía devuelta en el camión diciendo que en el almacén no hay espacio para cosas viejas."
                }
            },
            16: {
                "enunciado": "El personal del área de facturación/administración le solicita apoyo urgente para mover un lote de archivos pesados a un depósito:",
                "opciones": {
                    "A": "Responde de mala manera diciendo que a él no le pagan para mover papeles de oficina.",
                    "B": "Se sienta a esperar que el jefe de almacén le dé una orden por escrito antes de dar cualquier paso.",
                    "C": "Exige un pago en efectivo adicional antes de prestar cualquier ayuda a otro departamento.",
                    "D": "Coordina un momento oportuno con su supervisor y presta el apoyo solidario con buena disposición."
                }
            },
            17: {
                "enunciado": "Mientras organiza un anaquel, encuentra varios productos que vencen la próxima semana y no han rotado:",
                "opciones": {
                    "A": "Aparta los productos, elabora un reporte de riesgo de vencimiento y avisa al jefe para su remate comercial.",
                    "B": "Los esconde detrás de otros lotes para que el supervisor no lo culpe por no haberlos visto antes.",
                    "C": "Los bota en el contenedor de basura sin consultar para evitar que la gerencia se entere.",
                    "D": "Continúa acomodando el resto del anaquel sin prestar atención a las fechas de caducidad."
                }
            },
            18: {
                "enunciado": "La empresa instala cámaras de seguridad dentro de las naves del almacén para monitoreo de inventario:",
                "opciones": {
                    "A": "Busca puntos ciegos dentro del almacén para descansar o manipular bultos donde la cámara no lo enfoque.",
                    "B": "Comprende la medida como una protección para el resguardo de la mercancía y la seguridad del propio personal.",
                    "C": "Incita a sus compañeros a quejarse diciendo que la empresa los trata como delincuentes.",
                    "D": "Desconecta disimuladamente el cable de la cámara más cercana a su área de trabajo."
                }
            },
            19: {
                "enunciado": "Si se comete un error en el conteo o se rompe un paquete durante la faena:",
                "opciones": {
                    "A": "Intento parcharlo disimuladamente con tirro transparente para que pase desapercibido en el camión.",
                    "B": "Jamás en mi vida laboral se me ha resbalado, roto o caído un solo producto de las manos ni he contado mal.",
                    "C": "Cuando me he equivocado o se me ha dañado algo, lo he reportado de inmediato para corregirlo.",
                    "D": "Dejo el producto roto en el piso para que el personal de limpieza lo recoja y lo bote."
                }
            },
            20: {
                "enunciado": "Al momento de preparar un pedido, nota que un compañero de almacén está guardando herramientas o productos de la empresa en su bolso personal:",
                "opciones": {
                    "A": "Se queda callado y finge no ver nada para evitar ganarse problemas con sus compañeros de cuadrilla.",
                    "B": "Le pide a su compañero una parte de lo sustraído para guardar silencio y no delatarlo.",
                    "C": "Notifica con discreción e inmediatez al jefe de almacén o seguridad para frenar el hurto y proteger su integridad.",
                    "D": "Confronte físicamente al compañero en el pasillo a golpes frente a los choferes."
                }
            },
            21: {
                "enunciado": "Llega un cargamento grande y se requiere el esfuerzo coordinado de toda la cuadrilla para descargarlo antes del mediodía:",
                "opciones": {
                    "A": "Trabaja muy rápido al principio y luego se ausenta al baño durante 45 minutos para descansar.",
                    "B": "Deja que los compañeros más jóvenes hagan la fuerza pesada mientras usted solo lleva el control en papel.",
                    "C": "Provoca discusiones con el equipo quejándose constantemente de la cantidad de gandolas que llegan.",
                    "D": "Trabaja en equipo hombro a hombro, manteniendo la sincronía en la cadena humana y cuidando la postura ergonómica."
                }
            },
            22: {
                "enunciado": "Al finalizar la jornada, el pasillo donde trabajó queda con restos de cartón, plástico y paletas desordenadas:",
                "opciones": {
                    "A": "Se marcha diciendo que para eso hay personal contratado exclusivamente para la limpieza general.",
                    "B": "Recoge, despeja y ordena su área de trabajo antes de marcar la salida, dejando el pasillo listo para el día siguiente.",
                    "C": "Patea los restos de plástico debajo de los estantes para que no se vean a simple vista.",
                    "D": "Le exige a la empresa un pago adicional si quieren que barra el piso al terminar la estiba."
                }
            },
            23: {
                "enunciado": "El supervisor le pide realizar un conteo selectivo de un rubro de alto valor (licores, café, leche) durante el horario de almuerzo:",
                "opciones": {
                    "A": "Coordina con su supervisor para almorzar inmediatamente después y realiza el conteo físico con exactitud.",
                    "B": "Se niega rotundamente afirmando que el horario de almuerzo es intocable y que cuenten ellos mismos.",
                    "C": "Hace el conteo desde lejos sin mover las cajas, inventando los números para irse rápido a comer.",
                    "D": "Realiza el conteo de mala gana y anota cualquier cifra para salir del paso."
                }
            },
            24: {
                "enunciado": "Sobre los momentos de tensión o discusiones en el almacén:",
                "opciones": {
                    "A": "Si alguien me grita o me alza la voz en la plataforma, respondo exactamente con los mismos insultos.",
                    "B": "He tenido momentos en que he perdido un poco la paciencia con la lentitud de otros, pero sé controlarme y dialogar.",
                    "C": "Tengo una paciencia infinita; absolutamente nada ni nadie en este mundo puede hacerme molestar jamás.",
                    "D": "Cuando me enojo en el trabajo, tiro las cosas al piso y me niego a trabajar por varias horas."
                }
            },
            25: {
                "enunciado": "Durante la carga de una gandola para un cliente foráneo, nota que faltan 5 cajas para completar el pedido y no hay más stock en almacén:",
                "opciones": {
                    "A": "Completa las 5 cajas faltantes con otro producto de menor valor sin avisar al cliente ni al chofer.",
                    "B": "Carga el camión incompleto y deja que el chofer resuelva el problema con el cliente cuando llegue a destino.",
                    "C": "Notifica de inmediato a facturación y despacho para corregir la guía/factura antes de que el camión salga.",
                    "D": "Cierra la puerta del camión y firma la guía como si hubiese entregado la cantidad completa."
                }
            },
            26: {
                "enunciado": "Una transpaleta manual presenta una rueda trancada que dificulta el rodamiento:",
                "opciones": {
                    "A": "La sigue usando con fuerza bruta hasta que la rueda termine de romperse o dañe el piso.",
                    "B": "La esconde en un rincón oscuro para que otro compañero sea quien la use y asuma la culpa.",
                    "C": "Se niega a mover cualquier mercancía argumentando que no hay condiciones mecánicas para trabajar.",
                    "D": "Reporta la falla al jefe para su lubricación/reparación y utiliza una herramienta en buen estado."
                }
            },
            27: {
                "enunciado": "Debe colocar mercancía pesada en los niveles superiores de un estante metálico:",
                "opciones": {
                    "A": "La coloca arriba sin asegurar los topes ni zunchar la paleta para ahorrar tiempo de estiba.",
                    "B": "Utiliza los equipos adecuados, respeta los límites de carga por nivel y asegura la paleta según normas de apilamiento.",
                    "C": "Amontona las cajas en el pasillo violando el paso seguro para no tener que subir tanta altura.",
                    "D": "Pide a dos compañeros que la lancen desde abajo para evitar subir la escalera o usar el montacargas."
                }
            },
            28: {
                "enunciado": "Un transportista le ofrece pagarle a usted en efectivo para que le permita llevarse 3 tarimas de madera (paletas) de la empresa:",
                "opciones": {
                    "A": "Rechaza rotundamente el ofrecimiento, indicándole que los bienes de la empresa no se venden y reporta la situación.",
                    "B": "Acepta el dinero considerando que son solo paletas viejas y que nadie las va a extrañar.",
                    "C": "Le dice al chofer que se las lleve escondidas pero que le pague después fuera de las instalaciones.",
                    "D": "Deja las paletas cerca de la reja para que el transportista las tome por su cuenta sin involucrarse."
                }
            },
            29: {
                "enunciado": "Respecto al deseo de superación y compañerismo en el trabajo:",
                "opciones": {
                    "A": "Nunca en mi vida he sentido celos, envidia ni incomodidad por los ascensos o felicitaciones que reciben otros.",
                    "B": "A veces siento curiosidad o cierta sana rivalidad, pero me enfoco en cumplir bien con mis tareas y ganarme lo mío.",
                    "C": "Pienso que al que ascienden en el almacén es siempre por ser amigo personal de los jefes.",
                    "D": "No me interesa relacionarme con nadie porque los compañeros de trabajo siempre son desleales."
                }
            },
            30: {
                "enunciado": "Se detecta un faltante grave de inventario y la gerencia reúne a todo el personal para investigar lo ocurrido:",
                "opciones": {
                    "A": "Se muestra agresivo e insulta al personal de seguridad por sospechar de la cuadrilla de almacén.",
                    "B": "Aprovecha la reunión para acusar sin pruebas a compañeros con los que tiene problemas personales.",
                    "C": "Colabora con total transparencia en la auditoría, facilitando sus registros y cooperando con la investigación.",
                    "D": "No asiste al trabajo al día siguiente para no involucrarse en la investigación."
                }
            }
        }
    },

    # =========================================================================
    # 04. ANALISTA DE COBRANZA (CJS-COB)
    # =========================================================================
    "04_ANALISTA_DE_COBRANZA": {
        "codigo": "CJS-COB",
        "titulo": "EVALUACIÓN PSICOTÉCNICA SITUACIONAL EN COBRANZAS Y CONCILIACIÓN BANCARIA",
        "instrucciones": "Lea con atención cada situación laboral y de relacionamiento con clientes y vendedores. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con honestidad sobre su estilo real de recuperación de cartera, rigor numérico y apego a normas. Dispone de un máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "A primera hora de la mañana solicita los estados de cuenta a la Gerencia Administrativa para conciliar las cobranzas del día anterior, pero el banco muestra varias transferencias sin número de factura ni nombre del depositante claro:",
                "opciones": {
                    "A": "Aplica los montos al azar a los clientes más antiguos para limpiar los saldos bancarios rápido.",
                    "B": "Deja las transferencias sin conciliar durante semanas hasta que los clientes llamen a reclamar.",
                    "C": "Asume que son aportes de capital de los socios y no las registra en el módulo de cuentas por cobrar.",
                    "D": "Identifica montos y bancos de origen, cruza con los reportes de pago de los asesores de ruta y concilia los depósitos confirmados antes de la salida de despachos."
                }
            },
            2: {
                "enunciado": "Un asesor de ventas le insiste en que desbloquee en el sistema a un cliente clave con factura vencida de 35 días, prometiendo que el cliente pagará en efectivo al momento de recibir el nuevo pedido:",
                "opciones": {
                    "A": "Desbloquea al cliente de palabra asumiendo el riesgo para no perjudicar la comisión del vendedor.",
                    "B": "Mantiene el bloqueo en estricto apego a la política de crédito, explica al vendedor el procedimiento y le solicita gestionar el comprobante de pago previo a la liberación.",
                    "C": "Elimina la factura vencida del sistema administrativo para que el código quede limpio permanentemente.",
                    "D": "Le cobra una tarifa personal en efectivo al vendedor para agilizar el desbloqueo informal del cliente."
                }
            },
            3: {
                "enunciado": "Al verificar un comprobante de transferencia bancaria enviado por un cliente para saldar una deuda de $500, nota indicios de que la imagen fue editada digitalmente (captura falsa):",
                "opciones": {
                    "A": "Verifica minuciosamente en el estado de cuenta bancario real de la empresa, confirma la inexistencia de los fondos, frena el despacho y notifica a la Gerencia Administrativa y al Asesor.",
                    "B": "Aprueba el pago en el sistema asumiendo que el banco demora varias horas en reflejar los fondos.",
                    "C": "Le reenvía el comprobante falso a la fuerza de ventas felicitando al cliente por su puntualidad.",
                    "D": "Llama al cliente insultándolo de forma agresiva y amenazándolo con acciones legales inmediatas sin verificar con el banco."
                }
            },
            4: {
                "enunciado": "En su trayectoria profesional y gestión de cobro bajo presión:",
                "opciones": {
                    "A": "Si un cliente me habla con tono arrogante, le cuelgo el teléfono y me niego a atenderlo de por vida.",
                    "B": "En ocasiones he sentido frustración o desgaste mental al cobrar a clientes morosos difíciles, pero mantengo la firmeza profesional y el autocontrol.",
                    "C": "Jamás en toda mi vida laboral he sentido la menor molestia, tensión ni impaciencia al gestionar un cobro difícil.",
                    "D": "Prefiero que la fuerza de ventas cobre como quiera sin que yo tenga que llevar ningún control."
                }
            },
            5: {
                "enunciado": "Un cliente con alta mora se niega a cancelar la totalidad de una factura vencida, alegando que un lote de mercancía de hace dos meses le generó mermas que nadie le reconoció:",
                "opciones": {
                    "A": "Le condona la deuda completa por iniciativa propia para evitar seguir discutiendo por teléfono.",
                    "B": "Le dice al cliente que ese no es su problema y que le va a embargar el negocio al día siguiente.",
                    "C": "Modifica la factura en el sistema rebajando el precio sin contar con ninguna nota de crédito autorizada.",
                    "D": "Escucha el planteamiento, contacta a Almacén/Ventas para constatar si existe una nota de devolución formal y concilia un abono inmediato sobre el saldo no disputado."
                }
            },
            6: {
                "enunciado": "Un vendedor le hace entrega al final de la tarde de tres cheques de cobro de clientes foráneos para su entrega a la Gerencia Administrativa:",
                "opciones": {
                    "A": "Guarda los cheques sueltos en su gaveta sin contarlos ni llenar el formato de control hasta la semana entrante.",
                    "B": "Le devuelve los cheques al vendedor diciéndole que él mismo vaya a depositarlos al banco en efectivo.",
                    "C": "Revisa montos, firmas, fechas y endosos, llena el formato oficial de control y los entrega formalmente a la Gerencia Administrativa ese mismo día.",
                    "D": "Cambia uno de los cheques con un comerciante amigo para disponer de efectivo personal provisional."
                }
            },
            7: {
                "enunciado": "Al auditar la cartera de clientes de una ruta foránea, detecta que el 40% de los clientes supera los 30 días de mora permitidos por la empresa:",
                "opciones": {
                    "A": "Emite un informe consolidado de morosidad por ruta, aplica el bloqueo preventivo del canal y coordina con el Supervisor de Ventas un operativo de recuperación focalizado.",
                    "B": "Oculta la morosidad a la Gerencia General para no perjudicar la evaluación mensual del supervisor de ventas.",
                    "C": "Borra a los clientes morosos de la base de datos para que la cartera parezca saneada.",
                    "D": "Sugiere a la empresa que regale la mercancía vencida a los clientes para no tener que cobrarles."
                }
            },
            8: {
                "enunciado": "Son las 5:45 p.m. (su hora de salida es a las 6:00 p.m.) y la fuerza de ventas envía una ráfaga de 15 comprobantes de pago urgentes para liberar pedidos que deben viajar en la madrugada:",
                "opciones": {
                    "A": "Valida los 15 depósitos contra los saldos bancarios en línea, libera en el sistema las facturas que tengan fondos reales confirmados y deja el reporte cerrado para despacho.",
                    "B": "Apaga el computador inmediatamente a las 6:00 p.m. dejando todos los camiones parados hasta el día siguiente.",
                    "C": "Aprueba los 15 pedidos a ciegas sin entrar al banco para poder marcharse puntual a su casa.",
                    "D": "Borra los comprobantes del correo para justificar que nunca los recibieron a tiempo."
                }
            },
            9: {
                "enunciado": "Respecto a la rigurosidad en los cálculos numéricos y arqueo de comprobantes de pago:",
                "opciones": {
                    "A": "Jamás en ninguno de mis empleos anteriores he tenido una discrepancia de un solo centavo al conciliar un estado de cuenta.",
                    "B": "Considero que las diferencias pequeñas de dinero no tienen importancia en empresas grandes.",
                    "C": "Cuando he detectado un descuadre en una cuenta por cobrar, he revisado comprobante por comprobante hasta corregirlo con transparencia.",
                    "D": "Si el saldo de una cuenta no cuadra, prefiero atribuirlo a errores del software contable de la empresa."
                }
            },
            10: {
                "enunciado": "Un cliente realiza un pago en divisas en efectivo directamente en la oficina de cobranzas pero exige que le entreguen la mercancía sin emitir recibo oficial:",
                "opciones": {
                    "A": "Acepta el dinero en efectivo sin emitir recibo y se lo guarda en el bolsillo personal.",
                    "B": "Le grita al cliente acusándolo de estafador frente a los demás visitantes de la oficina.",
                    "C": "Recibe el efectivo y lo anota en un papel suelto para entregarlo en caja chica cuando se acuerde.",
                    "D": "Explica con firmeza y educación que todo ingreso requiere recibo oficial numerado y sellado, procesando el documento y entregando la copia conforme al cliente."
                }
            },
            11: {
                "enunciado": "Varios vendedores se quejan porque afirman que el listado de clientes bloqueados no se les notifica a tiempo, provocando que tomen pedidos que luego son rechazados:",
                "opciones": {
                    "A": "Les dice a los vendedores que ellos deberían memorizar la lista de morosos sin necesidad de reportes.",
                    "B": "Deja de bloquear clientes en el sistema para que ningún pedido sea rebotado nunca más.",
                    "C": "Establece una rutina de corte diario a primera hora: actualiza el estatus en el sistema y difunde el consolidado de bloqueos formalmente a la fuerza comercial.",
                    "D": "Bloquea el acceso de los vendedores al sistema de ventas para evitar que emitan reclamos."
                }
            },
            12: {
                "enunciado": "Un cliente con factura vencida de alto monto propone pagar con un cheque a fecha diferida de 20 días para que le despachen un pedido nuevo hoy:",
                "opciones": {
                    "A": "Acepta el cheque diferido y autoriza el despacho nuevo por cuenta propia sin consultar a nadie.",
                    "B": "Consulta la política de crédito institucional, somete el caso a la Gerencia Administrativa y no libera despacho nuevo hasta tanto el instrumento no sea liquidado o avalado formalmente.",
                    "C": "Rechaza el cheque de forma despectiva y rompe relaciones comerciales con el cliente de manera unilateral.",
                    "D": "Recibe el cheque y le pide al cliente una comisión en efectivo por haberle recibido el pago."
                }
            },
            13: {
                "enunciado": "Durante la conciliación de fin de mes, detecta que un depósito bancario de $300 fue acreditado por error dos veces en el sistema a un mismo cliente:",
                "opciones": {
                    "A": "Reversa el registro duplicado en el sistema, corrige el estado de cuenta real del cliente y deja la constancia de ajuste documentada en el informe mensual.",
                    "B": "Deja el error en el sistema para favorecer al cliente y que este tenga saldo a favor artificial.",
                    "C": "Borra la cuenta del cliente para que los auditores externos no se den cuenta del duplicado.",
                    "D": "Le cobra $50 al cliente por mantenerle el saldo a favor en el sistema administrativo."
                }
            },
            14: {
                "enunciado": "En relación con las jefaturas administrativas y las metas de cobranza fijadas:",
                "opciones": {
                    "A": "He tenido debates técnicos sobre porcentajes de morosidad con mis gerentes, pero siempre respaldé mi postura con análisis de cartera y acaté la meta corporativa.",
                    "B": "Las gerencias administrativas siempre fijan metas de recuperación absurdas que no se pueden cumplir en la calle.",
                    "C": "No tolero que supervisen mi gestión de llamadas porque nadie sabe cobrar mejor que yo.",
                    "D": "En todas las empresas donde he laborado he tenido gerentes de crédito y cobranza absolutamente perfectos y libres de fallas."
                }
            },
            15: {
                "enunciado": "Un asesor de ventas le solicita que le preste provisionalmente $100 en efectivo de los cobros recibidos del día para solventar una urgencia de gasolina en ruta:",
                "opciones": {
                    "A": "Le entrega el dinero en efectivo de la cobranza sin recibo confiando en su palabra de honor.",
                    "B": "Le presta el dinero pero le cobra un porcentaje de interés personal por el favor.",
                    "C": "Niega rotundamente la solicitud, explica que los fondos de cobranza son intocables y lo orienta a tramitar caja chica o viáticos por la vía regular.",
                    "D": "Le dice que tome el dinero directamente del sobre de cobranza sin que nadie los vea."
                }
            },
            16: {
                "enunciado": "Al revisar la antigüedad de saldos, observa que una cuenta por cobrar de hace 90 días no tiene ninguna gestión de cobro registrada en el expediente:",
                "opciones": {
                    "A": "Elimina la deuda del balance general para no alterar los indicadores de gestión del departamento.",
                    "B": "Acusa al departamento legal de negligencia sin antes haber realizado la gestión extrajudicial.",
                    "C": "Se desentiende del caso argumentando que las deudas viejas ya no se pueden recuperar jamás.",
                    "D": "Reconstruye el historial de facturas, ubica al cliente vía telefónica/presencial, envía el requerimiento formal de pago y coordina plan de liquidación o pase a cobranza legal."
                }
            },
            17: {
                "enunciado": "El sistema administrativo presenta un error de enlace y no actualiza automáticamente las notas de crédito de devoluciones emitidas por almacén:",
                "opciones": {
                    "A": "Cruza manualmente las notas de crédito autorizadas contra las facturas afectadas, aplica los descuentos correspondientes en la conciliación y levanta el ticket a Sistemas.",
                    "B": "Ignora las notas de crédito y cobra a los clientes el monto bruto completo sin reconocerles las devoluciones.",
                    "C": "Anula todas las facturas en el sistema provocando un descuadre en los libros de ventas.",
                    "D": "Se sienta a esperar que el departamento de Sistemas resuelva el problema sin hacer ningún seguimiento."
                }
            },
            18: {
                "enunciado": "Un cliente moroso se presenta en la oficina sumamente alterado y gritando, asegurando que le suspendieron el crédito de forma injusta:",
                "opciones": {
                    "A": "Le responde con gritos e insultos llamando al personal de seguridad para que lo saque a golpes.",
                    "B": "Mantiene la compostura y el tono profesional, lo invita a sentarse en un área privada, le proyecta el estado de cuenta con las fechas de mora y busca un acuerdo de pago civilizado.",
                    "C": "Le pide perdón avergonzada y le desbloquea el crédito ilimitado de inmediato para que se calle.",
                    "D": "Se encierra en el baño y deja al cliente gritando solo en el pasillo de la empresa."
                }
            },
            19: {
                "enunciado": "Sobre la confidencialidad de la solvencia financiera y deudas de los clientes:",
                "opciones": {
                    "A": "Comento públicamente en reuniones sociales qué comerciantes de la zona están quebrados o morosos.",
                    "B": "Jamás en toda mi vida he sentido la mínima curiosidad por saber cuánto dinero manejan las empresas de los clientes.",
                    "C": "Manejo la información financiera, saldos deudores y datos comerciales de los clientes con estricta reserva y ética profesional.",
                    "D": "Le vendo el listado de clientes morosos a empresas de cobranzas externas sin autorización de la Gerencia."
                }
            },
            20: {
                "enunciado": "Un supervisor de ventas le solicita que no reporte a la Gerencia General que dos de sus rutas están al 50% de cobro semanal para no perjudicar la reunión de negocio:",
                "opciones": {
                    "A": "Modifica las estadísticas en la presentación para que parezca que las rutas van al 100% de efectividad.",
                    "B": "Borra las facturas pendientes de cobro de esas dos rutas en el sistema administrativo.",
                    "C": "Presenta los indicadores reales con transparencia y rigor técnico, ofreciendo un desglose objetivo de los clientes que generan el retraso para apoyar la toma de decisiones.",
                    "D": "Acepta ocultar los datos si el supervisor le ofrece un regalo o beneficio personal."
                }
            },
            21: {
                "enunciado": "Al momento de conciliar los pagos de un cliente mayorista, detecta una diferencia menor de $5 entre la factura emitida y la transferencia realizada por comisiones bancarias:",
                "opciones": {
                    "A": "Bloquea al cliente mayorista y paraliza un despacho de $10.000 por los $5 de comisión bancaria sin mediar diálogo.",
                    "B": "Insulta al cajero del banco por teléfono acusándolo de descontar comisiones excesivas.",
                    "C": "Pone los $5 de su propio bolsillo sin documentar el ajuste para no tener que revisar el comprobante.",
                    "D": "Contacta al cliente, aclara el concepto de la deducción por comisión interbancaria, concilia el ajuste contable correspondiente y autoriza el despacho."
                }
            },
            22: {
                "enunciado": "La Gerencia Administrativa le solicita elaborar el informe semanal de recuperación de cartera y proyección de ingresos para el flujo de caja:",
                "opciones": {
                    "A": "Envía una hoja en blanco con una nota diciendo que el flujo de caja se calcula en la administración central.",
                    "B": "Consolida los cobros reales liquidados en banco, discrimina la mora por tramos de vencimiento y proyecta la recuperación estimada con base en compromisos confirmados.",
                    "C": "Copia las cifras del mes anterior sin actualizar ningún dato contable para terminar rápido.",
                    "D": "Se niega a elaborar informes estadísticos argumentando que su labor es solo revisar transferencias."
                }
            },
            23: {
                "enunciado": "Al recibir cheques de cobranza de manos de un asesor de ventas, nota que uno de los cheques no tiene la firma del titular o presenta tachaduras visibles:",
                "opciones": {
                    "A": "Recibe el cheque con tachaduras y lo manda al banco a ver si el cajero no se da cuenta del defecto.",
                    "B": "Modifica la firma o el monto del cheque con un bolígrafo para intentar corregir el error.",
                    "C": "Rechaza la recepción del instrumento no conforme, asienta la no recepción en la minuta y solicita al asesor gestionar el reemplazo inmediato con el cliente.",
                    "D": "Bota el cheque defectuoso a la basura sin avisar al asesor de ventas ni a la Gerencia."
                }
            },
            24: {
                "enunciado": "Sobre el autocontrol y manejo de la frustración ante metas de cobranza no alcanzadas:",
                "opciones": {
                    "A": "Si la cobranza del mes no llega a la meta, culpo a los vendedores y me niego a hablarles durante semanas.",
                    "B": "He tenido jornadas difíciles con cobros estancados, pero analizo la causa raíz, reoriento la estrategia de contacto y persisto con disciplina.",
                    "C": "Poseo una serenidad sobrehumana inalterable; ningún obstáculo económico o laboral me ha generado la menor preocupación jamás.",
                    "D": "Cuando la cobranza va mal, dejo de hacer llamadas y me dedico a navegar en redes sociales."
                }
            },
            25: {
                "enunciado": "Un cliente solicita que le asignen un límite de crédito mayor al autorizado por manual para realizar una compra de gran volumen:",
                "opciones": {
                    "A": "Le aumenta el límite de crédito en el sistema administrativo de forma unilateral sin solicitar ningún aval.",
                    "B": "Le niega la solicitud de manera grosera diciéndole que en esa empresa no se confía en nadie.",
                    "C": "Le dice al cliente que compre con el código de otro comerciante para burlar el límite del sistema.",
                    "D": "Solicita recaudos financieros actualizados, revisa su historial de pago y remite el expediente con recomendación técnica a la Gerencia Administrativa para su evaluación formal."
                }
            },
            26: {
                "enunciado": "Durante el cuadre diario de cobranzas, la analista detecta que un cliente realizó un pago por transferencia pero colocó un número de referencia equivocado en el reporte:",
                "opciones": {
                    "A": "Da por perdido el dinero y le vuelve a cobrar la totalidad de la deuda al cliente con intereses.",
                    "B": "Valida con el departamento de contabilidad y el banco el extracto detallado, coteja hora, cuenta de origen y monto exacto, y aplica la cobranza con la referencia corregida.",
                    "C": "Borra la factura del sistema para que no aparezca pendiente de cobro.",
                    "D": "Le cobra una multa en efectivo al cliente por equivocarse de número de referencia."
                }
            },
            27: {
                "enunciado": "Al cierre de la jornada a las 6:00 p.m., el sistema bancario concluye la compensación nocturna y se requiere verificar los últimos créditos recibidos para liberar los camiones que salen a las 5:00 a.m.:",
                "opciones": {
                    "A": "Apaga el computador puntualmente a las 6:00 p.m. y se marcha sin verificar, dejando la flota varada en el andén.",
                    "B": "Asume la extensión horaria con sentido de responsabilidad, revisa los últimos créditos ingresados, concilia los pedidos prioritarios y deja las órdenes liberadas.",
                    "C": "Aprueba todos los despachos a ciegas sin verificar los fondos en cuenta bancaria para irse a su hora.",
                    "D": "Se queja a gritos en el pasillo insultando a los clientes que pagan a última hora de la tarde."
                }
            },
            28: {
                "enunciado": "Se detecta que un asesor de ventas retuvo durante 48 horas el dinero en efectivo cobrado a un cliente antes de reportarlo a la empresa:",
                "opciones": {
                    "A": "Levanta el reporte formal de la irregularidad con los soportes de fecha de recibo vs. ingreso real, y lo eleva a la Gerencia Administrativa y al Supervisor de Ventas.",
                    "B": "Se queda callada para no tener problemas personales con el asesor de ventas.",
                    "C": "Le pide al asesor una parte del dinero en efectivo para no delatarlo ante la Gerencia General.",
                    "D": "Modifica la fecha del recibo en el sistema para que parezca que el vendedor entregó el dinero a tiempo."
                }
            },
            29: {
                "enunciado": "En su relación con otros compañeros de trabajo y reconocimientos departamentales:",
                "opciones": {
                    "A": "Nunca en toda mi vida he sentido la mínima envidia, molestia o recelo por los incentivos o reconocimientos que reciben otros compañeros.",
                    "B": "En ocasiones he sentido sana emulación ante los buenos resultados de otros, pero me concentro en optimizar mis índices de recuperación de cartera.",
                    "C": "Pienso que cuando felicitan a un vendedor o analista es solo porque tiene una relación de amistad con los jefes.",
                    "D": "No me gusta relacionarme con los compañeros de administración porque en las oficinas todos son hipócritas."
                }
            },
            30: {
                "enunciado": "Presidencia le encomienda realizar una auditoría confidencial sobre la cartera incobrable histórica para depuración legal de saldos:",
                "opciones": {
                    "A": "Comenta los hallazgos de la auditoría con los choferes y vendedores durante el receso del mediodía.",
                    "B": "Se niega a realizar la auditoría argumentando que no le pagan para revisar deudas de años anteriores.",
                    "C": "Ejecuta la auditoría con absoluto sigilo profesional: clasifica la cartera por causal de incobrabilidad, audita soportes físicos y entrega el informe reservado a Presidencia.",
                    "D": "Altera los expedientes para encubrir a clientes conocidos y que sus deudas sean perdonadas sin justificación."
                }
            }
        }
    },

    # =========================================================================
    # 05. ANALISTA DE COMPRAS (CJS-COM)
    # =========================================================================
    "05_ANALISTA_DE_COMPRAS": {
        "codigo": "CJS-COM",
        "titulo": "EVALUACIÓN PSICOTÉCNICA SITUACIONAL EN COMPRAS Y ABASTECIMIENTO",
        "instrucciones": "Lea con atención cada situación laboral y de negociación con proveedores. Marque con una equis [X] una sola opción (A, B, C o D) por pregunta. Responda con total honestidad sobre su estilo real de gestión de compras, control de costos y ética profesional. Dispone de un máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "Un proveedor habitual le envía una sugerencia de pedido para reposición mensual, pero al cruzar con el inventario físico y la rotación real nota que está sugiriendo un 40% más de mercancía lenta:",
                "opciones": {
                    "A": "Aprueba la orden sugerida a ciegas para mantener contento al representante de la marca.",
                    "B": "Cancela la relación comercial con el proveedor de forma inmediata sin consultar a la gerencia.",
                    "C": "Borra el producto del sistema para que no se pueda volver a pedir en la empresa.",
                    "D": "Ajusta las cantidades según el historial de venta y stock mínimo, sustenta la orden con datos de rotación y envía la orden de compra corregida."
                }
            },
            2: {
                "enunciado": "Al ingresar al sistema administrativo una factura de despacho de un proveedor clave, nota que aplicaron un incremento de precio del 8% que no fue notificado ni autorizado previamente:",
                "opciones": {
                    "A": "Modifica los precios de venta al público en el sistema de inmediato asumiendo el aumento sin avisar a nadie.",
                    "B": "Retiene el ingreso contable de la factura, contacta al proveedor para exigir la nota de crédito o la lista de precios oficial y notifica a la Gerencia Administrativa.",
                    "C": "Procesa la factura con sobreprecio para no atrasar la descarga de la mercancía en el almacén.",
                    "D": "Oculta la factura debajo de su escritorio para evitar confrontaciones con la gerencia."
                }
            },
            3: {
                "enunciado": "El departamento de almacén reporta que un lote de 20 cajas de producto de alta rotación llegó con empaques rotos y fecha de vencimiento próxima (menor a 60 días):",
                "opciones": {
                    "A": "Tramita de inmediato la nota de devolución/avería, retiene el pago equivalente y exige al proveedor la reposición inmediata de producto apto.",
                    "B": "Le ordena al almacén que reciba la mercancía dañada y la guarde al fondo del depósito.",
                    "C": "Le dice al jefe de almacén que busque vender ese producto averiado a mitad de precio sin factura.",
                    "D": "Rompe la guía de recepción del transporte para fingir que el camión nunca llegó a las instalaciones."
                }
            },
            4: {
                "enunciado": "En su trayectoria profesional y gestión administrativa bajo presión:",
                "opciones": {
                    "A": "Si un proveedor tarda en responder una cotización, le envío correos insultantes de inmediato.",
                    "B": "En ocasiones he sentido tensión ante quiebres de inventario o alzas de precios imprevistas, pero mantengo la calma y busco alternativas de suministro.",
                    "C": "Jamás en mi trayectoria laboral he sentido preocupación, cansancio o frustración ante un retraso logístico.",
                    "D": "Prefiero no registrar las órdenes de compra en el sistema para que nadie controle mis pedidos."
                }
            },
            5: {
                "enunciado": "A primera hora de la mañana debe remitir a la Gerencia Administrativa el reporte diario de cuentas por pagar para programación de pagos, pero tiene tres facturas pendientes por conciliar retenciones:",
                "opciones": {
                    "A": "Omite las tres facturas del reporte sin avisar para entregar el documento a tiempo.",
                    "B": "Pospone la entrega del reporte de cuentas por pagar hasta el final de la tarde retrasando los pagos.",
                    "C": "Inventa los montos de las retenciones en el sistema para cuadrar el reporte rápidamente.",
                    "D": "Concilia de inmediato los montos con los comprobantes de retención, actualiza el estado de cuenta y entrega el informe consolidado a primera hora."
                }
            },
            6: {
                "enunciado": "Un representante de ventas de un proveedor nuevo le ofrece un obsequio costoso y una \"comisión personal en efectivo\" si prioriza sus productos sobre los demás proveedores:",
                "opciones": {
                    "A": "Acepta el obsequio y la comisión, comprometiéndose a comprarle exclusivamente a esa marca.",
                    "B": "Negocia que la comisión en efectivo sea mayor para asegurar la exclusividad en la distribuidora.",
                    "C": "Rechaza de forma tajante el soborno, defiende la política de compras éticas de la empresa y reporta el incidente a Presidencia.",
                    "D": "Recibe el dinero pero reparte una parte con los asistentes de compras para que guarden silencio."
                }
            },
            7: {
                "enunciado": "Al realizar el inventario semanal conjunto con almacén, se detecta un faltante injustificado de 15 bultos de un producto importado de alto valor:",
                "opciones": {
                    "A": "Modifica el inventario teórico en el sistema para que coincida con lo que hay y no generar alarmas.",
                    "B": "Levanta el reporte formal de discrepancia, audita las facturas de ingreso contra salidas y despachos, y notifica a Almacén y Administración.",
                    "C": "Culpa directamente al chofer del proveedor sin haber revisado las guías de recepción firmadas.",
                    "D": "Asume la pérdida como una merma normal de la empresa sin realizar ninguna investigación."
                }
            },
            8: {
                "enunciado": "La empresa requiere reponer con urgencia una línea de productos críticos antes del fin de semana, pero el proveedor principal habitual tiene su línea de crédito suspendida por una factura vencida:",
                "opciones": {
                    "A": "Concilia con la Gerencia Administrativa el soporte de pago de la factura vencida, envía el comprobante al proveedor para liberar la cuenta y gestiona el despacho prioritario.",
                    "B": "Se desentiende del problema argumentando que las cuentas por pagar no son su responsabilidad.",
                    "C": "Espera a que termine el fin de semana a ver si el proveedor desbloquea la cuenta por su cuenta.",
                    "D": "Da de baja la línea de productos en el portafolio comercial sin consultar a la Gerencia de Ventas."
                }
            },
            9: {
                "enunciado": "Respecto a la precisión y rigurosidad en el ingreso de especificaciones de productos al sistema:",
                "opciones": {
                    "A": "Jamás en ninguno de mis empleos anteriores he cometido una sola equivocación al ingresar un código, marca o gramaje.",
                    "B": "Considero que registrar marcas o gramajes exactos es una pérdida de tiempo innecesaria.",
                    "C": "Cuando he cometido una imprecisión involuntaria en la carga de una ficha técnica, la he rectificado y notificado de inmediato.",
                    "D": "Si el sistema arroja un error en la descripción de un producto, prefiero culpar al departamento de almacén."
                }
            },
            10: {
                "enunciado": "Un proveedor le solicita con insistencia el envío del comprobante de retención de IVA e ISLR de una factura cancelada la semana pasada, pero el área de tributos no lo ha emitido:",
                "opciones": {
                    "A": "Le cuelga el teléfono al proveedor y bloquea sus mensajes de correo electrónico.",
                    "B": "Fabrica un comprobante de retención manual en formato digital sin validez tributaria para calmarlo.",
                    "C": "Le dice al proveedor que la empresa no emite retenciones y que resuelva con el SENIAT.",
                    "D": "Realiza la gestión interna prioritaria con el área administrativa/tributaria, obtiene el soporte oficial y lo remite de inmediato al proveedor disculpando la demora."
                }
            },
            11: {
                "enunciado": "Al registrar el ingreso de un cargamento de detergente, nota que la factura dice \"Presentación 500 g\" pero el producto descargado físicamente en almacén es de \"400 g\":",
                "opciones": {
                    "A": "Registra la factura como 500 g en el sistema porque así viene impreso en el papel legal.",
                    "B": "Le ordena a almacén que reciba y mezcle las presentaciones en el mismo anaquel.",
                    "C": "Frena el ingreso en el sistema, levanta la no conformidad física vs. documento, contacta al proveedor para la rectificación de la factura y registra la presentación real.",
                    "D": "Modifica la factura del proveedor con corrector líquido para que coincida con el físico."
                }
            },
            12: {
                "enunciado": "Debe presentar el reporte mensual de compras consolidando volúmenes adquiridos, variaciones de precios y notas de crédito pendientes:",
                "opciones": {
                    "A": "Envía un correo breve con dos líneas diciendo que las compras se ejecutaron según lo previsto.",
                    "B": "Consolida la data del sistema, elabora el análisis estadístico de variaciones de costos y presenta el balance detallado de notas de crédito aplicadas.",
                    "C": "Copia el informe del mes pasado cambiando únicamente las fechas para salir rápido del paso.",
                    "D": "Se niega a elaborar reportes estadísticos afirmando que su labor es solo comprar y no hacer gráficos."
                }
            },
            13: {
                "enunciado": "Dos proveedores ofrecen la misma categoría de productos con calidades similares, pero uno ofrece un 3% de descuento comercial y el otro ofrece entrega en 24 horas garantizada:",
                "opciones": {
                    "A": "Evalúa el nivel de stock en almacén: si hay riesgo de quiebre prioriza el tiempo de entrega; si el stock es saludable, aprovecha el margen del 3% coordinando con Ventas.",
                    "B": "Selecciona al proveedor que le caiga mejor a nivel personal sin evaluar precios ni tiempos.",
                    "C": "Divide la orden de compra a ciegas sin analizar la capacidad de almacenamiento de la empresa.",
                    "D": "Rechaza a ambos proveedores y deja desabastecida la empresa durante todo el mes."
                }
            },
            14: {
                "enunciado": "En relación con las políticas de compras y directrices establecidas por Presidencia:",
                "opciones": {
                    "A": "He tenido puntos de vista distintos sobre márgenes comerciales con mis directores, pero siempre presenté comparativas sustentadas y respeté la directriz final.",
                    "B": "La Presidencia de una empresa no conoce la realidad de las negociaciones de calle con los proveedores.",
                    "C": "No tolero que me exijan cotizaciones comparativas porque mi criterio como comprador es incuestionable.",
                    "D": "En todas las empresas donde he laborado he tenido directores y jefes absolutamente infalibles con los que jamás tuve ninguna discrepancia."
                }
            },
            15: {
                "enunciado": "El departamento de almacén le entrega los formatos de devolución de productos no aptos y retorno de cartón de dos semanas acumuladas para su gestión comercial:",
                "opciones": {
                    "A": "Guarda los formatos en una gaveta y se olvida de ellos porque no representan producto nuevo.",
                    "B": "Bota los formatos a la basura argumentando que el cartón y las averías no tienen valor comercial.",
                    "C": "Procesa formalmente los reclamos ante los proveedores, coordina la recolección física y exige la emisión de las notas de crédito correspondientes.",
                    "D": "Le exige al jefe de almacén que venda el cartón por su cuenta de manera informal."
                }
            },
            16: {
                "enunciado": "Un proveedor estratégico le informa que dentro de 72 horas entrará en vigencia un incremento general de precios del 15% en toda su cartera de productos:",
                "opciones": {
                    "A": "Guarda silencio y espera a que el aumento se aplique para registrar los nuevos costos más caros.",
                    "B": "Le pide al proveedor que le venda mercancía a título personal para comercializarla por su cuenta.",
                    "C": "Se queja de forma grosera con el proveedor amenazando con sacarlo del mercado.",
                    "D": "Analiza la capacidad financiera y de almacenaje, proyecta la demanda y gestiona una compra anticipada con precio viejo previa autorización de Presidencia."
                }
            },
            17: {
                "enunciado": "Al cotejar las facturas ingresadas al sistema contra las órdenes de compra aprobadas, detecta que un proveedor incluyó un cargo por flete no pactado:",
                "opciones": {
                    "A": "Reclama el cobro no autorizado con base en la orden de compra aprobada, solicita la nota de crédito y procesa el pago solo por el monto pactado.",
                    "B": "Paga el flete no pactado sin consultar para evitar discusiones con el departamento de despacho.",
                    "C": "Cancela todo el inventario recibido y exige que el camión regrese a retirar los productos del almacén.",
                    "D": "Altera la orden de compra original en el sistema para que coincida con el sobreprecio del proveedor."
                }
            },
            18: {
                "enunciado": "Se requiere coordinar la recepción de tres gandolas de flota primaria que coinciden en horario de llegada el mismo día en la sede central:",
                "opciones": {
                    "A": "Se desentiende de la logística afirmando que la recepción física es problema exclusivo de almacén.",
                    "B": "Coordina previamente con el Jefe de Almacén un cronograma de descarga escalonado por andén, priorizando los rubros de mayor demanda.",
                    "C": "Hace esperar a los tres transportistas en la calle durante 48 horas sin darles información de turno.",
                    "D": "Autoriza que los tres camiones descarguen al mismo tiempo en el patio central bloqueando las salidas."
                }
            },
            19: {
                "enunciado": "Sobre la confidencialidad de las listas de costos, descuentos especiales y márgenes de los proveedores:",
                "opciones": {
                    "A": "Comparto las listas de precios y costos de un proveedor con sus competidores directos para presionarlos.",
                    "B": "Jamás en toda mi vida he sentido la mínima curiosidad ni he mirado información comercial ajena.",
                    "C": "Custodio la información de costos, convenios de pago y márgenes de la cartera con absoluta reserva y ética profesional.",
                    "D": "Si un conocido me pide las condiciones de compra de la empresa, se las facilito para ayudarle en su negocio."
                }
            },
            20: {
                "enunciado": "Al revisar el inventario en el software, nota que un producto de alta rotación está a solo dos días de llegar a quiebre de stock (stock cero):",
                "opciones": {
                    "A": "Espera a que el producto se agote por completo y que los vendedores reclamen para emitir el pedido.",
                    "B": "Modifica la existencia en el sistema para que parezca que todavía hay suficiente inventario disponible.",
                    "C": "Activa de inmediato la orden de reposición prioritaria, contacta al proveedor para acordar despacho express y notifica a Ventas.",
                    "D": "Le dice a los vendedores que el producto fue descontinuado definitivamente por la empresa."
                }
            },
            21: {
                "enunciado": "Al momento de actualizar la lista de precios por aumento de un proveedor, el sistema presenta una lentitud extrema que impide guardar los cambios:",
                "opciones": {
                    "A": "Apaga el computador y se retira de la oficina dejando los precios desactualizados durante la venta del día.",
                    "B": "Envía la lista manuscrita con errores a los vendedores para que ellos calculen los precios a mano.",
                    "C": "Borra la base de datos de precios para forzar a Sistemas a reiniciar el servidor completo.",
                    "D": "Reporta la falla técnica a Sistemas con carácter prioritario, mantiene el control manual documentado y completa la actualización en cuanto se normalice la plataforma."
                }
            },
            22: {
                "enunciado": "Un proveedor le entrega un lote de productos donde el empaque secundario viene golpeado, pero el producto interno está en condiciones óptimas:",
                "opciones": {
                    "A": "Acepta la mercancía sin dejar constancia formal asumiendo el riesgo de que el cliente final lo rechace.",
                    "B": "Recibe la mercancía dejando constancia firmada en la nota de recepción, solicita al proveedor material de reempaque y notifica a Almacén.",
                    "C": "Rechaza la mercancía de forma agresiva e insulta al transportista en la plataforma de descarga.",
                    "D": "Oculta las cajas golpeadas en el almacén para que nadie se dé cuenta del estado de los empaques."
                }
            },
            23: {
                "enunciado": "Se debe generar la reposición de una línea de productos de consumo masivo con estacionalidad de alta demanda (ej. temporada escolar o navideña):",
                "opciones": {
                    "A": "Analiza el histórico de ventas de temporadas anteriores, valida los tiempos de entrega del proveedor y planifica la compra escalonada para asegurar stock sin saturar espacio.",
                    "B": "Compra una cantidad mínima idéntica a la de un mes normal ignorando el pico de ventas de la temporada.",
                    "C": "Pide cinco veces más de la capacidad de almacenamiento de la empresa sin consultar espacio con Almacén.",
                    "D": "Le traslada toda la responsabilidad del cálculo de compra a los asesores de venta de la calle."
                }
            },
            24: {
                "enunciado": "Sobre el control emocional y la tolerancia a la frustración ante fallas de proveedores:",
                "opciones": {
                    "A": "Si un proveedor incumple una fecha de entrega, le grito e insulto por teléfono para obligarlo a despachar.",
                    "B": "He experimentado molestia justificada ante despachos impuntuales, pero canalizo el reclamo con firmeza institucional y apego al contrato.",
                    "C": "Poseo una serenidad perfecta; jamás nada ni nadie en el ámbito laboral me ha causado la menor incomodidad o enfado.",
                    "D": "Cuando un proveedor me queda mal, cancelo todos los pagos de la empresa de forma unilateral como venganza."
                }
            },
            25: {
                "enunciado": "El Jefe de Almacén le informa que hay una diferencia de 5 bultos de más en un camión respecto a lo facturado por el proveedor:",
                "opciones": {
                    "A": "Le dice al jefe de almacén que esconda los 5 bultos para repartirlos entre los colaboradores de la oficina.",
                    "B": "Le pide al chofer que se lleve los 5 bultos y los venda por fuera para dividir las ganancias.",
                    "C": "Se desentiende del sobrante argumentando que los errores de facturación del proveedor no le competen.",
                    "D": "Notifica formalmente al proveedor sobre el sobrante físico para su debida facturación o recolección documentada."
                }
            },
            26: {
                "enunciado": "La Gerencia Administrativa le solicita un informe sobre la cartera de cuentas por pagar a proveedores con vencimiento mayor a 30 días:",
                "opciones": {
                    "A": "Oculta las facturas vencidas en el reporte para que la gestión financiera de compras parezca impecable.",
                    "B": "Emite el reporte detallado por antigüedad de saldos, concilia notas de crédito pendientes de cruzar y sugiere prioridades de pago según criticidad de abastecimiento.",
                    "C": "Envía una hoja en blanco diciendo que la empresa no le debe nada a ningún proveedor.",
                    "D": "Le traslada la responsabilidad de hacer el informe a los propios proveedores de la empresa."
                }
            },
            27: {
                "enunciado": "Al momento de generar una orden de compra, el proveedor le informa que descontinuó el producto principal pero ofrece un sustituto con diferente gramaje y mayor precio:",
                "opciones": {
                    "A": "Monta la orden de compra por el sustituto a ciegas sin validar margen ni consultar a Ventas ni Presidencia.",
                    "B": "Evalúa la ficha técnica, realiza el costeo y análisis de margen, consulta con la Gerencia Comercial la viabilidad de mercado y solicita autorización previa antes de emitir la orden.",
                    "C": "Deja de comprar esa categoría de productos y se niega a buscar soluciones de sustitución.",
                    "D": "Emite la orden por el producto descontinuado esperando que el sistema del proveedor resuelva solo."
                }
            },
            28: {
                "enunciado": "Se requiere coordinar con el departamento de ventas la colocación de un lote de mercancía que llegó con fecha de caducidad a 90 días:",
                "opciones": {
                    "A": "Coordina con la Gerencia de Ventas y Administración una estrategia comercial agresiva (oferta/combo/descuento por pronto pago) para garantizar la rotación inmediata del lote.",
                    "B": "Deja la mercancía en el almacén sin avisar a ventas hasta que el producto termine de vencerse.",
                    "C": "Modifica la fecha de caducidad en el empaque con un sello falso para engañar a los clientes.",
                    "D": "Culpa al personal de compras anterior y se niega a involucrarse en la rotación del inventario."
                }
            },
            29: {
                "enunciado": "En relación con las promociones, incentivos y reconocimientos profesionales:",
                "opciones": {
                    "A": "Nunca en toda mi vida he sentido la mínima envidia, recelo o inconformidad por los logros o ascensos de mis compañeros.",
                    "B": "A veces he sentido sana aspiración profesional ante los logros ajenos, pero me enfoco en optimizar mis procesos de negociación y compras.",
                    "C": "Pienso que cuando felicitan a un analista en la empresa es únicamente por favoritismo personal de los jefes.",
                    "D": "No me interesa colaborar con ninguna otra área porque en el departamento administrativo todos son rivales."
                }
            },
            30: {
                "enunciado": "Presidencia le encomienda liderar la negociación de un acuerdo de exclusividad y volumen con una marca líder del mercado:",
                "opciones": {
                    "A": "Firma el contrato a espaldas de la Gerencia sin revisar las cláusulas legales ni los compromisos de compra.",
                    "B": "Se niega a negociar argumentando que los acuerdos de volumen son muy arriesgados para la distribuidora.",
                    "C": "Prepara la mesa técnica: cruza histórico de rotación, analiza capacidad de almacenaje y flujo de pago, negocia mejores condiciones de crédito y presenta la propuesta estructurada a Presidencia.",
                    "D": "Delega la negociación en un pasante sin hacerle seguimiento ni revisar las condiciones financieras."
                }
            }
        }
    },

    # =========================================================================
    # 06. ANALISTA DE CONCILIACIÓN (CJS-CNC)
    # =========================================================================
    "06_ANALISTA_DE_CONCILIACION": {
        "codigo": "CJS-CNC",
        "titulo": "EVALUACIÓN PSICOTÉCNICA SITUACIONAL EN CONCILIACIÓN BANCARIA Y AUDITORÍA",
        "instrucciones": "Lea con detenimiento cada situación contable y bancaria. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con total honestidad sobre su rigor numérico, disciplina de auditoría de váuchers y apego a normas financieras. Dispone de un tiempo máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "Al revisar el estado de cuenta de una de las cuentas corrientes principales, detecta un débito bancario por $450 bajo el concepto de 'Comisión Especial' que no cuenta con soporte ni notificación previa:",
                "opciones": {
                    "A": "Asienta el monto como un gasto misceláneo menor en el libro contable para no retrasar el cuadre.",
                    "B": "Ignora el débito asumiendo que el banco lo reversará de forma automática el próximo mes.",
                    "C": "Le traslada la culpa a la analista de pagos acusándola de haber cometido un error de transferencia.",
                    "D": "Identifica la cuenta y referencia exacta, levanta el reclamo formal con el ejecutivo bancario, asienta la partida en conciliación como débito no reconocido y notifica a la Gerencia."
                }
            },
            2: {
                "enunciado": "Al conciliar un traspaso de fondos entre dos empresas del mismo grupo económico, nota que la empresa emisora registró la salida por $5.000 pero la receptora no tiene el crédito reflejado:",
                "opciones": {
                    "A": "Registra el ingreso ficticio en la empresa receptora para que ambos libros contables coincidan.",
                    "B": "Solicita el váucher original de la transferencia, verifica si la operación quedó retenida en cámara de compensación y coordina con tesorería el estatus real antes de asentar.",
                    "C": "Da de baja los $5.000 en la empresa emisora considerándolo una pérdida irrecuperable.",
                    "D": "Espera a que termine el año fiscal para revisar si la transferencia aparece en los balances anuales."
                }
            },
            3: {
                "enunciado": "Al cotejar los soportes físicos (váuchers de depósito) contra los ingresos registrados en el sistema por cobranzas, detecta que un váucher fue ingresado dos veces en fechas distintas:",
                "opciones": {
                    "A": "Anula de inmediato el asiento contable duplicado, corrige el saldo real de la cuenta y emite el reporte de inconsistencia a la analista de cobranzas y auditoría interna.",
                    "B": "Deja el asiento duplicado en el sistema porque genera un saldo a favor en los libros de la empresa.",
                    "C": "Rompe el váucher físico original para que no queden rastros de la duplicidad detectada.",
                    "D": "Le cobra una penalización en efectivo por cuenta propia a la persona que cargó el comprobante."
                }
            },
            4: {
                "enunciado": "En su experiencia laboral y manejo de operaciones numéricas bajo presión:",
                "opciones": {
                    "A": "Si una cuenta bancaria no me cuadra a la primera revisión, borro los asientos que estorben.",
                    "B": "En ocasiones he sentido cansancio visual ante largas listas de transacciones bancarias, pero verifico línea por línea hasta encontrar la diferencia.",
                    "C": "Jamás en toda mi vida laboral he cometido un error de digitación ni he dejado de cuadrar una cuenta al primer intento.",
                    "D": "Prefiero no conciliar las comisiones bancarias pequeñas porque quitan demasiado tiempo."
                }
            },
            5: {
                "enunciado": "En el cierre mensual de conciliación bancaria, un cheque emitido a un proveedor hace más de 120 días continúa apareciendo como 'girado y no cobrado' en el libro mayor:",
                "opciones": {
                    "A": "Borra el cheque del sistema contable sin verificar si el proveedor todavía posee el documento.",
                    "B": "Emite un nuevo cheque al proveedor sin anular el anterior ni solicitar la orden de pago.",
                    "C": "Asume que el proveedor regaló el servicio y registra el monto como una ganancia neta.",
                    "D": "Contacta al área de Cuentas por Pagar para verificar con el proveedor el estatus del cheque, solicita orden de caducidad/anulación y realiza el reverso contable correspondiente."
                }
            },
            6: {
                "enunciado": "Al recibir el reporte de pagos a proveedores extranjeros, observa que la tasa de cambio aplicada en la transferencia bancaria difiere de la tasa registrada en el comprobante contable:",
                "opciones": {
                    "A": "Modifica la tasa bancaria oficial a mano para que coincida con lo registrado en el software.",
                    "B": "Deja la diferencia abierta indefinidamente sin generar el diferencial cambiario en libros.",
                    "C": "Calcula el diferencial cambiario (ganancia o pérdida en cambio), realiza el asiento de ajuste respectivo y soporta la operación con el comprobante bancario internacional.",
                    "D": "Cancela el pago al proveedor extranjero de forma unilateral sin consultar a la Gerencia."
                }
            },
            7: {
                "enunciado": "Durante la conciliación diaria de nómina, constata que dos transferencias de sueldos fueron devueltas por el banco por datos de cuenta erróneos del trabajador:",
                "opciones": {
                    "A": "Notifica de inmediato al departamento de Nómina y Recursos Humanos con el reporte de rechazo, concilia la devolución en cuenta y mantiene la partida identificada para su reemisión.",
                    "B": "Oculta las transferencias devueltas esperando que los trabajadores reclamen su sueldo a fin de mes.",
                    "C": "Retira el dinero devuelto en efectivo de la cuenta bancaria para pagarle a los empleados a mano alzada.",
                    "D": "Registra la nómina como pagada al 100% ignorando los reintegros bancarios en el estado de cuenta."
                }
            },
            8: {
                "enunciado": "Son las 5:40 p.m. (su hora de salida es a las 6:00 p.m.) y la Gerencia Administrativa le solicita con urgencia el informe de cierre de conciliaciones de todas las cuentas bancarias para una junta directiva:",
                "opciones": {
                    "A": "Consolida los balances conciliados de cada cuenta, detalla las partidas en tránsito pendientes con su debida justificación y entrega el reporte ejecutivo a tiempo.",
                    "B": "Apaga el computador inmediatamente a las 6:00 p.m. diciendo que no le dio tiempo de terminar.",
                    "C": "Copia el informe del mes pasado cambiando solo la fecha para poder marcharse a su casa puntual.",
                    "D": "Envía una hoja en blanco con una nota diciendo que el banco no ha emitido los estados de cuenta."
                }
            },
            9: {
                "enunciado": "Respecto a la infalibilidad y exactitud en el cuadre de libros y balances:",
                "opciones": {
                    "A": "Jamás en ninguno de mis trabajos anteriores he tenido una diferencia de un solo centavo entre el libro mayor y el banco.",
                    "B": "Considero que las conciliaciones bancarias son trámites secundarios que no aportan valor a la empresa.",
                    "C": "Cuando he enfrentado una discrepancia en una cuenta corriente, he aplicado el método de auditoría cruzada hasta aclarar la partida.",
                    "D": "Si el saldo de una cuenta bancaria no coincide con el sistema, prefiero culpar al software administrativo."
                }
            },
            10: {
                "enunciado": "Al auditar los reintegros bancarios por cheques devueltos de clientes, nota que se debitaron comisiones por cheque devuelto que no han sido cargadas al cliente correspondiente:",
                "opciones": {
                    "A": "Asume las comisiones como gasto operativo de la empresa sin notificar a Cuentas por Cobrar.",
                    "B": "Borra el débito bancario del estado de cuenta digital para no tener que registrar la pérdida.",
                    "C": "Insulta al cajero del banco por teléfono acusándolo de cobrar tarifas abusivas.",
                    "D": "Registra la nota de débito bancaria en libros y emite el soporte a Cuentas por Cobrar para que el gasto sea trasladado y cobrado al cliente emisor del cheque devuelto."
                }
            },
            11: {
                "enunciado": "El software administrativo presenta una inconsistencia técnica y no permite conciliar de forma automática las operaciones de un banco secundario:",
                "opciones": {
                    "A": "Deja de conciliar las operaciones de ese banco durante meses hasta que actualicen el sistema.",
                    "B": "Se niega a trabajar argumentando que sin conciliación automática no se puede hacer nada.",
                    "C": "Ejecuta la conciliación manual mediante hojas de trabajo estructuradas, cruza voucher por váucher y reporta la falla a Sistemas para su pronta resolución.",
                    "D": "Inventa saldos ficticios en los libros para simular que la conciliación automática funcionó."
                }
            },
            12: {
                "enunciado": "Un directivo de la empresa le pide que no registre en la conciliación bancaria un retiro en efectivo de monto considerable realizado desde la cuenta corriente corporativa:",
                "opciones": {
                    "A": "Acepta no registrar el retiro y oculta la transacción contable para agradar al directivo.",
                    "B": "Explica con respeto y firmeza que todo movimiento bancario debe reflejarse en libros, asienta la partida como retiro pendiente por justificar y rinde cuentas formales a Presidencia.",
                    "C": "Modifica el estado de cuenta en formato digital eliminando la línea del retiro con un editor de texto.",
                    "D": "Le cobra una comisión personal en efectivo al directivo por encubrir el movimiento no justificado."
                }
            },
            13: {
                "enunciado": "Durante el análisis diario, encuentra un crédito bancario de $1.200 no identificado en el estado de cuenta que no coincide con ninguna factura ni cobranza reportada:",
                "opciones": {
                    "A": "Registra la partida en 'Depósitos no identificados en tránsito', notifica a Cobranzas y Ventas con fecha y referencia para su rastreo y evita aplicarlo a ciegas.",
                    "B": "Asigna el dinero a la cuenta del cliente que le caiga mejor para liquidarle sus deudas vencidas.",
                    "C": "Transfiere los $1.200 a su cuenta bancaria personal argumentando que si nadie lo reclama es suyo.",
                    "D": "Anula el movimiento bancario en el sistema para que la cuenta corriente cuadre en cero."
                }
            },
            14: {
                "enunciado": "En relación con las jefaturas y las directrices de cierre contable en sus empleos previos:",
                "opciones": {
                    "A": "He tenido divergencias de criterio técnico con auditores sobre la reclasificación de partidas, resolviéndolas con apego a las normas contables y respeto jerárquico.",
                    "B": "Los gerentes de contabilidad nunca entienden la dificultad real de conciliar cuentas con bancos lentos.",
                    "C": "No tolero que supervisen mis papeles de trabajo porque mi método contable es infalible.",
                    "D": "En todas las empresas donde he laborado he tenido jefes de contabilidad y finanzas absolutamente perfectos y libres de errores."
                }
            },
            15: {
                "enunciado": "Al verificar los váuchers de pago de proveedores extranjeros, detecta que falta la confirmación bancaria (SWIFT) de una transferencia de alto monto:",
                "opciones": {
                    "A": "Da por conciliada la operación asumiendo que el banco extranjero nunca pierde una transferencia.",
                    "B": "Borra la cuenta por pagar del sistema para aparentar que el proveedor ya cobró su dinero.",
                    "C": "Mantiene la partida en tránsito, solicita formalmente el mensaje SWIFT al banco intermediario y no cierra la conciliación de esa cuenta hasta tener el soporte legal.",
                    "D": "Le dice al proveedor extranjero que busque su dinero por su propia cuenta en el banco internacional."
                }
            },
            16: {
                "enunciado": "Al revisar las cuentas corrientes a primera hora, detecta que la cuenta presenta saldo negativo (sobregiro bancario no autorizado) debido al cobro de cheques imprevistos:",
                "opciones": {
                    "A": "Oculta el sobregiro a la Gerencia esperando que ingresen cobranzas durante el día para compensar.",
                    "B": "Se altera emocionalmente y le grita al mensajero por haber entregado los cheques al banco.",
                    "C": "Desconecta los teléfonos de la oficina para no tener que atender las llamadas del banco.",
                    "D": "Alerta de inmediato a la Gerencia Administrativa y Tesorería sobre el sobregiro, cuantifica los intereses asociados y coordina traspaso de fondos urgente para restituir la liquidez."
                }
            },
            17: {
                "enunciado": "Al conciliar los gastos bancarios mensuales, nota que el banco está cobrando un mantenimiento de cuenta un 20% más alto que la tarifa acordada contractualmente:",
                "opciones": {
                    "A": "Cuantifica el cobro indebido acumulado, prepara el informe comparativo con el contrato corporativo y tramita el reclamo de reintegro ante el banco.",
                    "B": "Asume el incremento como una tarifa normal sin verificar las cláusulas del contrato bancario.",
                    "C": "Cierra la cuenta corriente bancaria de forma unilateral sin la autorización de la Junta Directiva.",
                    "D": "Modifica las comisiones en el sistema contable para tapar la discrepancia tarifaria del banco."
                }
            },
            18: {
                "enunciado": "Se produce un retraso de tres días en la recepción física de los váuchers de depósito de una agencia foránea:",
                "opciones": {
                    "A": "Paraliza el trabajo completo de conciliación de todas las cuentas de la empresa por falta de esos váuchers.",
                    "B": "Solicita el envío digital inmediato de los soportes escaneados, realiza la conciliación preliminar y coteja los originales al momento de su recepción física.",
                    "C": "Aprueba las cuentas a ciegas sin revisar ningún comprobante físico ni digital.",
                    "D": "Acusa a los colaboradores de la agencia foránea de sustracción de dinero sin tener pruebas."
                }
            },
            19: {
                "enunciado": "Sobre la confidencialidad de los saldos bancarios y movimientos financieros corporativos:",
                "opciones": {
                    "A": "Comento los saldos de las cuentas bancarias de la empresa con amigos o conocidos en lugares públicos.",
                    "B": "Jamás en toda mi vida he sentido la mínima curiosidad por mirar el saldo de una cuenta ajena.",
                    "C": "Custodio la información de estados bancarios, transferencias y firmas autorizadas con estricta reserva profesional y claves de acceso protegidas.",
                    "D": "Si un proveedor me pregunta cuánto dinero hay en la cuenta de la empresa, se lo revelo sin dudar."
                }
            },
            20: {
                "enunciado": "Al auditar la conciliación bancaria de una empresa filial, observa que arrastra una partida conciliatoria de $800 desde hace más de 6 meses sin aclarar:",
                "opciones": {
                    "A": "Ajusta la diferencia contra capital contable sin hacer ninguna indagación histórica.",
                    "B": "Borra la cuenta bancaria del sistema para deshacerse de la partida vieja que incomoda el balance.",
                    "C": "Reconstruye el historial de movimientos de hace 6 meses, localiza el voucher o cheque no cobrado de origen y ejecuta el saneamiento formal documentado.",
                    "D": "Le cobra los $800 a los analistas nuevos que ingresaron recientemente al departamento."
                }
            },
            21: {
                "enunciado": "El sistema contable presenta lentitud y se requiere entregar el reporte de conciliación de divisas antes de las 12:00 m.:",
                "opciones": {
                    "A": "Apaga el equipo y se va a almorzar antes de hora argumentando que con sistemas lentos no trabaja.",
                    "B": "Envía el reporte del mes pasado para cumplir con la hora de entrega sin importar las cifras.",
                    "C": "Se queja a gritos en el pasillo insultando al personal técnico del departamento de Sistemas.",
                    "D": "Exporta los auxiliares a una hoja de cálculo local estructurada, efectúa el cruce analítico de divisas y entrega el informe conciliado a tiempo a la Gerencia."
                }
            },
            22: {
                "enunciado": "Durante la revisión de cheques cobrados por el banco, nota que un cheque fue pagado por un monto mayor al emitido originalmente en la orden de pago (posible alteración de cheque):",
                "opciones": {
                    "A": "Registra el gasto inflado en libros sin investigar para que la cuenta corriente cuadre rápido.",
                    "B": "Solicita de inmediato la imagen del cheque cobrado al banco, coteja con la copia de la orden de pago original, confirma la alteración y activa la denuncia bancaria y legal con la Gerencia.",
                    "C": "Culpa a la analista de cuentas por pagar antes de revisar la firma y el monto del documento físico.",
                    "D": "Oculta el cheque alterado en su gaveta para evitar involucrarse en investigaciones policiales."
                }
            },
            23: {
                "enunciado": "Al conciliar los traspasos de fondos entre cuentas propias, nota que una transferencia figura debitada de la cuenta origen, pero no fue acreditada en la cuenta destino tras 48 horas:",
                "opciones": {
                    "A": "Gestiona el reclamo formal con el banco con el número de referencia del débito, mantiene ambas partidas identificadas en conciliación y hace seguimiento diario hasta su acreditación.",
                    "B": "Da por perdido el dinero de la transferencia y registra una pérdida contable en el ejercicio.",
                    "C": "Asume que la cuenta destino se equivocó de titular y no realiza ninguna acción administrativa.",
                    "D": "Insulta al cajero del banco receptor y paraliza todas las transferencias bancarias de la compañía."
                }
            },
            24: {
                "enunciado": "Sobre el control emocional y la tolerancia a la frustración ante descuadres contables complejos:",
                "opciones": {
                    "A": "Si una cuenta bancaria no me cuadra tras media hora de trabajo, golpeo el escritorio y me niego a seguir revisando.",
                    "B": "He experimentado momentos de cansancio ante diferencias esquivas de pocos centavos, pero aplico método, paciencia y rigor hasta cuadrar el balance.",
                    "C": "Poseo una serenidad sobrehumana inalterable; ningún descuadre numérico o presión de auditoría me ha causado la menor incomodidad jamás.",
                    "D": "Cuando me saturo de números, cierro los libros con diferencias abiertas y me dedico a jugar en el teléfono."
                }
            },
            25: {
                "enunciado": "Un analista de pagos le solicita que le 'acomode' una conciliación bancaria para tapar un error involuntario de transferencia a una cuenta equivocada:",
                "opciones": {
                    "A": "Acepta alterar la conciliación contable para proteger a su compañero de una llamada de atención.",
                    "B": "Le pide dinero a su compañero a cambio de arreglar el balance en los libros contables.",
                    "C": "Le dice a su compañero que no diga nada y que borre el comprobante bancario del sistema.",
                    "D": "Niega rotundamente la solicitud, explica la obligatoriedad de la transparencia contable y lo orienta a registrar el error formalmente y tramitar el reverso con el banco."
                }
            },
            26: {
                "enunciado": "Al auditar las notas de crédito bancarias por intereses ganados en cuentas de inversión, observa que no han sido registradas en los libros contables durante los últimos tres meses:",
                "opciones": {
                    "A": "Deja los intereses fuera de los libros contables argumentando que son ganancias que no hacen falta registrar.",
                    "B": "Cuantifica los intereses acumulados de los tres meses, solicita los estados de cuenta respectivos, realiza los asientos de ingreso financiero y regulariza la conciliación.",
                    "C": "Borra las cuentas de inversión del sistema administrativo para no tener que calcular intereses.",
                    "D": "Transfiere los intereses bancarios a su cuenta personal como bonificación por haberlos descubierto."
                }
            },
            27: {
                "enunciado": "Al final de la jornada de cierre mensual, una cuenta bancaria secundaria presenta un descuadre menor de $15 entre el libro mayor y el estado bancario:",
                "opciones": {
                    "A": "Asienta un ajuste manual sin justificación bajo el concepto de 'Diferencia de Cuadre' para salir a las 6:00 p.m.",
                    "B": "Extiende su jornada de forma responsable, rastrea el origen de los $15 (comisión no registrada, retención o redondeo), concilia la partida exacta y deja el cierre saneado.",
                    "C": "Deja el balance con la diferencia abierta sin documentar y se retira sin avisar a la Gerencia.",
                    "D": "Se queja a gritos con sus compañeros afirmando que por $15 nadie debería quedarse trabajando."
                }
            },
            28: {
                "enunciado": "Debe elaborar el informe consolidado mensual de conciliaciones bancarias para la auditoría externa y la Junta Directiva:",
                "opciones": {
                    "A": "Estructura el informe consolidando todas las cuentas corrientes y de inversión, presenta el estado de partidas en tránsito por antigüedad, adjunta váuchers de soporte y formula recomendaciones de control interno.",
                    "B": "Envía capturas de pantalla borrosas del software contable sin análisis explicativo ni balance general.",
                    "C": "Copia el informe del año pasado cambiando únicamente los nombres de los bancos para salir del compromiso.",
                    "D": "Manifiesta que los informes de conciliación son innecesarios porque los bancos ya emiten sus propios estados de cuenta."
                }
            },
            29: {
                "enunciado": "En su relación con otros profesionales del área administrativa y reconocimientos laborales:",
                "opciones": {
                    "A": "Nunca en toda mi vida profesional he sentido la menor envidia, molestia ni celos por los ascensos o felicitaciones otorgadas a mis compañeros.",
                    "B": "A veces he sentido sana aspiración profesional ante los méritos ajenos, pero me concentro en pulir mi técnica de auditoría y análisis contable.",
                    "C": "Pienso que cuando felicitan a un contador o analista en la empresa es únicamente por favoritismo de los directores.",
                    "D": "No me interesa relacionarme con nadie del departamento porque en el área contable todos buscan sabotear el trabajo del otro."
                }
            },
            30: {
                "enunciado": "Presidencia le encomienda realizar una auditoría exhaustiva sobre las transacciones bancarias de una cuenta especial utilizada para pagos internacionales:",
                "opciones": {
                    "A": "Comenta los montos y movimientos de la cuenta especial con colaboradores de otras áreas durante el almuerzo.",
                    "B": "Se niega a realizar la auditoría argumentando que revisar pagos internacionales es muy engorroso.",
                    "C": "Ejecuta la auditoría con absoluto sigilo profesional: coteja transferencias vs. contratos y mensajes SWIFT, audita comisiones y comisiones intermediarias, y entrega el informe reservado a Presidencia.",
                    "D": "Modifica las cifras de la auditoría para encubrir pagos irregulares de personas conocidas."
                }
            }
        }
    },

    # =========================================================================
    # 08. ANALISTA DE LOGÍSTICA (CJS-LOG)
    # =========================================================================
    "08_ANALISTA_DE_LOGISTICA": {
        "codigo": "CJS-LOG",
        "titulo": "EVALUACIÓN PSICOTÉCNICA SITUACIONAL EN LOGÍSTICA, DESPACHO Y CONTROL SADA",
        "instrucciones": "Lea con atención cada situación logística y operativa. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con honestidad sobre su rigor en planes de carga, estricto apego a las guías SADA y control de facturas. Dispone de un tiempo máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "A primera hora de la mañana (7:45 a.m.), el supervisor de transporte exige dar salida a dos camiones de reparto porque los choferes tienen rutas largas, pero las guías SADA aún figuran en estatus 'En Trámite' en el portal:",
                "opciones": {
                    "A": "Autoriza la salida de los camiones entregando solo las facturas comerciales para no retrasar el itinerario.",
                    "B": "Le dice a los choferes que viajen sin papeles y que si los paran en alcabalas paguen una comisión informal.",
                    "C": "Imprime una captura de pantalla de la solicitud en trámite y le estampa un sello falso para que viajen.",
                    "D": "Frena de manera categórica la salida de las unidades, recordando que ninguna flota puede ni debe salir sin guía SADA y Plan de Carga aprobado, y prioriza la confirmación en el sistema."
                }
            },
            2: {
                "enunciado": "Al conciliar el inventario físico de rubros regulados en el almacén contra el inventario teórico registrado en el sistema SADA de la empresa, detecta una diferencia de 40 sacos de harina que no figuran en el portal:",
                "opciones": {
                    "A": "Ajusta el inventario físico escondiendo los 40 sacos en una zona ciega para no reportar la discrepancia.",
                    "B": "Levanta una auditoría inmediata, rastrea guías de recepción no confirmadas en la plataforma y concilia el inventario teórico vs. físico antes de emitir nuevos despachos para evitar sanciones de SUNAGRO.",
                    "C": "Emite guías ficticias a clientes al azar para rebajar los 40 sacos del sistema administrativo.",
                    "D": "Borra los registros de recepción del almacén para que el inventario físico cuadre con la web oficial."
                }
            },
            3: {
                "enunciado": "Un asesor comercial solicita procesar con urgencia una Nota de Crédito por mercancía devuelta por un cliente, pero la planilla carece de la firma del supervisor de almacén que certifique el reingreso físico del producto:",
                "opciones": {
                    "A": "Retiene la ejecución de la Nota de Crédito en el sistema, explicando que únicamente se procesan documentos con el soporte de motivo debidamente firmado por almacén y gerencia administrativa.",
                    "B": "Emite la Nota de Crédito de inmediato para colaborar con el asesor y que este cobre su comisión rápido.",
                    "C": "Falsifica la firma del supervisor de almacén en el formato de motivo para agilizar el proceso en el sistema.",
                    "D": "Anula la factura comercial original en el software sin generar ningún soporte contable ni de almacén."
                }
            },
            4: {
                "enunciado": "En su trayectoria profesional y desempeño bajo presión operativa:",
                "opciones": {
                    "A": "Si la plataforma de guías colapsa, me desquito gritando a los despachadores y choferes en el andén.",
                    "B": "En ocasiones he sentido fatiga o tensión al cuadrar simultáneamente planes de carga, guías y facturas, pero mantengo el orden documental y la calma.",
                    "C": "Jamás en toda mi vida laboral he sentido estrés, apuro ni he tenido la mínima duda al armar un plan de carga.",
                    "D": "Prefiero no conciliar las guías con las facturas porque en logística lo único importante es que los camiones rueden."
                }
            },
            5: {
                "enunciado": "Durante la verificación de un Plan de Carga para una gandola de 20 toneladas, nota que se incluyeron pedidos que exceden en 2.500 kg el peso máximo bruto vehicular permitido para esa unidad:",
                "opciones": {
                    "A": "Permite la salida de la gandola con sobrepeso asumiendo que los choferes saben cómo esquivar las balanzas.",
                    "B": "Altera los pesos unitarios en el sistema de guías colocándole menos kilogramos a cada bulto.",
                    "C": "Le dice al transportista que descargue el excedente en la carretera si nota presencia de fiscales viales.",
                    "D": "Detiene la carga, reestructura el Plan de Carga reasignando los 2.500 kg a otra unidad de ruta y concilia las facturas y guías SADA con el tonelaje reglamentario."
                }
            },
            6: {
                "enunciado": "Al momento de entregar las facturas confirmadas y libros de cobro a los asesores de ventas a primera hora, dos vendedores se niegan a firmar la relación de entrega de cuentas por cobrar:",
                "opciones": {
                    "A": "Les entrega los documentos sin firma para no generar discusiones en la oficina de logística.",
                    "B": "Rompe las facturas frente a los asesores para demostrarles autoridad en el departamento.",
                    "C": "Mantiene la custodia de las facturas confirmadas, niega su entrega física hasta tanto no firmen la relación formal por vendedor y notifica a la Coordinación de Logística y Ventas.",
                    "D": "Le cobra una multa en efectivo personal a cada asesor para entregarles las facturas sin firma."
                }
            },
            7: {
                "enunciado": "Un cliente reporta vía telefónica que recibió conforme su pedido de 500 bultos de arroz según la factura y guía SADA, pero en la plataforma oficial la guía aún permanece en estatus 'En Tránsito':",
                "opciones": {
                    "A": "Ingresa de inmediato al sistema SADA, verifica el acta de recepción digital del cliente, procede a pasar a tránsito y confirmar la recepción formal para cerrar el ciclo legal.",
                    "B": "Deja la guía en tránsito permanentemente sin confirmar, desentendiéndose del cierre en la plataforma.",
                    "C": "Anula la guía en el sistema SADA alegando que el cliente nunca recibió la mercancía.",
                    "D": "Le pide al cliente una transferencia bancaria a título personal para confirmarle la guía en la web."
                }
            },
            8: {
                "enunciado": "Son las 4:45 p.m. (su hora de salida es a las 5:00 p.m.) y retornan tres camiones de ruta que traen facturas desechadas (pedidos no entregados) que deben liquidarse para reingresar el stock y habilitar la carga nocturna:",
                "opciones": {
                    "A": "Asume la extensión horaria con compromiso, supervisa las facturas desechadas, liquida los documentos en el sistema y coordina con almacén el reintegro antes de retirarse.",
                    "B": "Apaga su computador a las 5:00 p.m. puntual dejando las facturas desechadas y la mercancía en el camión.",
                    "C": "Liquida las facturas como cobradas en efectivo a ciegas para marcharse rápido a su casa.",
                    "D": "Bota las facturas desechadas a la papelera argumentando que si no se vendieron no tienen valor."
                }
            },
            9: {
                "enunciado": "Respecto al rigor técnico y la exactitud en la emisión de documentos de movilización:",
                "opciones": {
                    "A": "Jamás en ninguno de mis empleos anteriores he cometido la más mínima imprecisión al cotejar un código SICA, dirección o número de factura.",
                    "B": "Considero que las normativas del sistema SADA son exageradas y no pasa nada si se incumplen de vez en cuando.",
                    "C": "Cuando he detectado una discrepancia entre una factura y su guía de movilización, he frenado el despacho hasta garantizar la concordancia total.",
                    "D": "Si una gandola es retenida en carretera por fallas en la guía, prefiero culpar a la gerencia de la empresa."
                }
            },
            10: {
                "enunciado": "Un asesor de ventas solicita que se le facture y emita guía SADA a un cliente nuevo, pero el código RIF presentado no coincide con los datos registrados en el portal SUNAGRO:",
                "opciones": {
                    "A": "Registra los datos incongruentes en el sistema para salir del paso y complacer al vendedor.",
                    "B": "Emite la guía utilizando los datos fiscales de la distribuidora para tapar el error del cliente.",
                    "C": "Le dice al vendedor que cobre a mano alzada en efectivo y despache el producto sin registro.",
                    "D": "Frena el registro en el sistema SADA, solicita al asesor el RIF y constancia SICA actualizada del cliente y procede a registrarlo con datos exactos verificados."
                }
            },
            11: {
                "enunciado": "Al revisar las órdenes de despacho del día, nota que Facturación procesó pedidos de un rubro que requiere obligatoriamente guía SADA, pero no generó la alerta para la emisión de la guía de movilización:",
                "opciones": {
                    "A": "Permite que el pedido se cargue en el camión sin guía confiando en que no habrá inspecciones en la ruta.",
                    "B": "Oculta las facturas debajo de su escritorio para evitar que el jefe de almacén le reclame.",
                    "C": "Interviene de inmediato, concilia la facturación, frena la salida del bulto y tramita la guía SADA requerida para ese rubro antes de armar el Plan de Carga definitivo.",
                    "D": "Modifica la factura en el sistema cambiándole el nombre al producto regulado por uno que no exija guía."
                }
            },
            12: {
                "enunciado": "Al momento de armar la ruta de reparto de una flota, el transportista le pide cambiar el orden de entrega establecido en el Plan de Carga para atender primero a un comercio amigo:",
                "opciones": {
                    "A": "Acepta el cambio verbal del transportista sin actualizar los documentos ni el itinerario de ruta.",
                    "B": "Evalúa la solicitud contra la geolocalización, tiempos de entrega y ventanas de recepción; si no afecta la eficiencia ni la normativa SADA, ajusta el Plan de Carga formalmente.",
                    "C": "Insulta al chofer de forma agresiva amenazándolo con quitarle el camión por hacer sugerencias.",
                    "D": "Le cobra $10 al chofer para autorizarle el cambio de itinerario por debajo de la mesa."
                }
            },
            13: {
                "enunciado": "Durante el arqueo semanal de facturas confirmadas y notas de crédito, detecta que una factura entregada a un asesor hace 15 días no aparece ni cobrada en el sistema ni en físico en el archivo:",
                "opciones": {
                    "A": "Emite la alerta formal a la Coordinación de Logística y Ventas con la copia de la relación firmada por el asesor, exigiendo la consignación física del documento o su liquidación.",
                    "B": "Da por perdida la factura y la borra del sistema contable para que el saldo no quede abierto.",
                    "C": "Asume el costo de la factura descontándoselo a los asistentes de almacén sin justificación.",
                    "D": "Emite una Nota de Crédito falsa por anulación total para cuadrar el archivo sin investigar."
                }
            },
            14: {
                "enunciado": "En su relación con jefaturas de logística y auditorías operativas en empleos anteriores:",
                "opciones": {
                    "A": "He tenido discrepancias sobre asignación de flotas con coordinadores de transporte, pero siempre sustenté mis decisiones en costos de ruta y acaté la instrucción final.",
                    "B": "La mayoría de los coordinadores de logística no saben nada de cómo se maneja la plataforma SADA en la práctica.",
                    "C": "No tolero que supervisen mis planes de carga porque mi método de distribución es perfecto.",
                    "D": "En todas las empresas donde he laborado he tenido coordinadores y jefes de logística absolutamente perfectos y libres de errores."
                }
            },
            15: {
                "enunciado": "Al cotejar las facturas confirmadas contra las devoluciones recibidas en almacén, encuentra una factura tachada donde se descontaron 10 cajas de producto sin formato de soporte de motivo:",
                "opciones": {
                    "A": "Procesa la Nota de Crédito por las 10 cajas basándose únicamente en el tachón de la factura.",
                    "B": "Rompe la factura tachada y le exige al chofer que pague las 10 cajas de su propio sueldo.",
                    "C": "Frena la liquidación de la devolución, contacta al cliente telefónicamente para validar el motivo real y exige a almacén el informe formal de recepción antes de procesar la NC.",
                    "D": "Modifica la liquidación anotando que el cliente pagó la totalidad del pedido en efectivo."
                }
            },
            16: {
                "enunciado": "Un transportista le pide que le firme el finiquito de ruta de una gandola, pero no ha entregado las copias de las guías SADA selladas por los tres clientes mayoristas que visitó:",
                "opciones": {
                    "A": "Le firma el finiquito a ciegas confiando en que los clientes sellaron los documentos correctamente.",
                    "B": "Le pide al chofer una parte de su viático para firmarle el finiquito sin revisar las guías.",
                    "C": "Bota la carpeta del camión para justificar que el chofer nunca se presentó a la oficina de logística.",
                    "D": "Niega el finiquito de ruta, retiene la liberación del transporte y exige la entrega inmediata de las guías SADA con sus respectivos sellos húmedos conforme a la ley."
                }
            },
            17: {
                "enunciado": "Al momento de generar los planes de carga, el sistema arroja que un cliente tiene dos facturas emitidas pero una de ellas tiene una dirección fiscal desactualizada que difiere de la guía SADA:",
                "opciones": {
                    "A": "Coordina con Facturación la anulación y refacturación inmediata con la dirección fiscal exacta, garantizando que la factura comercial y la guía SADA concilien perfectamente.",
                    "B": "Despacha el camión con las direcciones dispares esperando que la guardia nacional no compare los papeles.",
                    "C": "Modifica la guía SADA con corrector líquido para que coincida con el error de la factura.",
                    "D": "Anula ambas facturas y suspende la venta a ese cliente de forma indefinida."
                }
            },
            18: {
                "enunciado": "Se produce un corte prolongado en el servicio de internet en la sede principal a las 2:00 p.m., impidiendo emitir las guías SADA para los despachos de la madrugada:",
                "opciones": {
                    "A": "Se cruza de brazos y da por terminada la jornada laboral argumentando causas de fuerza mayor.",
                    "B": "Activa el protocolo de contingencia autorizado (conexión por punto de acceso móvil corporativo o traslado a sede alterna), avanzando con los planes de carga sin paralizar la flota.",
                    "C": "Autoriza la salida de los camiones sin guías emitiendo cartas manuscritas sin validez legal.",
                    "D": "Se marcha a su casa sin avisar a la Coordinación de Logística sobre el estatus de las unidades."
                }
            },
            19: {
                "enunciado": "Sobre la confidencialidad de las rutas comerciales, volúmenes de clientes y claves de acceso al sistema SADA:",
                "opciones": {
                    "A": "Comparto las claves de la plataforma gubernamental SADA con transportistas externos para que ellos emitan sus guías.",
                    "B": "Jamás en toda mi vida he sentido interés ni he mirado información operativa ajena a mis funciones.",
                    "C": "Manejo las claves de acceso, planes de carga y relaciones de facturación bajo estricta reserva y confidencialidad corporativa.",
                    "D": "Si tengo diferencias con la empresa, divulgo las rutas y clientes estratégicos con distribuidoras competidoras."
                }
            },
            20: {
                "enunciado": "Al revisar las facturas desechadas de una ruta, nota que un asesor de ventas reportó como 'rechazo por cliente ilocalizable' un pedido de un cliente mayorista de alta trayectoria:",
                "opciones": {
                    "A": "Liquida la factura como desechada sin indagar las causas de la no entrega del pedido.",
                    "B": "Destruye la factura y da por cerrada la ruta sin consultar al departamento comercial.",
                    "C": "Contacta de inmediato al cliente vía telefónica para validar la veracidad de la visita del transporte, coordina la reprogramación de entrega y reporta la anomalía a Ventas.",
                    "D": "Modifica la factura en el sistema para que figure como vendida y despachada con éxito."
                }
            },
            21: {
                "enunciado": "Al momento de consolidar las guías SADA emitidas en el día, nota que la sumatoria en kilogramos del sistema administrativo presenta un descuadre de 1.200 kg respecto al portal SUNAGRO:",
                "opciones": {
                    "A": "Modifica los números en el informe de gestión en Excel para ocultar el descuadre ante la gerencia.",
                    "B": "Desecha las guías emitidas y se niega a conciliar los kilogramos de los rubros regulados.",
                    "C": "Acusa a los choferes de hurto de mercancía sin haber realizado la auditoría documental previa.",
                    "D": "Realiza la conciliación cruzada ítem por ítem, detecta si hubo guías duplicadas o facturas no enlazadas, ajusta el balance y emite el informe consolidado exacto."
                }
            },
            22: {
                "enunciado": "Un chofer de reparto regresa a la planta con 15 bultos de mercancía averiada (rotas por mala estiba) y exige que se le liquiden como 'dañadas de fábrica' para no asumir el costo:",
                "opciones": {
                    "A": "Acepta registrarlas como daño de fábrica para evitar discusiones con el sindicato de choferes.",
                    "B": "Inspecciona la mercancía junto al supervisor de almacén, levanta el acta de daño operativo por mala estiba según la normativa y gestiona el cobro o reclamo respectivo según manual.",
                    "C": "Bota la mercancía rota en el patio de maniobras para que nadie se dé cuenta del daño.",
                    "D": "Le cobra $30 al chofer para ayudarlo a encubrir la avería en la liquidación de la ruta."
                }
            },
            23: {
                "enunciado": "Al entregar la relación de facturas pendientes por cobrar a la fuerza de ventas, nota que un asesor tiene asignadas facturas de clientes que pertenecen a otra zona geográfica:",
                "opciones": {
                    "A": "Reordena la relación de facturas, asigna cada cuenta por cobrar al asesor de la ruta correcta en el sistema y entrega las carpetas saneadas a la fuerza comercial.",
                    "B": "Deja las facturas mal asignadas para que los vendedores discutan entre ellos en la calle.",
                    "C": "Anula todas las facturas involucradas provocando un descuadre en los libros contables de la empresa.",
                    "D": "Le exige a los clientes que paguen en la sede principal si quieren que sus facturas sean corregidas."
                }
            },
            24: {
                "enunciado": "Sobre el autocontrol emocional ante reclamos de transportistas y retrasos operativos:",
                "opciones": {
                    "A": "Si un chofer me alza la voz reclamando por la demora de su guía, le respondo a golpes de inmediato.",
                    "B": "He tenido momentos de presión ante retrasos en la carga o fallas de sistema, pero mantengo la serenidad, la firmeza procedimental y el trato educado.",
                    "C": "Poseo una templanza infinita e inalterable; absolutamente ningún conflicto laboral ni problema de despacho ha logrado molestarme jamás.",
                    "D": "Cuando me enojo con los transportistas, cierro la oficina y dejo de emitir planes de carga durante todo el día."
                }
            },
            25: {
                "enunciado": "El supervisor de almacén le pide que procese una Nota de Crédito por $1.500 asegurando que él responderá verbalmente ante la gerencia, ya que la administradora está en una reunión fuera de la sede:",
                "opciones": {
                    "A": "Procesa la Nota de Crédito en el sistema de inmediato asumiendo la promesa verbal del supervisor de almacén.",
                    "B": "Altera la factura comercial en el sistema colocándole fecha retrasada para saltarse la Nota de Crédito.",
                    "C": "Emite la Nota de Crédito a nombre de otro cliente para que el monto no llame la atención.",
                    "D": "Retiene la emisión en el sistema y espera la autorización formal y firma de la Gerencia Administrativa conforme al procedimiento establecido para Notas de Crédito."
                }
            },
            26: {
                "enunciado": "Durante el cierre de liquidación, constata que una factura fue desechada porque el cliente rechazó el pedido debido a que la mercancía llegó fuera del horario comercial pactado:",
                "opciones": {
                    "A": "Oculta el motivo real en el sistema y asienta que el cliente no tenía dinero para pagar.",
                    "B": "Registra la factura como desechada con su causal exacta en el sistema, concilia el reingreso con almacén y emite la alerta a Logística y Ventas para optimizar los tiempos de ruta.",
                    "C": "Obliga al chofer a regresar al negocio del cliente de noche a golpear la puerta para que reciba.",
                    "D": "Rompe la factura y borra el pedido del sistema para que no afecte los indicadores de efectividad de ruta."
                }
            },
            27: {
                "enunciado": "Debe elaborar el informe periódico de actividades logísticas (guías SADA emitidas, facturas desechadas, planes de carga ejecutados y notas de crédito procesadas) para la Gerencia:",
                "opciones": {
                    "A": "Envía un correo con tres líneas diciendo que todas las flotas salieron a tiempo y que no hubo novedades.",
                    "B": "Estructura el informe consolidando estadísticas de efectividad de despacho, detalle de facturas desechadas por causal, balance de guías SADA y propuestas de optimización de tiempos.",
                    "C": "Copia el informe del mes anterior modificando únicamente los nombres de los choferes para salir del paso.",
                    "D": "Se niega a realizar informes estadísticos afirmando que su responsabilidad es solo despachar camiones."
                }
            },
            28: {
                "enunciado": "Al momento de entregar las guías SADA y planes de carga a primera hora, detecta que la placa del camión en el Plan de Carga difiere de la placa registrada en la guía de movilización:",
                "opciones": {
                    "A": "Detiene la entrega, verifica cuál es el vehículo asignado físicamente en el andén, corrige el documento discrepante de inmediato en sistema y garantiza la concordancia al 100% antes de la salida.",
                    "B": "Entrega los documentos con placas distintas diciendo al chofer que en las alcabalas nadie revisa las letras de la placa.",
                    "C": "Modifica la placa en la guía con un bolígrafo sobre la hoja impresa.",
                    "D": "Deja que el camión salga y le dice al transportista que si lo detienen diga que fue culpa del analista de sistemas."
                }
            },
            29: {
                "enunciado": "En su relación con compañeros del área de operaciones y reconocimientos laborales:",
                "opciones": {
                    "A": "Nunca en toda mi vida profesional he sentido el menor recelo, molestia ni envidia ante las felicitaciones o ascensos de otros compañeros de trabajo.",
                    "B": "En ocasiones he sentido sana emulación ante los logros de otros, pero me enfoco en perfeccionar mis controles de despacho y cero multas en la flota.",
                    "C": "Considero que cuando felicitan a un analista en la empresa es únicamente por compadrazgo con los directores.",
                    "D": "No me gusta colaborar con otros departamentos porque en las empresas todos buscan atribuirse el mérito ajeno."
                }
            },
            30: {
                "enunciado": "Presidencia le encomienda realizar una auditoría confidencial sobre las facturas desechadas y devoluciones de mercancía registradas en los últimos dos meses:",
                "opciones": {
                    "A": "Comenta los objetivos de la auditoría con los choferes y vendedores durante el receso del café.",
                    "B": "Se niega a realizar la auditoría argumentando que auditar facturas desechadas le generará antipatías con los asesores.",
                    "C": "Ejecuta la auditoría con absoluto sigilo profesional: coteja facturas desechadas vs. reingresos físicos en almacén, audita justificaciones y entrega el informe reservado a Presidencia.",
                    "D": "Altera los motivos de rechazo en los expedientes para encubrir a transportistas amigos."
                }
            }
        }
    },

    # =========================================================================
    # 09. ANALISTA DE SISTEMA SADA (CJS-SAD)
    # =========================================================================
    "09_ANALISTA_DE_SISTEMA_SADA": {
        "codigo": "CJS-SAD",
        "titulo": "EVALUACIÓN PSICOTÉCNICA SITUACIONAL EN SISTEMA SADA Y CONTROL DE DESPACHO",
        "instrucciones": "Lea con atención cada situación laboral y regulatoria. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con absoluta honestidad sobre su rigor legal, precisión en emisión de guías SADA y control de planes de carga. Dispone de un tiempo máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "A las 7:30 a.m., un chofer de reparto foráneo exige salir a ruta con la mercancía montada, alegando que la guía SADA aún está en trámite en la plataforma y que 'él resuelve con los guardias en la alcabala':",
                "opciones": {
                    "A": "Le entrega las facturas y permite que el camión arranque sin guía SADA para no demorar la ruta.",
                    "B": "Le pide al chofer una comisión informal en efectivo para emitirle una guía provisional falsa.",
                    "C": "Le dice al chofer que se vaya por vías alternas o trochas para evadir las alcabalas de control.",
                    "D": "Frena de forma tajante la salida del camión, recordando que ninguna unidad sale sin guía SADA y Plan de Carga conforme a la ley, y agiliza la aprobación en el sistema."
                }
            },
            2: {
                "enunciado": "Al cotejar la factura comercial contra la guía de movilización SADA que emitió la plataforma, nota que en la factura van 100 bultos de harina pero la guía SADA solo aprobó 80 bultos:",
                "opciones": {
                    "A": "Despacha los 100 bultos físicamente esperando que en las alcabalas no cuenten la carga completa.",
                    "B": "Retiene el despacho, coordina con Facturación el ajuste inmediato de la factura a 80 bultos o tramita la guía complementaria en el sistema para que coincidan al 100%.",
                    "C": "Modifica la guía SADA impresa a mano con un bolígrafo colocándole 100 bultos.",
                    "D": "Anula la factura comercial pero envía el camión cargado sin papeles legales."
                }
            },
            3: {
                "enunciado": "Al registrar un nuevo cliente comercial en la plataforma del sistema SADA, el código SICA del cliente arroja estatus de 'Bloqueado / Vencido' por el ente regulador:",
                "opciones": {
                    "A": "Notifica de inmediato al asesor comercial y al cliente sobre el bloqueo de su código SICA, frenando la emisión del pedido hasta su debida regularización ante SUNAGRO.",
                    "B": "Asigna el código SICA de otro cliente activo en el sistema para burlar el bloqueo de la plataforma.",
                    "C": "Emite la guía a nombre de la distribuidora fingiendo que es un traslado entre almacenes propios.",
                    "D": "Despacha la mercancía sin guía cobrando un recargo personal por el riesgo operativo."
                }
            },
            4: {
                "enunciado": "En su trayectoria laboral y manejo de plataformas gubernamentales bajo presión:",
                "opciones": {
                    "A": "Si la plataforma del SADA se cae, golpeo el computador e insulto a los choferes que esperan.",
                    "B": "En ocasiones he sentido tensión ante la lentitud de los servidores oficiales en horas de cierre, pero mantengo la serenidad y aplico los protocolos de contingencia.",
                    "C": "Jamás en toda mi vida laboral he sentido estrés, fatiga ni he tenido dudas al clasificar un código arancelario.",
                    "D": "Prefiero emitir las guías sin revisar los kilos de la carga para no perder tiempo leyendo pantallas."
                }
            },
            5: {
                "enunciado": "Un supervisor de ventas le solicita cambiar el destino de una guía SADA ya emitida y aprobada para redirigir una gandola de arroz a otro cliente de una ruta distinta:",
                "opciones": {
                    "A": "Le dice al chofer que desvíe el camión a la nueva dirección sin anular ni modificar la guía SADA.",
                    "B": "Adultera el documento digital en PDF cambiando la dirección fiscal del destinatario.",
                    "C": "Se desentiende del caso y deja que el supervisor coordine el desvío por teléfono.",
                    "D": "Rechaza el desvío irregular, explica el riesgo de retención por contrabando de extracción y gestiona la anulación formal de la guía en sistema antes de emitir una nueva conforme a derecho."
                }
            },
            6: {
                "enunciado": "Al momento de elaborar el Plan de Carga de una ruta mixta, el sistema de facturación incluye tanto productos regulados (rubros SADA) como productos no regulados:",
                "opciones": {
                    "A": "Emite una sola guía SADA metiendo todos los productos no regulados bajo el código de la harina.",
                    "B": "Se niega a facturar los productos no regulados argumentando que su trabajo es únicamente SADA.",
                    "C": "Discrimina con exactitud técnica los rubros regulados que exigen guía de movilización y elabora el Plan de Carga integrando la totalidad de la carga de la flota.",
                    "D": "Deja que el chofer decida en el andén qué mercancía declara y cuál oculta debajo de la lona."
                }
            },
            7: {
                "enunciado": "La plataforma SADA nacional presenta una caída general de conexión a las 4:00 p.m., justo cuando faltan 6 rutas críticas por emitir guías para la madrugada:",
                "opciones": {
                    "A": "Monitorea activamente la plataforma, prepara los borradores de planes de carga en local y coordina con la Gerencia Administrativa y Logística la reprogramación de salidas.",
                    "B": "Autoriza la salida de los camiones de madrugada sin guías diciendo que la culpa es de SUNAGRO.",
                    "C": "Imprime guías SADA viejas y les altera la fecha con un corrector y fotocopiadora.",
                    "D": "Se retira de la oficina a su hora habitual sin avisar el estado de las guías a Logística."
                }
            },
            8: {
                "enunciado": "Son las 5:45 p.m. (su hora de salida es a las 6:00 p.m.) y la plataforma SADA restablece servicio, permitiendo tramitar las guías pendientes de la flota de la mañana:",
                "opciones": {
                    "A": "Asume la extensión horaria con compromiso, procesa las guías pendientes, concilia contra facturación y entrega la documentación completa a despacho.",
                    "B": "Apaga el computador inmediatamente a las 6:00 p.m. dejando a la flota varada en el patio central.",
                    "C": "Procesa solo las guías de los choferes que le caen bien y deja a los demás sin documentación.",
                    "D": "Se queja a gritos en el pasillo insultando al personal de almacén por exigirle emitir las guías."
                }
            },
            9: {
                "enunciado": "Respecto a la precisión y exactitud en la carga de datos en el sistema SADA:",
                "opciones": {
                    "A": "Jamás en ninguno de mis empleos anteriores he cometido la más mínima equivocación al digitar un RIF, placa de camión o peso en kilogramos.",
                    "B": "Considero que las diferencias de pocos kilos en una guía de movilización no tienen ninguna relevancia legal.",
                    "C": "Cuando he detectado un desfase involuntario en la conciliación factura-guía, he procedido de inmediato a su corrección documental y anulación en sistema.",
                    "D": "Si una guía SADA es retenida en un punto de control, prefiero culpar al transportista que la llevaba."
                }
            },
            10: {
                "enunciado": "Un transportista le informa que tuvo que cambiar de camión a última hora por una avería mecánica y solicita salir con la guía SADA que tiene la placa del vehículo averiado:",
                "opciones": {
                    "A": "Le dice que arranque con esa guía y que si lo detienen diga que fue un error de imprenta.",
                    "B": "Modifica la placa en la guía impresa raspando el papel con una hojilla.",
                    "C": "Le cobra $20 al chofer para dejarlo salir con la placa equivocada.",
                    "D": "Detiene la unidad, tramita la anulación y reemisión de la guía con la placa y cédula del nuevo vehículo/conductor y actualiza el Plan de Carga de la ruta."
                }
            },
            11: {
                "enunciado": "Al conciliar las facturas del día con el sistema SADA, nota que un producto que requiere obligatoriamente guía de movilización fue facturado sin solicitar la emisión de la misma:",
                "opciones": {
                    "A": "Deja pasar la omisión para no generar fricciones con el departamento de facturación.",
                    "B": "Le pide al chofer que esconda el producto en el fondo del camión detrás de cajas no reguladas.",
                    "C": "Alerta de inmediato al facturador y al jefe de almacén, frena la salida del bulto y procesa la guía correspondiente antes de cargar la mercancía.",
                    "D": "Bota la factura comercial a la basura para que no queden registros del error."
                }
            },
            12: {
                "enunciado": "Un cliente comerciante solicita que en la guía SADA le coloquen una dirección de descarga diferente a la que aparece registrada en su código SICA fiscal:",
                "opciones": {
                    "A": "Acepta colocar la dirección informal que pide el cliente para evitar que rechace el pedido.",
                    "B": "Rechaza la solicitud con firmeza, recuerda que la normativa SUNAGRO exige que el despacho coincida con la dirección fiscal registrada y orienta al cliente a actualizar su código.",
                    "C": "Le dice al cliente que pague un soborno al chofer para que descargue donde quiera.",
                    "D": "Emite la guía en blanco para que el cliente llene los datos a su conveniencia."
                }
            },
            13: {
                "enunciado": "Durante la verificación matutina, el sistema administrativo arroja una venta de 2.000 kg de azúcar pero la guía SADA solo puede emitirse por cupo asignado de 1.500 kg:",
                "opciones": {
                    "A": "Emite la guía por los 1.500 kg autorizados, coordina con Facturación la nota de crédito o ajuste por los 500 kg excedentes y ajusta el Plan de Carga a la legalidad.",
                    "B": "Emite la guía por 1.500 kg pero despacha físicamente los 2.000 kg en el camión.",
                    "C": "Cancela todo el despacho y le dice al cliente que la empresa no le venderá más azúcar.",
                    "D": "Falsifica un certificado de cupo especial en Photoshop para guardarlo en los archivos."
                }
            },
            14: {
                "enunciado": "En su relación con jefaturas de operaciones y normativas gubernamentales en empleos previos:",
                "opciones": {
                    "A": "He tenido debates técnicos sobre tiempos de despacho con gerentes de logística, pero siempre defendí el cumplimiento de la providencia SADA y acaté la línea de mando.",
                    "B": "Las leyes de movilización de alimentos son absurdas y están hechas solo para frenar las ventas.",
                    "C": "No tolero que nadie me supervise cómo emito las guías porque conozco la plataforma mejor que nadie.",
                    "D": "En todas las empresas donde he laborado he tenido gerentes de operaciones absolutamente perfectos y libres de fallas."
                }
            },
            15: {
                "enunciado": "Al revisar el archivo diario de guías SADA emitidas, nota que faltan las copias firmadas y selladas de recepción de tres camiones que retornaron de ruta ayer:",
                "opciones": {
                    "A": "Asume que los camiones entregaron todo bien y archiva el legajo como cerrado sin verificar.",
                    "B": "Falsifica las firmas de recepción de los clientes en las copias de las guías SADA.",
                    "C": "Levanta el reporte de no conformidad, exige a Logística y a los choferes la entrega inmediata de las guías finiquitadas y alerta a la Gerencia Administrativa.",
                    "D": "Bota el Plan de Carga de esas rutas para evitar que auditoría interna detecte la falta."
                }
            },
            16: {
                "enunciado": "Un asesor de ventas le solicita emitir una guía SADA de urgencia para un pedido que aún no ha sido facturado ni autorizado por créditos:",
                "opciones": {
                    "A": "Emite la guía SADA de palabra confiando en que el vendedor facturará el pedido más tarde.",
                    "B": "Le cobra una tarifa personal en efectivo al asesor para emitirle la guía sin factura.",
                    "C": "Despacha la mercancía por su cuenta sin notificar a Almacén ni a Facturación.",
                    "D": "Niega rotundamente la solicitud, ratificando que toda guía SADA debe estar sustentada en una orden facturada y autorizada conforme al manual procedimental."
                }
            },
            17: {
                "enunciado": "Al momento de generar las guías a primera hora de la mañana, detecta que en el sistema se duplicó una orden de movilización generando dos guías con diferente correlativo para la misma factura:",
                "opciones": {
                    "A": "Procede a anular de inmediato la guía duplicada en la plataforma SADA, documenta la causal técnica de la anulación y conserva el soporte para el informe diario.",
                    "B": "Deja ambas guías activas en el sistema para que la empresa pague el doble de aranceles.",
                    "C": "Le entrega ambas guías al chofer para que intente vender una carga ficticia en la calle.",
                    "D": "Modifica la factura en el sistema para que coincida con la duplicidad de la guía."
                }
            },
            18: {
                "enunciado": "Se presenta una inspección imprevista de funcionarios de SUNAGRO en el andén de despacho de la empresa:",
                "opciones": {
                    "A": "Se esconde en el depósito y se niega a atender a los inspectores por temor a sanciones.",
                    "B": "Atiende la fiscalización con aplomo profesional, suministra los planes de carga, guías SADA vigentes y facturas en regla, y reporta de inmediato a la Gerencia General.",
                    "C": "Ofrece mercancía o dinero informal a los funcionarios antes de que comiencen a revisar.",
                    "D": "Discute agresivamente con los fiscales acusándolos de perseguir a la empresa privada."
                }
            },
            19: {
                "enunciado": "Sobre la custodia de claves de acceso gubernamentales y confidencialidad de la plataforma SADA:",
                "opciones": {
                    "A": "Comparto el usuario y la clave del sistema SADA de la empresa con choferes o amigos externos.",
                    "B": "Jamás en toda mi vida he sentido la mínima curiosidad por mirar un registro comercial o fiscal ajeno.",
                    "C": "Resguardo el usuario, contraseñas y certificados digitales bajo estricta reserva y protocolos de seguridad informática.",
                    "D": "Si me molesto con la gerencia, bloqueo la clave del sistema SADA para que nadie pueda despachar."
                }
            },
            20: {
                "enunciado": "Al cotejar el Plan de Carga de una flota, nota que el peso total en kilogramos cargado en la plataforma excede la capacidad de carga legal autorizada para ese camión:",
                "opciones": {
                    "A": "Autoriza la salida del camión sobrecargado ignorando el riesgo de multas viales o volcamientos.",
                    "B": "Modifica los kilogramos en la guía SADA colocándole menos peso para engañar a las básculas viales.",
                    "C": "Coordina de inmediato con Almacén y Logística la redistribución de la carga en otra unidad, ajusta el Plan de Carga y emite las guías conforme a la capacidad técnica del vehículo.",
                    "D": "Le exige al chofer que pague las multas de tránsito si lo detienen en una báscula."
                }
            },
            21: {
                "enunciado": "El sistema administrativo presenta un desfase de sincronización y no actualiza los números de factura en el módulo de enlaces SADA:",
                "opciones": {
                    "A": "Paraliza el trabajo de despacho de todo el día y se niega a realizar enlaces manuales.",
                    "B": "Emite guías con números de factura inventados para salir del paso rápidamente.",
                    "C": "Borra la base de datos de pedidos para forzar a los vendedores a cargar todo de nuevo.",
                    "D": "Realiza la conciliación manual uno a uno en la plataforma oficial, documenta los cruces en la hoja de control de despacho y levanta el ticket a Sistemas con urgencia."
                }
            },
            22: {
                "enunciado": "Un cliente se queja telefónicamente afirmando que el camión de la empresa llegó a su negocio pero la guía SADA venció su vigencia de 48 horas porque el transporte se retrasó:",
                "opciones": {
                    "A": "Le dice al cliente que reciba la mercancía con la guía vencida y que no se preocupe por las multas.",
                    "B": "Gestiona la anulación y reemisión de la guía de movilización por vigencia expirada en la plataforma, coordina con el chofer y envía la nueva guía digital para la recepción conforme.",
                    "C": "Insulta al chofer por haberse retrasado y se niega a solucionar la guía del cliente.",
                    "D": "Le cobra una tarifa administrativa al cliente para renovarle la vigencia del documento."
                }
            },
            23: {
                "enunciado": "Al auditar las órdenes de pedido del día, observa que una referencia de pasta alimenticia fue catalogada en el sistema de ventas con un código arancelario SADA equivocado:",
                "opciones": {
                    "A": "Emite la guía con el código erróneo asumiendo que ningún fiscal revisa los rubros secundarios.",
                    "B": "Corrige la codificación en el catálogo regulatorio, verifica que el inventario concilie con el rubro real y emite la guía bajo la descripción exacta exigida por providencia.",
                    "C": "Deja de emitir guías para ese producto durante todo el mes para evitar problemas de catálogo.",
                    "D": "Cambia la etiqueta física del producto en el almacén para que coincida con el error del sistema."
                }
            },
            24: {
                "enunciado": "Sobre el autocontrol y manejo de la presión ante colas de camiones en el andén:",
                "opciones": {
                    "A": "Si los choferes tocan la puerta de mi oficina exigiendo las guías, les grito e insulto para que respeten.",
                    "B": "He experimentado momentos de alta exigencia cuando coinciden varias flotas por salir, pero mantengo el orden secuencial, la precisión y la calma operativa.",
                    "C": "Poseo una serenidad sobrehumana inalterable; ningún retraso de plataforma ni reclamo de transportistas me ha causado estrés jamás.",
                    "D": "Cuando se acumulan los camiones en el patio, cierro con llave mi oficina y me retiro a descansar."
                }
            },
            25: {
                "enunciado": "Un supervisor de operaciones le ofrece omitir la emisión de guías SADA para despachos locales cortos a cambio de repartir el ahorro del costo arancelario:",
                "opciones": {
                    "A": "Acepta la propuesta para generar un beneficio económico adicional con los despachos locales.",
                    "B": "Negocia que el beneficio sea mayor para omitir guías también en rutas nacionales.",
                    "C": "Acepta pero le pide a los choferes que no digan nada si son detenidos en la calle.",
                    "D": "Rechaza de plano la propuesta ilegal, reafirma la obligatoriedad de movilización legal para evitar decomisos y reporta la situación de inmediato a la Gerencia General."
                }
            },
            26: {
                "enunciado": "Durante el cierre de la jornada, constata que una guía SADA emitida a las 8:00 a.m. no fue utilizada porque el cliente canceló el pedido antes de cargar el camión:",
                "opciones": {
                    "A": "Deja la guía abierta en la plataforma esperando que el sistema del Estado la cierre solo.",
                    "B": "Procesa la anulación inmediata de la guía en el portal SADA antes de que expire el plazo legal, asienta la justificación y archiva el comprobante de anulación.",
                    "C": "Guarda la guía para utilizársela a otro cliente en los despachos de la semana siguiente.",
                    "D": "Rompe la guía física y finge que el documento nunca fue emitido en el sistema."
                }
            },
            27: {
                "enunciado": "Debe elaborar el informe periódico de actividades de guías emitidas diariamente para la Gerencia de Operaciones:",
                "opciones": {
                    "A": "Envía un mensaje de texto de una sola línea diciendo que todas las guías del mes salieron bien.",
                    "B": "Estructura el informe consolidando número de guías emitidas, anuladas, kilogramos movilizados por rubro regulado, tiempos de respuesta y contingencias de plataforma.",
                    "C": "Copia el informe del mes anterior modificando únicamente los nombres de los choferes.",
                    "D": "Manifiesta que los informes de guías son innecesarios porque el Estado ya tiene el registro en su web."
                }
            },
            28: {
                "enunciado": "Al entregar la documentación de despacho a primera hora, se percata de que la factura tiene un error en el número de RIF del cliente pero la guía SADA salió con el RIF correcto:",
                "opciones": {
                    "A": "Coordina con Facturación la corrección inmediata de la factura comercial para que ambos documentos posean exactamente la misma identidad fiscal antes de liberar la flota.",
                    "B": "Despacha el camión con los documentos dispares confiando en que nadie notará el error.",
                    "C": "Modifica la factura con un bolígrafo encima de la impresión original.",
                    "D": "Anula la guía SADA correcta para que coincida con el error de la factura comercial."
                }
            },
            29: {
                "enunciado": "En su relación con otros analistas de la empresa y reconocimientos de gestión:",
                "opciones": {
                    "A": "Nunca en toda mi vida profesional he sentido el menor recelo, molestia ni envidia por las felicitaciones otorgadas a mis compañeros.",
                    "B": "A veces he sentido sana emulación profesional ante los méritos ajenos, pero me concentro en blindar la empresa contra sanciones y agilizar las salidas de flota.",
                    "C": "Pienso que cuando felicitan a un analista en la empresa es únicamente por amistad personal con los directores.",
                    "D": "Prefiero trabajar aislado sin comunicarme con nadie porque los demás departamentos siempre entorpecen mi labor."
                }
            },
            30: {
                "enunciado": "Presidencia le encomienda realizar una auditoría confidencial sobre el histórico de guías SADA anuladas en el último trimestre para evaluar riesgos de sanción:",
                "opciones": {
                    "A": "Comenta los detalles de la auditoría con los choferes y despachadores durante el receso.",
                    "B": "Se rehúsa a realizar la auditoría argumentando que auditar anulaciones no es su competencia.",
                    "C": "Ejecuta la auditoría con absoluto sigilo profesional: concilia guías anuladas vs. notas de crédito, verifica justificaciones legales en portal y entrega el informe reservado a Presidencia.",
                    "D": "Altera los motivos de anulación en los archivos para encubrir despachos irregulares de compañeros."
                }
            }
        }
    },
    # =========================================================================
    # 11. ASESOR DE VENTAS (IPC-T)
    # =========================================================================
    "11_ASESOR_DE_VENTAS": {
        "codigo": "IPC-T",
        "titulo": "EVALUACIÓN PSICOTÉCNICA ASESOR DE VENTAS",
        "instrucciones": "Lea atentamente cada una de las 30 situaciones. Marque con una equis [ X ] una sola opción (A, B, C o D) por cada pregunta. Sea totalmente honesto; no hay respuestas de libro, buscamos conocer su forma real de trabajar la calle y atender clientes. Dispone de un tiempo máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "Al llegar a un negocio clave de la ruta, el encargado le informa de mala manera que no tiene tiempo para atenderlo hoy y que regrese la próxima semana:",
                "opciones": {
                    "A": "Le pide educadamente 2 minutos para verificar inventario crítico del producto de mayor rotación y evitar quiebres.",
                    "B": "Le explica con firmeza que la ruta pasa solo hoy y que si no compra se quedará sin despacho semanal.",
                    "C": "Se retira de inmediato para evitar roces y anota la visita como fallida por causa del cliente.",
                    "D": "Espera sentado fuera del local hasta que el encargado se desocupe, aunque retrase el resto del día."
                }
            },
            2: {
                "enunciado": "En ocasiones, cuando el día se complica en la calle:",
                "opciones": {
                    "A": "Prefiero suspender el recorrido y reiniciar al día siguiente con mejor energía.",
                    "B": "Jamás he sentido cansancio ni desánimo ante un mal resultado.",
                    "C": "He llegado a dudar brevemente de si alcanzaré la meta, pero continúo la jornada.",
                    "D": "Suelo frustrarme y atribuirlo a las condiciones del mercado actual."
                }
            },
            3: {
                "enunciado": "La gerencia fija una cuota mensual que usted percibe un 25% por encima de la capacidad de compra de su zona:",
                "opciones": {
                    "A": "Solicita de inmediato una reunión con su supervisor para exigir que bajen la cuota antes de salir a la calle.",
                    "B": "Distribuye el exceso facturando mercancía extra a clientes de confianza sin consultarles previamente.",
                    "C": "Cumple su rutina habitual sabiendo que la gerencia comprenderá que la meta era poco realista.",
                    "D": "Desglosa la meta por cliente clave, planifica reactivación de inactivos y busca colocación de nuevos productos."
                }
            },
            4: {
                "enunciado": "Su supervisor le instruye visitar 18 clientes diarios, pero usted considera que con 12 visitas vende igual:",
                "opciones": {
                    "A": "Trabaja a su manera con 12 visitas y demuestra a fin de mes con números que su método funciona.",
                    "B": "Acata la instrucción de las 18 visitas, adaptando su tiempo sin descuidar el estándar de atención.",
                    "C": "Mantiene las 12 visitas y reporta 18 en la planilla para no tener roces con la supervisión.",
                    "D": "Se reúne con otros vendedores para quejarse de la exigencia poco práctica de la supervisión."
                }
            },
            5: {
                "enunciado": "Un cliente con factura vencida le insiste en que le tome pedido, prometiendo pagar ambas facturas la próxima semana:",
                "opciones": {
                    "A": "Explica la política de crédito, concilia un abono inmediato a la deuda vieja y tramita el pedido sujeto a liberación.",
                    "B": "Le niega la atención tajantemente y le suspende el despacho hasta que cancele la totalidad.",
                    "C": "Monta el pedido asumiendo el riesgo, priorizando no perder la venta del mes.",
                    "D": "Le aconseja comprar con el código de otro cliente amigo para burlar el bloqueo del sistema."
                }
            },
            6: {
                "enunciado": "Cuando el camión de reparto no entrega a tiempo a 3 clientes y estos le reclaman molestos a usted:",
                "opciones": {
                    "A": "Les aclara que es problema de despacho y les entrega el número telefónico del transportista.",
                    "B": "No atiende llamadas durante la tarde hasta tener certeza de que el pedido fue entregado.",
                    "C": "Se disculpa prometiendo descuentos no autorizados en la siguiente compra para calmar su molestia.",
                    "D": "Escucha el reclamo, valida el estatus con logística interna y coordina solución manteniendo informado al cliente."
                }
            },
            7: {
                "enunciado": "En su vida cotidiana o laboral:",
                "opciones": {
                    "A": "Si alguien me falta el respeto en la calle, respondo con la misma energía.",
                    "B": "A veces me cuesta entender decisiones de otros, pero mantengo el autocontrol.",
                    "C": "Nunca me he molestado ni he perdido la paciencia con ninguna persona.",
                    "D": "Rara vez expreso mi desacuerdo por temor a generar discusiones."
                }
            },
            8: {
                "enunciado": "Son las 3:30 p.m., ya superó su meta del día y aún le restan 4 clientes programados en el itinerario:",
                "opciones": {
                    "A": "Llama por teléfono a los clientes restantes para verificar si necesitan algo sin necesidad de trasladarse.",
                    "B": "Cierra el día y aprovecha el tiempo libre adelantando diligencias personales.",
                    "C": "Completa las 4 visitas programadas buscando sobrecumplir la meta y asegurar pedidos futuros.",
                    "D": "Reporta que los locales estaban cerrados para justificar no haber completado el recorrido físico."
                }
            },
            9: {
                "enunciado": "Al llegar a un comercio, nota que la competencia ocupó con publicidad el espacio asignado a su empresa:",
                "opciones": {
                    "A": "Retira y desecha la publicidad de la competencia de inmediato sin consultar al encargado.",
                    "B": "Negocia con el comerciante la reorganización del exhibidor, destacando la rotación y margen de su producto.",
                    "C": "Ignora la situación para evitar discusiones con el comerciante sobre el manejo de su espacio.",
                    "D": "Toma fotos y envía un reclamo al supervisor culpando a la empresa por falta de apoyo."
                }
            },
            10: {
                "enunciado": "Respecto al seguimiento de reglas e instrucciones en el trabajo:",
                "opciones": {
                    "A": "Jamás he cometido un error ni he incumplido una norma en ninguno de mis empleos anteriores.",
                    "B": "Considero que las normas son solo sugerencias que limitan la creatividad del vendedor.",
                    "C": "Prefiero seguir los protocolos establecidos, aunque en ocasiones operativas se requiera criterio propio.",
                    "D": "Solo cumplo las reglas cuando el supervisor está presente acompañándome en la ruta."
                }
            },
            11: {
                "enunciado": "Un compañero sufre una avería en su vehículo y le solicita apoyo para despachar dos cobranzas urgentes:",
                "opciones": {
                    "A": "Se niega, señalando que cada asesor responde individualmente por su ruta y dinero.",
                    "B": "Le cobra una comisión personal a su compañero por hacerle la gestión de cobro.",
                    "C": "Acepta apoyarlo de inmediato sin notificar a nadie, cobrando en efectivo por cuenta ajena.",
                    "D": "Consulta previamente con el supervisor y, si no afecta su recorrido, brinda el apoyo solicitado."
                }
            },
            12: {
                "enunciado": "La empresa lanza un producto nuevo de baja rotación y exige colocarlo en el 80% de los clientes de la ruta:",
                "opciones": {
                    "A": "Presenta el producto a cada cliente con argumentos de margen, exhibición y rotación.",
                    "B": "Factura el producto de forma camuflada dentro de los pedidos habituales de alta rotación.",
                    "C": "Solo ofrece el producto a los 2 o 3 clientes más grandes para cumplir el volumen sin visitar al resto.",
                    "D": "Decide no ofrecerlo para evitar reclamos futuros por acumulación de mercancía lenta."
                }
            },
            13: {
                "enunciado": "Su supervisor le realiza un llamado de atención formal por fallas en la puntualidad de sus reportes:",
                "opciones": {
                    "A": "Guarda silencio en la reunión, pero luego descalifica la autoridad del supervisor ante sus compañeros.",
                    "B": "Contradice al supervisor frente a todos, afirmando que lo único que cuenta es vender.",
                    "C": "Acepta la observación, asume su responsabilidad y ajusta su rutina diaria para reportar a tiempo.",
                    "D": "Se desmotiva y disminuye deliberadamente su ritmo de trabajo durante los días siguientes."
                }
            },
            14: {
                "enunciado": "Durante tres días seguidos se presentan lluvias torrenciales o fallas viales que complican el acceso a su zona:",
                "opciones": {
                    "A": "Realiza solo una o dos visitas cercanas y pasa el resto de la jornada en un punto de espera.",
                    "B": "Replantea la ruta atacando zonas accesibles, contacta vía telefónica a clientes anegados y coordina despachos.",
                    "C": "Se queda en su domicilio esperando que las condiciones climáticas y viales se normalicen.",
                    "D": "Notifica que no hay condiciones mínimas para trabajar y solicita justificación de ausencia."
                }
            },
            15: {
                "enunciado": "Al momento de cobrar en divisas, un cliente habitual le entrega un billete deteriorado que la empresa no recibe:",
                "opciones": {
                    "A": "Explica con tacto la política de recepción y solicita sustituirlo por otro billete o transferencia.",
                    "B": "Recibe el billete para evitar fricción con el cliente y luego intenta entregarlo camuflado en caja.",
                    "C": "Rechaza el pago de forma despectiva y le suspende el despacho de inmediato.",
                    "D": "Cambia el billete por uno personal propio asumiendo el riesgo de pérdida."
                }
            },
            16: {
                "enunciado": "Cuando reflexiona sobre su trayectoria laboral previa:",
                "opciones": {
                    "A": "He tenido diferencias de criterio con superiores, pero siempre se canalizaron profesionalmente.",
                    "B": "Generalmente mis supervisores no entendían la realidad del trabajo de campo.",
                    "C": "Siempre he preferido trabajar por mi cuenta porque no tolero que supervisen mis movimientos.",
                    "D": "En todos mis trabajos anteriores he tenido jefes perfectos con los que jamás tuve desacuerdos."
                }
            },
            17: {
                "enunciado": "Un cliente histórico amenaza con irse a la competencia si no le otorga un crédito extendido no autorizado:",
                "opciones": {
                    "A": "Cede a la exigencia del cliente y autoriza el crédito por cuenta propia para salvar la cuenta.",
                    "B": "Promete falsamente el crédito extendido para asegurar el pedido hoy y postergar el problema.",
                    "C": "Le dice al cliente que compre a la competencia, desestimando la importancia de su cuenta.",
                    "D": "Defiende la propuesta de valor del portafolio (servicio, margen, rotación) e involucra al supervisor."
                }
            },
            18: {
                "enunciado": "En el almacén le notifican quiebre de stock del producto principal que usted más vende en su zona:",
                "opciones": {
                    "A": "Se queja abiertamente con los clientes sobre la ineficiencia logística de la empresa.",
                    "B": "Continúa vendiendo el producto agotado esperando que el almacén resuelva oportunamente.",
                    "C": "Redirige su estrategia comercial impulsando productos sustitutos o secundarios del portafolio.",
                    "D": "Deja de hacer la ruta comercial hasta que restablezcan el inventario de ese producto."
                }
            },
            19: {
                "enunciado": "El supervisor implementa una aplicación móvil con geolocalización (GPS) para registrar visitas en tiempo real:",
                "opciones": {
                    "A": "Registra las visitas de toda la semana en un solo día sin acudir físicamente a los locales.",
                    "B": "Adopta la herramienta con disciplina y aprovecha el registro para optimizar sus tiempos de ruta.",
                    "C": "Se queja abiertamente argumentando que la medida demuestra desconfianza hacia los vendedores.",
                    "D": "Utiliza aplicaciones de ubicación falsa para burlar el rastreo satelital mientras atiende asuntos propios."
                }
            },
            20: {
                "enunciado": "Si se comete un error en la toma de un pedido comercial:",
                "opciones": {
                    "A": "Busco la manera de atribuir la falla al personal de facturación o de despacho.",
                    "B": "Jamás me he equivocado al tomar un código o un precio en mi vida.",
                    "C": "Asumo la equivocación ante el cliente y la empresa, gestionando la corrección de inmediato.",
                    "D": "Intento convencer al cliente de que él fue quien solicitó ese producto por equivocación."
                }
            },
            21: {
                "enunciado": "Al ingresar a un negocio, el dueño está ocupado discutiendo con un proveedor de otro rubro:",
                "opciones": {
                    "A": "Interrumpe la conversación para anunciar su llegada e insistir en que tiene la ruta retrasada.",
                    "B": "Se marcha del negocio inmediatamente sin registrar la visita ni esperar turno.",
                    "C": "Espera con prudencia o revisa el estado de anaqueles y lineales mientras el comerciante se desocupa.",
                    "D": "Se involucra en la discusión opinando sobre el tema para llamar la atención del cliente."
                }
            },
            22: {
                "enunciado": "La empresa ofrece una bonificación especial si el equipo de ventas de la región alcanza la meta grupal:",
                "opciones": {
                    "A": "Comparte buenas prácticas, apoya a compañeros rezagados y asegura su sobrecumplimiento individual.",
                    "B": "Se concentra únicamente en su zona, desentendiéndose del desempeño de los demás compañeros.",
                    "C": "Espera que los vendedores más antiguos cubran la cuota grupal con sus clientes grandes.",
                    "D": "Exige que la bonificación sea individual, desestimando el valor del trabajo coordinado."
                }
            },
            23: {
                "enunciado": "Un cliente le manifiesta que la competencia le ofrece un descuento del 5% adicional por pronto pago:",
                "opciones": {
                    "A": "Descalifica con agresividad a la empresa competidora frente al cliente.",
                    "B": "Analiza con el cliente el costo-beneficio del portafolio (frecuencia de entrega, calidad, margen real).",
                    "C": "Le iguala el descuento de palabra sin consultar ni tener la facultad para hacerlo.",
                    "D": "Se da por vencido y da de baja al cliente de su ruta activa."
                }
            },
            24: {
                "enunciado": "Respecto a los sentimientos de desmotivación o cansancio:",
                "opciones": {
                    "A": "Mi rendimiento depende casi por completo del estado de ánimo del mercado.",
                    "B": "Hay días más complejos que otros, pero la autodisciplina me mantiene enfocado en los objetivos.",
                    "C": "Absolutamente todos los días me levanto con exactamente el mismo nivel óptimo de motivación.",
                    "D": "Si amanezco desmotivado, rindo al mínimo indispensable durante esa jornada."
                }
            },
            25: {
                "enunciado": "El departamento de crédito bloquea a un cliente por una diferencia menor pendiente desde hace 48 horas:",
                "opciones": {
                    "A": "Insulta al personal de cobranza por frenarle una venta comisionable.",
                    "B": "Crea un código provisional con los datos de un familiar del cliente para saltarse la traba.",
                    "C": "Le indica al cliente que no le compre más a la distribuidora por ser demasiado estricta.",
                    "D": "Acude de inmediato al cliente, gestiona el pago del saldo y solicita la liberación formal."
                }
            },
            26: {
                "enunciado": "Al cierre del mes, queda a un 3% de alcanzar el escalafón más alto de comisiones y le queda solo una hora:",
                "opciones": {
                    "A": "Revisa su cartera, contacta a clientes de alta rotación y gestiona un pedido express para cerrar la brecha.",
                    "B": "Cierra el sistema y se conforma con el escalafón alcanzado.",
                    "C": "Carga una venta ficticia para cobrar la comisión y luego pide anularla al inicio del mes siguiente.",
                    "D": "Le pide al supervisor que le modifique manualmente la cuota para alcanzar el beneficio."
                }
            },
            27: {
                "enunciado": "Un comerciante le propone pagarle una factura en efectivo sin recibo, ofreciéndole una propina personal:",
                "opciones": {
                    "A": "Recibe el dinero sin reportarlo y lo utiliza como fondo para sus gastos de ruta.",
                    "B": "Acepta el dinero para resolver una urgencia y reporta la cobranza como pendiente.",
                    "C": "Rechaza la propuesta con firmeza, emite el recibo oficial y entrega el dinero en caja.",
                    "D": "Acepta la propuesta argumentando que las comisiones son insuficientes."
                }
            },
            28: {
                "enunciado": "Cuando un cliente se niega reiteradamente a comprarle durante cuatro visitas consecutivas:",
                "opciones": {
                    "A": "Confronta al comerciante exigiéndole una explicación por hacerle perder el tiempo.",
                    "B": "No vuelve a visitar el establecimiento y lo elimina de su plan de trabajo.",
                    "C": "Reporta que el negocio cerró sus puertas definitivamente.",
                    "D": "Evalúa las causas del rechazo, cambia el enfoque de presentación y persiste en la siguiente ronda."
                }
            },
            29: {
                "enunciado": "En las relaciones de trabajo con otros colegas:",
                "opciones": {
                    "A": "Nunca en mi vida he sentido envidia ni molestia por el éxito de un compañero.",
                    "B": "Pienso que cuando alguien vende mucho es porque le asignaron una ruta privilegiada.",
                    "C": "Reconozco los logros ajenos, aunque busco superarme para estar entre los mejores.",
                    "D": "Prefiero no relacionarme con otros vendedores porque en ventas todos son rivales."
                }
            },
            30: {
                "enunciado": "El supervisor le solicita acompañarlo durante toda la jornada para realizar una auditoría de campo:",
                "opciones": {
                    "A": "Solicita reposo médico el día anterior para evitar la evaluación en campo.",
                    "B": "Asume la jornada con naturalidad, mostrando su rutina real y abierto a recibir retroalimentación.",
                    "C": "Se muestra incómodo y tenso durante todo el trayecto por sentirse vigilado.",
                    "D": "Modifica completamente su forma de trabajar solo por ese día para dar una impresión artificial."
                }
            }
        }
    },
    # =========================================================================
    # 14. ASISTENCIA ADMINISTRATIVA CONTABLE (CJS-AAC)
    # =========================================================================
    "14_ASISTENCIA_ADMINISTRATIVA_CONTABLE": {
        "codigo": "CJS-AAC",
        "titulo": "EVALUACIÓN PSICOTÉCNICA SITUACIONAL EN ASISTENCIA ADMINISTRATIVA CONTABLE",
        "instrucciones": "Lea con atención cada situación laboral, contable y tributaria. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con absoluta honestidad sobre su rigor numérico, puntualidad en cierres de sistema y apego a normas fiscales. Dispone de un máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "El primer día hábil del mes a las 8:00 a.m. debe ejecutar el cierre de mes en el sistema administrativo (Cata Suite), pero nota que el módulo de ventas aún tiene tres facturas pendientes por sincronizar:",
                "opciones": {
                    "A": "Ejecuta el cierre a ciegas a las 8:00 a.m. sin importar que las tres facturas queden fuera del mes.",
                    "B": "Posterga el cierre de mes hasta mediados de quincena sin consultar con la gerencia.",
                    "C": "Anula las tres facturas pendientes en el sistema para forzar el cuadre automático.",
                    "D": "Coordina inmediatamente la sincronización prioritaria de las tres facturas, ejecuta el cierre formal de inventario y cuentas por cobrar, y resguarda los reportes en digital (PDF/Adobe) según manual."
                }
            },
            2: {
                "enunciado": "Al revisar y certificar el Libro de Compras del mes contra las facturas físicas originales de los proveedores, detecta que una factura tiene un error en el número de control fiscal impreso:",
                "opciones": {
                    "A": "Modifica el número de control con un bolígrafo sobre la factura física del proveedor.",
                    "B": "Retiene la inclusión en el libro fiscal, solicita de inmediato la refacturación o nota de corrección al proveedor, verifica la base imponible y el IVA, y asienta el comprobante debidamente saneado.",
                    "C": "Registra la factura con datos inventados para no tener diferencias con el contador externo.",
                    "D": "Bota la factura del proveedor a la basura para no tener que declararla ante el SENIAT."
                }
            },
            3: {
                "enunciado": "Al preparar las retenciones de ISLR por honorarios profesionales y servicios recibidos de la quincena, nota que el porcentaje de retención aplicado en el sistema fue del 1% en lugar del 3% legal aplicable:",
                "opciones": {
                    "A": "Ajusta de inmediato el cálculo a la alícuota legal del 3%, emite el comprobante de retención correcto, elabora la planilla para declaración y notifica a la administración.",
                    "B": "Deja la retención al 1% para beneficiar económicamente al proveedor del servicio.",
                    "C": "Elimina el comprobante de retención para que la empresa no tenga que enterar impuestos.",
                    "D": "Le cobra la diferencia del impuesto en efectivo personal al proveedor sin emitir recibo."
                }
            },
            4: {
                "enunciado": "En su experiencia laboral y desempeño en rutinas contables bajo presión:",
                "opciones": {
                    "A": "Si el contador me pide revisar una factura que ya archivé, le tiro las carpetas en el escritorio.",
                    "B": "En ocasiones he sentido tensión ante la proximidad de los plazos de declaración fiscal y cierres mensuales, pero mantengo la concentración y la precisión en los papeles de trabajo.",
                    "C": "Jamás en toda mi vida profesional he sentido estrés ni he tenido dudas al clasificar una cuenta de gastos.",
                    "D": "Prefiero archivar los comprobantes sin revisar las fechas para desocuparme rápido de la oficina."
                }
            },
            5: {
                "enunciado": "Durante la preparación de la declaración de impuestos municipales (SAMAT / Alcaldía), detecta que los ingresos brutos del libro de ventas difieren de los ingresos reflejados en el sistema Cata Suite:",
                "opciones": {
                    "A": "Declara un monto aproximado al azar ante la Alcaldía para cumplir con la fecha límite.",
                    "B": "Modifica los libros de ventas fiscales para que coincidan con la cifra menor y pagar menos tributos.",
                    "C": "Se desentiende de la declaración y deja que la Alcaldía multe a la empresa.",
                    "D": "Realiza la conciliación exhaustiva entre facturación, notas de crédito por devolución/descuento y el libro de ventas, identifica la causa raíz y declara los ingresos brutos reales certificados."
                }
            },
            6: {
                "enunciado": "Al conciliar las cuentas bancarias el primer día del mes, el banco no ha emitido los estados de cuenta sellados físicamente en la agencia:",
                "opciones": {
                    "A": "Se cruza de brazos y no realiza ninguna conciliación durante todo el mes.",
                    "B": "Inventa saldos contables en el libro mayor para simular que las cuentas están cuadradas.",
                    "C": "Descarga los extractos digitales preliminares para avanzar en el cruce de movimientos, y gestiona formalmente ante la entidad bancaria los estados de cuenta sellados para el legajo definitivo.",
                    "D": "Acusa a los cajeros del banco de negligencia y paraliza las actividades del departamento."
                }
            },
            7: {
                "enunciado": "Al preparar los papeles de trabajo de gastos estimados y provisiones del mes (obsolescencia de inventario, cuentas por cobrar incobrables y gastos fijos):",
                "opciones": {
                    "A": "Sustenta cada estimación con los reportes analíticos generados en Cata Suite, calcula las provisiones según las políticas contables y anexa los soportes a la carpeta digital y física.",
                    "B": "Coloca cifras idénticas a las del año pasado sin consultar los reportes del sistema.",
                    "C": "Deja las provisiones en cero para que la empresa muestre ganancias ficticias más altas.",
                    "D": "Le pide a los proveedores de gastos fijos que ellos mismos hagan los papeles de trabajo."
                }
            },
            8: {
                "enunciado": "Son las 5:45 p.m. (su hora de salida es a las 6:00 p.m.) del día 8 del mes, plazo límite normativo para imprimir y encuadernar los libros contables obligatorios:",
                "opciones": {
                    "A": "Asume la extensión horaria con compromiso profesional, culmina la impresión y verificación correlativa de los libros contables y los deja resguardados según el manual procedimental.",
                    "B": "Apaga los equipos inmediatamente a las 6:00 p.m. dejando los libros sin imprimir.",
                    "C": "Imprime solo las primeras tres páginas para aparentar que cumplió con la fecha límite.",
                    "D": "Se queja a gritos en el pasillo insultando a la administración por exigir libros impresos."
                }
            },
            9: {
                "enunciado": "Respecto al rigor técnico y la exactitud en el registro de números de control fiscal y fechas:",
                "opciones": {
                    "A": "Jamás en ninguno de mis empleos anteriores he cometido un solo error de digitación en una factura, comprobante o planilla fiscal.",
                    "B": "Considero que el orden cronológico estricto en los archivadores es una pérdida de tiempo innecesaria.",
                    "C": "Cuando he detectado una inconsistencia involuntaria en una fecha o correlativo contable, he procedido de inmediato a documentar la corrección formal en libros.",
                    "D": "Si una declaración tributaria sale con datos erróneos, prefiero culpar al sistema informático."
                }
            },
            10: {
                "enunciado": "Un directivo de la empresa le solicita retirar un soporte original de gasto de una carpeta contable ya cerrada y archivada para utilizarlo en un trámite personal:",
                "opciones": {
                    "A": "Le entrega el documento original sin dejar copia ni constancia en el archivo contable.",
                    "B": "Rompe la carpeta completa para evitar que se descubra la falta del documento.",
                    "C": "Cobra una comisión en efectivo por facilitar el documento confidencial de la empresa.",
                    "D": "Explica con respeto que los soportes originales archivados son inamovibles por auditoría fiscal, suministrando en su lugar una copia certificada debidamente sellada."
                }
            },
            11: {
                "enunciado": "Al revisar las Notas de Crédito emitidas en el mes para su incorporación al Libro de Ventas, nota que dos de ellas no tienen anexada la copia de la factura de origen afectada:",
                "opciones": {
                    "A": "Registra las Notas de Crédito sin soporte esperando que el SENIAT no las fiscalice.",
                    "B": "Anula las Notas de Crédito en el sistema sin avisar al cliente ni a facturación.",
                    "C": "Solicita a Facturación/Liquidación las copias de las facturas originales afectadas, constata que los montos de base imponible e IVA coincidan exactamente y completa el legajo fiscal.",
                    "D": "Modifica las fechas de las facturas a mano para evitar tener que buscar los soportes."
                }
            },
            12: {
                "enunciado": "Debe elaborar el informe periódico de actividades administrativas y contables realizadas durante el mes para la Gerencia:",
                "opciones": {
                    "A": "Envía un correo con dos líneas diciendo que la contabilidad se encuentra al día.",
                    "B": "Estructura el informe consolidando el estado del cierre en Cata Suite, resumen de retenciones enteradas (ISLR/SAMAT), estatus de conciliaciones bancarias y libros impresos.",
                    "C": "Copia el informe del mes anterior modificando solo la fecha para salir del paso.",
                    "D": "Manifiesta que los informes periódicos son innecesarios porque los números están en el sistema."
                }
            },
            13: {
                "enunciado": "Al auditar las facturas de compras de bienes y servicios recibidos, detecta que un proveedor incluyó gastos personales que no corresponden a la actividad económica de la compañía:",
                "opciones": {
                    "A": "Separa la factura, notifica a la administración sobre la no deducibilidad del gasto y evita registrarlo en el crédito fiscal del Libro de Compras para no violar la ley de IVA.",
                    "B": "Registra el gasto personal en el Libro de Compras para reducir el pago de IVA de la empresa.",
                    "C": "Paga la factura con dinero en efectivo de la caja chica sin asentar el egreso.",
                    "D": "Altera el concepto de la factura digitalmente para simular que es materia prima."
                }
            },
            14: {
                "enunciado": "En su relación con jefaturas de administración y contadores públicos en empleos previos:",
                "opciones": {
                    "A": "He tenido discrepancias técnicas sobre la provisión de gastos fijos con auditores, resolviéndolas mediante la revisión de normas contables y acatando la directriz superior.",
                    "B": "Los contadores externos siempre complican el trabajo sencillo de la oficina.",
                    "C": "No tolero que supervisen mis archivos porque mi sistema de archivo es perfecto.",
                    "D": "En todas las empresas donde he laborado he tenido gerentes administrativos absolutamente perfectos y libres de fallas."
                }
            },
            15: {
                "enunciado": "Durante la impresión de los reportes de inventario y cuentas por cobrar generados en Cata Suite al cierre de mes, la impresora se queda sin tóner a mitad del proceso:",
                "opciones": {
                    "A": "Deja la impresión incompleta y descarta el resguardo de los reportes del cierre de mes.",
                    "B": "Guarda los archivos en formato digital seguro (Adobe PDF), gestiona el reemplazo del tóner con suministros y culmina la impresión física para el archivo correspondiente.",
                    "C": "Borra los reportes del sistema para no tener que imprimirlos.",
                    "D": "Se retira de la oficina argumentando que sin impresora no se puede hacer nada administrativo."
                }
            },
            16: {
                "enunciado": "Un compañero de trabajo le pide que le filtre información confidencial sobre los honorarios profesionales y sueldos reflejados en las planillas de retención de ISLR:",
                "opciones": {
                    "A": "Le muestra las planillas y le permite fotocopiar los sueldos de sus compañeros.",
                    "B": "Vende la información de las retenciones a cambio de un almuerzo o dinero en efectivo.",
                    "C": "Publica los montos de honorarios profesionales en una cartelera para que todos los vean.",
                    "D": "Rechaza la solicitud con firmeza, recordando que la información tributaria y de remuneraciones es estrictamente confidencial bajo reserva profesional."
                }
            },
            17: {
                "enunciado": "Al cotejar el Libro de Ventas, nota que una factura emitida hace dos meses fue anulada administrativamente en el software pero no se emitió la correspondiente Nota de Crédito fiscal:",
                "opciones": {
                    "A": "Tramita la regularización técnica: solicita la emisión formal de la Nota de Crédito fiscal conforme a la providencia tributaria y realiza el ajuste en el período correspondiente.",
                    "B": "Borra la factura del libro de ventas histórico para que nadie se dé cuenta de la anulación.",
                    "C": "Deja el libro con el descuadre permanente argumentando que los meses viejos ya no importan.",
                    "D": "Modifica el número de control de otra factura para tapar el hueco fiscal."
                }
            },
            18: {
                "enunciado": "Se produce una falla en el servidor central que impide el acceso a Cata Suite el día que vence el plazo de pago del impuesto municipal (SAMAT):",
                "opciones": {
                    "A": "Deja vencer el plazo y asume que la empresa pague las multas e intereses moratorios.",
                    "B": "Utiliza los papeles de trabajo preliminares y reportes respaldados previamente en Adobe PDF, concilia las bases imponibles y gestiona el pago oportuno ante el ente tributario.",
                    "C": "Paga un soborno a los inspectores de la Alcaldía para que no revisen la fecha de pago.",
                    "D": "Desconecta los equipos de la oficina y se marcha a su casa antes del mediodía."
                }
            },
            19: {
                "enunciado": "Sobre la honradez y el resguardo de cheques o dinero en efectivo en el área administrativa:",
                "opciones": {
                    "A": "Si veo billetes o cheques sobre un escritorio en administración, me los guardo temporalmente.",
                    "B": "Jamás en toda mi vida he sentido la mínima curiosidad por mirar un extracto bancario ajeno ni tocar dinero que no me pertenezca.",
                    "C": "Custodio con absoluta integridad y pulcritud los valores, comprobantes de pago y fondos asignados, reportando cualquier anomalía de inmediato.",
                    "D": "Utilizo los fondos de retenciones tributarias para pagar gastos personales y los repongo después."
                }
            },
            20: {
                "enunciado": "Al revisar los soportes contables del mes para su archivo definitivo, observa que las carpetas de compras están desordenadas y sin separación cronológica:",
                "opciones": {
                    "A": "Guarda los papeles amontonados en una caja sin clasificar para terminar rápido.",
                    "B": "Bota las facturas más viejas para que la carpeta cierre fácilmente.",
                    "C": "Organiza minuciosamente los documentos en estricto orden cronológico por fecha de emisión, anexa sus comprobantes de retención de IVA e ISLR y rotula el archivador según manual.",
                    "D": "Le exige al personal de mantenimiento que ellos clasifiquen los comprobantes contables."
                }
            },
            21: {
                "enunciado": "Al momento de generar la provisión contable por obsolescencia de inventario en Cata Suite, el sistema arroja productos vencidos que no han sido dados de baja físicamente:",
                "opciones": {
                    "A": "Modifica las fechas de vencimiento de los productos en el sistema para que no generen provisión.",
                    "B": "Oculta el reporte de inventario a la gerencia para que no se note la pérdida.",
                    "C": "Anula el inventario completo en el sistema sin contar con autorización de la Dirección.",
                    "D": "Elabora el papel de trabajo reflejando la provisión real soportada en el reporte del sistema, y emite la alerta a la Gerencia Administrativa y Almacén para su disposición formal."
                }
            },
            22: {
                "enunciado": "El contador externo le indica que hay una diferencia de $50 entre la conciliación bancaria de una cuenta corriente y el saldo reflejado en el balance general de Cata Suite:",
                "opciones": {
                    "A": "Ajusta la diferencia mediante un asiento contable ficticio bajo el concepto de 'Gastos Varios'.",
                    "B": "Revisa transacción por transacción (cheques no cobrados, débitos por comisiones bancarias o transferencias en tránsito) hasta ubicar el origen exacto y asienta el ajuste documentado.",
                    "C": "Borra la cuenta bancaria del balance general para eliminar la diferencia que incomoda.",
                    "D": "Se niega a revisar el balance argumentando que $50 no afectan a una empresa grande."
                }
            },
            23: {
                "enunciado": "Al recibir los comprobantes de retención de ISLR emitidos por clientes especiales, nota que varios de ellos presentan números de RIF equivocados o montos que no coinciden con las facturas:",
                "opciones": {
                    "A": "Gestiona de inmediato ante los clientes la refacturación o emisión corregida de los comprobantes de retención, protegiendo el crédito fiscal deducible de la empresa.",
                    "B": "Modifica los comprobantes de retención de los clientes con un editor de imágenes digital.",
                    "C": "Da por perdidas las retenciones y las asume como gasto de la compañía sin reclamar.",
                    "D": "Insulta a los clientes por teléfono amenazándolos con no volver a venderles productos."
                }
            },
            24: {
                "enunciado": "Sobre el autocontrol emocional ante cierres de mes congestionados y plazos tributarios:",
                "opciones": {
                    "A": "Si la gerencia me pide un papel de trabajo a última hora, golpeo el teclado y me pongo a gritar.",
                    "B": "He tenido jornadas de alta presión por coincidencia de impuestos y cierres contables, pero organizo las prioridades con método, tranquilidad y rigor profesional.",
                    "C": "Poseo una templanza celestial inalterable; absolutamente ningún descuadre numérico ni exigencia de auditoría me ha causado la más mínima molestia jamás.",
                    "D": "Cuando me saturo de comprobantes, apago el computador y me retiro a descansar sin avisar."
                }
            },
            25: {
                "enunciado": "Un proveedor le solicita que le entregue el pago de su factura sin practicarle la retención de ISLR legal correspondiente, prometiendo asumir la responsabilidad por escrito:",
                "opciones": {
                    "A": "Acepta no practicar la retención de ISLR para quedar bien con el proveedor.",
                    "B": "Le cobra una comisión personal en efectivo al proveedor para eximirlo de la retención fiscal.",
                    "C": "Destruye la orden de retención y le paga el monto bruto completo sin consultar a nadie.",
                    "D": "Rechaza la solicitud con firmeza, explica la obligatoriedad legal de la empresa como agente de retención y aplica la deducción tributaria con su respectivo comprobante."
                }
            },
            26: {
                "enunciado": "Durante los primeros ocho días del mes, se deben imprimir los libros contables (Diario, Mayor e Inventario) pero el analista anterior dejó pendientes los del mes antepasado:",
                "opciones": {
                    "A": "Imprime únicamente el mes actual y deja el mes antepasado en blanco de forma permanente.",
                    "B": "Regulariza la secuencia: audita que los cierres de los meses pendientes estén saneados, imprime en orden cronológico correlativo los libros rezagados y completa los del mes vigente.",
                    "C": "Bota las hojas de los libros contables viejos para que nadie descubra el atraso.",
                    "D": "Modifica la numeración de los folios a mano con corrector líquido para saltarse los meses."
                }
            },
            27: {
                "enunciado": "Se requiere extender la jornada de trabajo 45 minutos para culminar la carga de la declaración del SAMAT en el portal tributario municipal antes del cierre de sistema a las 7:00 p.m.:",
                "opciones": {
                    "A": "Se marcha a las 6:00 p.m. puntual dejando la declaración sin procesar y exponiendo a la empresa a multas.",
                    "B": "Asume la extensión con compromiso institucional, culmina la transmisión de datos, descarga el certificado de declaración y comprobante de pago, y deja el legajo cerrado.",
                    "C": "Envía una declaración en cero de forma fraudulenta para salir rápido de la oficina.",
                    "D": "Se queja a gritos con los compañeros asegurando que la empresa abusa del personal administrativo."
                }
            },
            28: {
                "enunciado": "Al archivar los soportes contables del mes recién procesado, nota que la gaveta del archivador de metal no tiene llave y queda en un pasillo de acceso común:",
                "opciones": {
                    "A": "Traslada los legajos fiscales y soportes originales a un área de archivo seguro bajo llave, y reporta la anomalía a la administración para el reemplazo inmediato de la cerradura.",
                    "B": "Deja las carpetas contables abiertas en el pasillo sin importar que cualquiera pueda sustraerlas.",
                    "C": "Se lleva las carpetas con facturas originales a su casa particular para guardarlas.",
                    "D": "Bota los soportes contables del mes argumentando que ya están registrados en el sistema."
                }
            },
            29: {
                "enunciado": "En su relación con otros profesionales del área administrativa y aspiraciones laborales:",
                "opciones": {
                    "A": "Jamás en toda mi vida profesional he sentido la mínima envidia, molestia o recelo cuando felicitan o promueven a otro analista del departamento.",
                    "B": "A veces he sentido sana emulación o deseo de asumir cargos de mayor responsabilidad gerencial, pero me concentro en que mis cierres y libros fiscales sean impecables.",
                    "C": "Pienso que cuando felicitan a un asistente contable es únicamente por compadrazgo con la gerencia.",
                    "D": "No me gusta colaborar con los compañeros de administración porque todos buscan el beneficio propio."
                }
            },
            30: {
                "enunciado": "Presidencia le encomienda realizar una revisión confidencial sobre los soportes de gastos de representación de los últimos tres meses de una gerencia operativa:",
                "opciones": {
                    "A": "Comenta la asignación con los demás colaboradores durante el receso del mediodía.",
                    "B": "Se niega a realizar la revisión argumentando que no le gusta auditar a compañeros de trabajo.",
                    "C": "Ejecuta la revisión con absoluto sigilo profesional: coteja facturas originales vs. reportes en Cata Suite, verifica validez fiscal (RIF/control) y entrega el informe reservado a Presidencia.",
                    "D": "Altera los montos en los papeles de trabajo para encubrir gastos no justificados de personas conocidas."
                }
            }
        }
    },
    # =========================================================================
    # 13. AYUDANTE ALMACÉN Y DESPACHO (CJS-AYAD)
    # =========================================================================
    "13_AYUDANTE_ALMACEN_Y_DESPACHO": {
        "codigo": "CJS-AYAD",
        "titulo": "EVALUACIÓN PSICOTÉCNICA SITUACIONAL EN ALMACÉN Y DESPACHO POLIVALENTE",
        "instrucciones": "Lea con atención cada situación laboral tanto en el depósito como en el camión de reparto. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con honestidad sobre su forma real de actuar en carga, descarga, trato al cliente y cuidado de mercancía. Dispone de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "A mitad de mañana el Jefe de Almacén le indica que debe subirse al camión de despacho para apoyar una ruta foránea pesada porque un despachador se reportó indispuesto:",
                "opciones": {
                    "A": "Se niega rotundamente diciendo que a él solo lo contrataron para estar dentro del almacén.",
                    "B": "Acepta salir pero se queda sentado en la cabina del camión sin ayudar a bajar mercancía.",
                    "C": "Discute con el supervisor diciendo que salir a la calle es peligroso y que no le corresponde.",
                    "D": "Asume la asignación con disposición y polivalencia, verifica la guía de despacho junto al chofer, aborda la unidad y apoya activamente en la entrega de pedidos a los clientes."
                }
            },
            2: {
                "enunciado": "Durante el armado de pedidos (picking) en el almacén, la orden exige 30 cajas de galletas, pero en la paleta abierta hay un lote que vence en 40 días y al fondo uno que vence en 8 meses:",
                "opciones": {
                    "A": "Agarra las cajas que vencen en 8 meses porque están más accesibles y no pesan tanto.",
                    "B": "Aplica el método de rotación FIFO/FIFE: extrae y monta prioritariamente el lote que vence en 40 días, asegurando la rotación correcta de inventario para evitar mermas.",
                    "C": "Mezcla las cajas sin mirar las fechas de vencimiento para desocuparse rápido de la estiba.",
                    "D": "Oculta el lote que vence en 40 días detrás de unas tarimas vacías para no tener que cargarlo."
                }
            },
            3: {
                "enunciado": "Al entregar un pedido de 20 bultos en un supermercado de la ruta, el comerciante nota que 2 empaques están rasgados y derraman producto por mala manipulación durante el viaje:",
                "opciones": {
                    "A": "Notifica la no conformidad al chofer, anota el rechazo de los 2 bultos en la guía/factura con firma del cliente, resguarda el producto dañado en el camión y entrega el resto conforme.",
                    "B": "Insulta al comerciante exigiéndole que reciba las cajas rotas porque él no piensa cargarlas de vuelta.",
                    "C": "Bota los 2 bultos rasgados en una alcantarilla cercana para no tener que reportar la merma.",
                    "D": "Le cobra el dinero completo al cliente amenazándolo con no volver a despacharle a su negocio."
                }
            },
            4: {
                "enunciado": "En su rutina de trabajo físico, esfuerzo muscular y jornadas en calle:",
                "opciones": {
                    "A": "Si el camión no tiene aire acondicionado, me bajo en la primera esquina y me voy a mi casa.",
                    "B": "En ocasiones he sentido calor o cansancio físico en jornadas pesadas de carga y reparto, pero mantengo la energía, la actitud positiva y el cuidado de los productos.",
                    "C": "Jamás en toda mi vida he sentido la mínima fatiga, sed ni pesadez levantando sacos pesados.",
                    "D": "Prefiero trabajar sin botas de seguridad ni guantes porque me quitan rapidez al caminar."
                }
            },
            5: {
                "enunciado": "Al descargar una gandola de flota primaria en el andén de almacén, nota que una paleta de mayonesa viene desarmada y con bultos inclinados con riesgo de aplastamiento:",
                "opciones": {
                    "A": "Tira de los bultos de abajo bruscamente para que la paleta se caiga sola al piso.",
                    "B": "Se desentiende de la descarga y deja que los choferes foráneos resuelvan el problema.",
                    "C": "Pasa por el lado sin avisar esperando a ver a quién se le cae la mercancía encima.",
                    "D": "Detiene la descarga, señaliza el área de riesgo, desestiba manualmente desde arriba con cuidado y rearmar la carga sobre una paleta en buen estado antes de ingresarla al depósito."
                }
            },
            6: {
                "enunciado": "Al llegar a entregar en un negocio cerrado temporalmente por la hora del almuerzo, el chofer propone dejar los 15 bultos tirados en la acera frente al local:",
                "opciones": {
                    "A": "Acepta dejar la mercancía en la acera para terminar la ruta más rápido e irse a descansar.",
                    "B": "Le propone al chofer repartirse los 15 bultos entre los dos argumentando que el cliente no estaba.",
                    "C": "Recuerda que no se entrega carga sin acuse de recibo formal; resguarda el pedido en el camión, notifica a Logística y reprograma la entrega al terminar el resto del circuito.",
                    "D": "Rompe la factura del cliente y bota los papeles a la papelera del camión."
                }
            },
            7: {
                "enunciado": "Al finalizar la jornada de reparto en la tarde, el camión retorna a la sede con cartón de retorno, cajas vacías y 3 bultos de mercancía devuelta por clientes:",
                "opciones": {
                    "A": "Descarga el cartón en el área de reciclaje, entrega los bultos devueltos al Jefe de Almacén para su chequeo y reingreso, y coopera en el barrido e higiene del furgón del camión.",
                    "B": "Se baja del camión y se marcha de inmediato a su casa dejando el vehículo sucio y con carga adentro.",
                    "C": "Quema el cartón de retorno en el estacionamiento de la empresa para no tener que apilarlo.",
                    "D": "Deja la mercancía devuelta guardada en la cabina del camión durante todo el fin de semana."
                }
            },
            8: {
                "enunciado": "Son las 4:50 p.m. (su hora de salida habitual es a las 5:00 p.m.) y en el almacén se debe culminar la carga de un camión que sale a las 5:00 a.m. a una ruta lejana:",
                "opciones": {
                    "A": "Asume la extensión con compromiso y espíritu de equipo, apoya en el montaje y zunchado de la carga y asegura que el vehículo quede listo para la salida matutina.",
                    "B": "Suelta las cajas en medio del andén y se marcha a las 5:00 p.m. exacta sin importar que el camión quede a medias.",
                    "C": "Tira los bultos al camión con violencia para desquitarse por tener que trabajar a última hora.",
                    "D": "Se esconde detrás de las estibas del fondo para evitar que el despachador le pida ayuda."
                }
            },
            9: {
                "enunciado": "Respecto a la precisión y atención al detalle al cotejar productos contra facturas o guías:",
                "opciones": {
                    "A": "Jamás en ninguno de mis empleos anteriores he confundido un código de producto ni he contado mal un bulto en toda mi vida.",
                    "B": "Considero que leer las guías de despacho no hace falta porque los choferes se saben todo de memoria.",
                    "C": "Verifico con atención la descripción del producto, sabor, presentación y cantidad física antes de bajar la mercancía en el negocio del cliente.",
                    "D": "Si entrego un producto equivocado en la ruta, prefiero culpar al encargado del almacén que lo cargó."
                }
            },
            10: {
                "enunciado": "Un comerciante en la ruta le ofrece al ayudante regalarle $10 en efectivo si le baja una caja de atún adicional que supuestamente 'sobró en el conteo del camión':",
                "opciones": {
                    "A": "Acepta los $10 y le entrega la caja de atún al comerciante a espaldas del chofer.",
                    "B": "Le pide al comerciante $20 para entregarle dos cajas en lugar de una.",
                    "C": "Toma la caja y se la lleva a su casa escondida en su bolso personal.",
                    "D": "Rechaza el ofrecimiento de inmediato, explica que toda la carga está auditada bajo guía de despacho y reporta la irregularidad al chofer y a la administración."
                }
            },
            11: {
                "enunciado": "Al mover cajas pesadas de detergente o granos (25 kg) desde el camión hacia el depósito del cliente:",
                "opciones": {
                    "A": "Dobla la cintura con las piernas totalmente rectas levantando todo el peso con la columna.",
                    "B": "Lanza los sacos desde el camión hacia el piso de la acera arriesgando a romper el producto.",
                    "C": "Flexiona las rodillas manteniendo la espalda recta, pega la carga al cuerpo y empuja con la fuerza de las piernas utilizando carretilla si el recorrido es largo.",
                    "D": "Carga tres sacos juntos en el hombro tambaleándose y tropezando con los compradores."
                }
            },
            12: {
                "enunciado": "Al organizar las estibas en el almacén o dentro del furgón del camión, se deben ubicar productos pesados (sacos/granos) y productos frágiles (galletas/pastas):",
                "opciones": {
                    "A": "Coloca las cajas de galletas en la base y monta los sacos de 25 kg encima para apretar la carga.",
                    "B": "Estiba los productos pesados en la base de forma trabada y coloca los productos frágiles en los niveles superiores para evitar aplastamientos y mermas.",
                    "C": "Mezcla productos químicos de limpieza sobre fardos de arroz sin ninguna barrera de separación.",
                    "D": "Amontona las cajas de forma desordenada sin respetar los límites de altura de la batea."
                }
            },
            13: {
                "enunciado": "Durante la descarga manual en un cliente, tropieza con una banqueta en la entrada del local y se rompe una caja de salsa de tomate:",
                "opciones": {
                    "A": "Asume la situación con honestidad, limpia el área con apoyo del chofer para evitar caídas a los clientes del local, entrega el producto averiado para su registro y notifica al supervisor.",
                    "B": "Esconde los frascos rotos debajo del mostrador del cliente y sale corriendo hacia el camión.",
                    "C": "Le echa la culpa al comerciante acusándolo de haberle puesto una trampa para que se cayera.",
                    "D": "Le exige al comerciante que pague la caja rota amenazándolo con no despacharle más."
                }
            },
            14: {
                "enunciado": "En su relación con los choferes de despacho y jefes de almacén:",
                "opciones": {
                    "A": "He tenido discrepancias sobre cómo acomodar una ruta con compañeros de cuadrilla, pero dialogué con educación y acaté la instrucción operativa final.",
                    "B": "Los choferes de reparto siempre se quedan sentados al volante y le dejan toda la carga pesada al ayudante.",
                    "C": "No tolero que ningún chofer me diga cómo bajar las cajas porque yo sé hacer mi trabajo solo.",
                    "D": "En todas las empresas donde he laborado he tenido choferes y jefes absolutamente perfectos con los que jamás tuve el menor desacuerdo."
                }
            },
            15: {
                "enunciado": "Al momento de preparar un pedido en el almacén, nota que una caja de leche tiene el empaque abollado y manchado de humedad:",
                "opciones": {
                    "A": "La mete en medio de la paleta para que el cliente que la reciba en la calle no se dé cuenta.",
                    "B": "Se toma la leche en el pasillo con sus compañeros argumentando que ya está dañada.",
                    "C": "Separa el bulto, lo traslada al área de no conformes/averías y lo reemplaza por una unidad en perfecto estado para garantizar la calidad prometida al cliente.",
                    "D": "Bota la caja completa al basurero sin reportar para evitar llenar papeles de merma."
                }
            },
            16: {
                "enunciado": "Durante el trayecto de reparto, el chofer se detiene en un taller clandestino y le pide que le ayude a bajar 2 paletas de madera del camión para venderlas:",
                "opciones": {
                    "A": "Le ayuda a bajar las paletas y acepta una parte del dinero de la venta.",
                    "B": "Le propone vender también la carretilla de carga del camión para ganar más dinero.",
                    "C": "Se queda callado y finge que no vio nada cuando regresen a la sede principal.",
                    "D": "Se niega a participar en la maniobra, recuerda que las paletas son activos de la empresa y notifica el hecho a la Coordinación de Logística y Seguridad."
                }
            },
            17: {
                "enunciado": "Al terminar de descargar un camión foráneo en el almacén, quedan regados en el andén clavos oxidados, restos de madera de paletas y plástico elástico:",
                "opciones": {
                    "A": "Recoge de inmediato las maderas y clavos, barre el andén, deposita la basura en su contenedor y deja el área despejada y segura para el tránsito de personal y carretillas.",
                    "B": "Deja los clavos tirados en el piso diciendo que recoger basura es labor del personal de limpieza.",
                    "C": "Patea los restos de madera debajo de los camiones para no tener que barrer.",
                    "D": "Se sienta sobre los desperdicios a descansar sin importarle la seguridad de los compañeros."
                }
            },
            18: {
                "enunciado": "En una parada de la ruta comercial, un comerciante recibe su mercancía pero afirma que 'no va a firmar la factura ni a sellar porque el dueño del local salió':",
                "opciones": {
                    "A": "Le entrega la mercancía de todos modos sin documento firmado confiando en que el dueño pagará después.",
                    "B": "Explica con respeto que por política de despacho no puede soltar carga sin firma, cédula legible y acuse de recibo, y coordina con el chofer y el vendedor antes de descargar.",
                    "C": "Falsifica la firma del comerciante en la copia de la factura de la empresa.",
                    "D": "Descarga la mercancía en la acera y se marcha sin exigir ningún comprobante."
                }
            },
            19: {
                "enunciado": "Sobre la honestidad y el consumo de productos dentro del camión o almacén:",
                "opciones": {
                    "A": "Si en el camión se abre un paquete de galletas por un bache en la carretera, me las como sin avisar.",
                    "B": "Jamás en toda mi vida he sentido la tentación de probar un producto ni tomar un centavo ajeno sin permiso.",
                    "C": "Resguardo con integridad cada producto transportado o almacenado, reportando cualquier merma formalmente y entendiendo que la mercancía es propiedad del cliente y la empresa.",
                    "D": "Me llevo envases vacíos y cintas de embalar a mi casa argumentando que a la empresa le sobran."
                }
            },
            20: {
                "enunciado": "Al realizar el inventario físico diario en el almacén, el ayudante detecta que en una estiba faltan 4 fardos de arroz respecto al conteo de la mañana:",
                "opciones": {
                    "A": "Modifica los números en la planilla para tapar el faltante y evitar que regañen a la cuadrilla.",
                    "B": "Dice que las 4 cajas se las comieron los ratones para no tener que buscar en las otras estibas.",
                    "C": "Reporta la diferencia de inmediato al Jefe de Almacén, revisa las órdenes de despacho despachadas durante el turno y colabora en la aclaración del saldo físico vs. teórico.",
                    "D": "Acusa a los clientes que visitaron la empresa de haber sustraído los fardos sin pruebas."
                }
            },
            21: {
                "enunciado": "Al momento de embalar e identificar una paleta armada para despacho al día siguiente:",
                "opciones": {
                    "A": "Deja la paleta sin zunchar ni envolver para que los choferes la amarren como puedan.",
                    "B": "Amarra las cajas con mecates viejos que cortan y dañan los empaques de cartón.",
                    "C": "Pega una hoja ilegible escrita con lápiz que se borra con el roce de los camiones.",
                    "D": "Envuelve la carga firmemente con plástico elástico (envoplast) trabándolo a la base de madera, coloca la tarjeta de identificación de ruta y la ubica en la zona de despacho."
                }
            },
            22: {
                "enunciado": "Al llegar a entregar en un cliente ubicado en una calle con fuerte pendiente y lluvia, el camión debe estacionarse y la rampa de descarga está resbalosa:",
                "opciones": {
                    "A": "Se tira del camión corriendo con dos cajas pesadas para terminar rápido antes de mojarse.",
                    "B": "Verifica que las ruedas del camión tengan los tacos de seguridad (cuñas), usa calzado antiresbalante, baja la carga con precaución y transita con paso firme evitando resbalones.",
                    "C": "Se niega a bajar del camión y le dice al chofer que cancele la entrega del cliente por lluvia.",
                    "D": "Empuja las cajas desde arriba del camión hacia la acera para que caigan solas."
                }
            },
            23: {
                "enunciado": "Al finalizar el recorrido de despacho en la tarde, se debe colaborar en la limpieza e inspección básica del vehículo de reparto:",
                "opciones": {
                    "A": "Barre la plataforma de carga, recoge zunchos y papeles, retira los residuos de la cabina y reporta al chofer cualquier daño visible en la carrocería o compuertas.",
                    "B": "Deja la batea llena de basura y cáscaras de comida diciendo que limpiar el camión le toca al chofer.",
                    "C": "Bota la basura acumulada del camión en la puerta del almacén al llegar a la empresa.",
                    "D": "Se niega a revisar el vehículo argumentando que los ayudantes solo cargan bultos."
                }
            },
            24: {
                "enunciado": "Sobre el control emocional y el trato con comerciantes exigentes o de mal humor en la calle:",
                "opciones": {
                    "A": "Si un comerciante me apura de mala manera para que baje la carga rápido, le lanzo las cajas a los pies.",
                    "B": "He enfrentado clientes impacientes o con mal carácter en la ruta, pero mantengo la serenidad, la educación y realizo la entrega con profesionalismo y rapidez.",
                    "C": "Poseo una paz interior inalterable; absolutamente ningún maltrato verbal ni discusión me ha provocado la más mínima molestia jamás.",
                    "D": "Cuando un cliente me cae mal, le escondo las facturas para que no le bajen su pedido."
                }
            },
            25: {
                "enunciado": "Un chofer de reparto le propone al ayudante no entregar 2 bultos de un cliente mayorista asegurando que 'el cliente no los va a contar porque compra demasiado':",
                "opciones": {
                    "A": "Acepta la propuesta del chofer y se reparte la mercancía con él al terminar la ruta.",
                    "B": "Le pide al chofer que no sean 2 bultos sino 5 para que valga la pena el riesgo.",
                    "C": "Acepta pero le exige al chofer que le pague su parte en dólares en efectivo de inmediato.",
                    "D": "Rechaza la propuesta de forma categórica, reafirma que se debe entregar el 100% de la factura y notifica el incidente de inmediato a la Gerencia de Operaciones."
                }
            },
            26: {
                "enunciado": "Durante el trabajo de estiba en el almacén, nota que una paleta de madera tiene dos tablas rajadas y un clavo salido en la base:",
                "opciones": {
                    "A": "Monta 1.000 kg de producto sobre esa paleta dañada para salir rápido del paso.",
                    "B": "Descarta la paleta rota, la retira del área operativa para su reparación y traslada la carga a una paleta certificada en óptimas condiciones de soporte.",
                    "C": "Tapa la tabla rajada pegándole cartón encima para que no se note a simple vista.",
                    "D": "Deja la paleta dañada en el pasillo principal donde pasan las transpaletas y peatones."
                }
            },
            27: {
                "enunciado": "Se requiere apoyar a la cuadrilla de almacén en una jornada de inventario general de fin de mes que se extenderá dos horas después del horario habitual:",
                "opciones": {
                    "A": "Se niega a quedarse argumentando que a las 5:00 p.m. él suelta todo y se marcha.",
                    "B": "Asume la extensión con sentido de compromiso y colaboración, realiza los conteos físicos con rigor y apoya hasta culminar el cuadre del almacén.",
                    "C": "Se queda en el almacén pero se sienta a mirar el teléfono sin contar ninguna estiba.",
                    "D": "Se queja a gritos con sus compañeros asegurando que la empresa abusa del personal."
                }
            },
            28: {
                "enunciado": "Al descargar pedidos en un cliente mayorista, nota que el piso de la bodega del cliente está lleno de aceite derramado:",
                "opciones": {
                    "A": "Descarga los sacos de harina directamente sobre el charco de aceite manchando el producto.",
                    "B": "Solicita amablemente al cliente cartones limpios o una paleta plástica para aislar el piso, y asienta la mercancía en un área seca y limpia garantizando la calidad de entrega.",
                    "C": "Tira los bultos con fuerza para que se rompan sobre el aceite y culpar al cliente.",
                    "D": "Deja la mercancía abandonada en la calle a 20 metros del negocio del cliente."
                }
            },
            29: {
                "enunciado": "En su relación con otros ayudantes de la empresa y reconocimientos laborales:",
                "opciones": {
                    "A": "Jamás en toda mi vida he sentido la mínima envidia, recelo o molestia cuando felicitan a otro ayudante por su rendimiento y fuerza física.",
                    "B": "A veces he sentido sana emulación o deseo de destacar como el ayudante más productivo, pero me concentro en cargar con técnica, cuidar los productos y ser puntual.",
                    "C": "Pienso que cuando felicitan a un ayudante en la empresa es únicamente porque es compadre de los supervisores.",
                    "D": "Prefiero no enseñarle nada a los ayudantes nuevos porque cada quien debe resolver sus problemas solo."
                }
            },
            30: {
                "enunciado": "La Dirección le encomienda realizar un reconteo confidencial y discreto en una ruta de despacho ante sospechas de faltantes continuos en las entregas:",
                "opciones": {
                    "A": "Le avisa al chofer y a los clientes de la ruta sobre la revisión para alertarlos.",
                    "B": "Se niega a colaborar diciendo que a él no le pagan para vigilar a sus compañeros de trabajo.",
                    "C": "Ejecuta la verificación física bulto a bulto con estricta reserva y rigor, coteja contra las guías de carga y entrega el reporte privado a la Dirección.",
                    "D": "Modifica el reporte para encubrir al chofer si es su amigo personal de trabajo."
                }
            }
        }
    },
    # =========================================================================
    # 15. CONTADOR (CJS-CPUB)
    # =========================================================================
    "15_CONTADOR": {
        "codigo": "CJS-CPUB",
        "titulo": "EVALUACIÓN PSICOTÉCNICA SITUACIONAL EN CONTADURÍA PÚBLICA Y GESTIÓN FISCAL",
        "instrucciones": "Lea detenidamente cada situación financiera, técnica y legal. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con apego a las normas contables (VEN-NIF), ética profesional y leyes tributarias. Dispone de un tiempo máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "Al preparar el balance de ganancias y pérdidas para el cierre de ejercicio, la Dirección le sugiere diferir el registro de facturas de gastos reales para mostrar utilidades artificiales y facilitar un préstamo bancario:",
                "opciones": {
                    "A": "Acepta ocultar los gastos para favorecer la aprobación del crédito bancario de la empresa.",
                    "B": "Borra las facturas del sistema contable para que los auditores no encuentren inconsistencias.",
                    "C": "Cobra un porcentaje del préstamo como honorario profesional por acomodar el balance.",
                    "D": "Rechaza la propuesta con fundamento en el principio de devengo y la fe pública del contador, presentando estados financieros fidedignos que reflejen la realidad operativa de la institución."
                }
            },
            2: {
                "enunciado": "Al revisar y clasificar los documentos del mes, detecta varios cheques emitidos a proveedores que fueron devueltos o anulados por defectos de forma y no tienen el chequeo histórico correspondiente:",
                "opciones": {
                    "A": "Bota los cheques nulos a la basura para que no ocupen espacio físico en las carpetas.",
                    "B": "Examina los documentos, realiza la recapitulación histórica de las personas jurídicas afectadas, efectúa el reverso contable correspondiente y actualiza el control de cuentas por pagar.",
                    "C": "Registra los cheques como pagados en efectivo para que el libro de banco no tenga partidas abiertas.",
                    "D": "Le cobra una penalización personal en efectivo al proveedor por haber emitido un cheque con fallas."
                }
            },
            3: {
                "enunciado": "Al cotejar la nómina de pagos contra los asientos contables y la información de retenciones otorgada a Talento Humano, detecta un descuadre en las retenciones de ISLR y deducciones parafiscales:",
                "opciones": {
                    "A": "Ajusta de inmediato los asientos en el comprobante de diario, concilia las retenciones reales con Talento Humano y garantiza que los montos declarados coincidan con el libro mayor.",
                    "B": "Ignora la discrepancia y declara ante el fisco montos estimados sin revisar las nóminas.",
                    "C": "Modifica los sueldos en el sistema contable para forzar el cuadre sin avisar a nadie.",
                    "D": "Traslada el faltante contable a una cuenta de gastos varios no deducibles."
                }
            },
            4: {
                "enunciado": "En su trayectoria profesional y desempeño bajo la presión de cierres fiscales:",
                "opciones": {
                    "A": "Si la plataforma tributaria se satura a medianoche, cierro el portal y dejo que la empresa sea multada.",
                    "B": "En ocasiones he sentido tensión y cansancio mental ante plazos perentorios de declaración o auditorías imprevistas, pero mantengo la serenidad, la concentración y el rigor técnico.",
                    "C": "Jamás en toda mi vida profesional he sentido la menor fatiga, duda ni preocupación ante un cierre de ejercicio o auditoría externa.",
                    "D": "Prefiero delegar la revisión de libros contables sin inspeccionar para no agotarme la vista."
                }
            },
            5: {
                "enunciado": "Durante la auditoría interna del área de tesorería, nota que los ingresos bancarios por concepto de cobranzas que entran por caja no coinciden con los comprobantes de ingreso procesados:",
                "opciones": {
                    "A": "Asienta una pérdida extraordinaria de capital sin investigar el origen del descuadre.",
                    "B": "Permite que el cajero cuadre la diferencia colocando dinero en efectivo de su propio bolsillo.",
                    "C": "Oculta el descuadre bancario a la Junta Directiva para no perjudicar al personal de caja.",
                    "D": "Audita minuciosamente las boletas de depósito, recibos y movimientos en el programa de contabilidad, aísla la inconsistencia y presenta el informe de auditoría a la Gerencia."
                }
            },
            6: {
                "enunciado": "Al realizar el análisis de contabilidad de costes de una línea de productos, observa que los costos indirectos de fabricación no se están asignando bajo una base de distribución técnica:",
                "opciones": {
                    "A": "Asigna los costos al azar al producto más vendido para salir del paso rápidamente.",
                    "B": "Elimina el módulo de costos del sistema administrativo argumentando que no aporta valor.",
                    "C": "Desarrolla la estructura técnica de costos, codifica las cuentas según los lineamientos de la organización y genera los cuadros analíticos para la correcta fijación de precios y márgenes.",
                    "D": "Le dice a la gerencia que los costos de producción deben calcularse al ojo por ciento."
                }
            },
            7: {
                "enunciado": "Al contrastar los códigos de las cuentas contables con los asignados por la Unidad de Presupuesto, detecta que varias partidas de gastos fijos están imputadas en cuentas de inversión de capital:",
                "opciones": {
                    "A": "Corrige los registros contables mediante comprobante de ajuste, reclasifica las partidas según el catálogo oficial y homologa los códigos con la Unidad de Presupuesto.",
                    "B": "Deja las cuentas mal imputadas para que el presupuesto de gastos parezca que no se ha agotado.",
                    "C": "Borra las cuentas del catálogo del programa de contabilidad para que no se puedan comparar.",
                    "D": "Insulta al personal de presupuesto acusándolos de incapacidad técnica delante de los directivos."
                }
            },
            8: {
                "enunciado": "Son las 4:50 p.m. (su horario habitual es hasta las 5:00 p.m.) del día límite para enterar las retenciones de impuesto ante el portal de la Administración Tributaria y el sistema presenta lentitud:",
                "opciones": {
                    "A": "Asume la extensión horaria con responsabilidad profesional, persiste en el portal hasta completar el formulario gubernamental, descarga el certificado de pago y actualiza la cartelera tributaria.",
                    "B": "Apaga su computador a las 5:00 p.m. puntual diciendo que el SENIAT debe entender que su jornada culminó.",
                    "C": "Envía una declaración fraudulenta en cero para cumplir la hora y marcharse a su casa.",
                    "D": "Se queja a gritos en el pasillo insultando a las instituciones públicas del país."
                }
            },
            9: {
                "enunciado": "Respecto al rigor técnico y la exactitud en la codificación de asientos contables:",
                "opciones": {
                    "A": "Jamás en ninguno de mis empleos anteriores he tenido que corregir un solo asiento de diario ni he cometido un error de digitación en una cuenta en toda mi carrera.",
                    "B": "Considero que clasificar los comprobantes de ingreso con número correlativo es una pérdida de tiempo.",
                    "C": "Cuando he detectado una desviación en un registro procesado, he aplicado de inmediato la corrección formal documentada mediante notas de ajuste contable.",
                    "D": "Si el balance de comprobación no cuadra, prefiero atribuirle la culpa a fallas del software administrativo."
                }
            },
            10: {
                "enunciado": "Un directivo de la compañía le solicita emitir y firmar una certificación de ingresos inflada para una persona jurídica relacionada, con el fin de obtener una fianza comercial:",
                "opciones": {
                    "A": "Firma la certificación inflada a cambio de una bonificación económica especial de la gerencia.",
                    "B": "Le dice al directivo que falsifique la firma y el sello del contador para que él no tenga problemas.",
                    "C": "Emite la certificación sin revisar ningún soporte contable para complacer al directivo.",
                    "D": "Niega categóricamente la solicitud, recordando que su firma compromete su responsabilidad legal y el código de ética del contador, exigiendo soportes reales y auditables."
                }
            },
            11: {
                "enunciado": "Al examinar los documentos asignados para la declaración del impuesto a las actividades económicas municipales (Alcaldía), nota que los ingresos del libro de ventas difieren de los estados de cuenta:",
                "opciones": {
                    "A": "Declara la cifra menor sin conciliar para pagar menos tributos municipales.",
                    "B": "Presenta la declaración sin firmar para evadir responsabilidades en una fiscalización.",
                    "C": "Concilia los ingresos de caja y banco contra las ventas reales, deduce notas de crédito sustentadas y completa el formulario con la base imponible exacta exigida por la ordenanza.",
                    "D": "Soborna a los fiscales municipales para que no revisen los libros de ventas de la empresa."
                }
            },
            12: {
                "enunciado": "Al verificar la exactitud de los registros contables en el comprobante de diario procesado, nota que una compra a crédito por $10.000 fue cargada directamente a capital sin pasar por cuentas por pagar:",
                "opciones": {
                    "A": "Deja el registro como está para no tener que anular el comprobante de diario.",
                    "B": "Elabora el asiento de corrección en el programa de contabilidad, restaura la cuenta de pasivo correspondiente y deja la constancia técnica archivada en el legajo del mes.",
                    "C": "Borra la factura de compras de los archivos físicos para que coincida con el error de registro.",
                    "D": "Se niega a corregir el asiento afirmando que el programa de contabilidad no permite modificaciones."
                }
            },
            13: {
                "enunciado": "Para la toma de decisiones estratégicas, la Presidencia le solicita proyecciones financieras y análisis de estados financieros para evaluar la viabilidad de una inversión en nueva flota:",
                "opciones": {
                    "A": "Prepara los estados financieros proforma, evalúa flujos de caja, ratios de liquidez, rentabilidad y endeudamiento, y presenta el informe analítico con recomendaciones técnicas.",
                    "B": "Envía una hoja en blanco con una nota diciendo que el futuro de la empresa no se puede calcular.",
                    "C": "Copia las proyecciones de una empresa de internet sin considerar los números reales de la institución.",
                    "D": "Recomienda comprar la flota sin hacer ningún análisis financiero previo."
                }
            },
            14: {
                "enunciado": "En su relación con auditores externos y autoridades tributarias en empleos previos:",
                "opciones": {
                    "A": "He sostenido debates técnicos sobre la interpretación de providencias tributarias con fiscales y auditores, defendiendo la posición institucional con fundamentos legales y respeto profesional.",
                    "B": "Los inspectores tributarios y auditores externos solo buscan extorsionar a las empresas comerciales.",
                    "C": "No tolero que ningún auditor externo revise mis papeles de trabajo porque mi criterio es perfecto.",
                    "D": "En todas las empresas donde he laborado he tenido auditores y directores absolutamente perfectos que jamás tuvieron una sola discrepancia con mis estados financieros."
                }
            },
            15: {
                "enunciado": "Al momento de mantener en orden y actualizada la cartelera de información tributaria exigida por los entes gubernamentales:",
                "opciones": {
                    "A": "Deja la cartelera vacía o con declaraciones de hace 3 años para no perder tiempo pegando papeles.",
                    "B": "Pega fotocopias ilegibles y tachadas de declaraciones tributarias que no corresponden a la sede.",
                    "C": "Mantiene exhibidos de forma impecable el RIF vigente, última declaración de ISLR, patente municipal, solvencias y certificados actualizados, evitando sanciones en fiscalizaciones.",
                    "D": "Vende el espacio de la cartelera tributaria a comercios externos para publicidad particular."
                }
            },
            16: {
                "enunciado": "Durante el cierre mensual, nota que el módulo de cuentas por pagar arrastra facturas pendientes con más de 180 días de antigüedad que no han sido reclamadas por los proveedores:",
                "opciones": {
                    "A": "Da de baja las cuentas por pagar de forma unilateral y se apropia de los fondos en efectivo.",
                    "B": "Oculta las facturas en una gaveta para que los auditores no pregunten por los pasivos viejos.",
                    "C": "Paga las facturas a cuentas bancarias personales suyas simulando que son de los proveedores.",
                    "D": "Realiza la auditoría de cada caso, valida si existen retenciones no aplicadas o pagos no cruzados, contacta a compras y prepara el informe de pasivos para depuración formal."
                }
            },
            17: {
                "enunciado": "Al recibir y clasificar comprobantes de ingreso y egreso, detecta que varios documentos no cuentan con la firma de autorización del gerente responsable del gasto:",
                "opciones": {
                    "A": "Retiene el procesamiento contable del comprobante, solicita la firma y justificación de la gerencia autorizada conforme al manual de procedimientos y resguarda el control interno.",
                    "B": "Procesa los comprobantes sin firmas para no retrasar el registro en el diario contable.",
                    "C": "Falsifica la firma del gerente en los comprobantes de egreso para cerrar el lote rápido.",
                    "D": "Rompe los comprobantes que no tengan firma para que la administración no los pague."
                }
            },
            18: {
                "enunciado": "Se produce una reforma sustancial en la Ley de Impuesto sobre la Renta (ISLR) y en las normas contables aplicables que entrará en vigencia a partir del primer día del próximo mes:",
                "opciones": {
                    "A": "Ignora la reforma legal y continúa declarando y registrando bajo la normativa derogada.",
                    "B": "Estudia a fondo el nuevo marco legal, adapta el plan de cuentas y sistemas contables, capacita al personal administrativo y asegura la transición tributaria sin contingencias fiscales.",
                    "C": "Espera a que el SENIAT multe a la empresa para enterarse de cuáles eran los cambios de la ley.",
                    "D": "Renuncia a su cargo intempestivamente para no tener que estudiar las nuevas leyes fiscales."
                }
            },
            19: {
                "enunciado": "Sobre la confidencialidad de la información financiera, utilidades y patrimonio de la empresa:",
                "opciones": {
                    "A": "Comento las ganancias netas de la empresa y su situación financiera con personas ajenas en eventos sociales.",
                    "B": "Jamás en toda mi vida profesional he sentido la mínima curiosidad por mirar un estado de cuenta ajeno ni he tenido interés en asuntos que no sean de mi estricta competencia.",
                    "C": "Custodio la información contable, financiera y societaria bajo rigurosa reserva profesional, garantizando el secreto profesional que exige la ley del ejercicio de la contaduría.",
                    "D": "Si tengo diferencias con los dueños, revelo las estrategias contables a empresas de la competencia."
                }
            },
            20: {
                "enunciado": "Al auditar las cuentas por cobrar, detecta que un cliente corporativo tiene facturas canceladas en banco que aún figuran abiertas en el sistema contable:",
                "opciones": {
                    "A": "Deja las facturas abiertas en el sistema para que cobranzas le vuelva a cobrar al cliente.",
                    "B": "Borra la cuenta del cliente para que no aparezca en el balance general de la institución.",
                    "C": "Cruza las transferencias bancarias confirmadas contra los saldos del cliente, aplica los pagos en el sistema contable y emite el balance de antigüedad de saldos saneado.",
                    "D": "Le cobra una tarifa personal al cliente por actualizarle su estado de cuenta en el sistema."
                }
            },
            21: {
                "enunciado": "Al elaborar los comprobantes de movimientos contables de fin de mes, el sistema informático se satura y se pierde la sincronización de los asientos automáticos:",
                "opciones": {
                    "A": "Valida la integridad de la base de datos, coteja los asientos del diario contra los documentos físicos asignados, reingresa las partidas no consolidadas y asegura el cuadre del mayor.",
                    "B": "Inventa las cifras del balance general para no tener que revisar asiento por asiento.",
                    "C": "Apaga el servidor de contabilidad y se marcha a su casa argumentando fallas técnicas insalvables.",
                    "D": "Se queja a gritos en el departamento insultando a los técnicos de soporte informático."
                }
            },
            22: {
                "enunciado": "Durante una fiscalización presencial de la Administración Tributaria (SENIAT) en la sede de la empresa:",
                "opciones": {
                    "A": "Se encierra en su oficina y se niega a atender a los funcionarios fiscales por temor a sanciones.",
                    "B": "Atiende la fiscalización con solvencia técnica, suministra los libros de compras y ventas timbrados, comprobantes de retención y estados financieros solicitados, levantando acta formal.",
                    "C": "Ofrece un soborno al fiscal actuante para que cierre la revisión sin emitir observaciones.",
                    "D": "Discute agresivamente con los actuantes acusándolos de hostigamiento tributario."
                }
            },
            23: {
                "enunciado": "Al recibir los reportes de inventarios físicos para el cálculo del costo de ventas, nota una merma considerable que no cuenta con acta de destrucción o justificación operativa:",
                "opciones": {
                    "A": "Contabiliza la merma como un gasto normal deducible de impuestos sin solicitar el acta técnica.",
                    "B": "Modifica los inventarios en el sistema para que la merma desaparezca del costo de ventas.",
                    "C": "Solicita el acta de auditoría a Almacén y Control de Calidad, cuantifica el impacto en costos, aplica el tratamiento contable de la merma y evalúa su no deducibilidad fiscal según ley.",
                    "D": "Carga el monto de la merma a las cuentas por cobrar de los trabajadores del almacén sin pruebas."
                }
            },
            24: {
                "enunciado": "Sobre el autocontrol emocional ante requerimientos urgentes o discrepancias numéricas en balances:",
                "opciones": {
                    "A": "Si el balance no cuadra por pocos centavos, golpeo el monitor y me niego a seguir revisando.",
                    "B": "He enfrentado descuadres complejos y auditorías con alta exigencia, pero mantengo la paciencia analítica, el método de conciliación y la calma operativa hasta encontrar el origen.",
                    "C": "Poseo una serenidad celestial inalterable; absolutamente ningún descuadre numérico, inspección fiscal ni presión de cierre me ha causado estrés o preocupación jamás.",
                    "D": "Cuando me saturo de números, cierro los libros con diferencias abiertas y me voy a descansar."
                }
            },
            25: {
                "enunciado": "Un socio minoritario de la empresa le solicita información financiera confidencial para utilizarla en un litigio personal contra la Junta Directiva:",
                "opciones": {
                    "A": "Le entrega copias de los estados financieros confidenciales sin autorización de la Presidencia.",
                    "B": "Le cobra una suma en divisas al socio para entregarle los reportes financieros en un pendrive.",
                    "C": "Altera los estados financieros para perjudicar a la empresa en el proceso judicial.",
                    "D": "Rechaza la entrega informal, orienta a canalizar la solicitud por la vía estatutaria formal y notifica la situación a la Presidencia y al departamento legal."
                }
            },
            26: {
                "enunciado": "Al auditar las conciliaciones bancarias de fin de mes, encuentra una nota de débito no identificada por un monto significativo en la cuenta principal:",
                "opciones": {
                    "A": "Asienta la nota de débito como un gasto operativo cualquiera para cerrar el mes rápido.",
                    "B": "Gestiona de inmediato ante el ejecutivo bancario la copia del soporte de la nota de débito, asienta la partida en conciliación como no reconocida y formaliza el reclamo de reintegro.",
                    "C": "Borra la nota de débito del estado de cuenta bancario digital para que el libro mayor cuadre.",
                    "D": "Acusa a los analistas de administración de apropiación indebida sin antes investigar con el banco."
                }
            },
            27: {
                "enunciado": "Se requiere extender la jornada laboral para concluir la consolidación de los estados financieros auditados que deben ser presentados ante una asamblea extraordinaria de accionistas:",
                "opciones": {
                    "A": "Se marcha a su casa a las 5:00 p.m. diciendo que la asamblea de accionistas no es su problema.",
                    "B": "Asume la extensión horaria con compromiso profesional, culmina las notas explicativas a los estados financieros, audita los balances y entrega el expediente listo para la asamblea.",
                    "C": "Envía los balances incompletos y sin firmar para poder irse temprano de la oficina.",
                    "D": "Se queja a gritos con los socios asegurando que la empresa exige demasiado trabajo a los profesionales."
                }
            },
            28: {
                "enunciado": "Al culminar el período fiscal, los soportes contables originales (comprobantes de diario, facturas, cheques y declaraciones) deben ser resguardados legalmente:",
                "opciones": {
                    "A": "Garantiza el archivo cronológico estricto de los legajos físicos y digitales, debidamente foliados, rotulados y custodiados bajo llave durante los lapsos de prescripción fijados por la ley.",
                    "B": "Deja las cajas de comprobantes contables abiertas en un pasillo húmedo donde pueden dañarse.",
                    "C": "Bota los soportes contables a la basura argumentando que ya todo está registrado en la computadora.",
                    "D": "Se lleva las carpetas con comprobantes originales a su casa para utilizarlas como hojas de borrador."
                }
            },
            29: {
                "enunciado": "En su relación con otros profesionales de la contabilidad y reconocimientos laborales:",
                "opciones": {
                    "A": "Jamás en toda mi vida profesional he sentido la mínima envidia, recelo o inconformidad ante las felicitaciones, ascensos o logros de otros contadores o administradores.",
                    "B": "En ocasiones he sentido sana emulación o deseo de superación ante el éxito técnico de otros colegas, pero me concentro en pulir mis análisis y brindar un servicio contable de alta calidad.",
                    "C": "Pienso que cuando felicitan a un contador en una institución es únicamente por complacencia con los dueños.",
                    "D": "No me gusta compartir criterios técnicos con otros contadores porque en el gremio todos son desleales."
                }
            },
            30: {
                "enunciado": "Presidencia le encomienda realizar una auditoría reservada sobre los estados financieros de una empresa filial ante presuntas inconsistencias en el manejo de fondos:",
                "opciones": {
                    "A": "Le comenta los objetivos de la auditoría a los directores de la filial antes de iniciar la revisión.",
                    "B": "Se niega a realizar la auditoría argumentando que auditar empresas del mismo grupo genera conflictos.",
                    "C": "Ejecuta la auditoría con absoluto sigilo profesional: examina libros, audita cuentas bancarias, verifica registros y entrega el informe reservado y fundamentado a Presidencia.",
                    "D": "Modifica las evidencias en el informe para encubrir a colegas contadores que laboran en la filial."
                }
            }
        }
    },
    # =========================================================================
    # 16. COORDINACIÓN DE VENTAS (CJS-CSV)
    # =========================================================================
    "16_COORDINACION_DE_VENTAS": {
        "codigo": "CJS-CSV",
        "titulo": "EVALUACIÓN PSICOTÉCNICA EN COORDINACIÓN Y SUPERVISIÓN DE VENTAS",
        "instrucciones": "Lea con atención cada situación de estrategia comercial, liderazgo en calle y gestión de cobranza. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con objetividad sobre su estilo de supervisión, coaching, toma de decisiones y apego ético. Dispone de un máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "Al revisar el cierre de mes, nota que un asesor de ventas estrella concentró el 60% de su cuota de volumen en un solo cliente mayorista otorgándole crédito no autorizado, dejando al 40% de su territorio desatendido:",
                "opciones": {
                    "A": "Felicita al asesor en público por alcanzar el volumen bruto sin importar el riesgo de cartera.",
                    "B": "Le pide al asesor que divida la deuda ficticiamente en otros clientes para tapar la concentración.",
                    "C": "Le prohíbe al asesor volver a visitar al cliente mayorista de forma unilateral y sin análisis.",
                    "D": "Interviene la zona, audita la salud de la cuenta por cobrar, aplica la política de límite crediticio y reestructura el plan de ruteo para recuperar la cobertura horizontal del territorio."
                }
            },
            2: {
                "enunciado": "Durante la salida diaria de auditoría y acompañamiento en campo, observa que un vendedor nuevo titubea al presentar las promociones y cede ante el comerciante aceptando descuentos fuera de lista:",
                "opciones": {
                    "A": "Se burla del vendedor delante del comerciante para demostrar quién tiene la autoridad en la zona.",
                    "B": "Asume la negociación con empatía y modelado comercial en el acto, defiende la lista de precios oficial cerrando la venta y, al salir del local, retroalimenta pedagógicamente al colaborador.",
                    "C": "Deja que el vendedor regale el producto para no perder la venta y le descuenta la diferencia de su sueldo.",
                    "D": "Se marcha de la tienda dejando al vendedor solo y lo despide al regresar a la oficina."
                }
            },
            3: {
                "enunciado": "Al cotejar la proyección de ventas semanal contra los niveles de inventario en almacén, detecta que una línea prioritaria de alta rentabilidad está por quebrar stock físico en 72 horas:",
                "opciones": {
                    "A": "Coordina de inmediato con Logística y Compras la reposición urgente del inventario, ajusta el plan de cuotas por asesor priorizando canales clave y evita la venta de mercancía inexistente.",
                    "B": "Oculta el quiebre de stock y permite que la fuerza de ventas siga facturando productos agotados.",
                    "C": "Detiene las ventas de todo el portafolio de la empresa hasta que la mercancía llegue a la planta.",
                    "D": "Modifica los registros del sistema administrativo inflando el inventario teórico de forma ficticia."
                }
            },
            4: {
                "enunciado": "En su trayectoria profesional y liderazgo de equipos comerciales bajo presión de metas:",
                "opciones": {
                    "A": "Si la fuerza de ventas no llega al presupuesto del mes, me encierro en mi oficina y me niego a hablarles.",
                    "B": "En ocasiones he sentido frustración o desgaste mental ante meses con contracción del mercado, pero mantengo la serenidad, la motivación de la tropa y reajusto las tácticas de abordaje.",
                    "C": "Jamás en toda mi vida profesional he sentido la más mínima presión, incertidumbre ni desánimo ante una meta de ventas exigente.",
                    "D": "Prefiero supervisar a los vendedores únicamente por teléfono para no tener que caminar la calle."
                }
            },
            5: {
                "enunciado": "En una auditoría de calle a puntos de venta, constata que un comerciante tiene una nevera y un exhibidor exclusivo de la empresa lleno de productos de una marca de la competencia directa:",
                "opciones": {
                    "A": "Le regala el activo de comercialización al dueño del negocio para evitar una confrontación comercial.",
                    "B": "Desconecta el equipo para que los productos de la competencia se dañen dentro del local.",
                    "C": "Le cobra una tarifa personal en efectivo al comerciante por permitirle usar el mueble de la empresa.",
                    "D": "Dialoga con el cliente recordando el comodato de exclusividad, desaloja el producto ajeno, llena el equipo con el portafolio de la marca y levanta la minuta con el asesor de la ruta."
                }
            },
            6: {
                "enunciado": "Al analizar las rutas comerciales asignadas, nota que dos vendedores tienen cruces geográficos innecesarios que generan demoras en despachos y aumentan el costo logístico de distribución:",
                "opciones": {
                    "A": "Deja las rutas como están para no alterar la zona de confort de los vendedores antiguos.",
                    "B": "Optimiza las rutas comerciales mediante reingeniería de planillas de venta, balancea el número de clientes por día, coordina con Distribución la ventana horaria y capacita a los asesores.",
                    "C": "Le quita la cartera de clientes al vendedor con menor antigüedad para dársela completa a su amigo.",
                    "D": "Cancela las visitas presenciales e impone que todos los clientes compren por mensajes de texto."
                }
            },
            7: {
                "enunciado": "Al auditar las cuentas por cobrar de una zona foránea, detecta que varios clientes aparecen solventes en sistema pero manifiestan que le pagaron en efectivo al vendedor hace 10 días:",
                "opciones": {
                    "A": "Abre una investigación formal de auditoría de calle, coteja los recibos físicos contra los ingresos en banco, notifica a Gerencia y aplica las medidas disciplinarias y de saneamiento de cartera.",
                    "B": "Se queda callado y le da 15 días al vendedor para que devuelva el dinero sin dejar registros.",
                    "C": "Modifica los saldos en el software contable cargando la deuda a pérdidas de la empresa.",
                    "D": "Le cobra la deuda a los clientes nuevamente exigiéndoles que paguen doble."
                }
            },
            8: {
                "enunciado": "Son las 4:50 p.m. (su hora habitual de salida es a las 5:00 p.m.) y la Gerencia de Ventas solicita el reporte consolidado de indicadores comerciales y plan de acción de fin de mes:",
                "opciones": {
                    "A": "Asume la extensión horaria con compromiso ejecutivo, consolida las métricas de visita, efectividad, volumen y cobranza, y entrega el informe analítico para la toma de decisiones.",
                    "B": "Apaga su computador a las 5:00 p.m. en punto diciendo que los reportes ejecutivos no son prioritarios.",
                    "C": "Envía un informe con cifras inventadas al azar para salir rápido de la oficina.",
                    "D": "Se queja a gritos en el pasillo insultando a la Gerencia por exigir consolidaciones al cierre."
                }
            },
            9: {
                "enunciado": "Respecto al rigor técnico y la objetividad en la evaluación de la fuerza de ventas:",
                "opciones": {
                    "A": "Jamás en ninguno de mis empleos anteriores he tenido la más mínima discrepancia con un vendedor ni he cometido un error de cálculo de comisiones en toda mi trayectoria.",
                    "B": "Considero que evaluar a los vendedores con métricas estadísticas es una pérdida de tiempo irrelevante.",
                    "C": "Evalúo a mis colaboradores basándome en hechos, datos de campo, efectividad de visita y recuperación de cartera, brindando retroalimentación formativa y transparente.",
                    "D": "Si una zona de ventas no vende, prefiero culpar al departamento de facturación para no presionar al equipo."
                }
            },
            10: {
                "enunciado": "El dueño de una cadena de supermercados le propone al supervisor pagarle una comisión privada bajo la mesa si le autoriza una escala de precios por debajo del costo de la distribuidora:",
                "opciones": {
                    "A": "Acepta el soborno y autoriza los precios por debajo del costo perjudicando a la empresa.",
                    "B": "Le propone al cliente repartirse la mercancía de una gandola para venderla en el mercado informal.",
                    "C": "Acepta la propuesta pero le exige al cliente que le pague por adelantado en divisas en efectivo.",
                    "D": "Rechaza la propuesta de forma rotunda, defiende la rentabilidad institucional, protege la política de precios y reporta el intento de soborno a la Dirección General."
                }
            },
            11: {
                "enunciado": "Al realizar una reunión de ventas matutina, detecta desmotivación en el equipo debido a que un competidor ingresó agresivamente con promociones de bajo precio en la zona:",
                "opciones": {
                    "A": "Se une al desánimo del equipo y les dice que es imposible competir contra esos precios.",
                    "B": "Insulta a los vendedores acusándolos de cobardes y los amenaza con despedirlos a todos.",
                    "C": "Analiza la inteligencia de mercado, destaca los diferenciales de calidad, servicio y frecuencia de entrega de la marca, pauta planes de negocio a clientes clave y activa a la fuerza comercial.",
                    "D": "Autoriza a los vendedores a difamar a la marca competidora diciendo que sus productos son tóxicos."
                }
            },
            12: {
                "enunciado": "Un vendedor con excelente volumen de facturación se niega sistemáticamente a realizar cobranzas y auditar las facturas vencidas de sus clientes en la calle:",
                "opciones": {
                    "A": "Le retira la responsabilidad de cobro y le asigna un cobrador personal pagado por la empresa.",
                    "B": "Acompaña al asesor en ruta, le modela la técnica de cobranza asertiva, le demuestra que la venta no culmina hasta que se cobra y condiciona sus incentivos a la recuperación de cartera.",
                    "C": "Falsifica las firmas de los clientes en los recibos de cobro para limpiar el código del vendedor.",
                    "D": "Le perdona la morosidad a los clientes del vendedor estrella para que siga facturando sin trabas."
                }
            },
            13: {
                "enunciado": "Durante una auditoría de campo, constata que un mercaderista asignado a una cadena vitrina no asiste a su horario y deja los anaqueles vacíos acumulando quiebres en góndola:",
                "opciones": {
                    "A": "Levanta el acta de supervisión in situ con evidencia fotográfica, cita al colaborador a una sesión de retroalimentación, establece compromisos con fecha y aplica la medida disciplinaria formal.",
                    "B": "Deja pasar la falta porque el mercaderista es amigo personal de un directivo de la compañía.",
                    "C": "Acomoda el anaquel usted mismo todos los días para que el mercaderista pueda seguir faltando.",
                    "D": "Despide al colaborador a gritos en medio del supermercado frente a los clientes de la tienda."
                }
            },
            14: {
                "enunciado": "En su relación con directivos comerciales y directrices corporativas en empleos previos:",
                "opciones": {
                    "A": "He tenido divergencias técnicas sobre el enfoque de una campaña promocional con gerentes, pero expuse mis argumentos con base en la data de calle y acaté la directriz final de la empresa.",
                    "B": "Los directores de ventas siempre diseñan estrategias en oficinas con aire acondicionado que no sirven en la calle.",
                    "C": "No tolero que nadie supervise cómo manejo a mi equipo porque yo soy el único líder de la zona.",
                    "D": "En todas las empresas donde he laborado he tenido directores comerciales absolutamente perfectos que jamás cometieron un error de juicio."
                }
            },
            15: {
                "enunciado": "Al auditar la asignación de activos comerciales (neveras y exhibidores), nota que se entregaron 5 equipos en negocios que no cumplen con el volumen mínimo de compra requerido:",
                "opciones": {
                    "A": "Deja los equipos en esos locales argumentando que retirar exhibidores genera mala imagen.",
                    "B": "Reubica estratégicamente los activos comerciales hacia puntos de venta de alto tráfico y valor, formaliza las nuevas actas de comodato y optimiza el retorno de la inversión de la marca.",
                    "C": "Vende los exhibidores a los comerciantes por una suma en efectivo para recuperar el dinero.",
                    "D": "Rompe los contratos de comodato para que la empresa no pueda reclamar la propiedad del activo."
                }
            },
            16: {
                "enunciado": "Un asesor de ventas le solicita autorización para despacharle a un cliente que tiene 45 días de mora con una promesa de pago verbal para el fin de semana:",
                "opciones": {
                    "A": "Autoriza el despacho inmediato de palabra para que el asesor no pierda su comisión mensual.",
                    "B": "Triangula el pedido cargándoselo al código de otro cliente solvente para burlar el sistema.",
                    "C": "Le dice al chofer de despacho que entregue la mercancía sin factura comercial en el local.",
                    "D": "Rechaza la liberación del pedido, respalda la política de crédito institucional, orienta al asesor a negociar un abono a la deuda vencida y supedita el nuevo pedido a la regularización."
                }
            },
            17: {
                "enunciado": "Al presentarse continuas fallas en los despachos de ruta que generan devoluciones y quejas de clientes por pedidos incompletos o entregas tardías:",
                "opciones": {
                    "A": "Establece mesas de trabajo con Logística y Distribución, concilia los tiempos de carga y ventanas de entrega, audita el picking en almacén y diseña planes de despacho eficientes.",
                    "B": "Se desentiende del problema acusando públicamente al personal de transporte de incompetencia.",
                    "C": "Le aconseja a los clientes que dejen de comprarle a la distribuidora hasta que mejore el transporte.",
                    "D": "Modifica las facturas comerciales en el andén eliminando los productos que no se pudieron cargar."
                }
            },
            18: {
                "enunciado": "En una reunión de seguimiento comercial, dos supervisores de zona se disputan agresivamente la titularidad de un cliente mayorista de alto volumen ubicado en el límite territorial:",
                "opciones": {
                    "A": "Le asigna el cliente al supervisor que tenga mayor antigüedad sin revisar las zonas geográficas.",
                    "B": "Analiza la zonificación formal, la logística de reparto más eficiente y el historial de atención, dirime la controversia con criterio técnico objetivo y asienta la delimitación territorial por escrito.",
                    "C": "Divide la comisión del cliente a partes iguales entre los dos supervisores sin resolver la ruta de despacho.",
                    "D": "Se lava las manos y deja que los dos supervisores se enfrenten a golpes fuera de la oficina."
                }
            },
            19: {
                "enunciado": "Sobre la confidencialidad de las bases de datos de clientes, planes de negocio y márgenes comerciales:",
                "opciones": {
                    "A": "Facilito la lista de clientes del maestro con sus límites de crédito a empresas de la competencia.",
                    "B": "Jamás en toda mi vida profesional he sentido la mínima curiosidad por mirar una información comercial ajena ni he divulgado un plan estratégico de la empresa.",
                    "C": "Resguardo las bases de datos, cifras de venta y acuerdos comerciales con estricto sigilo, lealtad y reserva profesional.",
                    "D": "Vendo los planes de lanzamiento de nuevos productos a marcas rivales para obtener ingresos extra."
                }
            },
            20: {
                "enunciado": "Al revisar las herramientas de trabajo de sus colaboradores (teléfonos móviles de toma de pedidos, planillas, catálogos y material POP), nota que varios vendedores tienen equipos dañados:",
                "opciones": {
                    "A": "Les dice a los vendedores que ellos mismos deben comprar sus herramientas de trabajo de su sueldo.",
                    "B": "Suspende las ventas de los vendedores que tienen equipos dañados sin gestionar soluciones.",
                    "C": "Gestiona oportunamente con la Gerencia y Sistemas la reposición y mantenimiento de las herramientas de venta, garantizando la continuidad operativa y la eficiencia en la toma de pedidos.",
                    "D": "Oculta el daño de los equipos a la empresa para no generar gastos administrativos."
                }
            },
            21: {
                "enunciado": "Al lanzar una actividad promocional estratégica para el canal tradicional, detecta que los vendedores no están comunicando la mecánica a los clientes y guardan el material POP en sus morrales:",
                "opciones": {
                    "A": "Cancela la promoción y le dice a la Gerencia de Mercadeo que la fuerza de ventas no sirve.",
                    "B": "Sanciona económicamente a los vendedores sin explicarles la importancia comercial de la campaña.",
                    "C": "Sale a la calle con su equipo, modela la ejecución de la promoción en puntos de venta, supervisa la colocación del material POP y audita el impacto en el volumen de ventas del canal.",
                    "D": "Regala el material POP a sus familiares para decorar sus casas particulares."
                }
            },
            22: {
                "enunciado": "Durante el análisis de inteligencia de mercado en una ruta foránea, identifica que un nuevo competidor regional está captando clientes clave ofreciendo crédito a 60 días:",
                "opciones": {
                    "A": "Ignora la presencia del competidor asumiendo que los clientes nunca se irán con otra marca.",
                    "B": "Levanta la información de campo (precios, productos, condiciones), elabora un informe analítico para la Gerencia de Ventas y formula planes de negocio y fidelización para blindar la cartera.",
                    "C": "Amenaza a los comerciantes con no venderles más si le compran al nuevo competidor regional.",
                    "D": "Autoriza crédito a 90 días por su propia cuenta sin aval financiero ni autorización directiva."
                }
            },
            23: {
                "enunciado": "Al auditar las liquidaciones de cobro de la semana, nota que un asesor retuvo durante 48 horas una cobranza en divisas en efectivo antes de ingresarla a la administración:",
                "opciones": {
                    "A": "Interviene de inmediato, audita la ruta completa del asesor, exige el ingreso inmediato de los fondos a caja, levanta el expediente formal a Gerencia y aplica las medidas disciplinarias de ley.",
                    "B": "Acepta que el vendedor conserve el dinero en efectivo siempre y cuando le pague una comisión a usted.",
                    "C": "Oculta la retención de dinero a la Gerencia General para evitar problemas administrativos.",
                    "D": "Modifica las fechas de los recibos en el sistema contable para tapar la falta del vendedor."
                }
            },
            24: {
                "enunciado": "Sobre el autocontrol emocional ante objeciones agresivas o rechazo de clientes clave en campo:",
                "opciones": {
                    "A": "Si el dueño de un supermercado me levanta la voz reclamando por un despacho, le respondo a gritos.",
                    "B": "He enfrentado comerciantes difíciles y situaciones comerciales tensas, pero mantengo la serenidad, la empatía y la negociación basada en beneficios mutuos.",
                    "C": "Poseo una templanza celestial inalterable; absolutamente ningún conflicto comercial, insulto ni problema de ruta me ha generado el menor estrés jamás.",
                    "D": "Cuando me enojo con un comerciante, le ordeno a los choferes que bloqueen la entrada de su local con el camión."
                }
            },
            25: {
                "enunciado": "Un asesor de ventas le propone cobrar en efectivo facturas a crédito de clientes morosos y no reportarlas en el sistema hasta fin de mes para 'jugar con el dinero':",
                "opciones": {
                    "A": "Acepta la propuesta del asesor y se reparte los intereses del dinero retenido.",
                    "B": "Le propone al asesor que la retención no sea de una semana sino de tres meses para ganar más.",
                    "C": "Acepta pero le exige al asesor que le entregue una parte del dinero en dólares en mano propia.",
                    "D": "Rechaza la propuesta de forma categórica, advierte el carácter delictivo de la acción, separa preventivamente al asesor de la cobranza y reporta la situación a la Dirección General."
                }
            },
            26: {
                "enunciado": "Al momento de planificar el crecimiento de un cliente que posee un valor estratégico muy alto para la empresa:",
                "opciones": {
                    "A": "Le impone compras forzadas de productos de baja rotación sin importar si se le vencen en el negocio.",
                    "B": "Desarrolla un plan de negocio personalizado: analiza el sell-out del cliente, diseña combos atractivos, optimiza la visibilidad en góndola y acuerda metas conjuntas de crecimiento rentable.",
                    "C": "Le promete al cliente que la empresa le regalará una gandola de productos si cumple una meta verbal.",
                    "D": "Deja que el cliente compre lo que quiera sin asesorarlo sobre tendencias del mercado."
                }
            },
            27: {
                "enunciado": "Se requiere extender la jornada de trabajo para realizar una reunión de alineación estratégica y cierre comercial que culminará a las 7:00 p.m.:",
                "opciones": {
                    "A": "Se retira a las 5:00 p.m. puntual diciendo que las reuniones de ventas deben ser en horas de la mañana.",
                    "B": "Lidera la sesión con entusiasmo y profesionalismo, consolida las estrategias territoriales del mes siguiente, motiva al equipo comercial y asegura el compromiso de la fuerza de ventas.",
                    "C": "Asiste a la reunión pero se sienta al fondo a jugar con el teléfono celular sin aportar nada.",
                    "D": "Se queja a gritos con los vendedores asegurando que los jefes de ventas abusan de su tiempo."
                }
            },
            28: {
                "enunciado": "Al momento de auditar las herramientas y planillas necesarias de venta que utilizan sus colaboradores en la ruta:",
                "opciones": {
                    "A": "Mantiene las carpetas de ruta, censos de clientes y planillas de cobranza actualizadas, organizadas y foliadas, garantizando el control documental y la trazabilidad de cada zona.",
                    "B": "Deja las planillas de los vendedores tiradas en el piso de la oficina donde cualquiera puede verlas.",
                    "C": "Bota las planillas de cobranza viejas a la basura para tener más espacio en los estantes.",
                    "D": "Altera los nombres de los clientes en las planillas para inventar coberturas que no existen."
                }
            },
            29: {
                "enunciado": "En su relación con otros líderes comerciales y reconocimientos departamentales:",
                "opciones": {
                    "A": "Jamás en toda mi vida profesional he sentido la mínima envidia, recelo o inconformidad cuando felicitan o premian a otro coordinador o supervisor de ventas.",
                    "B": "A veces he sentido sana emulación o deseo de destacar como el mejor líder comercial, pero me concentro en que mi equipo sea el más rentable, disciplinado y con mejor servicio al cliente.",
                    "C": "Considero que cuando premian a un supervisor en la empresa es únicamente por adulación a los dueños.",
                    "D": "No me gusta compartir mis tácticas comerciales con otros supervisores porque en ventas todos son rivales."
                }
            },
            30: {
                "enunciado": "La Gerencia General le encomienda realizar una auditoría reservada sobre sospechas de triangulación de pedidos y cobros ficticios en una zona comercial vecina:",
                "opciones": {
                    "A": "Le avisa al supervisor de esa zona sobre la investigación para alertarlo antes de la auditoría.",
                    "B": "Se niega a realizar la auditoría argumentando que auditar zonas de otros supervisores no es ético.",
                    "C": "Ejecuta la auditoría de calle con absoluto sigilo profesional: visita a los clientes auditados, coteja facturas vs. saldos reales, audita entregas y entrega el informe reservado a Gerencia.",
                    "D": "Altera las conclusiones del informe para encubrir al supervisor de la zona si tiene amistad con él."
                }
            }
        }
    },

    # =========================================================================
    # 17. COORDINADOR ADMINISTRATIVO DE AGENCIA (CJS-COA)
    # =========================================================================
    "17_COORDINADOR_ADMINISTRATIVO_DE_AGENCIA": {
        "codigo": "CJS-COA",
        "titulo": "EVALUACIÓN PSICOTÉCNICA SITUACIONAL EN COORDINACIÓN ADMINISTRATIVA DE AGENCIA",
        "instrucciones": "Lea con atención cada situación gerencial y operativa de la agencia. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con total honestidad sobre su estilo real de control, custodia de valores y liderazgo operativo. Dispone de un tiempo máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "Al momento de recibir la recaudación diaria en divisas en efectivo de la analista de cobranzas para su custodia y entrega a relación interna, detecta un billete de $50 presuntamente falso:",
                "opciones": {
                    "A": "Lo recibe y lo coloca en medio del fajo de dinero para que pase desapercibido en el banco.",
                    "B": "Le descuenta el dinero a la analista de cobranzas de su sueldo sin levantar ningún acta.",
                    "C": "Rechaza el lote completo de cobranza paralizando el cuadre de caja de toda la agencia.",
                    "D": "Retiene el billete aplicando protocolo de verificación, levanta la minuta de discrepancia junto a la analista, ajusta el recibo de entrega y notifica al Gerente de Agencia."
                }
            },
            2: {
                "enunciado": "Durante el cierre diario de liquidación y caja a las 5:00 p.m., el sistema arroja una diferencia pendiente de $120 entre las facturas liquidadas y las cobranzas reportadas:",
                "opciones": {
                    "A": "Modifica manualmente el reporte del sistema para que cuadre en cero y marcharse a su casa.",
                    "B": "Extiende la jornada, revisa recibo por recibo contra las órdenes de despacho, identifica si el desfase es por cobranza en tránsito o error de carga y deja el cierre saneado.",
                    "C": "Cierra el sistema a la fuerza dejando la inconsistencia abierta para resolverla al día siguiente.",
                    "D": "Acusa a los cajeros de sustracción indebida antes de auditar los comprobantes físicos."
                }
            },
            3: {
                "enunciado": "El Jefe de Almacén le informa que la flota de reparto se quedó sin combustible a mitad de jornada y que el presupuesto de flota asignado para el mes ya se agotó:",
                "opciones": {
                    "A": "Analiza el gasto acumulado de flota, gestiona de inmediato una partida de contingencia justificada con la Gerencia General y audita el consumo de combustible de los camiones.",
                    "B": "Autoriza usar el dinero en efectivo de la cobranza diaria de divisas sin dejar ningún comprobante.",
                    "C": "Suspende las entregas de la semana completa y se niega a buscar soluciones administrativas.",
                    "D": "Le exige a los choferes que paguen la gasolina de sus propios bolsillos para poder trabajar."
                }
            },
            4: {
                "enunciado": "En su trayectoria profesional y gestión de control interno:",
                "opciones": {
                    "A": "Si un cajero comete una equivocación menor al contar, lo despido de inmediato sin mediar palabra.",
                    "B": "He experimentado momentos de alta exigencia en cierres operativos o auditorías fiscales, pero mantengo la precisión en los números y la calma en el equipo.",
                    "C": "Jamás en toda mi vida laboral he sentido el menor síntoma de cansancio, presión o estrés ante un descuadre contable.",
                    "D": "Prefiero no capacitar a mi equipo de agencia para que dependan siempre de mis decisiones."
                }
            },
            5: {
                "enunciado": "En la revisión mensual de deberes formales, detecta que los comprobantes de retención de IVA e ISLR de varios proveedores no fueron emitidos a tiempo en el portal tributario:",
                "opciones": {
                    "A": "Deja pasar la omisión esperando que el SENIAT no realice fiscalizaciones en esa sucursal.",
                    "B": "Borra las facturas del sistema administrativo para fingir que nunca fueron recibidas.",
                    "C": "Paga comisiones informales a gestores externos para evadir las sanciones tributarias.",
                    "D": "Cuantifica el impacto fiscal, elabora y transmite las retenciones extemporáneas de inmediato y reporta a la Gerencia el correctivo para evitar multas mayores."
                }
            },
            6: {
                "enunciado": "Se genera una fuerte fricción entre el área de ventas y el facturador de la agencia porque varios pedidos prioritarios no han sido impresos para carga en almacén:",
                "opciones": {
                    "A": "Se pone del lado de ventas y le grita al facturador exigiendo que trabaje más rápido.",
                    "B": "Prohíbe a los vendedores entrar al área administrativa y suspende la facturación del día.",
                    "C": "Interviene de inmediato, revisa la cola de pedidos pendientes, prioriza por itinerario de salida de camiones y establece una ventana de corte de carga coordinada.",
                    "D": "Se encierra en su oficina y deja que los empleados discutan hasta que se cansen."
                }
            },
            7: {
                "enunciado": "Al auditar la caja chica de la agencia, observa vales provisionales de efectivo firmados por empleados desde hace más de 15 días sin facturas de respaldo:",
                "opciones": {
                    "A": "Rompe los vales y pone dinero propio para tapar el faltante antes de que llegue la auditoría.",
                    "B": "Frena la entrega de nuevos fondos, exige la entrega inmediata de facturas legales o el reembolso en efectivo y reporta la desviación a la Gerencia General.",
                    "C": "Convierte los vales en gastos ficticios de papelería en el sistema administrativo.",
                    "D": "Despide a todos los colaboradores involucrados sin iniciar un proceso de descargo formal."
                }
            },
            8: {
                "enunciado": "A primera hora de la mañana (8:00 a.m.), debe emitir el reporte de estados de cuenta bancarios para la analista de cobranzas, pero la conexión bancaria está temporalmente caída:",
                "opciones": {
                    "A": "Activa la conexión de respaldo, consulta los saldos por la aplicación bancaria móvil autorizada y emite el listado preliminar de créditos para no paralizar la cobranza.",
                    "B": "Le dice a la analista de cobranzas que no se puede trabajar y se sienta a esperar que vuelva el sistema.",
                    "C": "Autoriza la entrega de mercancía a crédito sin validar si los clientes transfirieron.",
                    "D": "Envía un correo con cifras inventadas del día anterior para aparentar que cumplió con el horario."
                }
            },
            9: {
                "enunciado": "Respecto a la precisión y el rigor en el manejo de fondos de la empresa:",
                "opciones": {
                    "A": "Jamás en toda mi carrera administrativa he tenido un solo centavo de diferencia en un arqueo o conciliación.",
                    "B": "Considero que las diferencias pequeñas de caja son normales y no vale la pena auditarlas.",
                    "C": "Cuando he detectado una diferencia en caja o libros, he realizado el arqueo exhaustivo hasta identificar la causa.",
                    "D": "Si falta dinero en la caja de la agencia, prefiero atribuirlo a fallas del sistema contable."
                }
            },
            10: {
                "enunciado": "Un funcionario público se presenta en la agencia exigiendo una 'colaboración en productos' para no levantar un acta por supuestas fallas en la cartelera fiscal:",
                "opciones": {
                    "A": "Entrega los productos solicitados de forma clandestina cargándolos a mermas de almacén.",
                    "B": "Insulta al funcionario de forma agresiva y lo expulsa a empujones de la agencia.",
                    "C": "Pide dinero de la caja chica para pagarle al funcionario y evitar problemas legales.",
                    "D": "Solicita formalmente el acta de inspección por escrito, exhibe los recaudos legales al día y contacta de inmediato a la Consultoría Jurídica y a la Gerencia General."
                }
            },
            11: {
                "enunciado": "El inventario físico de la agencia arroja una pérdida significativa en productos de alta rotación respecto al inventario teórico del sistema:",
                "opciones": {
                    "A": "Realiza un ajuste contable automático rebajando el sistema para que nadie se alerte.",
                    "B": "Culpa exclusivamente al personal de limpieza de la agencia sin revisar la custodia de llaves.",
                    "C": "Lidera una auditoría cruzada de entradas, salidas y despachos, revisa las cámaras de seguridad junto a control interno y formaliza el informe de desviación patrimonial.",
                    "D": "Oculta el informe de inventario y no le entrega las cifras a la Gerencia General."
                }
            },
            12: {
                "enunciado": "Debe comunicar al personal de la agencia un cambio en las políticas de horas extras y control de asistencia biometrico:",
                "opciones": {
                    "A": "Pega una circular en la puerta sin explicar los motivos y amenaza con amonestar a quien proteste.",
                    "B": "Convoca a una reunión operativa, expone con claridad los lineamientos corporativos, aclara dudas y establece el seguimiento del registro con equidad.",
                    "C": "Le dice a los empleados que ella está en desacuerdo con la norma pero que debe cumplirla por culpa de la sede central.",
                    "D": "Permite que sus colaboradores más cercanos sigan cobrando horas extras sin registrarlas."
                }
            },
            13: {
                "enunciado": "Llega un transportista foráneo con una gandola de reposición pero la factura de origen presenta errores en las cantidades y precios unitarios:",
                "opciones": {
                    "A": "Recibe la mercancía físicamente, coteja con la orden de compra, emite la nota de recepción con las cantidades reales verificadas y notifica a Compras para la corrección formal.",
                    "B": "Se niega a recibir el camión y lo devuelve a su lugar de origen sin consultar a Logística.",
                    "C": "Firma la factura original como si todo estuviera correcto y asume las diferencias en la agencia.",
                    "D": "Modifica la factura del proveedor con un bolígrafo para que coincida con lo que llegó."
                }
            },
            14: {
                "enunciado": "En relación con las directrices de la Gerencia General y los procesos de fiscalización previa:",
                "opciones": {
                    "A": "He tenido discrepancias de enfoque con mis superiores sobre presupuestos de agencia, pero siempre expuse mis argumentos con balances auditados y acaté la línea final.",
                    "B": "La Gerencia General nunca comprende las verdaderas necesidades operativas que se viven en una agencia.",
                    "C": "Considero que las normas corporativas no aplican cuando se trata de agilizar el trabajo diario.",
                    "D": "En todas las empresas donde he trabajado he tenido directores y gerentes totalmente perfectos y sin ningún defecto."
                }
            },
            15: {
                "enunciado": "Se detecta que un lote de facturas a crédito no cuenta con el soporte de recepción firmado y sellado por los clientes:",
                "opciones": {
                    "A": "Descarta las facturas y las da por incobrables sin hacer ninguna gestión de campo.",
                    "B": "Falsifica las firmas y sellos de los clientes en los comprobantes de recepción para cerrar la auditoría.",
                    "C": "Levanta el inventario de facturas sin soporte, coordina con la supervisión de ventas la recolección urgente de firmas y retiene comisiones asociadas hasta regularizar.",
                    "D": "Le exige al analista de cobranzas que pague las facturas que no tienen soporte físico."
                }
            },
            16: {
                "enunciado": "Al consolidar las variaciones de nómina de la agencia (horas extras, reposos, faltas), nota que se incluyeron horas extras de un colaborador que no tienen aprobación del jefe de área:",
                "opciones": {
                    "A": "Aprueba las horas extras para no generar malestar en el colaborador.",
                    "B": "Modifica las horas de todos los demás trabajadores para que el gasto no se note en el consolidado.",
                    "C": "Se queja del colaborador frente a toda la oficina avergonzándolo públicamente.",
                    "D": "Excluye el concepto no autorizado de la nómina preliminar, consulta con el jefe de área el soporte correspondiente y ajusta la relación definitiva con transparencia."
                }
            },
            17: {
                "enunciado": "La Gerencia General le solicita un plan de optimización de gastos operativos de la agencia para reducir los costos fijos en un 10%:",
                "opciones": {
                    "A": "Audita cada partida presupuestaria (servicios, consumibles, mantenimiento de flota), identifica gastos superfluos y presenta una propuesta técnica viable sin afectar la operatividad.",
                    "B": "Elimina el servicio de agua potable y limpieza de la agencia para recortar costos rápidamente.",
                    "C": "Responde que en la agencia no se puede reducir ni un solo dólar y se niega a enviar el plan.",
                    "D": "Envía cifras de ahorro ficticias que no corresponden a la realidad operativa del negocio."
                }
            },
            18: {
                "enunciado": "Se presenta una falla eléctrica prolongada en la agencia que impide el uso de computadoras durante el cierre de facturación de la tarde:",
                "opciones": {
                    "A": "Despacha a todo el personal a sus hogares a las 2:00 p.m. y cancela los despachos del día siguiente.",
                    "B": "Activa el protocolo de contingencia (generador auxiliar o facturación manual autorizada con registro en libros de control) garantizando la continuidad de la flota.",
                    "C": "Permite la salida de camiones cargados con mercancía sin ningún tipo de guía ni factura de despacho.",
                    "D": "Se sienta a esperar que el servicio eléctrico regrese sin coordinar ninguna acción con el equipo."
                }
            },
            19: {
                "enunciado": "Sobre la reserva y manejo de información financiera confidencial de la agencia:",
                "opciones": {
                    "A": "Comento los montos de facturación diaria y sueldos de la agencia con amigos o familiares cercanos.",
                    "B": "Jamás en toda mi vida he sentido la mínima tentación ni he sentido interés por enterarme de información privada.",
                    "C": "Custodio la información de recaudación, salarios y márgenes bajo estricto sigilo profesional y claves de acceso blindadas.",
                    "D": "Utilizo los reportes financieros de la empresa para compararlos con negocios de la competencia en conversaciones públicas."
                }
            },
            20: {
                "enunciado": "Al revisar las cuentas por cobrar, detecta que una factura de alto monto emitida a un cliente corporativo tiene 45 días de vencida sin gestión documentada:",
                "opciones": {
                    "A": "Da de baja la cuenta por cobrar en el sistema contable sin hacer ninguna llamada al cliente.",
                    "B": "Continúa despachando pedidos al cliente corporativo para no perder la relación comercial.",
                    "C": "Emite el estado de cuenta formal, bloquea la facturación adicional en sistema y coordina una reunión de cobro con el representante legal del cliente.",
                    "D": "Contrata a cobradores externos informales sin la debida autorización de la Gerencia General."
                }
            },
            21: {
                "enunciado": "El sistema administrativo de la agencia presenta lentitud extrema y la analista de facturación no puede emitir los despachos de la flota secundaria:",
                "opciones": {
                    "A": "Insulta al personal de Sistemas por teléfono y paraliza la atención de los clientes.",
                    "B": "Se desentiende del problema argumentando que los sistemas informáticos no son su competencia.",
                    "C": "Envía a los choferes a la calle sin facturas diciéndoles que cobren en efectivo a mano alzada.",
                    "D": "Coordina soporte técnico inmediato con Sistemas, prioriza la facturación de las rutas foráneas más distantes y redistribuye estaciones de trabajo operativas."
                }
            },
            22: {
                "enunciado": "Al realizar el arqueo semanal de divisas para entrega a la relación interna, constata que faltan $100 en la caja de seguridad:",
                "opciones": {
                    "A": "Pone $100 de su dinero personal para tapar el descuadre y evitar una investigación de auditoría.",
                    "B": "Levanta el acta de arqueo formal detallando la diferencia, revisa el libro de entradas/salidas y accesos a la caja fuerte y notifica a la Gerencia General y Auditoría Interna.",
                    "C": "Culpa al mensajero interno antes de verificar los comprobantes de egreso de caja.",
                    "D": "Altera el balance de cierre colocando que el dinero fue entregado al banco."
                }
            },
            23: {
                "enunciado": "La agencia debe renovar con urgencia los permisos de bomberos y sanidad que vencen la próxima semana para evitar clausuras:",
                "opciones": {
                    "A": "Consolida los recaudos técnicos, programa las inspecciones correspondientes, tramita los pagos de tasas y mantiene la cartelera fiscal con las constancias de trámite al día.",
                    "B": "Espera a que los inspectores lleguen a la agencia para negociar un pago informal bajo la mesa.",
                    "C": "Falsifica el sello de renovación en el documento anterior para exhibirlo en la cartelera.",
                    "D": "Posterga el trámite argumentando que la agencia está muy ocupada con las ventas."
                }
            },
            24: {
                "enunciado": "Sobre el manejo de situaciones de alta tensión con subordinados o pares:",
                "opciones": {
                    "A": "Si un colaborador cuestiona una orden mía, le grito para hacer valer mi rango jerárquico.",
                    "B": "He tenido momentos de molestia comprensible ante descuidos operativos, pero corrijo en privado con apego a las normas y sin perder el respeto.",
                    "C": "Tengo una paciencia absoluta e inalterable; absolutamente ningún conflicto o error humano me ha generado enfado jamás.",
                    "D": "Cuando tengo diferencias con un compañero, lo aíslo y me niego a trabajar con su departamento."
                }
            },
            25: {
                "enunciado": "Un cliente acude a la agencia con una factura cancelada exigiendo la entrega inmediata de su pedido, pero en almacén no hay stock disponible:",
                "opciones": {
                    "A": "Le dice al cliente de mala manera que no hay mercancía y que regrese el mes que viene.",
                    "B": "Le entrega mercancía de otro cliente que ya estaba apartada y facturada para salir del paso.",
                    "C": "Le reembolsa dinero en efectivo de la recaudación del día sin emitir nota de crédito ni registrar el egreso.",
                    "D": "Atiende al cliente con cortesía, revisa el cronograma de reposición de gandolas, ofrece alternativas de entrega prioritaria o gestiona la nota de crédito formal si el cliente lo prefiere."
                }
            },
            26: {
                "enunciado": "Al finalizar el mes, el departamento de Logística solicita la aprobación del pago de facturas de fletes que presentan kilometrajes no justificados:",
                "opciones": {
                    "A": "Aprueba los pagos de fletes sin revisar para mantener una buena relación con los transportistas.",
                    "B": "Retiene las facturas observadas, solicita la auditoría de rutas y guías de despacho a Logística y autoriza exclusivamente los servicios debidamente justificados.",
                    "C": "Rompe las facturas de fletes y prohíbe la entrada de los transportistas a la agencia.",
                    "D": "Le cobra una comisión a los transportistas para agilizarles el pago de las facturas dudosas."
                }
            },
            27: {
                "enunciado": "Se requiere extender la jornada de trabajo hasta altas horas de la noche debido al retraso en la llegada de una gandola con mercancía de alto valor que debe ser recibida y custodiada:",
                "opciones": {
                    "A": "Cierra la agencia a las 5:00 p.m. exacta y deja la gandola estacionada en la calle sin custodia.",
                    "B": "Asume la extensión horaria con liderazgo, coordina la seguridad del recinto, supervisa la recepción administrativa y garantiza el resguardo de la mercancía.",
                    "C": "Se marcha a su casa y le deja toda la responsabilidad de la recepción al vigilante de turno.",
                    "D": "Se queja amargamente frente a los transportistas asegurando que la empresa abusa del personal."
                }
            },
            28: {
                "enunciado": "Debe presentar el informe mensual de gestión de la agencia a la Gerencia General consolidando gastos, cuentas por cobrar, inventarios y variaciones de nómina:",
                "opciones": {
                    "A": "Estructura un informe ejecutivo completo con análisis de desviaciones, cumplimiento de presupuestos, estadísticas de recaudación y recomendaciones operativas.",
                    "B": "Envía capturas de pantalla desordenadas del sistema administrativo sin análisis ni conclusiones.",
                    "C": "Copia el informe del mes pasado cambiando únicamente el encabezado para no perder tiempo.",
                    "D": "Manifiesta que los informes estadísticos son una pérdida de tiempo y que la Gerencia debería ir a la agencia a ver los números."
                }
            },
            29: {
                "enunciado": "En su relación con otros líderes de agencia y evaluaciones corporativas:",
                "opciones": {
                    "A": "Nunca en mi vida profesional he sentido la menor inconformidad ni desacuerdo frente a las decisiones de la junta directiva.",
                    "B": "He tenido discrepancias legítimas con directrices centrales, canalizándolas de manera formal mediante propuestas sustentadas con datos operativos.",
                    "C": "Considero que las demás agencias de la empresa trabajan menos y reciben mejores beneficios que la mía.",
                    "D": "No me interesa colaborar con otras sedes de la empresa porque cada agencia debe competir por su cuenta."
                }
            },
            30: {
                "enunciado": "La Gerencia General le solicita realizar una investigación reservada sobre sospechas de fuga de inventario en el área de despacho de la agencia:",
                "opciones": {
                    "A": "Comenta la investigación con los choferes y despachadores durante el receso de café.",
                    "B": "Se niega a investigar argumentando que no quiere tener problemas con los trabajadores de la agencia.",
                    "C": "Ejecuta la auditoría con absoluta confidencialidad, recopila evidencias en libros de salida y grabaciones, y entrega el informe reservado con recomendaciones a la Gerencia General.",
                    "D": "Altera los registros de inventario para encubrir a los sospechosos si son empleados antiguos."
                }
            }
        }
    },

    # =========================================================================
    # 18. COORDINADOR DE PROCESOS (CJS-CPR)
    # =========================================================================
    "18_COORDINADOR_DE_PROCESOS": {
        "codigo": "CJS-CPR",
        "titulo": "EVALUACIÓN PSICOTÉCNICA SITUACIONAL EN COORDINACIÓN DE PROCESOS",
        "instrucciones": "Lea con detenimiento cada situación operativa, de auditoría interna y estandarización de procesos. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con objetividad sobre su criterio técnico, capacidad de resolver controversias y apego a normas. Dispone de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "Al auditar los procesos en curso del área de Facturación y Liquidación, detecta que los analistas aplican criterios distintos para emitir Notas de Débito por fletes y gastos financieros:",
                "opciones": {
                    "A": "Permite que cada analista continúe aplicando su propio criterio para evitar discusiones operativas.",
                    "B": "Elimina las Notas de Débito del sistema contable para que nadie tenga que calcularlas.",
                    "C": "Le dice a los analistas que cobren los gastos en efectivo por fuera del sistema administrativo.",
                    "D": "Mapea el flujo actual, diseña un procedimiento estándar unificado para Notas de Débito con el líder de área, valida con Gerencia y capacita al personal para su cumplimiento formal."
                }
            },
            2: {
                "enunciado": "En la revisión semanal de Abonos y Sobrantes de caja, nota que un cajero presenta un sobrante recurrente de divisas que no está respaldado por recibos ni diferencias cambiarias explicadas:",
                "opciones": {
                    "A": "Se reparte el sobrante de dinero en efectivo con el cajero al finalizar el arqueo semanal.",
                    "B": "Frena la autorización del movimiento, audita las transacciones de la semana comprobando el origen de los fondos, levanta la minuta técnica y reporta a Gerencia Administrativa.",
                    "C": "Modifica los registros del sistema para que el sobrante desaparezca y el arqueo cuadre en cero.",
                    "D": "Insulta al cajero en el pasillo central de la empresa acusándolo de robo delante de todos."
                }
            },
            3: {
                "enunciado": "Al revisar las Devoluciones Manuales y Automáticas del mes, constata que el 40% de las devoluciones manuales carecen del soporte físico de motivo firmado por Almacén y Administración:",
                "opciones": {
                    "A": "Levanta la no conformidad, frena la validación de las devoluciones sin soporte, audita el inventario físico con Almacén e implementa el plan de acción correctivo con los líderes de área.",
                    "B": "Autoriza las devoluciones manuales sin soporte para que los analistas no se retrasen en el cierre.",
                    "C": "Rompe los reportes de devoluciones para que los auditores externos no detecten las fallas.",
                    "D": "Despide a todos los analistas de liquidación de forma inmediata sin consultar con la Gerencia."
                }
            },
            4: {
                "enunciado": "En su trayectoria profesional y manejo de controversias en auditorías internas:",
                "opciones": {
                    "A": "Si un líder de departamento no está de acuerdo con mi informe de procesos, le dejo de hablar y lo saboteo.",
                    "B": "En ocasiones he sentido resistencia o tensión al auditar y corregir malas prácticas arraigadas en el personal, pero mantengo la firmeza metodológica, el respeto y la pedagogía.",
                    "C": "Jamás en toda mi vida profesional he sentido la menor frustración, duda ni cansancio mental al implementar un nuevo proceso.",
                    "D": "Prefiero no auditar a los departamentos difíciles para evitar ganarme antipatías en la oficina."
                }
            },
            5: {
                "enunciado": "En la revisión mensual de Caja Moneda Extranjera y Caja Consumo Interno, detecta que se realizaron compras de suministros de oficina pagadas en divisas sin factura legal:",
                "opciones": {
                    "A": "Registra los egresos sin soporte asignándolos a cuentas de pérdidas diversas sin investigar.",
                    "B": "Bota los recibos informales a la basura para que el arqueo de moneda extranjera cuadre a la fuerza.",
                    "C": "Le pide al encargado de caja que reponga el dinero en efectivo de su propio sueldo en ese instante.",
                    "D": "Levanta el arqueo con la observación de falta de soporte fiscal, establece el procedimiento de legalización de comprobantes y define el protocolo estricto para compras por caja chica."
                }
            },
            6: {
                "enunciado": "Al evaluar el proceso de compras e inventarios, constata que Compras emite órdenes sin verificar la existencia física en almacén, generando sobrestock de rubros de baja rotación:",
                "opciones": {
                    "A": "Prohíbe que el departamento de compras vuelva a realizar pedidos durante tres meses.",
                    "B": "Se desentiende del problema argumentando que las compras son responsabilidad del departamento comercial.",
                    "C": "Diseña e implementa el flujo de integración Compras-Inventarios, estableciendo la validación de stock mínimo y máximo antes de autorizar cualquier orden en el sistema administrativo.",
                    "D": "Modifica las fechas de vencimiento de los productos en sobrestock para que parezcan nuevos."
                }
            },
            7: {
                "enunciado": "Durante la revisión mensual de movimientos internos y ajustes administrativos, observa que se han realizado 15 ajustes manuales de inventario sin memorando de justificación:",
                "opciones": {
                    "A": "Audita cada ajuste manual contra los conteos físicos de almacén, identifica a los usuarios que ejecutaron los movimientos, solicita las justificaciones formales y restringe los accesos.",
                    "B": "Aprueba los ajustes manuales a ciegas asumiendo que los jefes de almacén saben lo que hacen.",
                    "C": "Elimina el módulo de ajustes del sistema administrativo para que nadie pueda corregir errores.",
                    "D": "Cobra una comisión en efectivo a los almacenistas por validarles los ajustes sin soporte."
                }
            },
            8: {
                "enunciado": "Son las 5:45 p.m. (su hora de salida habitual es a las 6:00 p.m.) y la Gerencia General le solicita con urgencia el informe de conciliación de procesos de cierre para una junta directiva mañana a primera hora:",
                "opciones": {
                    "A": "Asume la extensión horaria con compromiso profesional, consolida las métricas de las áreas administrativas, valida los indicadores de cierre y deja el informe ejecutivo entregado.",
                    "B": "Apaga su computador a las 6:00 p.m. puntual diciendo que los informes urgentes se piden en la mañana.",
                    "C": "Envía un informe con cifras inventadas para salir del paso y marcharse a su casa a tiempo.",
                    "D": "Se queja a gritos en el pasillo insultando a la Gerencia por exigir reportes al final de la jornada."
                }
            },
            9: {
                "enunciado": "Respecto a la objetividad técnica y la imparcialidad en la evaluación de procesos:",
                "opciones": {
                    "A": "Jamás en ninguno de mis empleos anteriores he cometido un error de análisis estadístico ni he tenido un sesgo personal al auditar un departamento.",
                    "B": "Considero normal encubrir las fallas de los amigos de trabajo cuando me toca auditar sus áreas.",
                    "C": "Evalúo los procesos basándome estrictamente en datos numéricos, manuales de procedimiento y evidencias documentales, manteniendo total imparcialidad técnica.",
                    "D": "Si un proceso sale mal evaluado, prefiero culpar al software administrativo para no señalar personas."
                }
            },
            10: {
                "enunciado": "Un líder de área le ofrece regalos personales para que no reporte en el informe mensual que su departamento tiene retrasos graves en la conciliación bancaria:",
                "opciones": {
                    "A": "Acepta los obsequios y maquilla las estadísticas del informe para que el área parezca eficiente.",
                    "B": "Negocia que los regalos sean de mayor valor a cambio de no auditar su departamento durante un año.",
                    "C": "Se apropia de los estados de cuenta bancarios para esconder los retrasos del líder de área.",
                    "D": "Rechaza la propuesta de forma categórica, reafirma la ética de control de gestión y presenta el informe real con el plan de acción necesario para regularizar los atrasos."
                }
            },
            11: {
                "enunciado": "Al diseñar e implementar un nuevo proceso de liquidación de rutas para reducir el tiempo de espera de los choferes, los analistas antiguos se resisten a usar el nuevo formato digital:",
                "opciones": {
                    "A": "Cancela el nuevo proceso y permite que los analistas sigan trabajando con hojas sueltas manuales.",
                    "B": "Amonesta y sanciona a los analistas de inmediato sin explicarles el funcionamiento del cambio.",
                    "C": "Desarrolla sesiones de inducción y capacitación práctica, demuestra cómo el nuevo flujo reduce la carga laboral, acompaña la transición y mide la mejora en tiempos de respuesta.",
                    "D": "Bota a la basura las computadoras de los analistas que se quejen del nuevo proceso."
                }
            },
            12: {
                "enunciado": "En la revisión mensual de conciliaciones bancarias, nota que dos cuentas en moneda nacional presentan partidas en tránsito de más de 90 días sin conciliar:",
                "opciones": {
                    "A": "Borra las partidas en tránsito del libro mayor para que la cuenta bancaria cuadre a la fuerza.",
                    "B": "Convoca al analista de conciliación y al contador, reconstruye el histórico de las partidas abiertas, exige los soportes bancarios y establece la regularización definitiva del saldo.",
                    "C": "Deja las partidas abiertas indefinidamente argumentando que los bancos siempre tienen diferencias.",
                    "D": "Le exige al analista de conciliación que pague las diferencias bancarias de su propio bolsillo."
                }
            },
            13: {
                "enunciado": "La Gerencia le solicita identificar con los líderes de área las principales fugas de tiempo y cuellos de botella en el ciclo Comercial-Facturación-Despacho:",
                "opciones": {
                    "A": "Realiza un levantamiento de tiempos y movimientos en cada etapa, analiza la integración de sistemas, identifica duplicidades de funciones y formula el plan de optimización con metas medibles.",
                    "B": "Envía un correo con dos líneas diciendo que todo el retraso es culpa exclusiva de los choferes.",
                    "C": "Modifica los horarios de trabajo de los empleados a su capricho sin consultar con Talento Humano.",
                    "D": "Se niega a realizar el estudio afirmando que medir tiempos no es trabajo de un coordinador."
                }
            },
            14: {
                "enunciado": "En su relación con directivos y gerencias funcionales en empleos anteriores:",
                "opciones": {
                    "A": "He tenido divergencias técnicas sobre el rediseño de un proceso con gerentes de área, pero sustenté mi propuesta en indicadores estadísticos de eficiencia y acaté la decisión corporativa.",
                    "B": "Los gerentes de administración nunca entienden nada sobre cómo se estandarizan los procesos.",
                    "C": "No tolero que nadie opine sobre mis manuales de procedimiento porque mi metodología es infalible.",
                    "D": "En todas las empresas donde he laborado he tenido directores y jefes de área absolutamente perfectos que jamás cometieron un error de procedimiento."
                }
            },
            15: {
                "enunciado": "Al auditar el proceso de Cobranzas, detecta que los analistas no notifican oportunamente el listado de clientes bloqueados por mora a la fuerza de ventas:",
                "opciones": {
                    "A": "Oculta el hallazgo para no generar fricciones entre el departamento de cobranzas y los vendedores.",
                    "B": "Diseña un proceso automatizado de alerta diaria de clientes bloqueados en el sistema administrativo, establece la responsabilidad del envío a primera hora y capacita al equipo comercial.",
                    "C": "Prohíbe que la empresa le vuelva a vender a crédito a ningún cliente del maestro.",
                    "D": "Insulta a los analistas de cobranza acusándolos de negligencia delante de la fuerza de ventas."
                }
            },
            16: {
                "enunciado": "Se detecta que el personal de nuevo ingreso en el departamento administrativo comete errores recurrentes en la digitación de facturas y notas de crédito:",
                "opciones": {
                    "A": "Diseña y dirige un programa estructurado de inducción y capacitación técnica en el manejo del sistema administrativo, evalúa el aprendizaje y realiza seguimiento a la curva de error.",
                    "B": "Solicita el despido inmediato de todos los nuevos ingresos sin darles oportunidad de capacitarse.",
                    "C": "Asume usted mismo la digitación de todas las facturas y notas de crédito de los nuevos empleados.",
                    "D": "Deja que sigan cometiendo errores argumentando que la práctica hace al maestro."
                }
            },
            17: {
                "enunciado": "Al revisar los abonos de clientes ingresados en el sistema administrativo, encuentra recibos de caja provisionales que no fueron cruzados contra los estados de cuenta bancarios:",
                "opciones": {
                    "A": "Valida los abonos provisionales de forma automática para reducir la cartera morosa en el papel.",
                    "B": "Rompe los recibos de caja provisionales para que los clientes tengan que pagar de nuevo.",
                    "C": "Revisa la comprobación bancaria real de cada abono antes de autorizar la aplicación en cuenta, identifica los pendientes por conciliar y formaliza el protocolo de validación semanal.",
                    "D": "Le cobra un recargo personal en efectivo a los clientes por revisarles los recibos provisionales."
                }
            },
            18: {
                "enunciado": "Dos jefaturas departamentales no se ponen de acuerdo sobre quién debe custodiar y archivar físicamente las guías de despacho selladas por los clientes:",
                "opciones": {
                    "A": "Tira las guías de despacho al suelo del pasillo para que ellos decidan quién las recoge.",
                    "B": "Analiza el flujo documental, la providencia legal y la cadena de custodia, define con claridad el alcance de cada cargo en el manual de procedimientos y somete la resolución a Gerencia.",
                    "C": "Bota las copias de las guías de despacho a la basura diciendo que el papel ya no se usa.",
                    "D": "Se lava las manos y deja que los dos jefes resuelvan la disputa peleando en la oficina."
                }
            },
            19: {
                "enunciado": "Sobre la confidencialidad de la información financiera, márgenes y estadísticas corporativas:",
                "opciones": {
                    "A": "Comparto los informes de rentabilidad y procesos internos de la empresa con amigos en reuniones sociales.",
                    "B": "Jamás en toda mi vida profesional he sentido la mínima curiosidad por mirar un informe que no me corresponda.",
                    "C": "Manejo la información estadística, auditorías de procesos y datos administrativos bajo estricta reserva, ética profesional y protocolos de seguridad de la información.",
                    "D": "Si una empresa competidora me ofrece dinero, le facilito los manuales de procesos de la compañía."
                }
            },
            20: {
                "enunciado": "Al auditar el módulo de Inventarios en el sistema administrativo, detecta que hay artículos con costo promedio negativo debido a errores en la secuencia de registro de entradas y salidas:",
                "opciones": {
                    "A": "Deja los costos en negativo argumentando que los sistemas informáticos siempre tienen fallas.",
                    "B": "Borra los artículos del sistema administrativo para que no aparezcan en los balances generales.",
                    "C": "Rastrea la secuencia cronológica de transacciones que generó la distorsión, coordina con Contabilidad y Sistemas el recálculo formal de costos y estandariza el procedimiento de carga.",
                    "D": "Altera manualmente las listas de precios de venta para compensar los costos negativos."
                }
            },
            21: {
                "enunciado": "Durante la revisión mensual de Devoluciones Automáticas, nota que el sistema rechaza notas de crédito por diferencias de centavos entre el precio de venta y el precio devuelto:",
                "opciones": {
                    "A": "Ajusta la parametrización de tolerancia de redondeo en el software administrativo junto a Sistemas, documenta la regla técnica y elabora el plan de acción para evitar reprocesos.",
                    "B": "Obliga a los clientes a pagar los centavos de diferencia en efectivo para poder procesar la devolución.",
                    "C": "Anula todas las devoluciones automáticas y exige que se hagan únicamente a mano con bolígrafo.",
                    "D": "Se niega a revisar el sistema argumentando que los problemas informáticos le tocan a Sistemas."
                }
            },
            22: {
                "enunciado": "Se requiere elaborar el informe periódico de actividades de control y verificación de procesos para la Gerencia General:",
                "opciones": {
                    "A": "Envía un mensaje de texto diciendo que todos los procesos de la empresa funcionan a la perfección.",
                    "B": "Estructura el informe consolidando auditorías realizadas (devoluciones, abonos, cajas, conciliaciones), desvíos detectados, estado de los planes de acción e impacto en la eficiencia.",
                    "C": "Copia el informe del mes pasado cambiando únicamente las fechas para salir rápido del paso.",
                    "D": "Manifiesta que los informes de procesos son innecesarios porque los jefes ya conocen su trabajo."
                }
            },
            23: {
                "enunciado": "Al auditar el proceso de recepción de compras, detecta que Almacén recibe materias primas sin que el proveedor entregue la factura o nota de entrega formal:",
                "opciones": {
                    "A": "Diseña e implementa el protocolo de recepción ciega controlada y prohíbe el ingreso formal a inventario disponible sin documento mercantil legal, garantizando el control interno.",
                    "B": "Permite que sigan recibiendo sin papeles argumentando que lo importante es tener mercancía.",
                    "C": "Le dice al personal de almacén que esconda la materia prima sin papeles en un sótano.",
                    "D": "Insulta al chofer del proveedor y le prohíbe la entrada a la planta de por vida."
                }
            },
            24: {
                "enunciado": "Sobre el autocontrol emocional ante auditorías complejas o detección de irregularidades graves:",
                "opciones": {
                    "A": "Si detecto un fraude en una caja, me pongo a gritar e insultar a todos los empleados del área.",
                    "B": "He enfrentado hallazgos delicados en revisiones de procesos, pero mantengo la serenidad, la objetividad analítica, la reserva y procedo según el protocolo formal de investigación.",
                    "C": "Poseo una templanza celestial inalterable; absolutamente ningún hallazgo de auditoría ni discusión de trabajo me ha causado estrés o preocupación jamás.",
                    "D": "Cuando me saturo de revisar procesos, apago la computadora y me marcho a descansar sin avisar."
                }
            },
            25: {
                "enunciado": "Un supervisor le solicita que apruebe en el informe mensual una serie de devoluciones manuales que no tienen soporte, asegurando que él se hace responsable de palabra:",
                "opciones": {
                    "A": "Aprueba las devoluciones sin soporte confiando en la palabra del supervisor.",
                    "B": "Le cobra una tarifa personal en efectivo al supervisor para aprobarle las devoluciones dudosas.",
                    "C": "Destruye los registros de esas devoluciones para que no queden rastros en el sistema.",
                    "D": "Rechaza la aprobación sin soporte físico reglamentario, recuerda que la normativa exige firmas autorizadas y asienta la no conformidad en el informe de control de procesos."
                }
            },
            26: {
                "enunciado": "Al auditar el proceso de caja chica en moneda extranjera, detecta que se realizaron préstamos personales provisionales con dinero de la empresa registrados en papelitos sueltos:",
                "opciones": {
                    "A": "Guarda los papelitos en su bolsillo y acepta que se sigan prestando divisas de la caja chica.",
                    "B": "Frena de inmediato la práctica irregular, exige la restitución formal de los fondos, levanta el acta de auditoría a la Gerencia y estandariza el manual de custodia de caja.",
                    "C": "Pide prestado dinero en divisas de la caja chica para sus propios gastos personales.",
                    "D": "Quema los papelitos sueltos para que nadie se entere de los préstamos irregulares."
                }
            },
            27: {
                "enunciado": "Se requiere extender la jornada de trabajo para culminar la auditoría de un arqueo imprevisto de almacén ordenado por Presidencia ante un descuadre masivo:",
                "opciones": {
                    "A": "Se marcha a las 6:00 p.m. puntual diciendo que las auditorías imprevistas deben hacerse en horario de oficina.",
                    "B": "Asume la extensión con alto sentido de compromiso y rigor técnico, ejecuta el conteo y validación de movimientos en sistema y entrega el informe reservado a Presidencia.",
                    "C": "Firma el arqueo sin contar las paletas para poder irse a su casa temprano.",
                    "D": "Se queja a gritos en el andén asegurando que en esa empresa no respetan el horario de los empleados."
                }
            },
            28: {
                "enunciado": "Al revisar los expedientes de procesos y manuales de procedimientos de la organización:",
                "opciones": {
                    "A": "Mantiene los flujogramas, manuales de cargos y procedimientos actualizados, con control de versiones digital y físico, disponibles para auditorías y accesibles a los líderes de área.",
                    "B": "Deja los manuales amontonados en una caja húmeda sin clasificar ni actualizar desde hace años.",
                    "C": "Bota los manuales de procedimientos a la basura diciendo que las normas escritas no sirven de nada.",
                    "D": "Altera los manuales para inventar funciones que no corresponden a los cargos de la empresa."
                }
            },
            29: {
                "enunciado": "En su relación con otros coordinadores de la organización y reconocimientos laborales:",
                "opciones": {
                    "A": "Jamás en toda mi vida profesional he sentido la menor envidia, molestia o recelo cuando felicitan o promueven a otro coordinador de departamento.",
                    "B": "En ocasiones he sentido sana emulación profesional ante el reconocimiento de otros, pero me concentro en que los procesos de la empresa sean eficientes, blindados y transparentes.",
                    "C": "Pienso que cuando felicitan a un coordinador es únicamente por compadrazgo con los directores.",
                    "D": "No me gusta relacionarme con los otros coordinadores porque todos buscan sabotear el trabajo de mi área."
                }
            },
            30: {
                "enunciado": "Presidencia le encomienda realizar una auditoría reservada y confidencial sobre presunta manipulación de ajustes administrativos en la Gerencia de Compras:",
                "opciones": {
                    "A": "Le avisa al Gerente de Compras sobre la investigación para que acomode los papeles antes de la revisión.",
                    "B": "Se niega a realizar la auditoría argumentando que auditar compras le genera problemas internos.",
                    "C": "Ejecuta la auditoría con absoluto sigilo profesional: coteja compras vs. entradas de almacén, valida precios, analiza ajustes y entrega el informe reservado y fundamentado a Presidencia.",
                    "D": "Modifica las evidencias en el informe para encubrir compras irregulares de personas amigas."
                }
            }
        }
    },

    # =========================================================================
    # 19. COORDINADOR DE TALENTO HUMANO (CJS-CTH)
    # =========================================================================
    "19_COORDINADOR_DE_TALENTO_HUMANO": {
        "codigo": "CJS-CTH",
        "titulo": "EVALUACIÓN PSICOTÉCNICA SITUACIONAL EN COORDINACIÓN DE TALENTO HUMANO",
        "instrucciones": "Lea con atención cada situación laboral, de gestión de personas y normativa legal. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con absoluta honestidad sobre su criterio de liderazgo, confidencialidad, mediación y apego a la ley. Dispone de un máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "Un supervisor de operaciones le exige contratar de inmediato a un familiar directo para un cargo de chofer de reparto, saltándose las pruebas psicotécnicas, la validación de referencias y el examen médico preempleo:",
                "opciones": {
                    "A": "Contrata al familiar de inmediato para evitar roces con el supervisor operativo.",
                    "B": "Le pide al familiar que empiece a trabajar sin contrato ni papeles legales.",
                    "C": "Falsifica los resultados de las pruebas psicotécnicas para que el expediente parezca aprobado.",
                    "D": "Explica con firmeza técnica que las políticas de selección y reclutamiento son de obligatorio cumplimiento para garantizar la idoneidad y seguridad de la empresa, e incorpora al candidato al proceso regular."
                }
            },
            2: {
                "enunciado": "Al procesar la prenómina quincenal dentro del lapso establecido, un trabajador acude a su oficina reclamando que no le aplicaron una cuota de descuento por préstamo personal que él solicitó retrasar verbalmente:",
                "opciones": {
                    "A": "Modifica la prenómina borrando el préstamo del sistema sin autorización formal.",
                    "B": "Revisa el contrato de préstamo firmado, explica que todo ajuste de cuotas requiere solicitud escrita con visto bueno de Gerencia, aplica el descuento legal y orienta al colaborador en el trámite reglamentario.",
                    "C": "Le presta dinero en efectivo de su propio bolsillo para compensar el descuento.",
                    "D": "Discute a gritos con el trabajador acusándolo de querer estafar a la compañía."
                }
            },
            3: {
                "enunciado": "Al auditar los expedientes del personal que manipula alimentos en el almacén, detecta que 6 trabajadores tienen los certificados de salud y manipulación de alimentos (Ministerio de Salud/Sanidad) vencidos:",
                "opciones": {
                    "A": "Levanta la relación de inmediato, coordina con la jefatura de almacén las jornadas de renovación médica ante las autoridades de sanidad y gestiona la regularización para evitar sanciones y clausuras.",
                    "B": "Oculta los expedientes vencidos esperando que no se presente ninguna inspección sanitaria.",
                    "C": "Pone sellos falsificados en los certificados médicos para simular que están vigentes.",
                    "D": "Despide a los 6 trabajadores de forma inmediata y sin liquidación por tener los papeles vencidos."
                }
            },
            4: {
                "enunciado": "En su trayectoria profesional y manejo de reclamos laborales bajo presión:",
                "opciones": {
                    "A": "Si un trabajador entra a mi oficina en tono alterado, le cierro la puerta en la cara y me niego a escucharlo.",
                    "B": "En ocasiones he sentido desgaste emocional al mediar despidos o conflictos graves entre colaboradores, pero mantengo la compostura, la empatía y la firmeza institucional.",
                    "C": "Jamás en toda mi vida laboral he sentido la más mínima tensión, duda ni agotamiento mental al resolver un conflicto entre empleados.",
                    "D": "Prefiero no atender consultas de los trabajadores para que no me quiten tiempo en mis labores de oficina."
                }
            },
            5: {
                "enunciado": "Dos líderes departamentales tienen un fuerte enfrentamiento personal en el pasillo que afecta el clima laboral y paraliza la coordinación entre Almacén y Ventas:",
                "opciones": {
                    "A": "Se pone del lado del líder que mejor le cae y le prohíbe la entrada a la oficina al otro.",
                    "B": "Redacta una circular pública burlándose de ambos líderes frente a toda la empresa.",
                    "C": "Ignora la disputa argumentando que los problemas personales no le competen a Talento Humano.",
                    "D": "Convoca a ambos colaboradores a una sesión privada de mediación, analiza las causas objetivas del conflicto, establece acuerdos de trabajo respetuosos y formaliza el seguimiento en actas."
                }
            },
            6: {
                "enunciado": "Al momento de preparar la premiación del 'Empleado del Mes' y la celebración de los cumpleañeros, el comité organizador sugiere suspender el evento para no interrumpir la jornada:",
                "opciones": {
                    "A": "Cancela el evento definitivamente y nunca más vuelve a programar actividades de bienestar.",
                    "B": "Defiende el valor de los programas de bienestar y motivación, coordina una pausa planificada que no afecte la productividad y ejecuta el reconocimiento formal impulsando el sentido de pertenencia.",
                    "C": "Utiliza el presupuesto de los cumpleañeros para hacer una fiesta privada fuera de la empresa.",
                    "D": "Entrega el premio del empleado del mes a su propio asistente sin haber evaluado a nadie."
                }
            },
            7: {
                "enunciado": "Se requiere procesar el finiquito y liquidación de prestaciones sociales de un colaborador que renunció voluntariamente tras 3 años de servicio:",
                "opciones": {
                    "A": "Calcula los conceptos de ley con exactitud matemática (antigüedad, vacaciones, utilidades fraccionadas), prepara el finiquito documentado, convoca al trabajador y formaliza el pago y descargo legal.",
                    "B": "Retiene el pago de la liquidación durante meses como castigo por haberse ido de la empresa.",
                    "C": "Modifica la fecha de ingreso en el expediente para pagarle la mitad de lo que le corresponde por ley.",
                    "D": "Le entrega el dinero en un sobre sin recibo ni desglose legal de conceptos."
                }
            },
            8: {
                "enunciado": "Son las 4:55 p.m. (su hora de salida habitual es a las 5:00 p.m.) y la Gerencia General le solicita con urgencia la prenómina consolidada y reportes de incidencias para autorizar los pagos de mañana:",
                "opciones": {
                    "A": "Asume la extensión horaria con responsabilidad, verifica cierres de asistencia, horas extras y préstamos, y entrega la prenómina auditada para garantizar el pago puntual del personal.",
                    "B": "Apaga su computador a las 5:00 p.m. puntual diciendo que la nómina puede esperar hasta el lunes.",
                    "C": "Envía la prenómina con datos incompletos y sin revisar para poder irse a su casa a tiempo.",
                    "D": "Se queja a gritos en el pasillo insultando a la Gerencia por pedir datos a última hora."
                }
            },
            9: {
                "enunciado": "Respecto a la confidencialidad de los expedientes del personal y datos salariales:",
                "opciones": {
                    "A": "Jamás en toda mi vida profesional he sentido la mínima curiosidad ni he mirado un expediente ajeno fuera de mi estricta función laboral.",
                    "B": "Considero normal comentar los sueldos y descuentos de los jefes con amigos durante el almuerzo.",
                    "C": "Custodio la información salarial, expedientes de los trabajadores y datos familiares bajo estricta reserva, ética profesional y archivos protegidos bajo llave.",
                    "D": "Si un trabajador me cae mal, publico en la cartelera las sanciones y amonestaciones que tiene."
                }
            },
            10: {
                "enunciado": "Un colaborador le solicita en privado que no le descuente en nómina un adelanto de sueldo que solicitó, prometiendo devolvérselo a usted en efectivo a fin de mes:",
                "opciones": {
                    "A": "Acepta el trato y no registra el descuento en el sistema para beneficiar a su amigo.",
                    "B": "Le cobra un porcentaje de interés personal al trabajador para no aplicarle el descuento.",
                    "C": "Elimina el registro del adelanto en la base de datos de administración.",
                    "D": "Rechaza la propuesta de inmediato, explica la obligatoriedad de la transparencia en remuneraciones y aplica los descuentos según el cronograma legal establecido."
                }
            },
            11: {
                "enunciado": "Al entregar los formatos de evaluación de desempeño a los jefes y supervisores, nota que varios supervisores califican a todos sus subordinados con la nota máxima sin haberlos evaluado:",
                "opciones": {
                    "A": "Acepta las evaluaciones infladas sin cuestionar para no tener trabajo adicional.",
                    "B": "Modifica las notas a mano colocándole malas calificaciones a los que a usted le caigan mal.",
                    "C": "Se reúne con los supervisores, explica los criterios objetivos de medición, la importancia del feedback para la capacitación y exige una evaluación fundamentada en resultados reales.",
                    "D": "Bota los formatos de evaluación a la papelera argumentando que evaluar no sirve para nada."
                }
            },
            12: {
                "enunciado": "Un funcionario de un organismo del Estado (Ministerio del Trabajo / Inspectoría) se presenta en la sede solicitando la solvencia laboral, registros de asistencia y contratos del personal:",
                "opciones": {
                    "A": "Se esconde en el archivo y se niega a atender al funcionario público por miedo a multas.",
                    "B": "Atiende la inspección con profesionalismo, suministra la documentación formal solicitada, levanta la minuta de visita y notifica de inmediato a la Gerencia General y Legal.",
                    "C": "Ofrece dinero en efectivo al funcionario para que se retire sin revisar los libros de asistencia.",
                    "D": "Discute de forma agresiva con el inspector acusándolo de perseguir a la empresa privada."
                }
            },
            13: {
                "enunciado": "Durante el diseño del programa anual de capacitación, los trabajadores solicitan talleres de manejo de estrés y liderazgo, pero la dirección pide enfocarse en productividad operativa:",
                "opciones": {
                    "A": "Estructura un plan equilibrado que integra la formación en competencias técnicas de productividad con módulos de bienestar y relaciones humanas, demostrando a Gerencia el impacto integral.",
                    "B": "Cancela el plan de capacitaciones diciendo que no se puede complacer a ambas partes.",
                    "C": "Contrata a familiares suyos para dar charlas improvisadas sin experiencia profesional.",
                    "D": "Elabora informes falsos de capacitaciones que nunca se dictaron para cumplir ante la ley."
                }
            },
            14: {
                "enunciado": "En su relación con directivos y decisiones de desvinculación laboral en empleos previos:",
                "opciones": {
                    "A": "He tenido divergencias técnicas sobre la procedencia de una sanción con directivos, pero siempre presenté los soportes legales correspondientes y acaté la decisión final corporativa.",
                    "B": "Los directivos de las empresas nunca se preocupan por el bienestar de los trabajadores.",
                    "C": "No permito que nadie opine sobre contrataciones porque la selección es exclusiva mía.",
                    "D": "En todas las empresas donde he laborado he tenido gerentes generales absolutamente perfectos y libres de cualquier falla humana."
                }
            },
            15: {
                "enunciado": "Al revisar el registro de datos personales y grupo familiar de los colaboradores, nota que más del 30% de los expedientes carecen de actas de matrimonio y partidas de nacimiento de los hijos:",
                "opciones": {
                    "A": "Deja los expedientes incompletos asumiendo que esos recaudos no son importantes.",
                    "B": "Organiza una jornada interna de actualización de datos, emite circulares informativas con fecha límite y completa los expedientes garantizando los beneficios de ley a la familia.",
                    "C": "Elimina a las cargas familiares del sistema para no tener que pagar beneficios contractuales.",
                    "D": "Falsifica los documentos civiles de los familiares para cerrar las carpetas rápido."
                }
            },
            16: {
                "enunciado": "Se acerca el aniversario de la empresa y las festividades de fin de año, y se requiere planificar las actividades culturales y deportivas con presupuesto restringido:",
                "opciones": {
                    "A": "Suspende todas las actividades diciendo que sin presupuesto alto no vale la pena celebrar nada.",
                    "B": "Gasta el doble del presupuesto asignado sin autorización de la Gerencia General.",
                    "C": "Cobra una entrada obligatoria en dólares a los trabajadores para poder costear el evento.",
                    "D": "Diseña un plan creativo y austero: coordina torneos deportivos internos, reconocimientos de antigüedad, gestiona convenios institucionales y fomenta la integración sin exceder los costos."
                }
            },
            17: {
                "enunciado": "Al momento de realizar la inducción a un grupo de 5 nuevos ingresos, el supervisor de área exige que los trabajadores pasen directo al andén a cargar sin recibir la inducción:",
                "opciones": {
                    "A": "Hace valer el protocolo institucional: imparte la inducción en políticas, seguridad integral y normativas, y entrega formalmente al personal capacitado para evitar accidentes y bajas tempranas.",
                    "B": "Deja que los trabajadores ingresen a laborar sin explicarles normas de seguridad ni políticas.",
                    "C": "Les entrega un folleto arrugado en la puerta y les dice que lean mientras van cargando bultos.",
                    "D": "Despide a los trabajadores nuevos porque el supervisor se mostró impaciente."
                }
            },
            18: {
                "enunciado": "Un colaborador acude a Talento Humano denunciando una situación de acoso laboral (mobbing) por parte de su jefe inmediato:",
                "opciones": {
                    "A": "Le dice al colaborador que no sea exagerado y que aprenda a aguantar la presión del trabajo.",
                    "B": "Recibe la denuncia con empatía y estricta confidencialidad, aplica el protocolo de investigación interna, toma declaraciones a las partes y remite el informe objetivo a la Dirección.",
                    "C": "Comenta la denuncia con los demás empleados en el comedor durante el almuerzo.",
                    "D": "Amonesta al trabajador que denunció por considerar que genera chismes en la empresa."
                }
            },
            19: {
                "enunciado": "Sobre la honestidad y el manejo de recursos destinados a eventos de bienestar y dotaciones:",
                "opciones": {
                    "A": "Me llevo los uniformes sobrantes, combos de comida o premios de rifas a mi casa para mi uso personal.",
                    "B": "Jamás en toda mi vida he sentido el más mínimo deseo de tomar un premio ni beneficio que no me corresponda.",
                    "C": "Administro y resguardo los recursos de bienestar, dotaciones de uniformes y premios con total transparencia, rindiendo cuentas detalladas con facturas y actas de entrega.",
                    "D": "Vendo los uniformes de la empresa a personas ajenas para obtener ingresos propios."
                }
            },
            20: {
                "enunciado": "Al elaborar el informe periódico de actividades de Talento Humano para la Junta Directiva (rotación, ausentismo, contrataciones, finiquitos y capacitaciones):",
                "opciones": {
                    "A": "Envía un correo con dos líneas diciendo que todo el personal se encuentra trabajando normalmente.",
                    "B": "Altera los índices de rotación para ocultar que muchas personas han renunciado en el mes.",
                    "C": "Estructura el informe consolidando métricas objetivas de gestión humana, análisis de clima laboral, efectividad de capacitaciones y propuestas estratégicas de mejora.",
                    "D": "Manifiesta que redactar reportes es una pérdida de tiempo y se niega a presentar cifras."
                }
            },
            21: {
                "enunciado": "Al revisar las solicitudes de permisos médicos, detecta que un trabajador consignó un reposo emitido por un centro de salud con tachaduras evidentes y fecha alterada:",
                "opciones": {
                    "A": "Aprueba el reposo con tachaduras para no tener confrontaciones con el colaborador.",
                    "B": "Rompe el reposo médico y le descuenta los días sin darle oportunidad de aclarar.",
                    "C": "Insulta al trabajador en el pasillo llamándolo mentiroso delante de sus compañeros.",
                    "D": "Retiene la aprobación, valida la autenticidad del documento ante la institución emisora según protocolo, levanta el expediente formal y procede con las medidas disciplinarias de ley."
                }
            },
            22: {
                "enunciado": "Se requiere establecer convenios con instituciones educativas o de salud en beneficio de los colaboradores y sus familias:",
                "opciones": {
                    "A": "Deja pasar la asignación argumentando que a los trabajadores solo les interesa el dinero.",
                    "B": "Identifica necesidades prioritarias del personal, negocia alianzas estratégicas con clínicas, farmacias o institutos técnicos con tarifas preferenciales y difunde los beneficios formalmente.",
                    "C": "Firma convenios con empresas de amigos personales que no ofrecen ningún beneficio real al trabajador.",
                    "D": "Le cobra una comisión a los trabajadores por cada vez que utilicen un convenio de la empresa."
                }
            },
            23: {
                "enunciado": "Durante el cálculo de las remuneraciones del mes, se produce un error en el software administrativo que duplica el pago del bono de puntualidad a un grupo de trabajadores:",
                "opciones": {
                    "A": "Notifica de inmediato la falla al departamento de Sistemas y a la Administración, corrige la prenómina antes de la dispersión bancaria y deja asentado el ajuste con transparencia.",
                    "B": "Permite que se pague el dinero duplicado y le pide a los trabajadores que le compartan la mitad.",
                    "C": "Oculta el error esperando que la administración no revise los montos totales del banco.",
                    "D": "Descuenta el doble del dinero a los trabajadores el mes siguiente sin darles ninguna explicación."
                }
            },
            24: {
                "enunciado": "Sobre el autocontrol emocional ante situaciones de conflicto o discusiones sindicales/laborales:",
                "opciones": {
                    "A": "Si un dirigente o trabajador me alza la voz reclamando un beneficio, le respondo con gritos e insultos.",
                    "B": "He enfrentado discusiones complejas con personal demandante, pero mantengo el autocontrol, el apego al marco legal y una postura serena y conciliadora.",
                    "C": "Poseo una templanza celestial inalterable; absolutamente ningún conflicto ni reclamo laboral me ha generado molestia o incomodidad en toda mi vida.",
                    "D": "Cuando me saturo de reclamos de los trabajadores, me encierro con llave en mi oficina y no atiendo a nadie."
                }
            },
            25: {
                "enunciado": "Un candidato a un cargo clave en la empresa le ofrece pagarle $200 en efectivo si le entrega las preguntas de la evaluación psicotécnica antes de la entrevista:",
                "opciones": {
                    "A": "Acepta el soborno y le facilita las respuestas del test para asegurar su contratación.",
                    "B": "Negocia que le pague $400 por asegurarle el puesto sin hacerle ninguna prueba.",
                    "C": "Le entrega las pruebas a cambio de que el candidato le haga un favor personal en el futuro.",
                    "D": "Rechaza la propuesta de forma tajante, descalifica inmediatamente al candidato por vulneración ética y emite el informe de alerta a la Dirección General."
                }
            },
            26: {
                "enunciado": "Al auditar los registros de asistencia biométrica, constata que un colaborador marca la entrada y salida de un compañero ausente utilizando su carnet:",
                "opciones": {
                    "A": "Guarda silencio para no perjudicar la amistad que mantiene con ambos colaboradores.",
                    "B": "Levanta la no conformidad formal con los videos de seguridad, notifica a la jefatura de área y activa el procedimiento disciplinario contemplado en la ley contra ambos implicados.",
                    "C": "Le cobra una multa personal en efectivo a los trabajadores para no acusarlos ante los directores.",
                    "D": "Borra los registros biométricos del sistema para que no queden evidencias del fraude."
                }
            },
            27: {
                "enunciado": "Se requiere extender la jornada laboral para atender a un colaborador accidentado en ruta foránea y coordinar su ingreso a la clínica bajo la póliza de la empresa:",
                "opciones": {
                    "A": "Se marcha a su casa puntual a las 5:00 p.m. diciendo que los accidentes de ruta le tocan al seguro.",
                    "B": "Asume la contingencia con alta sensibilidad y compromiso humano, gestiona la admisión clínica, contacta a los familiares y acompaña el proceso médico hasta dejarlo a salvo.",
                    "C": "Le dice a la familia del trabajador que ellos mismos resuelvan el ingreso hospitalario.",
                    "D": "Se queja con los médicos de la clínica por tener que esperar la atención del paciente."
                }
            },
            28: {
                "enunciado": "Al momento de archivar los expedientes de personal en el área de archivo central:",
                "opciones": {
                    "A": "Mantiene los expedientes organizados por orden alfabético y departamental, actualizados con sus contratos, evaluaciones y amonestaciones, y resguardados bajo estricto control de llaves.",
                    "B": "Deja los expedientes tirados en el suelo de la oficina expuestos a la vista de cualquier visitante.",
                    "C": "Bota los expedientes de los trabajadores que renunciaron para tener más espacio en los estantes.",
                    "D": "Mezcla los documentos de distintos trabajadores en una sola carpeta sin identificar."
                }
            },
            29: {
                "enunciado": "En su relación con otros profesionales de la organización y aspiraciones de crecimiento:",
                "opciones": {
                    "A": "Jamás en toda mi vida profesional he sentido la mínima envidia o disconformidad cuando premian o felicitan a otro jefe o coordinador de área.",
                    "B": "En ocasiones he sentido sana emulación o deseo de que se valore más el rol de Talento Humano, pero me concentro en que la gestión de personal sea justa, productiva y de excelencia.",
                    "C": "Considero que cuando felicitan a un empleado en la empresa es únicamente por adulación a los dueños.",
                    "D": "Prefiero no tener ningún contacto con los jefes de otras áreas porque todos buscan culpar a RRHH de sus fallas."
                }
            },
            30: {
                "enunciado": "Presidencia le encomienda realizar una auditoría reservada y confidencial sobre denuncias de cobros indebidos de viáticos y horas extras en una gerencia funcional:",
                "opciones": {
                    "A": "Comenta la investigación con los supervisores de esa gerencia durante el desayuno.",
                    "B": "Se niega a realizar la auditoría argumentando que auditar horas extras genera enemigos internos.",
                    "C": "Ejecuta la auditoría con absoluto sigilo profesional: coteja biométricos vs. hojas de ruta y recibos, audita soportes y entrega el informe reservado y sustentado a Presidencia.",
                    "D": "Modifica las cifras del informe para encubrir a colaboradores con los que tiene relación de amistad."
                }
            }
        }
    },

    # =========================================================================
    # 20. COORDINADOR DE OPERACIONES (CJS-COC)
    # =========================================================================
    "20_COORDINADOR_DE_OPERACIONES": {
        "codigo": "CJS-COC",
        "titulo": "EVALUACIÓN PSICOTÉCNICA EN COORDINACIÓN DE OPERACIONES COMERCIALES",
        "instrucciones": "Lea detenidamente cada situación gerencial y operativa. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con honestidad sobre su estilo de liderazgo, apego presupuestario, rigor legal y toma de decisiones. Dispone de un tiempo máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "Al analizar el cierre mensual de la agencia, observa que la Efectividad de Entrega cayó al 78% y la Demanda Insatisfecha subió un 12% debido a cuellos de botella en el despacho matutino:",
                "opciones": {
                    "A": "Modifica los reportes estadísticos para disimular la caída de los indicadores ante la Dirección.",
                    "B": "Culpa exclusivamente a los choferes y exige sanciones masivas sin revisar los procesos internos.",
                    "C": "Cancela las rutas foráneas para maquillar los porcentajes de efectividad en las zonas cercanas.",
                    "D": "Analiza la causa raíz con Almacén y Distribución, estructura un plan de acción correctivo con ventanas de carga escalonadas y hace seguimiento diario a la recuperación de metas."
                }
            },
            2: {
                "enunciado": "Se detecta una variación presupuestaria crítica imprevista por reparaciones mayores de la flota que excede la partida mensual asignada a la agencia:",
                "opciones": {
                    "A": "Paga las reparaciones utilizando dinero en efectivo no declarado de la caja chica.",
                    "B": "Justifica detalladamente la variación por partida ante la Dirección de Administración, proyecta la necesidad con antelación y gestiona la autorización previa formal.",
                    "C": "Detiene todos los camiones de reparto durante un mes para no gastar fondos adicionales.",
                    "D": "Solicita dinero prestado a proveedores externos a título personal comprometiendo a la empresa."
                }
            },
            3: {
                "enunciado": "Al auditar las instalaciones de la agencia, constata que los permisos de bomberos y certificaciones sanitarias vencen en 15 días hábiles:",
                "opciones": {
                    "A": "Activa de inmediato los trámites de renovación, audita extintores e infraestructura con Seguridad Industrial y asegura la vigencia legal para evitar sanciones o cierres.",
                    "B": "Espera a que los entes gubernamentales visiten la sede para iniciar la gestión de permisos.",
                    "C": "Consigue constancias provisionales adulteradas a través de gestores informales.",
                    "D": "Se desentiende del caso argumentando que la permisología es competencia exclusiva de Legal."
                }
            },
            4: {
                "enunciado": "En su trayectoria profesional dirigiendo operaciones de alto nivel:",
                "opciones": {
                    "A": "Si un proyecto corporativo sufre retrasos, abandono la coordinación y culpo a mi equipo.",
                    "B": "En ocasiones he sentido alta presión ante contingencias operativas simultáneas, pero mantengo la claridad analítica, la templanza gerencial y la disciplina en la ejecución.",
                    "C": "Jamás en toda mi vida profesional he sentido estrés, fatiga ni he tenido dudas al tomar decisiones de negocio complejas.",
                    "D": "Prefiero no involucrarme en temas de seguridad industrial para no asumir responsabilidades."
                }
            },
            5: {
                "enunciado": "En el almacén principal se acumula producto no conforme y material retornable (paletas/envases) sin clasificar, invadiendo pasillos de tránsito peatonal:",
                "opciones": {
                    "A": "Ordena botar el material retornable a la basura para despejar el almacén rápidamente.",
                    "B": "Permite que el desorden continúe mientras no ocurra un accidente grave de montacargas.",
                    "C": "Esconde el material en una zona no techada exponiéndolo al deterioro por lluvia.",
                    "D": "Implementa los estándares corporativos de Seguridad, Orden y Limpieza (5S), define áreas delimitadas para mermas y retorna los vacíos según el plan dinámico de ventas."
                }
            },
            6: {
                "enunciado": "Al coordinar con Gestión de Talento, nota un retraso en la entrega de dotaciones e implementos de protección personal (EPP) al personal obrero de la agencia:",
                "opciones": {
                    "A": "Ignora la situación y permite que el personal opere sin calzado de seguridad ni guantes.",
                    "B": "Interviene con Talento Humano y Compras para agilizar la entrega inmediata, garantizando el estricto cumplimiento de los compromisos laborales y de seguridad industrial.",
                    "C": "Le descuenta dinero a los trabajadores para comprar los implementos en el mercado local.",
                    "D": "Suspende las operaciones de la agencia de forma indefinida hasta recibir la dotación."
                }
            },
            7: {
                "enunciado": "La Dirección Comercial propone un incremento del 20% en el volumen de ventas para el próximo trimestre en su zona de influencia:",
                "opciones": {
                    "A": "Elabora el estudio de factibilidad operativa, evalúa capacidad de almacenamiento, flota y recursos presupuestarios, y establece el plan integral de soporte comercial.",
                    "B": "Rechaza el crecimiento comercial de forma tajante diciendo que la agencia ya está al límite.",
                    "C": "Acepta el incremento a ciegas sin verificar si cuenta con la flota necesaria para distribuir.",
                    "D": "Altera los datos de capacidad de los camiones prometiendo despachos imposibles de cumplir."
                }
            },
            8: {
                "enunciado": "Son las 4:55 p.m. (su hora de salida habitual es a las 5:00 p.m.) y una gandola de reposición primaria sufre un vuelco menor en el acceso a la agencia bloqueando el portón principal:",
                "opciones": {
                    "A": "Asume el liderazgo de la contingencia en el sitio, coordina el aseguramiento de la carga, la seguridad de las personas, el despeje vial y la continuidad operativa de la base.",
                    "B": "Se marcha a las 5:00 p.m. exacta aduciendo que el rescate de gandolas le compete a Tránsito.",
                    "C": "Ordena forzar el vehículo accidentado con un montacargas sin evaluar riesgos mecánicos.",
                    "D": "Se encierra en su oficina y apaga su teléfono celular para no atender a los transportistas."
                }
            },
            9: {
                "enunciado": "Respecto al rigor técnico en el seguimiento presupuestario de su agencia:",
                "opciones": {
                    "A": "Jamás en ninguno de mis cargos anteriores he tenido una variación de un solo centavo entre lo presupuestado y lo ejecutado a lo largo de toda mi carrera.",
                    "B": "Considero que elaborar presupuestos detallados por partida es una pérdida de tiempo innecesaria.",
                    "C": "Ejerzo un control presupuestario riguroso, monitorizo desviaciones en tiempo real y justifico técnicamente cualquier requerimiento con base en la rentabilidad del negocio.",
                    "D": "Si una partida presupuestaria se sobregira, prefiero ocultarla reclasificando gastos sin autorización."
                }
            },
            10: {
                "enunciado": "Un proveedor de transporte le propone entregarle una comisión en efectivo si le adjudica de forma exclusiva las rutas de distribución foráneas con tarifas sobrevaloradas:",
                "opciones": {
                    "A": "Acepta el pago informal y firma el contrato de exclusividad con el proveedor costoso.",
                    "B": "Negocia que la comisión sea mayor a cambio de no exigirle pólizas de seguro de carga.",
                    "C": "Comparte el dinero del soborno con los supervisores para mantener la complicidad.",
                    "D": "Rechaza la propuesta de forma categórica, defiende la transparencia corporativa, licita las rutas bajo criterios de costo-eficiencia y reporta el hecho a la Dirección General."
                }
            },
            11: {
                "enunciado": "Al revisar los indicadores de productividad de los almacenes, detecta que los tiempos de carga superan en un 40% el estándar corporativo establecido:",
                "opciones": {
                    "A": "Tolera la lentitud asumiendo que los operarios no pueden mejorar su rendimiento.",
                    "B": "Despide a la cuadrilla de carga sin analizar las fallas mecánicas de los equipos.",
                    "C": "Implementa junto al Jefe de Almacén una estrategia de mejora continua, optimiza la preparación previa (pre-picking) y capacita al personal para alcanzar el estándar.",
                    "D": "Modifica los relojes de control para que parezca que los camiones cargaron a tiempo."
                }
            },
            12: {
                "enunciado": "Se requiere balancear los recursos monetarios de la agencia transfiriendo fondos de la partida de mantenimiento menor a la de combustible debido al aumento de rutas:",
                "opciones": {
                    "A": "Realiza el traslado de dinero de forma clandestina sin solicitar aprobación a nadie.",
                    "B": "Formula la solicitud formal de reclasificación presupuestaria sustentando el impacto operativo y solicita la autorización previa de la Gerencia General antes de ejecutarla.",
                    "C": "Deja a los camiones sin combustible y cancela los despachos a los clientes foráneos.",
                    "D": "Toma fondos destinados al pago de beneficios del personal para cubrir la gasolina."
                }
            },
            13: {
                "enunciado": "Durante una inspección fiscal y parafiscal sorpresiva de los entes gubernamentales en la agencia:",
                "opciones": {
                    "A": "Atiende la fiscalización con solvencia gerencial, presenta los libros contables, solvencias vigentes y soportes de deberes formales, levantando la minuta institucional.",
                    "B": "Cierra las puertas de la agencia y se niega a recibir a los funcionarios públicos.",
                    "C": "Ofrece dádivas a los inspectores para evitar la revisión de la documentación legal.",
                    "D": "Confronta agresivamente a los fiscales acusándolos de persecución comercial."
                }
            },
            14: {
                "enunciado": "En su relación con directores corporativos y decisiones estratégicas en empleos previos:",
                "opciones": {
                    "A": "He tenido divergencias técnicas sobre asignación de inversiones con directores, pero presenté análisis de factibilidad basados en datos y acaté disciplinadamente la directriz final.",
                    "B": "Los directores generales nunca comprenden las complejidades reales de la operación en campo.",
                    "C": "No tolero que supervisen mi agencia porque dentro de mi ámbito territorial mando únicamente yo.",
                    "D": "En todas las empresas donde he laborado he tenido juntas directivas absolutamente perfectas que jamás cometieron un solo error estratégico."
                }
            },
            15: {
                "enunciado": "Al realizar el seguimiento diario de inventarios, detecta una acumulación crítica de productos de baja rotación que vencen en 60 días:",
                "opciones": {
                    "A": "Oculta el producto al fondo del almacén para que no afecte las auditorías visuales.",
                    "B": "Diseña junto a la Dirección Comercial un plan de salida dinámico (promociones, combos, transferencias), minimizando mermas y protegiendo el capital de trabajo.",
                    "C": "Bota la mercancía a la basura antes de que venza para no registrar pérdidas en su gestión.",
                    "D": "Modifica las fechas de vencimiento en el sistema informático para ganar tiempo."
                }
            },
            16: {
                "enunciado": "Un grupo de colaboradores de la agencia amenaza con paralizar los despachos alegando inconformidad con el pago de un beneficio contractual:",
                "opciones": {
                    "A": "Ignora las demandas y amenaza a los trabajadores con despido masivo inmediato.",
                    "B": "Cede a todas las exigencias sin consultar presupuestos ni verificar los contratos vigentes.",
                    "C": "Se marcha de la sede dejando la agencia paralizada y desprotegida.",
                    "D": "Establece una mesa de diálogo junto a Gestión de Talento, revisa los acuerdos formales con objetividad, aclara dudas con base en nómina y restablece la operación."
                }
            },
            17: {
                "enunciado": "Al evaluar el Plan Estratégico de Seguridad Industrial, se detecta que no se han realizado los simulacros de evacuación anuales ni el mantenimiento de la red contra incendios:",
                "opciones": {
                    "A": "Prioriza y presupuesta el mantenimiento de bombas y mangueras, programa los simulacros con Bomberos y asegura que la agencia opere bajo estándares seguros y auditables.",
                    "B": "Firma las planillas de simulacros certificando que se hicieron aunque hayan sido simuladas en papel.",
                    "C": "Desactiva las alarmas contra incendios para evitar que suenen por fallas técnicas.",
                    "D": "Manifiesta que los simulacros son una pérdida de horas hombre que frena la facturación."
                }
            },
            18: {
                "enunciado": "Se plantea una nueva iniciativa corporativa para digitalizar el control de inventarios que requiere capacitar al personal y modificar las rutinas de trabajo:",
                "opciones": {
                    "A": "Rechaza la iniciativa corporativa alegando que el sistema manual antiguo funciona bien.",
                    "B": "Evalúa el impacto en su área, lidera el proyecto de adopción tecnológica, capacita al equipo junto a Sistemas y asegura la alineación con las metas del negocio.",
                    "C": "Deja que los líderes funcionales implementen el sistema solos sin supervisión gerencial.",
                    "D": "Boicotea el proyecto informático reportando fallas falsas a la Dirección General."
                }
            },
            19: {
                "enunciado": "Sobre la reserva y custodia de información estratégica, márgenes y planes de negocio de la agencia:",
                "opciones": {
                    "A": "Comento las debilidades logísticas y márgenes de la empresa con colegas en eventos sociales.",
                    "B": "Jamás en toda mi vida he sentido la mínima curiosidad por proyectos o datos que no me competan.",
                    "C": "Custodio la información operativa, costos de flete, presupuestos y estrategias con estricto secreto profesional y lealtad corporativa.",
                    "D": "Facilito información de costos operativos a agencias competidoras para comparar sueldos."
                }
            },
            20: {
                "enunciado": "En la revisión de los servicios generales y facilidades de la agencia, se reportan fallas continuas en la planta eléctrica de emergencia y en el suministro de agua:",
                "opciones": {
                    "A": "Deja que la planta eléctrica falle y paraliza la facturación cada vez que se interrumpe la red pública.",
                    "B": "Culpa al personal de mantenimiento por el estado de las instalaciones sin asignar recursos.",
                    "C": "Gestiona los mantenimientos preventivos y correctivos, asegura el stock de combustible auxiliar y garantiza el funcionamiento ininterrumpido de las facilidades de la sede.",
                    "D": "Vende las partes mecánicas de la planta eléctrica como chatarra para generar ingresos extras."
                }
            },
            21: {
                "enunciado": "Al auditar las operaciones de ventas, detecta que se están aprobando despachos a zonas de alto riesgo de seguridad vial sin aplicar los protocolos de resguardo:",
                "opciones": {
                    "A": "Suspende de forma definitiva las ventas en todas las zonas periféricas del estado.",
                    "B": "Deja que los camiones sigan saliendo sin escolta ni monitoreo GPS asumiendo el riesgo.",
                    "C": "Le dice a los choferes que compren armas personales para defender la mercancía.",
                    "D": "Revisa las rutas críticas, coordina con Seguridad Patrimonial horarios seguros y seguimiento satelital, y preserva la integridad física del personal y la carga."
                }
            },
            22: {
                "enunciado": "Al finalizar el trimestre, la Gerencia General le solicita la propuesta de presupuesto operativo de su agencia para el ejercicio fiscal siguiente:",
                "opciones": {
                    "A": "Copia el presupuesto del año anterior incrementando un 10% lineal a todas las cuentas sin análisis.",
                    "B": "Construye el presupuesto base cero con los líderes funcionales de su sede, proyecta necesidades reales de flota, almacén y servicios, y sustenta cada partida ante la Gerencia General.",
                    "C": "Pide un monto excesivo no justificado para asegurarse de que le sobre dinero durante el año.",
                    "D": "Se niega a formular el presupuesto diciendo que los gastos deben calcularse mes a mes."
                }
            },
            23: {
                "enunciado": "Se presenta una contradicción operativa entre la meta comercial de despacho inmediato y la política de almacén que exige cuarentena de 24 horas para revisión de calidad:",
                "opciones": {
                    "A": "Hace prevalecer el estándar de calidad y cumplimiento normativo, coordina con Ventas el ajuste de las promesas de entrega y optimiza los tiempos de liberación técnica.",
                    "B": "Salta la revisión de calidad y despacha el producto sin certificación para cumplir la venta.",
                    "C": "Deja que los departamentos de Ventas y Calidad resuelvan la disputa discutiendo en el andén.",
                    "D": "Modifica los reportes de calidad firmando en lugar del laboratorista o inspector."
                }
            },
            24: {
                "enunciado": "Sobre el autocontrol emocional ante situaciones de crisis operativa o accidentes graves:",
                "opciones": {
                    "A": "Si ocurre un incendio o siniestro en la agencia, entro en pánico y abandono el recinto corriendo.",
                    "B": "He enfrentado incidentes operativos severos, pero mantengo la compostura, activo los protocolos de emergencia con serenidad y guío al equipo con liderazgo efectivo.",
                    "C": "Poseo una templanza sobrehumana inalterable; absolutamente ninguna crisis, amenaza ni catástrofe ha perturbado mi pulso jamás en la vida.",
                    "D": "Cuando me saturo de problemas en la agencia, apago mi teléfono y me retiro por varios días."
                }
            },
            25: {
                "enunciado": "Un supervisor funcional de almacén le solicita autorizar el pago de horas extras duplicadas a un grupo de operarios para compensar que no se les otorgó un bono extraordinario:",
                "opciones": {
                    "A": "Aprueba las horas extras fraudulentas para evitarse reclamos del personal obrero.",
                    "B": "Le propone al supervisor repartir el dinero de las horas extras entre los dos.",
                    "C": "Falsifica los reportes de biométrico para que las horas extras cuadren en la nómina.",
                    "D": "Rechaza la solicitud con firmeza, reafirma que la nómina debe reflejar tiempos reales laborados y canaliza formalmente los incentivos a través de las políticas de Talento Humano."
                }
            },
            26: {
                "enunciado": "Durante el monitoreo de materiales retornables, constata que los clientes retienen un 35% de las paletas de la empresa, generando faltantes para la carga de nuevos pedidos:",
                "opciones": {
                    "A": "Compra paletas desechables no certificadas con riesgo de volcamiento de carga pesada.",
                    "B": "Diseña junto a Distribución y Ventas un mecanismo estricto de control y canje paleta por paleta, audita a los clientes morosos de envases y recupera los activos de la empresa.",
                    "C": "Carga a los choferes el costo total de las paletas retenidas por los comerciantes.",
                    "D": "Despacha los productos sin paletas colocándolos sueltos en el piso del camión."
                }
            },
            27: {
                "enunciado": "Se requiere coordinar la logística de atención para una jornada extraordinaria de auditoría corporativa que revisará la agencia durante todo el fin de semana:",
                "opciones": {
                    "A": "Se niega a asistir el fin de semana diciendo que su contrato estipula labores de lunes a viernes.",
                    "B": "Planifica y lidera el soporte operativo, asegura el acceso ordenado a la información y facilidades de la sede, y participa activamente coordinando a su equipo de líderes.",
                    "C": "Deja encargado a un vigilante para que atienda solo a los auditores corporativos.",
                    "D": "Se queja ante los trabajadores asegurando que la Corporación realiza auditorías para hostigar."
                }
            },
            28: {
                "enunciado": "Al revisar los indicadores de gestión financiera de la agencia, observa un incremento desmedido en el costo de flete por tonelada distribuida:",
                "opciones": {
                    "A": "Identifica la causa en la baja densidad de carga y rutas subutilizadas, rediseña el plan dinámico de despacho maximizando el factor de estiba y reduce el costo logístico unitario.",
                    "B": "Oculta el incremento en el informe financiero para que la Gerencia General no le llame la atención.",
                    "C": "Aumenta unilateralmente el precio de venta de los productos para compensar el gasto de flete.",
                    "D": "Cancela el servicio de distribución propia obligando a los clientes a buscar la carga en planta."
                }
            },
            29: {
                "enunciado": "En su relación con otros gerentes de agencia y reconocimientos dentro de la corporación:",
                "opciones": {
                    "A": "Jamás en toda mi vida profesional he sentido el menor recelo o inconformidad cuando otra agencia de la empresa es premiada como la más productiva del año.",
                    "B": "A veces he sentido sana emulación o deseo de que mi equipo lidere los resultados nacionales, pero me concentro en la excelencia operativa, el orden y la rentabilidad de mi sede.",
                    "C": "Considero que cuando premian a otra agencia es únicamente por favoritismo personal de la Dirección.",
                    "D": "No me gusta compartir buenas prácticas con otras agencias porque cada coordinador compite solo."
                }
            },
            30: {
                "enunciado": "La Junta Directiva le encomienda liderar un proyecto piloto reservado para evaluar la viabilidad de abrir una nueva sucursal comercial en una localidad vecina:",
                "opciones": {
                    "A": "Divulga los planes de expansión de la empresa con empresarios locales de la zona evaluada.",
                    "B": "Se niega a realizar el estudio argumentando que su trabajo se limita únicamente a su sede actual.",
                    "C": "Ejecuta el estudio de factibilidad con absoluto sigilo profesional: analiza mercado, rutas, costos operativos, leyes locales y entrega el informe ejecutivo y reservado a la Directiva.",
                    "D": "Altera los datos del estudio de mercado para forzar la apertura de la sucursal en un terreno propio."
                }
            }
        }
    },

    # =========================================================================
    # 21. DESPACHADOR (CJS-DSP)
    # =========================================================================
    "21_DESPACHADOR": {
        "codigo": "CJS-DSP",
        "titulo": "EVALUACIÓN PSICOTÉCNICA SITUACIONAL EN DESPACHO, FLOTA Y LIDERAZGO DE RUTA",
        "instrucciones": "Lea con atención cada situación de distribución, manejo de flota y trato con clientes. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con absoluta honestidad sobre su estilo de liderazgo, resolución de conflictos en calle y apego a normas. Dispone de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "Al chequear la mercancía entregada por Almacén contra el lote de facturas antes de cerrar el camión, detecta que faltan 4 cajas de aceite que figuran como facturadas para el primer cliente de la ruta:",
                "opciones": {
                    "A": "Arranca a la ruta de inmediato esperando que el cliente no cuente los bultos en la descarga.",
                    "B": "Tacha el producto en la factura del cliente con un bolígrafo y le cobra menos dinero sin avisar.",
                    "C": "Le dice a su ayudante que busque 4 cajas de cualquier otro producto para meterlas en el furgón.",
                    "D": "Frena la salida, cuida que no existan faltantes notificando de inmediato al Jefe de Almacén y Facturación, y no arranca hasta cargar el producto o ajustar legalmente la factura."
                }
            },
            2: {
                "enunciado": "A primera hora de la mañana (7:45 a.m.), debe validar las condiciones del vehículo asignado revisando el check-list emitido por Logística y Seguridad:",
                "opciones": {
                    "A": "Firma la planilla a ciegas sin mirar la unidad para poder salir de la planta antes que los demás.",
                    "B": "Revisa minuciosamente niveles de aceite, agua, frenos, neumáticos, luces, extintor y herramientas de seguridad, asentando el estado real y reportando cualquier anomalía antes de encender el motor.",
                    "C": "Ignora que un neumático está bajo de aire y sale a carretera diciendo que en el camino lo calibra.",
                    "D": "Le entrega las llaves al ayudante de despacho para que él maneje el camión sin tener licencia."
                }
            },
            3: {
                "enunciado": "Al llegar a entregar en un supermercado clave, el cliente manifiesta que rechazará 5 bultos porque llegaron aplastados y manchados por mala manipulación dentro de la batea:",
                "opciones": {
                    "A": "Mantiene la calma, notifica en el acto al área de Administración y Ventas, asienta formalmente la devolución en la factura con firma y sello del cliente, y resguarda el producto devuelto.",
                    "B": "Discute agresivamente con el cliente amenazándolo con no volver a llevarle mercancía a su negocio.",
                    "C": "Deja los bultos rotos en la acera y se marcha rápidamente para que el cliente no pueda reclamar.",
                    "D": "Obliga al ayudante a pagar las 5 cajas rotas en efectivo delante de los compradores del local."
                }
            },
            4: {
                "enunciado": "En su trayectoria profesional y liderazgo de cuadrilla bajo presión:",
                "opciones": {
                    "A": "Si la carretera tiene mucho tráfico o cola, me bajo del camión y me voy a almorzar sin avisar.",
                    "B": "En ocasiones he sentido tensión ante retrasos mecánicos o reclamos de clientes en ruta, pero mantengo la serenidad, la actitud de servicio y la coordinación con el equipo.",
                    "C": "Jamás en toda mi vida laboral he sentido el menor estrés, molestia ni cansancio manejando en carretera.",
                    "D": "Prefiero trabajar solo sin ayudantes para no tener que explicarle nada a nadie."
                }
            },
            5: {
                "enunciado": "Un cliente le pide que le desvíe el camión 15 kilómetros fuera de la ruta establecida para descargarle en una bodega privada de un familiar:",
                "opciones": {
                    "A": "Acepta hacer el viaje fuera de ruta para complacer al cliente y gastar combustible de la empresa.",
                    "B": "Le cobra $40 en efectivo al comerciante por hacer el flete clandestino y se gasta el dinero.",
                    "C": "Le presta el camión de la distribuidora al comerciante para que él mismo mueva la carga.",
                    "D": "Explica con firmeza que la unidad tiene uso exclusivo limitado a las rutas autorizadas de la empresa, niega el desvío y coordina la entrega en el local registrado en la factura."
                }
            },
            6: {
                "enunciado": "Al coordinar el orden de carga y entrega de 16 clientes en una ruta que combina pueblos foráneos y zonas céntricas:",
                "opciones": {
                    "A": "Carga los pedidos al azar sin revisar direcciones, teniendo que desarmar el camión en cada parada.",
                    "B": "Ordena las entregas de manera inteligente: estiba al fondo los últimos clientes y adelante los primeros según el itinerario vial, optimizando tiempos de descarga y consumo de combustible.",
                    "C": "Atiende primero a los clientes que le regalan refrescos o comida sin importar la distancia geográfica.",
                    "D": "Deja que el ayudante cargue el camión como pueda mientras usted conversa con otros choferes en el patio."
                }
            },
            7: {
                "enunciado": "Al finalizar la ruta a las 4:30 p.m., el despachador debe retornar a la empresa y procesar el cierre operativo:",
                "opciones": {
                    "A": "Entrega las facturas limpias, ordenadas y firmadas, rinde cuentas del cobro en Administración para liquidar dentro del lapso normativo de 15 horas, descarga el cartón/vacíos y reporta novedades.",
                    "B": "Se lleva las facturas y el dinero de la cobranza para su casa y liquida dos días después.",
                    "C": "Deja el camión abierto en la calle con las llaves pegadas y se va a su casa en mototaxi.",
                    "D": "Bota el cartón de retorno en un terreno baldío para no perder tiempo descargándolo en el almacén."
                }
            },
            8: {
                "enunciado": "Son las 4:50 p.m. (su hora de salida habitual es a las 5:00 p.m.) y al llegar al último cliente de la ruta este le pide esperar 20 minutos mientras consigue el efectivo completo para pagar:",
                "opciones": {
                    "A": "Espera con paciencia y sentido comercial, contacta a Ventas/Administración para validar el cierre, asegura el cobro exacto, entrega la mercancía y regresa a liquidar a la base.",
                    "B": "Le deja la mercancía fiada sin factura firmada ni dinero y arranca el camión a toda prisa.",
                    "C": "Insulta al comerciante a gritos frente a sus empleados y le tira las cajas al suelo.",
                    "D": "Cancela el pedido de inmediato por capricho y se marcha sin intentar coordinar la solución."
                }
            },
            9: {
                "enunciado": "Respecto al cuidado, mantenimiento e higiene del vehículo de carga asignado:",
                "opciones": {
                    "A": "Jamás en ninguno de mis empleos anteriores mi camión ha tenido una falla mecánica, pinchazo de caucho ni una sola mancha de suciedad en la carrocería en toda mi vida.",
                    "B": "Considero que lavar la batea y revisar el aceite del camión es una pérdida de tiempo irrelevante.",
                    "C": "Cuido la unidad asignada con responsabilidad preventiva, mantengo la cabina y furgón limpios y reporto al instante cualquier sonido o desgaste mecánico para alargar su vida útil.",
                    "D": "Si el camión sufre un golpe en la carrocería por un mal cruce, prefiero culpar al vigilante de la planta."
                }
            },
            10: {
                "enunciado": "Un comerciante le propone al despachador pagarle $50 en efectivo si le entrega 3 bultos de un producto que supuestamente 'sobró en el conteo del camión':",
                "opciones": {
                    "A": "Acepta el dinero y le entrega los 3 bultos sobrantes repartiéndose la ganancia con el ayudante.",
                    "B": "Le propone al cliente entregarle mercancía todas las semanas a cambio de una comisión mensual fija.",
                    "C": "Se apropia de la mercancía sobrante y se la lleva para su casa en su bolso particular.",
                    "D": "Rechaza la propuesta con total honestidad, notifica el sobrante a Almacén para el retorno formal a inventario y emite la novedad a la Gerencia Comercial."
                }
            },
            11: {
                "enunciado": "Durante el trayecto de reparto en una carretera con lluvia intensa y curvas pronunciadas:",
                "opciones": {
                    "A": "Maneja a máxima velocidad compitiendo con otros camiones para llegar primero a la ciudad.",
                    "B": "Apaga las luces del camión para ahorrar batería mientras conduce bajo el aguacero.",
                    "C": "Modera la velocidad a los límites de seguridad, aumenta la distancia de frenado al doble, enciende luces de emergencia en zonas de baja visibilidad y protege la carga y la vida del equipo.",
                    "D": "Conduce con una sola mano mientras envía mensajes de texto por el teléfono celular."
                }
            },
            12: {
                "enunciado": "Al momento de entregar en un supermercado, el cliente le pide que le reciba un cheque a fecha diferida de 30 días, cuando la factura emitida por la empresa indica 'Contado Estricto':",
                "opciones": {
                    "A": "Acepta el cheque diferido por su cuenta sin consultar a nadie y le entrega la mercancía al cliente.",
                    "B": "Se comunica de inmediato con la fuerza de ventas y Crédito y Cobranzas para verificar si existe una autorización formal; de no haberla, exige el pago de contado antes de bajar el pedido.",
                    "C": "Rompe la factura del cliente y le regala la mercancía diciendo que la empresa tiene mucho dinero.",
                    "D": "Le cobra $10 al comerciante para recibirle el cheque no autorizado a espaldas de la empresa."
                }
            },
            13: {
                "enunciado": "Durante el recorrido de la ruta, el indicador de presión de aceite del motor se va a cero y suena una alarma en el tablero del camión:",
                "opciones": {
                    "A": "Se detiene de inmediato a la derecha fuera de la vía, apaga el motor para evitar fundirlo, coloca los triángulos de seguridad y reporta la falla a la Coordinación de Logística y Seguridad.",
                    "B": "Sigue manejando a fondo para intentar llegar al próximo pueblo antes de que el camión se apague.",
                    "C": "Desconecta el cable de la alarma del tablero para que deje de sonar y continúa trabajando.",
                    "D": "Abandona el camión cargado en la carretera y se devuelve a su casa en transporte público."
                }
            },
            14: {
                "enunciado": "En su relación con los ayudantes de despacho y compañeros de trabajo:",
                "opciones": {
                    "A": "He tenido diferencias de opinión con ayudantes sobre la forma de descargar bultos, resolviéndolas con diálogo respetuoso, liderazgo claro y dando el ejemplo en la faena.",
                    "B": "Los ayudantes de despacho son todos unos flojos que solo sirven para quejarse del peso.",
                    "C": "No tolero que ningún ayudante me hable dentro de la cabina del camión porque yo soy el jefe.",
                    "D": "En todas las empresas donde he laborado he tenido ayudantes de ruta absolutamente perfectos que jamás cometieron una equivocación."
                }
            },
            15: {
                "enunciado": "Al momento de entregar la mercancía, el ayudante tropieza y se cae un fardo de azúcar rasgándose tres paquetes sobre la acera:",
                "opciones": {
                    "A": "Insulta al ayudante a gritos en medio de la calle y lo amenaza con golpearlo al regresar a la planta.",
                    "B": "Guarda el producto roto en el camión sin decir nada e intenta entregárselo a otro cliente distraído.",
                    "C": "Auxilia a su ayudante verificando que no se haya lastimado, asume la responsabilidad del equipo con madurez, levanta la no conformidad formal y notifica la avería para su liquidación.",
                    "D": "Le exige al dueño del negocio que le pague el fardo de azúcar que se rompió en su acera."
                }
            },
            16: {
                "enunciado": "Al llegar a entregar en un cliente tradicional, el dueño no se encuentra y el encargado del local afirma que no va a firmar ni a sellar la factura porque 'él no está autorizado':",
                "opciones": {
                    "A": "Le deja la mercancía en el negocio sin firma ni sello confiando en la palabra del encargado.",
                    "B": "Falsifica la firma del dueño en la copia de la factura de la empresa para poder irse rápido.",
                    "C": "Bota la mercancía a la basura y le dice al supervisor que el negocio estaba cerrado.",
                    "D": "Explica con respeto que por normas de seguridad no puede soltar carga sin firma y cédula legible; contacta al asesor de ventas para ubicar al dueño y resguarda el pedido en el camión."
                }
            },
            17: {
                "enunciado": "Al estibar la carga en el camión antes de salir a la ruta asignada:",
                "opciones": {
                    "A": "Distribuye el peso de manera uniforme sobre los ejes, coloca los bultos pesados en la base con estiba trabada, asegura los productos frágiles arriba y amarra la carga con trincas seguras.",
                    "B": "Coloca toda la carga pesada en la parte trasera del camión haciendo que la dirección delantera flote.",
                    "C": "Amontona las cajas sueltas sin amarrar dejando que se golpeen contra las compuertas en cada curva.",
                    "D": "Apila sacos de harina pesados directamente sobre cajas de galletas de vidrio sin ninguna protección."
                }
            },
            18: {
                "enunciado": "Al realizar el control diario de consumo de combustible del camión según el kilometraje recorrido en la ruta:",
                "opciones": {
                    "A": "Anota litros y kilometrajes ficticios en la planilla para no tener que bajarse a revisar el tablero.",
                    "B": "Registra con exactitud los kilómetros de salida y llegada, anota el combustible surtido con su factura, controla el rendimiento por kilómetro y reporta cualquier consumo anómalo a Logística.",
                    "C": "Extrae combustible del tanque del camión con una manguera para venderlo en garrafas por su cuenta.",
                    "D": "Deja que el camión se quede sin gasoil en medio de una autopista por descuido."
                }
            },
            19: {
                "enunciado": "Sobre la honradez y la custodia del dinero recaudado por cobranzas en la ruta:",
                "opciones": {
                    "A": "Utilizo el dinero en efectivo que cobro de las facturas para pagar gastos personales y lo repongo después.",
                    "B": "Jamás en toda mi vida he sentido la mínima curiosidad por mirar el dinero ajeno ni he tocado un centavo que no sea mío.",
                    "C": "Custodio cada factura, cheque y dinero en efectivo recaudado con absoluta pulcritud e integridad, entregando el 100% de los fondos en Administración el mismo día.",
                    "D": "Si un cliente me paga una factura de contado, le digo a la empresa que el cliente no pagó para quedarme con el dinero una semana."
                }
            },
            20: {
                "enunciado": "Al llegar a un cliente de ruta foránea, este le plantea una queja muy molesta afirmando que el asesor de ventas le prometió un descuento que no aparece reflejado en la factura:",
                "opciones": {
                    "A": "Le dice al cliente que el vendedor es un estafador y que no le compre más a la distribuidora.",
                    "B": "Rompe la factura delante del cliente y le deja la mercancía gratis para calmar su molestia.",
                    "C": "Escucha la inquietud con empatía y educación, le muestra la factura oficial, contacta de inmediato al asesor de ventas y a la Gerencia Comercial para aclarar la diferencia y concilia la entrega.",
                    "D": "Se da la media vuelta sin responderle y se va del negocio con la mercancía insultando al cliente."
                }
            },
            21: {
                "enunciado": "Al momento de circular por una zona urbana concurrida, el camión roza levemente el retrovisor de un vehículo particular estacionado:",
                "opciones": {
                    "A": "Acelera a fondo para darse a la fuga antes de que el dueño del vehículo particular se dé cuenta.",
                    "B": "Le echa la culpa al ayudante diciéndole que él no le avisó que el carro estaba cerca.",
                    "C": "Amenaza al dueño del carro particular con golpearlo si se atreve a reclamarle el golpe.",
                    "D": "Detiene la marcha en lugar seguro, evalúa el daño con calma y respeto, levanta el reporte formal del incidente y coordina la atención del siniestro con la empresa y el seguro vehicular."
                }
            },
            22: {
                "enunciado": "Al entregar pedidos en una zona de alta afluencia peatonal, el ayudante deja las compuertas traseras del camión abiertas mientras lleva dos cajas a un negocio a 30 metros de distancia:",
                "opciones": {
                    "A": "Se queda sentado dentro de la cabina mirando el teléfono sin vigilar la carga abierta.",
                    "B": "Llama la atención a su ayudante con liderazgo formativo, le recuerda que la compuerta debe cerrarse y asegurarse en cada bajada, y asume la vigilancia de la unidad para evitar hurtos.",
                    "C": "Se baja del camión y se va a tomar café dejando el camión totalmente desprotegido.",
                    "D": "Insulta al ayudante con groserías frente a los peatones en la acera pública."
                }
            },
            23: {
                "enunciado": "Al terminar de descargar los pedidos en el último negocio de la ruta foránea, en la batea del camión quedan regados plásticos, cartones rotos y zunchos de embalaje:",
                "opciones": {
                    "A": "Barre y organiza el furgón del camión junto al ayudante, resguarda los vacíos y cartones de retorno ordenadamente y deja el vehículo higiénico antes de emprender el retorno a planta.",
                    "B": "Bota los plásticos y basuras por la ventana del camión hacia la carretera mientras va manejando.",
                    "C": "Deja la batea llena de basura y dice que el camión lo debe lavar el personal de mantenimiento.",
                    "D": "Quema la basura adentro del camión con riesgo de incendiar la carrocería."
                }
            },
            24: {
                "enunciado": "Sobre el control emocional y la tolerancia a la frustración ante demoras en el andén de carga:",
                "opciones": {
                    "A": "Si el almacén tarda en entregarme la carga a primera hora, golpeo las mesas y me niego a salir a ruta.",
                    "B": "He experimentado demoras operativas en el andén, pero coordino con el equipo de almacén, optimizo el tiempo revisando facturas y mantengo la disposición para salir a tiempo.",
                    "C": "Poseo una serenidad sobrehumana inalterable; absolutamente ningún retraso de carga ni problema de tráfico me ha generado molestia jamás en toda mi vida.",
                    "D": "Cuando me enojo con el Jefe de Almacén, manejo el camión a exceso de velocidad para romper la mercancía."
                }
            },
            25: {
                "enunciado": "Un chofer de otra empresa le propone desviar 5 cajas de mercancía de su camión para venderlas en un mercado informal y repartirse las ganancias a mitad:",
                "opciones": {
                    "A": "Acepta la propuesta y entrega las 5 cajas diciendo en la empresa que se las robaron en la ruta.",
                    "B": "Le propone al otro chofer robarse el camión completo con toda la carga para salir del país.",
                    "C": "Acepta pero le exige al otro chofer que le pague por adelantado en efectivo.",
                    "D": "Rechaza la propuesta de inmediato con total firmeza moral, recuerda que la carga está bajo su custodia legal y reporta la situación a Seguridad y Logística."
                }
            },
            26: {
                "enunciado": "Durante la ruta, el camión presenta una falla menor en una manguera de aire que produce una pequeña fuga pero permite seguir rodando con lentitud:",
                "opciones": {
                    "A": "Ignora la fuga de aire y sigue manejando a alta velocidad con riesgo de quedarse sin frenos.",
                    "B": "Se detiene en una estación de servicio o taller autorizado de la empresa, reporta la novedad a Mantenimiento, efectúa la reparación preventiva y reanuda la ruta de forma segura.",
                    "C": "Amarra la manguera rota con una tira de plástico de embalar y sigue rodando sin reportar nada.",
                    "D": "Deja el camión botado en medio de la carretera y apaga el teléfono corporativo."
                }
            },
            27: {
                "enunciado": "Se requiere extender la jornada de trabajo para completar las entregas de una ruta que sufrió retrasos por un derrumbe vial en la carretera nacional:",
                "opciones": {
                    "A": "Cancela las entregas que faltan y se devuelve a la empresa dejando a los clientes desabastecidos.",
                    "B": "Asume la extensión con compromiso y sentido de servicio, coordina con Logística y los clientes los horarios de llegada y completa la distribución con responsabilidad.",
                    "C": "Remata la mercancía a mitad de precio en la carretera para poder regresar temprano a su casa.",
                    "D": "Se queja a gritos con los clientes asegurando que la empresa es desorganizada."
                }
            },
            28: {
                "enunciado": "Al culminar el turno diario de trabajo en la sede principal:",
                "opciones": {
                    "A": "Estaciona la unidad en el andén asignado, apaga el motor, aplica el freno de estacionamiento, cierra compuertas con precinto/candado, entrega las llaves y reporta el finiquito de ruta.",
                    "B": "Deja el camión estacionado en la calle frente a la empresa con las llaves pegadas y la batea abierta.",
                    "C": "Se lleva el camión de la distribuidora para su casa particular para usarlo de vehículo familiar.",
                    "D": "Deja el camión en neutro sin freno en una pendiente con riesgo de choque contra otros vehículos."
                }
            },
            29: {
                "enunciado": "En su relación con otros despachadores de la empresa y reconocimientos laborales:",
                "opciones": {
                    "A": "Jamás en toda mi vida profesional he sentido la mínima envidia o disconformidad cuando felicitan a otro chofer por su puntualidad y cero mermas.",
                    "B": "En ocasiones he sentido sana emulación o deseo de ser reconocido como el mejor despachador de flota, pero me concentro en cuidar mi vehículo, ser puntual y atender bien a los clientes.",
                    "C": "Pienso que cuando felicitan a un despachador en la empresa es únicamente por amistad íntima con los gerentes.",
                    "D": "No me gusta colaborar con los choferes nuevos porque cada quien debe aprender a manejar solo."
                }
            },
            30: {
                "enunciado": "La Gerencia le solicita realizar un acompañamiento reservado en la ruta de otro camión para auditar presuntas irregularidades en la entrega de facturas de crédito:",
                "opciones": {
                    "A": "Le cuenta al chofer investigado todo lo que la Gerencia le pidió revisar antes de salir a la ruta.",
                    "B": "Se niega a realizar la auditoría argumentando que no le gusta vigilar a sus compañeros de trabajo.",
                    "C": "Ejecuta la auditoría con absoluta reserva y rigor profesional: verifica entregas físicas vs. facturas en mano, constata acuses de recibo y entrega el informe reservado a la Gerencia.",
                    "D": "Altera el informe para encubrir irregularidades del chofer si es su amigo de trabajo."
                }
            }
        }
    },

    # =========================================================================
    # 22. MANTENIMIENTO Y LIMPIEZA INTEGRAL (CJS-MNL)
    # =========================================================================
    "22_MANTENIMIENTO_Y_LIMPIEZA": {
        "codigo": "CJS-MNL",
        "titulo": "EVALUACIÓN PSICOTÉCNICA SITUACIONAL EN MANTENIMIENTO Y LIMPIEZA INTEGRAL",
        "instrucciones": "Lea con atención cada situación laboral y de higiene en las instalaciones. Marque con una equis [X] una sola opción (A, B, C o D) por pregunta. Responda con honestidad sobre su forma real de trabajar, cuidar los equipos y aplicar las normas de seguridad. Dispone de un máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "Al realizar la limpieza de la franja sanitaria de separación entre la pared y la primera estiba del almacén principal, nota acumulación de polvo, telarañas y restos de cartón detrás de una paleta:",
                "opciones": {
                    "A": "Pasa por encima barriendo solo por donde se ve a simple vista en el pasillo principal.",
                    "B": "Tapa la suciedad empujando los bultos contra la pared para que no se note la falta de aseo.",
                    "C": "Le dice a los montacarguistas que limpien ellos porque mover cajas da mucho trabajo.",
                    "D": "Utiliza los implementos adecuados, despeja la franja sanitaria respetando la distancia de pared, retira los residuos y deja el perímetro libre para el control de plagas y auditorías."
                }
            },
            2: {
                "enunciado": "Al ingresar a limpiar las oficinas administrativas y de ventas, encuentra escritorios con computadoras encendidas, pantallas y documentos importantes sobre los mesones:",
                "opciones": {
                    "A": "Pasa un trapo empapado en agua con cloro directamente sobre los teclados y pantallas.",
                    "B": "Desempolva con paño de microfibra seco o ligeramente humedecido con producto antiestático, sin mover papeles de su sitio y cuidando no desconectar ni mojar los cables y equipos.",
                    "C": "Apaga las computadoras desconectando los cables de la pared de golpe para terminar rápido.",
                    "D": "Revuelve los documentos confidenciales de los escritorios para ver qué información contienen."
                }
            },
            3: {
                "enunciado": "Al revisar el área de los baños a media mañana, nota que se agotó el papel higiénico, el jabón líquido y las toallas de mano, y el piso está mojado con riesgo de resbalones:",
                "opciones": {
                    "A": "Coloca de inmediato el aviso preventivo de 'Piso Húmedo', seca el suelo, desinfecta lavamanos e inodoros y repone oportunamente el papel, jabón y toallas en sus dispensadores.",
                    "B": "Cierra la puerta del baño con llave para que nadie entre hasta el final de la tarde.",
                    "C": "Deja el piso mojado sin colocar advertencias asumiendo que los empleados deben caminar con cuidado.",
                    "D": "Pone papel periódico y espera que el piso se seque sin colocar ningún aviso preventivo."
                }
            },
            4: {
                "enunciado": "En su rutina de trabajo y ejecución física de faenas pesadas:",
                "opciones": {
                    "A": "Si alguien ensucia el piso recién trapeado, le lanzo el tobo de agua sucia a los pies.",
                    "B": "En ocasiones he sentido fatiga física o calor ante jornadas de limpieza profunda en almacenes, pero mantengo el ritmo, el aseo y el orden de las áreas asignadas.",
                    "C": "Jamás en toda mi vida he sentido pereza, cansancio ni he sudado durante una faena de limpieza pesada.",
                    "D": "Prefiero esconder los implementos de limpieza para que nadie me pida limpiar imprevistos."
                }
            },
            5: {
                "enunciado": "En la zona de carga y descarga y área de montacargas, se derrama aceite hidráulico en el piso mientras una gandola espera para ser llenada con pedidos:",
                "opciones": {
                    "A": "Echa agua con jabón sobre el aceite aumentando el riesgo de patinazos del montacargas.",
                    "B": "Se desentiende del derrame argumentando que el aceite es culpa exclusiva del chofer.",
                    "C": "Tapa el charco de aceite colocando paletas de madera encima para que la gente pase.",
                    "D": "Delimita la zona con conos o señalización, aplica material absorbente (aserrín o arena), recoge los residuos contaminados y desengrasa la superficie dejando el área segura."
                }
            },
            6: {
                "enunciado": "Al momento de preparar los químicos para limpiar baños y pisos (cloro, desengrasante, desinfectante), su supervisor le recuerda el uso obligatorio de los Guantes y Equipos de Protección (EPI):",
                "opciones": {
                    "A": "Mezcla cloro puro con desengrasante y ácido en un envase cerrado inhalando los gases tóxicos.",
                    "B": "Se niega a usar los guantes argumentando que le hacen sudar las manos y le quitan velocidad.",
                    "C": "Utiliza los guantes de goma asignados, calzado de seguridad y dosifica los productos químicos con las proporciones adecuadas para proteger su salud y las instalaciones.",
                    "D": "Prepara los químicos con las manos desnudas y salpica las paredes para que huela a limpio."
                }
            },
            7: {
                "enunciado": "Al finalizar la jornada de limpieza en la cocina y comedor de la empresa, quedan platos sucios en el fregadero y restos de comida sobre las mesas del personal:",
                "opciones": {
                    "A": "Lava y desinfecta el fregadero, limpia mesones y electrodomésticos, retira las sobras de comida en bolsas selladas y deja el comedor higienizado para evitar plagas.",
                    "B": "Deja los restos de comida en las mesas diciendo que el que comió debe limpiar su desorden.",
                    "C": "Tira los platos sucios a la basura para no tener que fregarlos al final de la tarde.",
                    "D": "Pasa un trapo sucio sobre las mesas regando la grasa sin aplicar ningún producto desinfectante."
                }
            },
            8: {
                "enunciado": "Son las 5:45 p.m. (su hora de salida habitual es a las 6:00 p.m.) y en el pasillo principal de la administración se rompe un termo grande de café manchando el piso y ventanales:",
                "opciones": {
                    "A": "Asume la contingencia con disposición, coloca el aviso de precaución, recoge los vidrios y limpia la mancha de café dejando el pasillo pulcro antes de retirarse.",
                    "B": "Apaga las luces y se marcha a las 5:50 p.m. diciendo que a esa hora ya no le corresponde limpiar.",
                    "C": "Cubre el charco de café con una alfombra vieja para que nadie lo note hasta el día siguiente.",
                    "D": "Se queja a gritos e insulta a los empleados de administración por ser descuidados."
                }
            },
            9: {
                "enunciado": "Respecto al cuidado, reporte y resguardo de los suministros de limpieza:",
                "opciones": {
                    "A": "Jamás en ninguno de mis empleos anteriores se me ha desgastado, roto o extraviado un coleto, cepillo o esponja de limpieza.",
                    "B": "Considero que llevar un inventario de cloro y jabón es una tontería porque son productos baratos.",
                    "C": "Llevo un control responsable de los suministros, utilizo las cantidades justas sin desperdiciar y solicito con tiempo el reabastecimiento antes de que se agoten.",
                    "D": "Si se acaba el desinfectante en la oficina, simplemente limpio solo con agua de la llave sin avisar."
                }
            },
            10: {
                "enunciado": "Un compañero de trabajo le pide que le regale un galón de cloro y un paquete de papel higiénico del depósito de la empresa para llevárselo a su casa:",
                "opciones": {
                    "A": "Le entrega los productos a espaldas de la gerencia para ganarse la simpatía de su compañero.",
                    "B": "Le propone vender los materiales de limpieza de la empresa afuera y repartir el dinero.",
                    "C": "Le dice que los tome él mismo para que usted no tenga responsabilidad si los descubren.",
                    "D": "Rechaza la solicitud con firmeza, explica que los suministros son para uso exclusivo de las instalaciones de la empresa y resguarda el depósito bajo llave."
                }
            },
            11: {
                "enunciado": "Debe realizar la limpieza de cristales, ventanales altos y espejos en el área de recepción y oficinas:",
                "opciones": {
                    "A": "Limpia los vidrios usando trapos con grasa dejando los cristales manchados y opacos.",
                    "B": "Se sube sobre una silla de oficina con ruedas para alcanzar las ventanas altas arriesgándose a caer.",
                    "C": "Utiliza limpiavidrios adecuado, paño suave sin pelusas o haragán, y emplea una escalera tipo tijera estable y segura respetando las normas de seguridad industrial.",
                    "D": "Golpea los vidrios con fuerza para quitar el polvo sin importarle romperlos."
                }
            },
            12: {
                "enunciado": "En la zona de preparación de pedidos del almacén (picking), el piso acumula restos de plástico elástico (zunchos y envoplast) que pueden enredarse en las ruedas de las transpaletas:",
                "opciones": {
                    "A": "Pasa por el lado sin recoger los plásticos argumentando que esa área le toca a los almacenistas.",
                    "B": "Barre y despeja de inmediato la zona de preparación, embolsa los plásticos en los contenedores de reciclaje y mantiene el paso de las carretillas libre de obstrucciones.",
                    "C": "Patea los zunchos de plástico debajo de los estantes para que no se vean en el medio.",
                    "D": "Prende fuego a los plásticos en una esquina del almacén para eliminarlos más rápido."
                }
            },
            13: {
                "enunciado": "Al mover un mueble pesado en el área de gerencia para limpiar el rodapié, tropieza accidentalmente con una lámpara decorativa y se quiebra la base:",
                "opciones": {
                    "A": "Notifica de inmediato el accidente a su jefe inmediato, recoge con cuidado los fragmentos para evitar cortes y asume la situación con honestidad y transparencia.",
                    "B": "Esconde la lámpara rota en la papelera y niega saber lo que ocurrió cuando pregunten.",
                    "C": "Le echa la culpa al vigilante de turno afirmando que él debió haber roto la lámpara de noche.",
                    "D": "Pega la base con cinta adhesiva disimuladamente para que se le caiga a la persona que la toque después."
                }
            },
            14: {
                "enunciado": "En relación con las instrucciones y supervisión de sus tareas diarias:",
                "opciones": {
                    "A": "He tenido llamados de atención sobre rincones que no quedaron del todo limpios, pero acepté la corrección con humildad y repasé el área hasta dejarla perfecta.",
                    "B": "Los jefes de oficina nunca valoran el esfuerzo físico de la persona que limpia.",
                    "C": "No tolero que nadie revise si dejé los baños limpios porque sé perfectamente cómo hacer mi faena.",
                    "D": "En todos mis trabajos anteriores he tenido supervisores absolutamente perfectos que jamás me encontraron una sola mota de polvo."
                }
            },
            15: {
                "enunciado": "Durante la rutina de desecho de basura al final de la tarde, nota que las bolsas negras de los contenedores principales están rotas y gotean líquidos en el piso del pasillo:",
                "opciones": {
                    "A": "Arrastra las bolsas rotas por todo el pasillo dejando un camino de suciedad hasta la calle.",
                    "B": "Deja la basura en los pasillos de la oficina durante todo el fin de semana para no ensuciarse.",
                    "C": "Coloca una bolsa doble para contener el derrame, traslada los desechos con cuidado al depósito externo y trapea de inmediato el líquido derramado desinfectando la zona.",
                    "D": "Bota la basura en el estacionamiento de los clientes para terminar más rápido."
                }
            },
            16: {
                "enunciado": "La empresa le encomienda la responsabilidad de abrir oficinas a primera hora (7:45 a.m.), encender luces, y al final de la jornada apagar aires acondicionados, luces y cerrar accesos:",
                "opciones": {
                    "A": "Deja las puertas abiertas y los aires acondicionados encendidos toda la noche por descuido.",
                    "B": "Se va antes de la hora dejando las luces prendidas y las llaves pegadas en la cerradura exterior.",
                    "C": "Se niega a encender y apagar equipos diciendo que su única función es pasar coleto.",
                    "D": "Cumple puntualmente con los horarios de apertura y cierre, verifica que los equipos no operativos queden apagados, apaga luces y asegura puertas resguardando la infraestructura."
                }
            },
            17: {
                "enunciado": "Al limpiar las paredes y puertas del área de ventas, observa manchas de grasa y huellas de manos acumuladas cerca de los interruptores de luz:",
                "opciones": {
                    "A": "Aplica agua jabonosa suave con esponja no abrasiva, retira las manchas cuidando no humedecer los interruptores eléctricos y seca las superficies dejando la pintura intacta.",
                    "B": "Raspa las paredes con una espátula de metal pelando la pintura para quitar la mancha.",
                    "C": "Pinta con un marcador encima de las manchas para tapar la suciedad de forma rápida.",
                    "D": "Deja las paredes sucias diciendo que no le corresponde limpiar huellas de otros empleados."
                }
            },
            18: {
                "enunciado": "Se produce una fuga de agua imprevista en una tubería del lavamanos de un baño inundando el pasillo de la administración:",
                "opciones": {
                    "A": "Se queda mirando la inundación sin hacer nada esperando que llegue un plomero externo.",
                    "B": "Cierra la llave de paso de agua inmediatamente para frenar la fuga, coloca la advertencia de peligro, retira el agua con haragán/mopa y reporta la avería técnica al supervisor.",
                    "C": "Cierra la puerta del pasillo y se va a almorzar dejando que el agua llegue a las oficinas.",
                    "D": "Se queja con los empleados diciendo que los baños de esa empresa no sirven para nada."
                }
            },
            19: {
                "enunciado": "Sobre la honradez y el respeto por objetos personales o dinero olvidado en las oficinas:",
                "opciones": {
                    "A": "Si veo billetes sueltos o monedas sobre un escritorio vacío, me los guardo en el bolsillo sin decir nada.",
                    "B": "Jamás en toda mi vida he sentido la mínima curiosidad por mirar un objeto ajeno ni he tocado nada que no sea mío.",
                    "C": "Cuando encuentro dinero, cargadores, teléfonos u objetos olvidados en escritorios o baños, los entrego intactos de inmediato a la Gerencia o a su dueño.",
                    "D": "Si encuentro pertenencias ajenas en la oficina, las boto al cesto de basura para no tener que cargarlas."
                }
            },
            20: {
                "enunciado": "En la limpieza profunda del almacén, se requiere mover estanterías bajas y tarimas vacías para barrer el polvo acumulado en el piso:",
                "opciones": {
                    "A": "Barre solo alrededor de las tarimas dejando una capa gruesa de suciedad debajo de ellas.",
                    "B": "Lanza las tarimas de madera bruscamente contra los productos terminados para apartarlas.",
                    "C": "Mueve las tarimas con cuidado manteniendo posturas ergonómicas (espalda recta y rodillas flexionadas), barre a fondo, desinfecta el área y reubica el mobiliario en orden.",
                    "D": "Se niega a mover las tarimas argumentando que el trabajo de almacén es exclusivo de los hombres."
                }
            },
            21: {
                "enunciado": "Al momento de llenar el reporte diario de tareas asignadas (baños, oficinas, comedor, almacén), no le dio tiempo de limpiar los vidrios del pasillo central:",
                "opciones": {
                    "A": "Marca en el reporte que limpió los vidrios al 100% fingiendo haber culminado la labor.",
                    "B": "Rompe la hoja de reporte para no tener que dar explicaciones sobre las tareas del día.",
                    "C": "Acusa a los recepcionistas de haberle impedido trabajar para justificar el retraso.",
                    "D": "Registra con honestidad las áreas completadas, anota la tarea pendiente en el informe y la prioriza a primera hora del día siguiente coordinando con su supervisor."
                }
            },
            22: {
                "enunciado": "En el comedor de la empresa, el microondas presenta acumulación de salpicaduras de comida y malos olores por falta de aseo de los usuarios:",
                "opciones": {
                    "A": "Desconecta el microondas y lo bota a la basura para que nadie más caliente comida.",
                    "B": "Limpia y desinfecta el interior y exterior del electrodoméstico con productos aptos para uso alimentario, elimina olores y deja el equipo higiénico y operativo para el personal.",
                    "C": "Pasa el mismo coleto del piso por dentro del microondas para limpiar más rápido.",
                    "D": "Pega un cartel insultando a todos los empleados de la empresa por ser desordenados."
                }
            },
            23: {
                "enunciado": "Se requiere apoyar en la movilización de material de oficina y mobiliario (mesas y archivadores vacíos) por remodelación de un departamento:",
                "opciones": {
                    "A": "Colabora activamente con el equipo, mueve el mobiliario con precaución cuidando paredes y pisos de rayones, y deja las áreas despejadas y limpias.",
                    "B": "Arrastra los muebles pesados por el piso rayando toda la superficie de porcelanato o madera.",
                    "C": "Se niega rotundamente a mover nada afirmando que a él solo lo contrataron para barrer y coletear.",
                    "D": "Golpea los muebles contra las puertas para demostrar su enojo por el trabajo adicional."
                }
            },
            24: {
                "enunciado": "Sobre el control emocional y las relaciones con el personal de otras áreas:",
                "opciones": {
                    "A": "Si alguien me pide que limpie un derrame justo cuando acabo de terminar, le respondo a gritos e insultos.",
                    "B": "He tenido momentos de fastidio cuando pisan el piso recién trapeado, pero comprendo la dinámica del trabajo, mantengo la educación y repaso la zona con cortesía.",
                    "C": "Poseo una paz interior perfecta; absolutamente ninguna falta de respeto ni descuido ajeno me ha hecho sentir la más mínima molestia jamás.",
                    "D": "Cuando me enojo con un departamento, dejo los baños de esa área sucios durante una semana como castigo."
                }
            },
            25: {
                "enunciado": "Un proveedor de químicos de limpieza le ofrece entregarle envases con producto adulterado o rebajado con agua a cambio de compartir el dinero de la factura:",
                "opciones": {
                    "A": "Acepta los productos rebajados para ganarse un dinero extra con el proveedor.",
                    "B": "Le propone al proveedor no entregar ningún producto y dividirse el pago completo de la empresa.",
                    "C": "Acepta el producto dañado y le echa la culpa a la empresa por comprar químicos de mala calidad.",
                    "D": "Rechaza rotundamente la propuesta, defiende la calidad de los insumos y la seguridad de las instalaciones, y notifica de inmediato el intento de fraude a la Administración."
                }
            },
            26: {
                "enunciado": "Al limpiar los mesones y accesorios de los baños, nota una fuga de agua permanente en el tanque del inodoro que genera desperdicio constante:",
                "opciones": {
                    "A": "Ignora la fuga de agua dejando que el tanque bote agua durante meses.",
                    "B": "Reporta la anomalía en el formato de mantenimiento preventivo a su jefe inmediato para su pronta reparación, cerrando la llave de arresto si el bote es abundante.",
                    "C": "Golpea el inodoro con un martillo intentando arreglarlo a la fuerza y termina quebrando la losa.",
                    "D": "Cierra el baño con candado para no tener que reportar nada a la administración."
                }
            },
            27: {
                "enunciado": "Se requiere extender la jornada de trabajo 45 minutos para apoyar en la limpieza y desinfección profunda del almacén previo a una inspección sanitaria gubernamental:",
                "opciones": {
                    "A": "Se niega a quedarse argumentando que a las 6:00 p.m. suelta el cepillo esté como esté la sede.",
                    "B": "Asume la extensión con compromiso y responsabilidad, apoya en el lavado y desinfección de pisos y paredes, y asegura que las instalaciones queden en óptimas condiciones.",
                    "C": "Se queda en el trabajo pero se esconde detrás de las estibas del almacén para no hacer nada.",
                    "D": "Se queja a gritos con los compañeros asegurando que la empresa abusa del personal obrero."
                }
            },
            28: {
                "enunciado": "Al terminar su faena diaria, los implementos de trabajo (mopas, tobo, escobas, cepillos y bayetas) quedan sucios y con residuos de agua estancada:",
                "opciones": {
                    "A": "Lava, escurre y desinfecta las mopas y bayetas, vacía y enjuaga los tobos, cuelga las escobas para no deformar las cerdas y deja el cuarto de limpieza pulcro y ventilado.",
                    "B": "Deja el agua sucia dentro del tobo con la mopa remojada pudriéndose hasta el día siguiente.",
                    "C": "Tira los implementos mojados en medio del pasillo para que los empleados tropiecen.",
                    "D": "Bota los cepillos a la basura todos los días para que la empresa tenga que comprar nuevos."
                }
            },
            29: {
                "enunciado": "En su relación con otros compañeros de servicios generales y reconocimientos laborales:",
                "opciones": {
                    "A": "Jamás en toda mi vida he sentido la mínima envidia, recelo o inconformidad cuando felicitan a otro trabajador por su buen desempeño.",
                    "B": "En ocasiones he sentido sana emulación o deseo de que también reconozcan mi esfuerzo, pero me concentro en que mis áreas sean las más limpias e higiénicas de la sede.",
                    "C": "Pienso que cuando felicitan a un empleado de limpieza es únicamente porque es un chismoso de los jefes.",
                    "D": "No me gusta hablar con nadie de la empresa porque todos los compañeros de trabajo son falsos."
                }
            },
            30: {
                "enunciado": "La Gerencia le solicita revisar discretamente los botes de basura y casilleros de un área común ante sospechas de consumo de sustancias no permitidas o desvío de herramientas:",
                "opciones": {
                    "A": "Comenta la solicitud con todos los empleados en el comedor durante el desayuno.",
                    "B": "Se niega a colaborar argumentando que revisar papeleras no es parte de su trabajo.",
                    "C": "Ejecuta la labor de limpieza e inspección con absoluta reserva y discreción profesional, reportando cualquier hallazgo de manera privada y confidencial a la Gerencia.",
                    "D": "Altera los contenedores para encubrir a compañeros amigos que hayan dejado objetos indebidos."
                }
            }
        }
    },

    # =========================================================================
    # 23. MERCADERISTA / PROMOCIÓN Y GESTIÓN COMERCIAL (CJS-MPR)
    # =========================================================================
    "23_MERCADERISTA": {
        "codigo": "CJS-MPR",
        "titulo": "EVALUACIÓN PSICOTÉCNICA SITUACIONAL EN PROMOCIÓN Y GESTIÓN COMERCIAL",
        "instrucciones": "Lea con atención cada situación laboral en el punto de venta. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con honestidad sobre su desempeño en piso de venta, cuidado de activos de la empresa y relación con clientes y vendedores. Dispone de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "Al visitar un supermercado catalogado como 'Punto de Venta Vitrina', nota que la nevera o exhibidor propio de la empresa está lleno de botellas y productos de una marca competidora:",
                "opciones": {
                    "A": "Deja los productos de la competencia adentro para no incomodar al encargado del comercio.",
                    "B": "Desconecta el equipo comercial para que los productos de la competencia se dañen.",
                    "C": "Llena el exhibidor con más productos ajenos para llenar los espacios vacíos rápidamente.",
                    "D": "Conversa con el gerente de tienda recordando el contrato de exclusividad del activo, retira con cuidado el producto ajeno, limpia el equipo y lo llena al 100% con el portafolio de la empresa."
                }
            },
            2: {
                "enunciado": "Durante la jornada en un comercio de alto tráfico, el asesor de ventas de la ruta le pide que le apoye cerrando una venta y cobrando en efectivo un pedido de emergencia a un cliente:",
                "opciones": {
                    "A": "Se niega de forma tajante diciendo que a un mercaderista jamás le corresponde tocar dinero ni pedidos.",
                    "B": "Apoya la gestión comercial: toma el pedido sugerido, recibe el cobro emitiendo el recibo correspondiente, entrega el dinero intacto a liquidación y notifica al asesor.",
                    "C": "Recibe el dinero en efectivo del cliente y se lo guarda en su bolsillo personal sin entregar recibo.",
                    "D": "Le dice al cliente que no compre nada porque el camión de la empresa siempre llega tarde."
                }
            },
            3: {
                "enunciado": "Al momento de entregar el material publicitario (afiches, cenefas, habladores de precio) asignado para el mes, el supervisor le solicita presentar el inventario y balance de uso:",
                "opciones": {
                    "A": "Presenta el registro detallado con las planillas de recepción firmadas por cada cliente vitrina, fotos de instalación en punto de venta y el stock físico sobrante en orden.",
                    "B": "Dice que botó el material a la basura porque a los comerciantes no les gusta colocar afiches.",
                    "C": "Entrega un reporte con firmas inventadas por usted para justificar el uso de la publicidad.",
                    "D": "Manifiesta que el material publicitario se le perdió en el transporte público y no tiene registro."
                }
            },
            4: {
                "enunciado": "En su rutina de trabajo de campo y relación con la fuerza de ventas:",
                "opciones": {
                    "A": "Si un vendedor de la empresa me pide una sugerencia de exhibición, lo ignoro por completo.",
                    "B": "En ocasiones he sentido fatiga por las largas caminatas y el calor en la ruta comercial, pero mantengo la energía, el cuidado de la imagen y la atención esmerada.",
                    "C": "Jamás en toda mi vida laboral he sentido cansancio físico, desánimo ni molestia al realizar trabajo en la calle.",
                    "D": "Prefiero no hablar con ningún cliente para terminar rápido el recorrido diario."
                }
            },
            5: {
                "enunciado": "En la reunión semanal de ventas, la Gerencia le solicita impartir una charla de 15 minutos a los vendedores sobre mejores prácticas de exhibición y cómo defender el espacio en el anaquel:",
                "opciones": {
                    "A": "Se niega a hablar en público argumentando que enseñar a los vendedores no forma parte de su sueldo.",
                    "B": "Asiste a la reunión a burlarse de los vendedores que tienen menos conocimientos de mercadeo.",
                    "C": "Deja que la reunión transcurra en silencio sin aportar ninguna sugerencia de Trade Marketing.",
                    "D": "Prepara ejemplos visuales claros con fotos reales de la calle, explica las técnicas de impacto visual, zonas calientes del anaquel y capacita con entusiasmo a la fuerza comercial."
                }
            },
            6: {
                "enunciado": "Un comerciante de un punto de venta estratégico se niega a recibir la nueva promoción de la empresa porque asegura que los clientes no conocen el producto:",
                "opciones": {
                    "A": "Se molesta con el comerciante y le dice que su negocio se va a quedar en la quiebra por anticuado.",
                    "B": "Se retira del local sin decir nada y le pide al vendedor que no visite más a ese cliente.",
                    "C": "Le explica con paciencia las bondades de la promoción, las ganancias por rotación, le instala material POP llamativo y ofrece una degustación en el mostrador para impulsar la venta.",
                    "D": "Le propone al comerciante vender el producto vencido a mitad de precio para que salga rápido."
                }
            },
            7: {
                "enunciado": "Al auditar los activos de comercialización de la empresa en una ruta, descubre que un exhibidor entregado en comodato fue trasladado por el dueño a su casa particular:",
                "opciones": {
                    "A": "Levanta la minuta formal de desvío del activo comercial, dialoga con el cliente sobre la cláusula legal de comodato en punto de venta y reporta de inmediato a la Gerencia de Ventas.",
                    "B": "Deja que el cliente se quede con el mueble en su casa argumentando que son cosas viejas.",
                    "C": "Le cobra una mensualidad en efectivo al cliente para permitirle tener el activo en su hogar.",
                    "D": "Destruye los documentos de entrega del mueble para que la empresa no pueda reclamarlo."
                }
            },
            8: {
                "enunciado": "Son las 5:45 p.m. (su hora habitual es hasta las 6:00 p.m.) y en un supermercado vitrina se va a realizar un evento especial nocturno que requiere reforzar el impacto visual de la marca:",
                "opciones": {
                    "A": "Asume la extensión horaria con flexibilidad y compromiso comercial, ajusta la exhibición con material promocional de impacto y garantiza la presencia impecable de la marca.",
                    "B": "Se marcha a las 5:50 p.m. puntual diciendo que las ventas nocturnas no son su responsabilidad.",
                    "C": "Se sienta en una esquina de la tienda a mirar las redes sociales hasta que termine el evento.",
                    "D": "Desordena el anaquel a propósito para que la supervisión no lo vuelva a asignar a eventos nocturnos."
                }
            },
            9: {
                "enunciado": "Respecto a la puntualidad y el cumplimiento de visitas a los clientes del maestro:",
                "opciones": {
                    "A": "Jamás en ninguno de mis empleos anteriores he llegado un solo segundo tarde a una tienda ni me he saltado un cliente de la ruta por lluvias o fallas viales.",
                    "B": "Considero que visitar a los clientes pequeños del maestro es una pérdida de tiempo innecesaria.",
                    "C": "Cumplo con disciplina el cronograma de visitas establecido, notificando con anticipación y transparencia cualquier eventualidad insalvable en el traslado.",
                    "D": "Si el día está lluvioso, me quedo en mi casa descansando sin avisar a la supervisión."
                }
            },
            10: {
                "enunciado": "El encargado de un supermercado de alto tráfico le solicita que le regale dos cajas de material publicitario (gorras, camisas, bolígrafos) para su uso familiar a cambio de una cabecera de góndola:",
                "opciones": {
                    "A": "Le entrega todo el material publicitario para comprar el favor del encargado.",
                    "B": "Acepta el trato y además le regala productos de la distribuidora para asegurar la amistad.",
                    "C": "Se roba el material de otros compañeros de trabajo para entregárselo al encargado.",
                    "D": "Explica con firmeza y educación que el material publicitario está auditado para eventos y clientes finales, y gestiona la exhibición destacando la rotación de la marca."
                }
            },
            11: {
                "enunciado": "Al recorrer el piso de venta, nota que los clientes no se detienen frente a la góndola de la marca porque los productos están ubicados en la zona fría (nivel del suelo y sin iluminación):",
                "opciones": {
                    "A": "Deja los productos allí abandonados argumentando que esa fue la orden de la tienda.",
                    "B": "Pega afiches tapando los vidrios del supermercado sin autorización del gerente.",
                    "C": "Negocia con el jefe de sala una reubicación estratégica a la altura de los ojos y manos, mejora la iluminación y coloca habladores llamativos para romper la vista del comprador.",
                    "D": "Insulta al personal de limpieza de la tienda por no iluminar el pasillo de la marca."
                }
            },
            12: {
                "enunciado": "Un asesor de ventas tiene dificultades para colocar una línea nueva de productos en su ruta porque no domina los argumentos técnicos de mercadeo:",
                "opciones": {
                    "A": "Se burla del asesor de ventas diciéndole que no sirve para el comercio.",
                    "B": "Acompaña al asesor en dos visitas clave, le modela cómo presentar los beneficios de la marca, el margen de ganancia y el material POP, reforzando la sinergia comercial.",
                    "C": "Le dice al vendedor que le pague la mitad de su comisión si quiere que le enseñe a vender.",
                    "D": "Le aconseja al vendedor que engañe a los clientes inventando funciones falsas del producto."
                }
            },
            13: {
                "enunciado": "Durante la revisión de un lote de productos en un punto de venta vitrina, detecta que varios empaques presentan polvo acumulado y manchas de humedad en la base:",
                "opciones": {
                    "A": "Retira los productos, limpia y seca a fondo el estante, higieniza cada empaque y asegura que la presentación visual proyecte la máxima calidad y pulcritud de la marca.",
                    "B": "Coloca los empaques manchados al frente para que salgan rápido antes de que se ensucien más.",
                    "C": "Tapa las manchas de humedad pegándole cinta adhesiva negra encima a los empaques.",
                    "D": "Deja la suciedad como está diciendo que la limpieza del supermercado le toca a los empleados de tienda."
                }
            },
            14: {
                "enunciado": "En relación con las políticas de mercadeo y lineamientos de exhibición bajados por la Gerencia de Ventas:",
                "opciones": {
                    "A": "He tenido debates técnicos sobre la practicidad de ciertos afiches con jefes de mercadeo, pero siempre aporté sugerencias de campo constructivas y acaté la pauta final.",
                    "B": "Las directrices que envía la gerencia de ventas casi nunca se pueden aplicar en la calle.",
                    "C": "No tolero que me supervisen cómo organizo los muebles porque nadie sabe más de calle que yo.",
                    "D": "En todas las empresas donde he laborado he tenido gerentes de ventas absolutamente perfectos y libres de cualquier error."
                }
            },
            15: {
                "enunciado": "Al visitar a un cliente clave del maestro comercial, el dueño le manifiesta su molestia porque el vendedor de la ruta no le ha tomado el pedido semanal:",
                "opciones": {
                    "A": "Le dice al cliente que el vendedor es un incompetente y le recomienda comprar a otra distribuidora.",
                    "B": "Le cuelga el teléfono al cliente o se marcha del establecimiento dejándolo con la palabra en la boca.",
                    "C": "Escucha con empatía, anota el requerimiento exacto, brinda información de las ofertas vigentes, canaliza el pedido de inmediato con el asesor y supervisa que se facture.",
                    "D": "Modifica las listas de precios en el mostrador para regalarle un descuento no autorizado al cliente."
                }
            },
            16: {
                "enunciado": "La empresa le entrega un exhibidor de pie (activo comercial) de alto valor para ser instalado en un punto de venta vitrina de gran afluencia:",
                "opciones": {
                    "A": "Lo deja tirado en la acera frente al negocio para que los empleados del local lo instalen si quieren.",
                    "B": "Vende el exhibidor a una chatarrería para obtener dinero personal extra.",
                    "C": "Se lleva el exhibidor a su casa para usarlo como estante de herramientas personales.",
                    "D": "Realiza el armado técnico, lo ubica en el punto de mayor tráfico peatonal del local, levanta el acta de entrega de comodato firmada por el dueño y toma la foto de respaldo."
                }
            },
            17: {
                "enunciado": "Al organizar la exhibición de una marca líder de alimentos, el espacio físico del anaquel asignado es sumamente estrecho:",
                "opciones": {
                    "A": "Optimiza el espacio vertical: utiliza bandejas escalonadas, maximiza el frenteo de los productos de mayor rotación y coloca cabezales que destaquen la marca a distancia.",
                    "B": "Empuja los productos de las otras marcas al suelo para abrir espacio a la fuerza.",
                    "C": "Amontona los productos unos encima de otros hasta que se caigan y se rompan.",
                    "D": "Se rinde de inmediato y deja la mitad de la mercancía guardada en cajas cerradas en el pasillo."
                }
            },
            18: {
                "enunciado": "En una jornada de alto tráfico en un supermercado vitrina, un cliente tropieza accidentalmente con una torre de productos y derrama varios empaques en el suelo:",
                "opciones": {
                    "A": "Le grita e insulta al cliente exigiéndole que pague la mercancía dañada en ese mismo instante.",
                    "B": "Mantiene la calma, auxilia al cliente verificando que no se haya lastimado, aísla la zona, limpia el producto derramado y reestructura la torre de forma más segura y estable.",
                    "C": "Sale corriendo del supermercado para no tener que limpiar el derrame de producto.",
                    "D": "Culpa al personal de seguridad de la tienda y se niega a reorganizar la mercancía."
                }
            },
            19: {
                "enunciado": "Sobre la administración de materiales promocionales, premios y degustaciones:",
                "opciones": {
                    "A": "Regalo los premios y promociones de la marca a mis familiares y amigos personales.",
                    "B": "Jamás en toda mi vida he sentido la mínima tentación de tomar un caramelo ni un folleto que no me pertenezca.",
                    "C": "Administro y entrego los premios y material promocional estrictamente a los clientes que cumplen con la mecánica de compra en el punto de venta.",
                    "D": "Vendo los premios de la empresa a otros comerciantes para obtener ingresos propios."
                }
            },
            20: {
                "enunciado": "Al revisar el maestro de clientes, nota que varios establecimientos tradicionales no conocen el catálogo de lanzamientos de la distribuidora:",
                "opciones": {
                    "A": "Asume que si no conocen el catálogo es porque no tienen dinero para comprar y no los visita.",
                    "B": "Rompe los catálogos nuevos para no tener que cargarlos en su morral durante la faena.",
                    "C": "Diseña una ruta de divulgación: visita a los clientes, presenta el catálogo con muestras físicas, explica las promociones y conecta las oportunidades de compra con el vendedor.",
                    "D": "Les cobra una tarifa a los clientes por mostrarles el catálogo de productos nuevos."
                }
            },
            21: {
                "enunciado": "Al momento de enviar las evidencias fotográficas de ejecución en los puntos de venta, el teléfono móvil presenta lentitud para subir las imágenes:",
                "opciones": {
                    "A": "Apaga el teléfono y da por terminada la semana de trabajo sin reportar nada.",
                    "B": "Descarga fotos de internet de supermercados de otros países y las hace pasar por sus tiendas.",
                    "C": "Insulta al equipo de soporte técnico de la empresa en los grupos corporativos.",
                    "D": "Guarda las fotos con la geolocalización activa, aprovecha una conexión de red estable al cierre del día, envía el reporte consolidado y notifica la novedad técnica al supervisor."
                }
            },
            22: {
                "enunciado": "El propietario de un supermercado vitrina le propone colocar un afiche publicitario gigante de la marca en la fachada principal si la empresa le pinta el local comercial:",
                "opciones": {
                    "A": "Le promete al comerciante que la empresa le pintará el negocio completo sin consultar a nadie.",
                    "B": "Escucha la propuesta de alto impacto, toma las medidas y fotografías de la fachada y traslada la oportunidad a la Gerencia de Ventas y Mercadeo para su evaluación presupuestaria.",
                    "C": "Le dice al comerciante de forma grosera que la empresa no gasta dinero en locales feos.",
                    "D": "Pinta la fachada con sus propios recursos y le cobra una comisión al dueño del supermercado."
                }
            },
            23: {
                "enunciado": "Al finalizar la exhibición en un punto de venta clave, le sobran varias cenefas y habladores en perfecto estado:",
                "opciones": {
                    "A": "Los clasifica, guarda en su bolso de trabajo protegidos del polvo y la humedad para utilizarlos en los siguientes clientes vitrina del itinerario.",
                    "B": "Los rompe y los tira al cesto de basura de la tienda para no llevar peso en el bolso.",
                    "C": "Los deja abandonados en el mostrador del comercio para que los niños jueguen con ellos.",
                    "D": "Los pega en las paredes de la calle de forma desordenada en zonas prohibidas."
                }
            },
            24: {
                "enunciado": "Sobre el manejo del estrés y la tolerancia ante la negativa de clientes difíciles:",
                "opciones": {
                    "A": "Si un comerciante me niega el permiso de colocar un afiche, le pateo las puertas del local.",
                    "B": "He tenido negativas de comerciantes cerrados a las promociones, pero mantengo la serenidad, la sonrisa comercial y vuelvo a insistir en visitas posteriores con mejores propuestas.",
                    "C": "Poseo una paciencia celestial inalterable; absolutamente ningún rechazo comercial ni actitud grosera me ha afectado jamás.",
                    "D": "Cuando un cliente me dice que no, me pongo a llorar en medio del pasillo del supermercado."
                }
            },
            25: {
                "enunciado": "Un promotor de otra compañía le pide que le ceda parte del espacio asignado en el exhibidor propio de la empresa para colocar sus productos a cambio de compartir comisiones:",
                "opciones": {
                    "A": "Acepta el dinero y permite que la marca competidora use el exhibidor de la empresa.",
                    "B": "Le propone al competidor vender el mueble comercial entre los dos y repartirse las ganancias.",
                    "C": "Se une con el competidor para hablar mal de los productos de la distribuidora en el pasillo.",
                    "D": "Rechaza la propuesta de inmediato, defiende la exclusividad del activo de la empresa y recuerda que los espacios comerciales están blindados por contrato institucional."
                }
            },
            26: {
                "enunciado": "Durante el recorrido por los puntos de venta, nota que las etiquetas de precio de su producto están desactualizadas y muestran un monto más alto que el de la promoción vigente:",
                "opciones": {
                    "A": "No dice nada porque mientras más caro esté el producto más gana la distribuidora.",
                    "B": "Solicita con amabilidad al personal de precios del supermercado la actualización del hablador oficial, coloca el material POP de oferta visible y garantiza que el comprador vea el beneficio.",
                    "C": "Modifica los habladores de precio del supermercado con un marcador encima del código de barras.",
                    "D": "Discute a gritos con los clientes en la cola de la caja acusándolos de no saber leer precios."
                }
            },
            27: {
                "enunciado": "Se requiere apoyar a la fuerza de ventas en una temporada de alta demanda comercial (ej. Navidad o aniversario comercial), lo cual implica ajustar los horarios de visita:",
                "opciones": {
                    "A": "Se niega a cualquier ajuste de horario argumentando que él solo trabaja minutos exactos.",
                    "B": "Asume el requerimiento con flexibilidad y compromiso, coordina con la supervisión el plan de apoyo en piso de venta y asegura que todos los puntos vitrina queden abastecidos.",
                    "C": "Acepta el horario pero falta a las visitas de las tiendas los fines de semana sin avisar.",
                    "D": "Se queja constantemente frente a los dueños de los supermercados sobre la exigencia de la empresa."
                }
            },
            28: {
                "enunciado": "Debe presentar el informe mensual de actividades de mercadeo y estado de los activos comerciales a la Gerencia de Ventas:",
                "opciones": {
                    "A": "Estructura el informe consolidando cobertura de tiendas, balance de material POP instalado, censo de exhibidores propios en calle, fotos de impacto y sugerencias de la fuerza de ventas.",
                    "B": "Envía un mensaje de voz diciendo que todas las tiendas del mes quedaron muy bonitas.",
                    "C": "Copia el informe de otro compañero cambiando solo su nombre en la portada.",
                    "D": "Manifiesta que los informes de mercadeo no sirven para nada y se niega a elaborarlo."
                }
            },
            29: {
                "enunciado": "En su relación con otros promotores y vendedores de la organización:",
                "opciones": {
                    "A": "Jamás en toda mi vida profesional he sentido la mínima envidia, recelo o inconformidad por las felicitaciones o comisiones que ganan otros vendedores.",
                    "B": "A veces he sentido sana emulación o deseo de destacar como el mejor promotor, pero me enfoco en que mis puntos de venta vitrina sean los de mayor rotación y mejor imagen.",
                    "C": "Pienso que cuando felicitan a un promotor en la empresa es únicamente por favoritismo de los gerentes.",
                    "D": "No me gusta compartir mis técnicas de exhibición con nadie porque los demás no merecen aprender."
                }
            },
            30: {
                "enunciado": "La Gerencia le solicita realizar una verificación reservada en varios supermercados clave sobre sospechas de mal uso de neveras y exhibidores propios de la marca:",
                "opciones": {
                    "A": "Comenta la investigación con los empleados de las tiendas durante el recorrido matutino.",
                    "B": "Se niega a realizar la auditoría argumentando que vigilar neveras no es trabajo de mercaderista.",
                    "C": "Ejecuta la verificación con discreción y rigor: toma fotografías del estado físico, constata exclusividad de productos, levanta el informe detallado y lo entrega directamente a Gerencia.",
                    "D": "Altera el informe para encubrir a comerciantes amigos que tienen productos ajenos en las neveras de la empresa."
                }
            }
        }
    },
    
    # =========================================================================
    # 25. SUPERVISOR DE COBRANZA Y RECUPERACIÓN DE CARTERA (CJS-SCB)
    # =========================================================================
    "25_SUPERVISOR_DE_COBRANZA": {
        "codigo": "CJS-SCB",
        "titulo": "EVALUACIÓN PSICOTÉCNICA EN SUPERVISIÓN DE COBRANZA Y RECUPERACIÓN DE CARTERA",
        "instrucciones": "Lea con atención cada situación laboral, de recuperación de cartera y análisis crediticio. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con objetividad sobre su rigor numérico, firmeza en políticas de crédito, negociación y ética. Dispone de un máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "Un asesor de ventas solicita con insistencia que autorice un pedido bloqueado por mora a un cliente que tiene facturas con más de 45 días de vencimiento, prometiendo que el cliente pagará mañana:",
                "opciones": {
                    "A": "Desbloquea el pedido en el sistema inmediatamente para no frenar la venta del asesor.",          
                    "B": "Borra la deuda vencida del sistema para que el pedido pase los filtros automáticos.",          
                    "C": "Le pide al asesor una comisión personal en efectivo por hacerle el favor del desbloqueo.",          
                    "D": "Mantiene el bloqueo en el sistema, evalúa el estatus real de solvencia, exige un abono sustancial comprobado en banco y supedita la liberación al cumplimiento de la política de cuentas por cobrar."
                }
            },
            2: {
                "enunciado": "A primera hora de la mañana (8:00 a.m.), debe solicitar a la Gerencia Administrativa los estados de cuenta bancarios para conciliar los cobros reportados ayer:",
                "opciones": {
                    "A": "Omite pedir los estados de cuenta y valida los cobros basándose únicamente en capturas de pantalla de WhatsApp.",
                    "B": "Solicita formalmente los estados de cuenta bancarios a primera hora, cruza cada transferencia y depósito contra las facturas del sistema y procesa la aplicación exacta de los fondos.",
                    "C": "Asienta los cobros en el sistema sin verificar si el dinero ingresó a las cuentas de la empresa.",
                    "D": "Espera a final de mes para conciliar todos los bancos juntos para no interrumpir a la administración."
                }
            },
            3: {
                "enunciado": "Al auditar las cuentas por cobrar de la Ruta P60 (Créditos a Empleados), detecta que dos colaboradores tienen saldos vencidos acumulados sin que se les haya aplicado el descuento respectivo en nómina:",
                "opciones": {
                    "A": "Notifica de inmediato a Talento Humano y Administración con el reporte detallado de la Ruta P60, solicitando la aplicación del cronograma de descuento por nómina acordado.",
                    "B": "Borra los saldos de la Ruta P60 argumentando que a los empleados no se les debe cobrar.", 
                    "C": "Cobra la deuda a los empleados en efectivo personal sin entregarles comprobante de pago.", 
                    "D": "Amonesta verbalmente a los empleados en medio del comedor de la empresa frente a todos."      
                }
            },
            4: {
                "enunciado": "En su trayectoria profesional y manejo de la presión ante metas de recuperación de liquidez:",          
                "opciones": {
                    "A": "Si la gerencia me exige bajar la morosidad a fin de mes, insulto a los vendedores y apago el teléfono.",          
                    "B": "En ocasiones he sentido tensión y cansancio mental al negociar con deudores morosos o conciliar carteras complejas, pero mantengo la serenidad, la firmeza y la estrategia analítica.",          
                    "C": "Jamás en toda mi vida profesional he sentido la menor preocupación, fatiga ni estrés al gestionar cobranzas difíciles.",          
                    "D": "Prefiero no llamar a los clientes con deudas viejas para evitar que se molesten conmigo."          
                }
            },
            5: {
                "enunciado": "Al monitorear la Ruta P50 (Cuentas por Cobrar a Clientes Internos de la Empresa), nota que se despacharon pedidos a una unidad interna sin registrar el comprobante de cargo contable:",          
                "opciones": {
                    "A": "Deja la cuenta sin registrar asumiendo que los movimientos internos no requieren control.",          
                    "B": "Carga la deuda de la unidad interna a la cuenta personal de un cliente comercial externo.",          
                    "C": "Factura los productos a precio cero para que el inventario no refleje faltantes.",          
                    "D": "Audita la transacción, genera el documento de cargo correspondiente en la Ruta P50, valida con el responsable de la unidad interna y garantiza la conciliación con inventarios."          
                }
            },
            6: {
                "enunciado": "Al recibir los cheques cobrados en la calle por la fuerza de ventas al cierre de la tarde:",          
                "opciones": {
                    "A": "Guarda los cheques en su gaveta personal sin registrar durante varios días.",          
                    "B": "Llena el formato de control de cheques detallando banco, número, monto y cliente, y los entrega a diario bajo firma de recepción a la Gerencia Administrativa.",          
                    "C": "Endosa los cheques a su propio nombre para cobrarlos por ventanilla en el banco.",          
                    "D": "Devuelve los cheques a los vendedores diciéndoles que ellos mismos los lleven al banco."          
                }
            },
            7: {
                "enunciado": "Al auditar la cartera general, identifica un grupo de 15 clientes comerciales que superan los 31 días de atraso en sus pagos:",          
                "opciones": {
                    "A": "Planifica y ejecuta la gestión de cobranza telefónica inmediata, documenta los compromisos de pago en el sistema, envía los estados de cuenta actualizados y coordina con los asesores de ruta.",          
                    "B": "Bloquea a los clientes y les envía mensajes con insultos y amenazas personales.",          
                    "C": "Da las deudas por perdidas y las envía a pérdida contable sin realizar ninguna gestión.",          
                    "D": "Le exige a los choferes de reparto que vayan a confiscar bienes de los locales comerciales."          
                }
            },
            8: {
                "enunciado": "Son las 4:50 p.m. (su horario habitual es hasta las 5:00 p.m.) y la Gerencia solicita con urgencia el informe de clientes bloqueados actualizado para definir el corte de facturación nocturno:",          
                "opciones": {
                    "A": "Asume la extensión horaria con compromiso profesional, procesa las últimas conciliaciones bancarias, actualiza la lista de clientes bloqueados y la remite a Ventas y Facturación.",          
                    "B": "Se marcha a las 5:00 p.m. puntual diciendo que los clientes bloqueados deben revisarse al día siguiente.",          
                    "C": "Envía una lista desactualizada de la semana pasada sin revisar los cobros del día.",          
                    "D": "Desbloquea a todos los clientes morosos en el sistema para no tener que hacer el informe."          
                }
            },
            9: {
                "enunciado": "Respecto al rigor técnico y la exactitud en el cálculo de intereses y saldos morosos:",          
                "opciones": {
                    "A": "Jamás en ninguno de mis empleos anteriores he cometido un error de digitación ni he tenido una diferencia de un solo centavo en una conciliación de cobranzas.",          
                    "B": "Considero que monitorear facturas vencidas a menos de 15 días es una pérdida de tiempo innecesaria.",          
                    "C": "Reviso meticulosamente cada cifra, fecha valor en cuenta y comprobante de retención, asegurando que el estado de cuenta del cliente refleje exactamente su saldo contable.",          
                    "D": "Si el saldo de un cliente no cuadra, prefiero atribuirle el error al software administrativo."          
                }
            },
            10: {
                "enunciado": "Un comerciante moroso le ofrece pagarle $100 en efectivo \"por fuera\" si le elimina del sistema el historial de mora y le autoriza un nuevo crédito abierto:",          
                "opciones": {
                    "A": "Acepta el dinero del comerciante y le borra el historial de días de crédito en el sistema.",          
                    "B": "Le propone al comerciante que le pague $200 para duplicarle el cupo de crédito sin soportes.",          
                    "C": "Comparte el dinero del soborno con el asesor de ventas para que ninguno de los dos lo reporte.",          
                    "D": "Rechaza la propuesta de forma rotunda, ratifica la inalterabilidad del historial crediticio y notifica el intento de soborno a la Gerencia Administrativa y Legal."          
                }
            },
            11: {
                "enunciado": "Al realizar la llamada de cobro a un cliente con saldo vencido a 35 días, este le asegura que hace dos semanas le entregó el pago en efectivo al vendedor de la zona:",          
                "opciones": {
                    "A": "Le dice al cliente que es un mentiroso y le cuelga el teléfono de forma descortés.",          
                    "B": "Da por pagada la factura en el sistema sin pedirle comprobantes ni recibos al cliente.",          
                    "C": "Solicita amablemente al cliente la copia del recibo de cobro firmado por el asesor, coteja de inmediato con los ingresos de caja y levanta la alerta formal ante la supervisión de ventas.",          
                    "D": "Modifica la factura en el sistema para que figure como un descuento comercial no cobrado."          
                }
            },
            12: {
                "enunciado": "Un asesor de ventas solicita que se le desbloquee un pedido urgente asegurando que el cliente ya hizo la transferencia, pero el dinero aún no aparece acreditado en la cuenta de la empresa:",          
                "opciones": {
                    "A": "Autoriza el pedido basándose en la imagen del comprobante bancario que le envió el asesor.",          
                    "B": "Explica la norma institucional: ningún pedido bloqueado se libera hasta que los fondos estén efectivamente disponibles en la cuenta bancaria de la empresa, evitando fraudes por transferencias falsas.",          
                    "C": "Presta su propia tarjeta de crédito para avalar el pedido del cliente en el sistema.",          
                    "D": "Anula la factura anterior del cliente para que el sistema permita facturar la nueva carga."          
                }
            },
            13: {
                "enunciado": "Al analizar la solvencia y confiabilidad de un cliente nuevo que solicita una línea de crédito de $5.000, los estados financieros reflejan pérdidas y las referencias bancarias arrojan cheques devueltos:",          
                "opciones": {
                    "A": "Emite un dictamen técnico desfavorable para la línea de crédito solicitada, propone comenzar con operaciones de contado o pagos contra entrega y resguarda el patrimonio de la empresa.",          
                    "B": "Aprueba el crédito de $5.000 de todos modos esperando que el cliente mejore sus finanzas.",          
                    "C": "Le aprueba un crédito mayor de $10.000 para ayudar al comerciante a salir de sus deudas.",          
                    "D": "Bota la carpeta de solicitud de crédito a la papelera sin emitir ningún informe a la Gerencia."          
                }
            },
            14: {
                "enunciado": "En su relación con la fuerza de ventas y supervisores comerciales en empleos previos:",          
                "opciones": {
                    "A": "He tenido divergencias técnicas sobre el límite de crédito de ciertos clientes con supervisores de ventas, defendiendo la política de cobranzas con datos financieros y respeto profesional.",          
                    "B": "Los vendedores siempre son unos irresponsables que solo buscan vender sin importar si el cliente paga.",          
                    "C": "No permito que nadie de ventas me pregunte por qué un cliente está bloqueado porque yo mando en cobranzas.",          
                    "D": "En todas las empresas donde he laborado he tenido equipos de ventas absolutamente perfectos que jamás tuvieron un solo cliente moroso."          
                }
            },
            15: {
                "enunciado": "Durante la recepción de los cobros gestionados por la fuerza de ventas, nota que un asesor presenta comprobantes de retención de IVA e ISLR con el número de RIF equivocado:",          
                "opciones": {
                    "A": "Recibe los comprobantes con errores fiscales y da por cancelada la factura en el sistema.",          
                    "B": "Devuelve los comprobantes al asesor, explica la no deducibilidad fiscal del documento mal emitido y solicita la corrección inmediata con el cliente antes de aplicar el descargo de cartera.",          
                    "C": "Altera el número de RIF a mano con un bolígrafo sobre el comprobante emitido por el cliente.",          
                    "D": "Bota los comprobantes a la basura y le cobra el monto del impuesto al vendedor en efectivo."          
                }
            },
            16: {
                "enunciado": "Al emitir el listado matutino de clientes bloqueados por mora, nota que un cliente estratégico de alto volumen comercial cayó en bloqueo automático por un saldo mínimo de $5 derivado de un ajuste:",          
                "opciones": {
                    "A": "Deja al cliente bloqueado durante una semana sin avisar a nadie para que aprenda a pagar centavos.",          
                    "B": "Borra la cuenta completa del cliente mayorista del catálogo del sistema administrativo.",          
                    "C": "Le cobra $50 de recargo administrativo al cliente por haber generado el bloqueo del sistema.",          
                    "D": "Analiza el estatus, identifica que el saldo es una diferencia menor de redondeo, gestiona el ajuste administrativo correspondiente y autoriza el pedido notificando oportunamente a Ventas."          
                }
            },
            17: {
                "enunciado": "Se requiere establecer el cronograma mensual de cobros y plazos de crédito para la temporada alta de ventas de la distribuidora:",          
                "opciones": {
                    "A": "Diseña el cronograma balanceando plazos según el historial de rotación y pago de cada canal, establece días fijos de gestión telefónica y coordina con Ventas para maximizar el retorno de dinero.",          
                    "B": "Establece que todos los clientes de la empresa deben pagar estrictamente el mismo día del mes.",          
                    "C": "Otorga 90 días de crédito a todos los clientes sin importar su historial para que vendan más.",          
                    "D": "Se niega a elaborar cronogramas argumentando que cada cliente paga cuando puede."          
                }
            },
            18: {
                "enunciado": "En la revisión cotidiana de cuentas por cobrar, detecta que una factura a crédito emitida hace 60 días no tiene firma ni sello de recepción conforme del cliente en el archivo físico:",          
                "opciones": {
                    "A": "Oculta la falta del soporte físico esperando que el cliente pague voluntariamente por teléfono.",          
                    "B": "Levanta la no conformidad formal, coordina con la supervisión de despacho y ventas la regularización inmediata del soporte en calle y asegura la base legal del cobro.",          
                    "C": "Falsifica la firma y sello del comerciante sobre la copia de la factura de la empresa.",          
                    "D": "Anula la factura en el sistema contable dando por perdida la mercancía entregada."          
                }
            },
            19: {
                "enunciado": "Sobre la confidencialidad de la solvencia, límites de crédito y deudas de los clientes de la empresa:",          
                "opciones": {
                    "A": "Comento las deudas y problemas de liquidez de los comerciantes con amigos en reuniones sociales.",          
                    "B": "Jamás en toda mi vida profesional he sentido la mínima curiosidad por mirar un estado financiero ajeno ni he comentado cifras de clientes fuera de mi trabajo.",          
                    "C": "Custodio la información financiera de los clientes, saldos por cobrar y datos de solvencia bajo estricta reserva y secreto profesional.",          
                    "D": "Publico en redes sociales los nombres de los clientes morosos para presionarlos a pagar."          
                }
            },
            20: {
                "enunciado": "Al auditar las cobranzas de un canal de distribución institucional, nota que los pagos se están registrando con retraso de 5 días en el sistema administrativo por falta de personal:",          
                "opciones": {
                    "A": "Deja que el retraso continúe acumulándose hasta que la cobranza colapse por completo.",          
                    "B": "Registra cobros ficticios en el sistema para que la estadística de recaudación del mes se vea alta.",          
                    "C": "Reestructura el flujo de trabajo diario, prioriza la conciliación bancaria matutina y garantiza que la información de cobros se actualice en tiempo real para liberar pedidos sin demoras.",          
                    "D": "Exige a la Gerencia Administrativa que cierre el canal institucional para trabajar menos."          
                }
            },
            21: {
                "enunciado": "Al momento de elaborar el informe periódico de actividades de cobranza para la Dirección (rotación de cartera, días calle, efectividad de cobro y clientes bloqueados):",          
                "opciones": {
                    "A": "Estructura el informe consolidando indicadores de días calle (DSO), monto recuperado vs. meta, detalle de cartera morosa mayor a 31 días y estado de las rutas P50 y P60.",          
                    "B": "Envía un correo con dos líneas diciendo que la cobranza va bien y que casi todos los clientes pagaron.",          
                    "C": "Copia el informe del mes anterior modificando únicamente las fechas para salir del compromiso.",          
                    "D": "Manifiesta que los informes de cobranza son innecesarios porque los números están en el banco."          
                }
            },
            22: {
                "enunciado": "Un cliente con deuda vencida de $3.000 acude a su oficina manifestando problemas severos de flujo de caja y solicita un acuerdo de pago financiado en 4 partes semanales:",          
                "opciones": {
                    "A": "Insulta al cliente y le dice que no le acepta ningún acuerdo y que lo va a demandar de inmediato.",          
                    "B": "Analiza la propuesta, exige una inicial en el acto, formaliza un convenio de pago firmado con pagaré o garantías, suspende nuevos créditos y hace seguimiento semanal al cumplimiento.",          
                    "C": "Le perdona la mitad de la deuda al cliente sin consultar con la Gerencia Administrativa.",          
                    "D": "Acepta el acuerdo de palabra sin firmar ningún documento legal ni registrarlo en el sistema."          
                }
            },
            23: {
                "enunciado": "Al auditar la Ruta P50 (Clientes Internos), constata que una de las sucursales de la empresa acumula saldos pendientes de liquidación de inventario transferido hace más de 60 días:",          
                "opciones": {
                    "A": "Convoca una reunión de conciliación con el encargado de la sucursal y Administración, audita los consumos y transferencias, y regulariza los cargos internos de la cuenta.",          
                    "B": "Pasa la deuda interna de la sucursal como una pérdida irrecuperable en el balance general.",          
                    "C": "Cierra la sucursal de forma arbitraria sin contar con la autorización de la Dirección General.",          
                    "D": "Ignora el atraso argumentando que como es una cuenta interna el dinero se queda en casa."          
                }
            },
            24: {
                "enunciado": "Sobre el autocontrol emocional y la asertividad al negociar con deudores hostiles o alterados:",          
                "opciones": {
                    "A": "Si un cliente moroso me grita por teléfono diciéndome que no me va a pagar, le respondo con groserías.",          
                    "B": "He enfrentado llamadas y reuniones con clientes molestos y agresivos, pero mantengo la compostura profesional, el tono educado y encauzo la conversación hacia soluciones de pago viables.",          
                    "C": "Poseo una serenidad sobrehumana inalterable; absolutamente ninguna ofensa, discusión ni reclamo de cobranza me ha generado incomodidad o molestia jamás.",          
                    "D": "Cuando me enojo con un deudor, le bloqueo todos los pedidos a sus familiares en la empresa."          
                }
            },
            25: {
                "enunciado": "Un asesor de ventas le solicita que le reciba un cheque de un cliente sin fondos confirmados para desbloquearle un pedido, asegurando que \"el lunes cae el dinero\":",          
                "opciones": {
                    "A": "Acepta el cheque sin fondos y autoriza el pedido para apoyar al asesor de ventas.",          
                    "B": "Le cobra un porcentaje en efectivo al asesor por correr el riesgo del cheque devuelto.",          
                    "C": "Modifica la fecha del cheque con corrector líquido para depositarlo semanas después.",          
                    "D": "Rechaza la recepción del instrumento sin fondos, ratifica la normativa de prevención de riesgo financiero y mantiene el pedido retenido hasta contar con fondos reales disponibles."          
                }
            },
            26: {
                "enunciado": "Durante la revisión diaria de cheques recibidos de la fuerza de ventas, nota que un cheque no tiene el nombre de la empresa como beneficiario y no está cruzado:",          
                "opciones": {
                    "A": "Recibe el cheque irregular y lo deposita en su propia cuenta bancaria personal.",          
                    "B": "Devuelve el cheque al asesor de inmediato, explica la normativa de cobro que exige emisión a nombre de la empresa y cruzado, y exige la sustitución por un instrumento conforme.",          
                    "C": "Altera el cheque con un bolígrafo escribiendo el nombre de la empresa sobre el beneficiario.",          
                    "D": "Rompe el cheque del cliente y bota los pedazos a la papelera del departamento."          
                }
            },
            27: {
                "enunciado": "Se requiere extender la jornada de trabajo para realizar una auditoría de cartera exhaustiva solicitada por Presidencia ante un cierre fiscal extraordinario:",          
                "opciones": {
                    "A": "Se marcha a su casa puntual a las 5:00 p.m. diciendo que la auditoría debe hacerse en horas de oficina.",          
                    "B": "Asume la extensión con compromiso y rigor técnico, audita saldos mayores a 31 días, concilia abonos bancarios y entrega el informe ejecutivo y saneado a Presidencia.",          
                    "C": "Envía cifras aproximadas al azar para poder retirarse temprano de las instalaciones.",          
                    "D": "Se queja a gritos con los compañeros asegurando que la empresa abusa del personal administrativo."          
                }
            },
            28: {
                "enunciado": "Al momento de mantener el archivo y los expedientes crediticios de los clientes comerciales:",          
                "opciones": {
                    "A": "Mantiene los expedientes de crédito ordenados con su RIF vigente, estados financieros auditados, referencias bancarias confirmadas y contratos de fianza resguardados bajo llave.",          
                    "B": "Deja las solicitudes de crédito y documentos confidenciales tirados en las mesas de la oficina.",          
                    "C": "Bota los expedientes de los clientes que pagan puntual argumentando que ya no se necesitan.",          
                    "D": "Mezcla los documentos de clientes morosos con las facturas de proveedores sin clasificar."          
                }
            },
            29: {
                "enunciado": "En su relación con otros supervisores del área administrativa y reconocimientos laborales:",          
                "opciones": {
                    "A": "Jamás en toda mi vida profesional he sentido el menor recelo, envidia o molestia cuando felicitan a otro supervisor de departamento por su buena gestión.",          
                    "B": "En ocasiones he sentido sana emulación o deseo de que se reconozca la labor silenciosa de cobranzas, pero me enfoco en mantener la cartera sana, recuperar liquidez y cumplir metas.",          
                    "C": "Considero que cuando premian a un supervisor en la empresa es únicamente por adulación a la gerencia.",          
                    "D": "No me gusta colaborar con los supervisores de facturación porque siempre entorpecen mi labor."          
                }
            },
            30: {
                "enunciado": "Presidencia le encomienda realizar una auditoría reservada sobre presuntas cobranzas en efectivo no declaradas en una ruta comercial manejada por un supervisor de ventas:",          
                "opciones": {
                    "A": "Le avisa al supervisor de ventas investigado para que arregle las cuentas antes de la auditoría.",          
                    "B": "Se niega a realizar la auditoría argumentando que revisar cobranzas de compañeros genera roces internos.",          
                    "C": "Ejecuta la auditoría con absoluto sigilo profesional: visita a los clientes de la ruta, coteja facturas vs. recibos de caja en mano, cruza depósitos y entrega el informe reservado a Presidencia.",          
                    "D": "Modifica las evidencias del informe para encubrir al supervisor si tiene una relación de amistad con él."          
                }
            }
        }
    },
    # =========================================================================
    # 26. SUPERVISOR DE LOGÍSTICA, ALMACÉN Y DESPACHO (CJS-GLA)
    # =========================================================================
    "26_SUPERVISOR_DE_LOGISTICA": {
        "codigo": "CJS-GLA",
        "titulo": "EVALUACIÓN PSICOTÉCNICA EN GESTIÓN DE LOGÍSTICA, ALMACÉN Y DESPACHO",
        "instrucciones": "Lea con atención cada situación de supervisión, almacén y despacho. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con objetividad sobre su liderazgo de equipo, rigor técnico, cuidado de activos y apego a normas. Dispone de un máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "Al revisar las carpetas vehiculares de la flota que saldrá a ruta foránea, detecta que dos camiones tienen la póliza de Responsabilidad Civil Vehicular (RCV) y el permiso sanitario vencidos:",
                "opciones": {
                    "A": "Permite la salida de los camiones pidiéndole a los choferes que evadan las alcabalas de control.",
                    "B": "Falsifica las fechas en las copias de los certificados para que pasen las inspecciones viales.",
                    "C": "Envía los camiones a la ruta y le dice a los choferes que paguen comisiones si los detienen.",
                    "D": "Frena de inmediato la salida de ambas unidades, reasigna la carga a vehículos con documentación legal al día y tramita la renovación urgente de pólizas y permisos."
                }
            },
            2: {
                "enunciado": "Durante la recepción de insumos y mercancía de un proveedor foráneo en el andén de almacén, nota que 50 bultos de producto alimenticio tienen fecha de vencimiento menor a 30 días:",
                "opciones": {
                    "A": "Recibe la mercancía a ciegas sin reportar la fecha corta para evitar discusiones con el proveedor.",
                    "B": "No acepta el ingreso del lote de fecha corta según la política de recepción, levanta la no conformidad formal y notifica de inmediato a Compras y a la Gerencia Administrativa.",
                    "C": "Ingresa el producto al almacén y lo mezcla con el stock nuevo para que los ayudantes no se den cuenta.",
                    "D": "Le cobra una penalización personal en efectivo al chofer del proveedor para dejarlo descargar."
                }
            },
            3: {
                "enunciado": "Al inspeccionar el proceso de carga de un camión de 8 toneladas, observa que los operarios colocaron el 70% del peso en la parte trasera del furgón, desbalanceando los ejes de la unidad:",
                "opciones": {
                    "A": "Ordena detener la carga, corrige la estiba balanceando el peso de forma uniforme sobre los ejes, asegura la carga trabada y verifica el cumplimiento de las normas de seguridad vial.",
                    "B": "Deja que el camión salga desbalanceado argumentando que el chofer sabrá cómo maniobrar en carretera.",
                    "C": "Coloca sacos de arena en el parachoque delantero para compensar el peso sin desarmar la batea.",
                    "D": "Insulta a los operarios a gritos en el andén y se desentiende de la supervisión de la carga."
                }
            },
            4: {
                "enunciado": "En su trayectoria profesional y liderazgo de equipos operativos bajo presión:",
                "opciones": {
                    "A": "Si coinciden varios problemas mecánicos y retrasos de carga, abandono las instalaciones y apago el teléfono.",
                    "B": "En ocasiones he sentido alta exigencia física y mental ante picos de despacho y fallas de transporte, pero mantengo el autocontrol, la organización y la serenidad gerencial.",
                    "C": "Jamás en toda mi vida profesional he sentido el menor estrés, preocupación ni cansancio liderando operaciones de almacén o transporte.",
                    "D": "Prefiero supervisar sentado en mi oficina sin bajar al andén ni revisar los camiones."
                }
            },
            5: {
                "enunciado": "En la revisión de inventarios del almacén, constata que existen lotes de productos de alta rotación con fechas próximas a vencer que quedaron estancados detrás de mercancía recién ingresada:",
                "opciones": {
                    "A": "Deja el producto en el fondo esperando que la fuerza de ventas lo pida por casualidad.",
                    "B": "Bota el producto próximo a vencer a la basura antes de que caduque para no generar reportes.",
                    "C": "Modifica los registros del sistema borrando las fechas de caducidad de los lotes.",
                    "D": "Aplica el método FIFO/PEPS de inmediato, reubica físicamente el lote al frente de las estibas y coordina con Ventas y Administración su salida comercial prioritaria."
                }
            },
            6: {
                "enunciado": "Al auditar el formato de control de combustible de la flota y planta eléctrica exigido por Presidencia, detecta que un camión presenta un consumo 35% superior a su ruta habitual sin justificación:",
                "opciones": {
                    "A": "Modifica los números en el reporte para que el consumo parezca normal ante Presidencia.",
                    "B": "Inicia la auditoría técnica inmediata: inspecciona mecánicamente el motor y posibles fugas, cruza kilometraje recorrido vs. litros surtidos y eleva el informe a Gerencia.",
                    "C": "Descuenta el exceso de combustible al chofer directamente de su sueldo sin investigar la causa.",
                    "D": "Deja de suministrar combustible al camión paralizando los despachos comerciales de esa zona."
                }
            },
            7: {
                "enunciado": "Se produce un accidente laboral en el andén donde un ayudante de despacho sufre una torcedura fuerte de tobillo al bajar de la batea de un camión:",
                "opciones": {
                    "A": "Brinda primeros auxilios inmediatos, gestiona el traslado oportuno del trabajador a un centro asistencial de salud y reporta formalmente la incidencia a la Gerencia y a Seguridad Laboral.",
                    "B": "Le dice al trabajador que siga cargando bultos para no perder el ritmo del despacho.",
                    "C": "Oculta el accidente amenazando al personal para que nadie informe a las autoridades.",
                    "D": "Le da $10 al colaborador para que se vaya a su casa en mototaxi y no vaya a la clínica."
                }
            },
            8: {
                "enunciado": "Son las 4:55 p.m. (su hora habitual de salida es a las 5:00 p.m.) y una cuadrilla de despacho debe realizar una jornada extraordinaria nocturna por la llegada tardía de una gandola primaria:",
                "opciones": {
                    "A": "Asume la extensión horaria con compromiso, coordina la cena y el transporte seguro del personal a sus viviendas al finalizar, y supervisa la descarga hasta dejar la carga resguardada.",
                    "B": "Se marcha a las 5:00 p.m. en punto dejando al personal solo y sin transporte nocturno.",
                    "C": "Ordena a los trabajadores que se queden sin cena y que regresen a sus casas caminando de madrugada.",
                    "D": "Cierra los portones con candado y se va sin permitir que la gandola descargue la mercancía."
                }
            },
            9: {
                "enunciado": "Respecto al rigor en el control de inventarios de repuestos, baterías y equipos de transporte:",
                "opciones": {
                    "A": "Jamás en ninguno de mis empleos anteriores se me ha extraviado una herramienta, repuesto ni he tenido una diferencia de inventario en toda mi vida.",
                    "B": "Considero que llevar el control serializado de baterías y neumáticos en uso es una pérdida de tiempo.",
                    "C": "Mantengo un inventario estricto de repuestos, baterías y herramientas, auditando su vida útil y verificando que cada salida esté respaldada por una orden de taller.",
                    "D": "Si falta un neumático de repuesto en el taller, prefiero culpar al vigilante nocturno."
                }
            },
            10: {
                "enunciado": "Un chofer de reparto le informa por teléfono que tuvo un choque en carretera foránea, no hay heridos pero la carrocería del camión quedó golpeada:",
                "opciones": {
                    "A": "Le dice al chofer que se dé a la fuga antes de que llegue la policía de tránsito.",
                    "B": "Le propone al chofer pagar un mecánico clandestino para pintar el camión y no avisar a la empresa.",
                    "C": "Se desentiende del problema diciendo que los choferes deben resolver sus accidentes solos.",
                    "D": "Brinda debida asistencia al chofer, realiza la previa notificación al seguro de la empresa, coordina el resguardo de la mercancía y levanta la minuta formal del siniestro."
                }
            },
            11: {
                "enunciado": "Al coordinar con el departamento de ventas, los supervisores comerciales se quejan de que las órdenes de pedido no se despachan en los tiempos pautados:",
                "opciones": {
                    "A": "Responde a las quejas con agresividad diciendo que Ventas no sabe lo que cuesta mover carga.",
                    "B": "Cancela la entrega de pedidos de los clientes más quejosos como represalia.",
                    "C": "Audita el flujo de preparación y estiba, sincroniza las ventanas horarias con el Supervisor de Despacho y establece un cronograma de salidas monitoreado en tiempo real.",
                    "D": "Ordena cargar los camiones con pedidos al azar sin revisar las órdenes de los clientes."
                }
            },
            12: {
                "enunciado": "Al verificar el estado de la planta eléctrica de emergencia de la empresa, nota que tiene poco combustible y el último mantenimiento preventivo venció hace dos meses:",
                "opciones": {
                    "A": "Esperan a que ocurra un apagón eléctrico en la zona para revisar si la planta todavía prende.",
                    "B": "Gestiona mediante Administración la compra de filtros y aceite para el mantenimiento preventivo, abastece el tanque de combustible auxiliar y garantiza su operatividad continua.",
                    "C": "Vende el combustible de la planta eléctrica a transportistas externos para generar ingresos extras.",
                    "D": "Desconecta la planta eléctrica de la red del almacén para evitar que los operarios la usen."
                }
            },
            13: {
                "enunciado": "Durante la verificación diaria de las unidades de despacho a primera hora, detecta que un camión tiene los frenos desgastados y bota líquido por la rueda delantera:",
                "opciones": {
                    "A": "Retiene la unidad en el taller de inmediato, prohíbe su salida a ruta por riesgo de accidente fatal y gestiona la compra urgente de repuestos y reparación mecánica.",
                    "B": "Autoriza la salida del camión indicándole al chofer que maneje despacio y use solo el freno de motor.",
                    "C": "Le dice al chofer que le eche agua al depósito de frenos para que aguante el viaje de ida y vuelta.",
                    "D": "Obliga al ayudante de despacho a viajar sobre el estribo para revisar la rueda mientras rueda."
                }
            },
            14: {
                "enunciado": "En su relación con directores de operaciones y gerencias funcionales en empleos previos:",
                "opciones": {
                    "A": "He tenido divergencias técnicas sobre la asignación de flotas o presupuestos de mantenimiento, resolviéndolas con indicadores de costo-eficiencia y acatando la directriz superior.",
                    "B": "Los gerentes administrativos nunca entienden las necesidades mecánicas de los camiones de carga.",
                    "C": "No tolero que nadie supervise cómo organizo el almacén porque yo tengo mi propio método infalible.",
                    "D": "En todas las empresas donde he laborado he tenido directores y jefes absolutamente perfectos que jamás cometieron un solo error de juicio."
                }
            },
            15: {
                "enunciado": "Al auditar el área de almacenamiento, nota que el mantenimiento e imagen de las instalaciones está descuidado (luminarias quemadas, suciedad en pisos y goteras sobre las estibas):",
                "opciones": {
                    "A": "Deja las goteras abiertas argumentando que la empresa debe contratar albañiles externos.",
                    "B": "Diseña y ejecuta un plan de mantenimiento general: reubica la mercancía en riesgo, gestiona reparaciones eléctricas y de pintura, y coordina jornadas de fumigación y limpieza profunda.",
                    "C": "Cubre la mercancía mojada con cartones rotos para que la humedad no se note a simple vista.",
                    "D": "Apaga las luces del almacén para que los jefes no vean la suciedad en los pasillos de tránsito."
                }
            },
            16: {
                "enunciado": "Un contratista externo (mecánico o albañil) le ofrece entregar una factura inflada por la reparación de un camión para repartirse el dinero excedente con usted:",
                "opciones": {
                    "A": "Acepta la factura inflada y tramita el pago ante Administración para cobrar su parte.",
                    "B": "Le propone al contratista inflar todas las reparaciones del mes para tener un ingreso fijo.",
                    "C": "Acepta el trato y le entrega repuestos usados de la empresa al mecánico para que los venda.",
                    "D": "Rechaza de forma rotunda la propuesta ilícita, suspende al contratista del catálogo de servicios y reporta el intento de fraude a la Gerencia Administrativa."
                }
            },
            17: {
                "enunciado": "Al llegar la fuerza de ventas con mercancía devuelta por clientes de rutas foráneas:",
                "opciones": {
                    "A": "Recibe la mercancía mediante chequeo riguroso de condiciones físicas y fechas, clasifica entre aptos para reingreso o mermas, y formaliza el reporte consensuado con Ventas y Administración.",
                    "B": "Se niega a recibir las devoluciones argumentando que los vendedores deben quedarse con el producto.",
                    "C": "Tira los productos devueltos en el patio de maniobras para que los camiones les pasen por encima.",
                    "D": "Reingresa productos vencidos directamente a la estiba de venta para salir de ellos rápido."
                }
            },
            18: {
                "enunciado": "Se requiere coordinar la logística integral para técnicos especializados que prestarán servicios temporales en la planta durante dos semanas:",
                "opciones": {
                    "A": "Deja a los técnicos foráneos sin alojamiento ni comida diciendo que ellos deben resolver sus gastos.",
                    "B": "Gestiona oportunamente el hospedaje, alimentación, traslados internos y suministros de trabajo para el personal técnico foráneo, asegurando el cumplimiento de la obra en tiempo récord.",
                    "C": "Aloja a los técnicos en el suelo del almacén entre las paletas de mercancía para no gastar dinero.",
                    "D": "Se queja ante la Gerencia asegurando que atender a contratistas externos no le corresponde a Logística."
                }
            },
            19: {
                "enunciado": "Sobre la custodia y reserva de las rutas comerciales, inventarios críticos y asignación de flotas:",
                "opciones": {
                    "A": "Divulgo las rutas foráneas de transporte y horarios de salida con personas desconocidas en paradas viales.",
                    "B": "Jamás en toda mi vida he sentido la mínima curiosidad por mirar un dato ajeno ni he comentado asuntos internos.",
                    "C": "Mantengo estricta reserva y confidencialidad sobre el movimiento de flotas, inventarios de valor y rutas estratégicas, protegiendo la seguridad del personal y la carga.",
                    "D": "Vendo los cronogramas de entrega de la empresa a distribuidoras competidoras."
                }
            },
            20: {
                "enunciado": "Al revisar las órdenes de pedido del día, el Supervisor de Despacho nota que la capacidad volumétrica de los camiones asignados es insuficiente para cubrir la totalidad de la demanda:",
                "opciones": {
                    "A": "Cancela los despachos de los pueblos más lejanos de forma unilateral sin avisar a los clientes.",
                    "B": "Monta carga en los techos de los camiones arriesgando el volcamiento de las unidades en carretera.",
                    "C": "Coordina de forma inteligente el ruteo: reasigna pedidos según densidad geográfica, balancea el peso en unidades disponibles y programa una segunda vuelta de entrega eficiente.",
                    "D": "Se cruza de brazos diciendo que si faltan camiones la culpa es de la Junta Directiva."
                }
            },
            21: {
                "enunciado": "Durante el recorrido por el almacén, observa que los montacarguistas y operarios de picking circulan sin casco ni botas de seguridad, y utilizan teléfonos celulares mientras operan maquinaria:",
                "opciones": {
                    "A": "Interviene de inmediato, exige el uso obligatorio de los implementos de protección, prohíbe el uso de celulares durante la manipulación de carga y refuerza las normas de seguridad integral.",
                    "B": "Permite que sigan usando el teléfono celular mientras no choquen contra los racks.",
                    "C": "Les quita los teléfonos celulares a los operarios y se los guarda en su bolsillo personal.",
                    "D": "Bota los equipos de protección a la basura diciendo que los operarios trabajan mejor libres."
                }
            },
            22: {
                "enunciado": "Al finalizar el mes, debe presentar a la Gerencia Administrativa el informe de gestión de almacén, logística de flota y mantenimiento general:",
                "opciones": {
                    "A": "Envía un correo con tres líneas diciendo que todos los camiones rodaron y que el almacén está bien.",
                    "B": "Estructura el informe consolidando indicadores de efectividad de despacho, rotación de inventarios, consumo de combustible, horas de planta eléctrica y costos de mantenimiento vehicular.",
                    "C": "Copia el informe del mes pasado cambiando únicamente las fechas para salir rápido del compromiso.",
                    "D": "Se niega a presentar informes argumentando que el trabajo de logística se ve en el patio y no en papeles."
                }
            },
            23: {
                "enunciado": "Al auditar las devoluciones de facturas en ruta, nota que los choferes no entregan los comprobantes de cobranza ni concilian con la administración en el tiempo pautado:",
                "opciones": {
                    "A": "Apoya el proceso de gestión de cobranzas, coordina con el personal de despacho la entrega formal de facturas y valores, y asegura la liquidación rigurosa de cada ruta dentro del lapso legal.",
                    "B": "Permite que los choferes guarden el dinero de la cobranza en sus casas durante una semana.",
                    "C": "Rompe las facturas con observaciones para no tener que conciliar con el departamento de cobranzas.",
                    "D": "Le cobra una comisión personal a los choferes para no reportar los atrasos de liquidación."
                }
            },
            24: {
                "enunciado": "Sobre el autocontrol emocional ante reclamos de choferes o transportistas foráneos alterados:",
                "opciones": {
                    "A": "Si un chofer me levanta la voz reclamando por la tardanza de su carga, lo reto a pelear a golpes en el andén.",
                    "B": "He enfrentado momentos tensos con transportistas y personal de ruta, pero mantengo la compostura, la educación y resuelvo el conflicto con diálogo firme y apego a normas.",
                    "C": "Poseo una serenidad sobrehumana inalterable; absolutamente ningún conflicto laboral ni problema vial me ha generado molestia jamás en toda mi vida.",
                    "D": "Cuando me enojo con los transportistas, cierro las compuertas del almacén y paralizo la carga."
                }
            },
            25: {
                "enunciado": "Un supervisor de ventas le solicita que le despache mercancía sin orden de facturación formal emitida por el sistema, prometiendo que mañana a primera hora la factura:",
                "opciones": {
                    "A": "Despacha la mercancía de palabra confiando en la promesa del supervisor comercial.",
                    "B": "Le pide dinero prestado al supervisor a cambio de permitirle sacar los productos sin factura.",
                    "C": "Modifica los registros de inventario a mano para que la salida no figure en el sistema.",
                    "D": "Niega rotundamente la salida de la mercancía, recordando que todo despacho debe contar con orden formal validada y factura legal según el manual procedimental."
                }
            },
            26: {
                "enunciado": "Al verificar el estado de los vehículos asignados al transporte de alimentos, nota que dos furgones tienen olores residuales y filtraciones de polvo:",
                "opciones": {
                    "A": "Carga los alimentos en los camiones sucios diciendo que el empaque de plástico los protege.",
                    "B": "Detiene la carga, ordena el lavado, desinfección y sellado de filtraciones de los furgones, y asegura que las unidades cumplan con los estándares sanitarios antes de recibir los pedidos.",
                    "C": "Le echa perfume ambiental a la batea sucia para disimular los malos olores del furgón.",
                    "D": "Deja que los camiones salgan con filtraciones esperando que no llueva en la carretera."
                }
            },
            27: {
                "enunciado": "Se requiere extender la jornada de trabajo para realizar el inventario mensual rotativo de almacén y cuadre de flota que culminará a las 9:00 p.m.:",
                "opciones": {
                    "A": "Se retira a las 5:00 p.m. puntual diciendo que los inventarios nocturnos no están en su horario de oficina.",
                    "B": "Lidera la jornada con energía y rigor, organiza las cuadrillas de conteo físico, garantiza la cena y traslado seguro del equipo y entrega el balance cuadrado a la Gerencia.",
                    "C": "Se queda en la sede pero se encierra en una oficina a dormir mientras los operarios cuentan solos.",
                    "D": "Se queja a gritos con los operarios asegurando que la empresa abusa del personal de logística."
                }
            },
            28: {
                "enunciado": "Al momento de coordinar la salida de los camiones de ruta a primera hora de la mañana:",
                "opciones": {
                    "A": "Supervisa en el andén el check-list de cada vehículo (frenos, fluidos, luces), verifica la documentación legal en carpeta, constata la estiba trabada y da la salida formal a tiempo.",
                    "B": "Se queda sentado en su oficina tomando café y deja que los camiones salgan sin ninguna revisión.",
                    "C": "Firma los check-lists a ciegas sin mirar si los camiones tienen aceite o neumáticos desgastados.",
                    "D": "Permite que los choferes arranquen sin verificar si las compuertas llevan candado o precinto."
                }
            },
            29: {
                "enunciado": "En su relación con otros supervisores de la organización y reconocimientos laborales:",
                "opciones": {
                    "A": "Jamás en toda mi vida profesional he sentido el menor recelo, envidia o disconformidad cuando felicitan o premian a otro supervisor o líder de la empresa.",
                    "B": "En ocasiones he sentido sana emulación o deseo de que mi equipo de logística y almacén sea el más destacado, pero me concentro en trabajar con orden, seguridad y cero mermas.",
                    "C": "Considero que cuando premian a un líder en la empresa es únicamente por favoritismo de los dueños.",
                    "D": "No me gusta colaborar con los supervisores de otras áreas porque cada quien debe cuidar su puesto."
                }
            },
            30: {
                "enunciado": "Presidencia le encomienda realizar una auditoría reservada en el patio de maniobras ante sospechas de extracción no autorizada de combustible y repuestos en la flota:",
                "opciones": {
                    "A": "Le cuenta a los choferes y mecánicos sobre la investigación para que tomen precauciones.",
                    "B": "Se niega a realizar la auditoría argumentando que vigilar el patio le genera problemas con el personal.",
                    "C": "Ejecuta la auditoría con absoluto sigilo profesional: inspecciona tanques, contrasta kilometrajes, audita seriales de baterías/cauchos y entrega el informe reservado a Presidencia.",
                    "D": "Modifica las evidencias del informe para encubrir a amigos de trabajo que hayan tomado combustible."
                }
            }
        }
    },
    # =========================================================================
    # 24. OPERADOR DE MONTACARGAS (CJS-MTC)
    # =========================================================================
    "24_OPERADOR_DE_MONTACARGAS": {
        "codigo": "CJS-MTC",
        "titulo": "EVALUACIÓN PSICOTÉCNICA SITUACIONAL EN OPERACIÓN DE MONTACARGAS Y SEGURIDAD",
        "instrucciones": "Lea con atención cada situación laboral y de maniobra operativa. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con honestidad sobre su forma real de operar la máquina, cuidar la carga y aplicar las normas de seguridad. Dispone de un máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "Al encender el montacargas a primera hora de la mañana para validar las condiciones del equipo, nota que el pedal de freno baja hasta el fondo y tiene poca presión hidráulica:",
                "opciones": {
                    "A": "Comienza a operar el montacargas con cuidado frenando con el freno de mano o retroceso.",
                    "B": "Desconecta la alarma de freno para que no suene y trabaja solo en pasillos planos.",
                    "C": "Le echa agua al depósito de líquido de frenos para completar el nivel y arranca a cargar.",
                    "D": "No opera la máquina, coloca el aviso de \"Equipo Fuera de Servicio\", asienta la falla en el check-list y reporta de inmediato al supervisor y mantenimiento."
                }
            },
            2: {
                "enunciado": "Al descargar una paleta de 1.200 kg de un camión entrante, la carga viene con una altura de 1,80 metros que le bloquea completamente la visión hacia adelante:",
                "opciones": {
                    "A": "Acelera hacia adelante sacando la cabeza por un lado del mástil para intentar ver el camino.",
                    "B": "Desplaza el montacargas en reversa a velocidad moderada, con vista panorámica despejada hacia atrás y tocando la bocina en intersecciones y esquinas ciegas.",
                    "C": "Le pide a un ayudante de almacén que se monte parado sobre las uñas para que le avise si hay obstáculos.",
                    "D": "Empuja la paleta con las puntas de las uñas a ras de piso sin encarrilarla bien para que no tape."
                }
            },
            3: {
                "enunciado": "Al bajar una paleta de mayonesa del rack industrial para llevarla a despacho, observa que varias cajas del segundo nivel tienen líquido derramado y están aplastadas:",
                "opciones": {
                    "A": "Traslada la paleta con precaución a la zona de cuarentena/averías, identifica el daño, asienta el reporte de no conformidad de calidad y avisa al supervisor.",
                    "B": "Lleva la paleta directo al camión de despacho para que el chofer resuelva el problema con el cliente.",
                    "C": "Esconde las cajas aplastadas en el fondo de una estiba para que nadie se dé cuenta del daño.",
                    "D": "Bota los envases rotos en el contenedor de basura sin notificar para no atrasar la carga."
                }
            },
            4: {
                "enunciado": "En su rutina de trabajo como operador de montacargas y manejo de tensión:",
                "opciones": {
                    "A": "Si un despachador me apura para cargar un camión, le paso el montacargas cerca para asustarlo.",
                    "B": "En ocasiones he sentido tensión ante ritmos acelerados de carga y descarga, pero mantengo la serenidad, la velocidad segura y el apego estricto a las normas.",
                    "C": "Jamás en toda mi vida laboral he sentido la mínima presión, cansancio visual ni estrés operando maquinaria pesada.",
                    "D": "Prefiero manejar el montacargas sin cinturón de seguridad ni casco porque me incomodan para maniobrar."
                }
            },
            5: {
                "enunciado": "Al apilar una paleta pesada en el tercer nivel de una estantería industrial (rack), nota que la estructura metálica del rack tiene una abolladura pronunciada en la base:",
                "opciones": {
                    "A": "Golpea la columna abollada con las uñas del montacargas para intentar enderezarla.",
                    "B": "Coloca la paleta pesada en ese nivel de todos modos asumiendo que los racks aguantan mucho peso.",
                    "C": "Tapa la abolladura pegando una etiqueta amarilla encima para que pase la inspección visual.",
                    "D": "Se abstiene de colocar carga en ese módulo, señaliza la zona de peligro y reporta la deformación estructural al supervisor para su reparación técnica urgente."
                }
            },
            6: {
                "enunciado": "Al momento de abastecer de combustible (GLP o diésel) al montacargas al inicio de su jornada:",
                "opciones": {
                    "A": "Fuma un cigarrillo mientras cambia la bombona de gas para relajarse del trabajo matutino.",
                    "B": "Deja el motor del montacargas encendido mientras conecta la manguera de combustible para ahorrar tiempo.",
                    "C": "Apaga el motor, verifica que no haya fuentes de ignición cerca, usa guantes de protección, inspecciona fugas con agua jabonosa y registra los litros o cambio de bombona en el control diario.",
                    "D": "Golpea la válvula de la bombona de gas con una llave de hierro si nota que está trancada."
                }
            },
            7: {
                "enunciado": "Al transitar con el montacargas sin carga por los pasillos principales del almacén:",
                "opciones": {
                    "A": "Conduce con las uñas completamente abajo (a 15-20 cm del suelo) y el mástil ligeramente inclinado hacia atrás, respetando el límite de velocidad y los pasos peatonales.",
                    "B": "Maneja con las uñas elevadas a media altura (1,5 metros) para no tropezar con bultos sueltos.",
                    "C": "Acelera al máximo en las rectas del almacén haciendo sonar las llantas para probar la máquina.",
                    "D": "Permite que dos compañeros de almacén se suban a los estribos del montacargas para darles un aventón."
                }
            },
            8: {
                "enunciado": "Son las 4:50 p.m. (su hora de salida es a las 5:00 p.m.) y arriba al andén una gandola con materia prima urgente que debe ser descargada para no generar costos de sobreestadía:",
                "opciones": {
                    "A": "Asume la extensión horaria con compromiso profesional, ejecuta la descarga con máxima seguridad y concentración, y deja la mercancía ubicada en su lugar asignado.",
                    "B": "Apaga el montacargas a las 5:00 p.m. exacta, deja las uñas en el aire y se marcha sin avisar.",
                    "C": "Descarga las paletas a toda velocidad tirándolas de golpe contra el piso para salir rápido.",
                    "D": "Se esconde detrás de las estibas del almacén para que no lo vean y no le pidan que descargue."
                }
            },
            9: {
                "enunciado": "Respecto a la precisión de maniobra y respeto a los peatones en el almacén:",
                "opciones": {
                    "A": "Jamás en ninguno de mis empleos anteriores he tenido el más mínimo roce con un rack, paleta ni he rozado un objeto en toda mi trayectoria como operador.",
                    "B": "Considero que los peatones en el almacén siempre deben apartarse rápido porque el montacargas pesa más.",
                    "C": "Mantengo siempre una distancia prudencial de peatones, reduzco la marcha en cruces y utilizo la bocina para anunciar mi paso de forma preventiva.",
                    "D": "Si golpeo una paleta por ir distraído, prefiero culpar al despachador que la dejó mal ubicada."
                }
            },
            10: {
                "enunciado": "Un compañero de trabajo le pide que use las uñas del montacargas como elevador de personas para subirlo al techo a cambiar un bombillo:",
                "opciones": {
                    "A": "Lo sube parado sobre las uñas desnudas indicándole que se agarre fuerte del mástil.",
                    "B": "Lo sube parado sobre una paleta de madera suelta sin barandas ni arnés de seguridad.",
                    "C": "Le dice que se suba rápido antes de que el supervisor pase por el pasillo central.",
                    "D": "Rechaza la solicitud de manera categórica, recordando que está estrictamente prohibido usar el montacargas para elevar personas sin canastilla certificada y arnés."
                }
            },
            11: {
                "enunciado": "Al mover una paleta de productos hacia la zona de despacho, nota que el suelo del andén tiene manchas de aceite y residuos de plástico elástico (envoplast) tirados:",
                "opciones": {
                    "A": "Pasa por encima del aceite a alta velocidad patinando las ruedas motrices de la máquina.",
                    "B": "Ignora los plásticos dejando que se enrollen en el eje de las ruedas del montacargas.",
                    "C": "Detiene la marcha, delimita la zona resbaladiza, apoya en la limpieza del aceite con material absorbente y retira los plásticos para evitar atascamientos mecánicos y accidentes.",
                    "D": "Se queja insultando a los ayudantes de despacho y se niega a seguir trabajando en todo el día."
                }
            },
            12: {
                "enunciado": "Al intentar levantar una paleta de carga muy pesada, las ruedas traseras del montacargas se despegan del suelo (pérdida de estabilidad por sobrecarga):",
                "opciones": {
                    "A": "Le pide a tres ayudantes de almacén que se monten en el contrapeso trasero para hacer balance.",
                    "B": "Baja la carga de inmediato al suelo, suspende la maniobra, verifica el peso contra la placa de capacidad del equipo y divide la carga en dos paletas para operarla de forma segura.",
                    "C": "Acelera hacia adelante con las ruedas en el aire para ver si la inercia le permite moverla.",
                    "D": "Inclina el mástil totalmente hacia adelante para que la paleta se deslice por gravedad."
                }
            },
            13: {
                "enunciado": "Durante el traslado de un lote de azúcar, el montacargas sufre un recalentamiento súbito en la transmisión y empieza a botar humo por el compartimento del motor:",
                "opciones": {
                    "A": "Se detiene de inmediato en un lugar seguro y ventilado, baja las horquillas al piso, apaga el motor, señaliza la máquina y reporta la contingencia a Mantenimiento.",
                    "B": "Sigue manejando hasta completar la descarga para no retrasar los despachos de la tarde.",
                    "C": "Le echa agua fría directamente al motor encendido arriesgándose a fracturar componentes.",
                    "D": "Deja el montacargas abandonado con la carga en alto en medio del portón principal de entrada."
                }
            },
            14: {
                "enunciado": "En su relación con jefaturas y normas de seguridad en sus empleos previos:",
                "opciones": {
                    "A": "He tenido observaciones de supervisores sobre el ángulo de inclinación de la carga, aceptando la corrección técnica y ajustando mi maniobra según los estándares.",
                    "B": "Los jefes de almacén exigen demasiado cuidado pero no saben lo difícil que es maniobrar con prisa.",
                    "C": "No permito que nadie supervise cómo manejo porque yo sé más de montacargas que cualquier ingeniero.",
                    "D": "En todas las empresas donde he laborado he tenido supervisores de operaciones absolutamente perfectos que jamás tuvieron que hacerme una sugerencia."
                }
            },
            15: {
                "enunciado": "Al momento de introducir las uñas en una paleta de doble entrada para descargarla de una gandola:",
                "opciones": {
                    "A": "Mete las uñas inclinadas hacia abajo rasgando la madera y perforando los sacos inferiores.",
                    "B": "Empuja la paleta con una sola uña para cuadrarla a la fuerza antes de levantarla.",
                    "C": "Ajusta la apertura de las uñas a la anchura de la paleta, nivela las horquillas en paralelo al suelo, entra hasta el fondo del palé y levanta suavemente asegurando la carga.",
                    "D": "Entra a toda velocidad golpeando la carga contra la pared metálica de la batea del camión."
                }
            },
            16: {
                "enunciado": "Un chofer foráneo le ofrece pagarle $15 en efectivo para que lo descargue a él primero, saltándose el orden de llegada establecido en el almacén:",
                "opciones": {
                    "A": "Acepta el dinero y descarga al chofer amigo dejando esperando a los que llegaron antes.",
                    "B": "Negocia que le pague $30 por descargarlo rápido y le guarda un puesto en el andén.",
                    "C": "Le pide al chofer que le regale mercancía de la gandola para darle prioridad de descarga.",
                    "D": "Rechaza la oferta tajantemente, respeta el orden de llegada fijado por Logística y reporta el intento de soborno a la Gerencia de Almacén."
                }
            },
            17: {
                "enunciado": "Al transportar mercancía por una rampa o plano inclinado dentro de las instalaciones del almacén:",
                "opciones": {
                    "A": "Sube y baja con la carga orientada hacia la parte superior de la rampa (sube hacia adelante y baja en reversa), manteniendo la carga estable contra el mástil inclinado.",
                    "B": "Baja la rampa hacia adelante con la carga en alto arriesgando un volcamiento frontal.",
                    "C": "Realiza giros en \"U\" en medio de la rampa para probar la estabilidad de las ruedas.",
                    "D": "Baja la rampa en punto muerto (neutro) apagando el motor para ahorrar combustible."
                }
            },
            18: {
                "enunciado": "Al realizar el control diario de consumo de combustible del montacargas, nota una diferencia notable de consumo en comparación con las horas trabajadas en el horómetro:",
                "opciones": {
                    "A": "Llena la planilla con números falsos para que el cálculo matemático coincida en el papel.",
                    "B": "Revisa si existen fugas visibles en el sistema de combustible, asienta las lecturas reales del horómetro y reporta la anomalía a Mantenimiento para su inspección técnica.",
                    "C": "Extrae combustible del montacargas con una manguera para uso en su vehículo personal.",
                    "D": "Ignora la discrepancia argumentando que el combustible es gasto que asume la empresa."
                }
            },
            19: {
                "enunciado": "Sobre la honestidad y la custodia de productos durante la operación del equipo:",
                "opciones": {
                    "A": "Si al bajar una paleta se rompe una caja de galletas, me como los productos con los compañeros del patio.",
                    "B": "Jamás en toda mi vida laboral he sentido la menor tentación de tomar un producto ajeno ni he ocultado un daño material.",
                    "C": "Custodio la mercancía con total integridad, reportando cualquier merma o daño accidental de inmediato por los canales regulares de calidad.",
                    "D": "Me llevo envases de plástico y herramientas del taller a mi casa sin pedir permiso a nadie."
                }
            },
            20: {
                "enunciado": "Debe apilar paletas de sacos de harina en un bloque de almacenamiento en piso (estiba en bloque):",
                "opciones": {
                    "A": "Apila las paletas torcidas unas sobre otras sin importar que queden al borde del colapso.",
                    "B": "Coloca cuatro niveles de paletas pesadas sobre una paleta base que tiene maderas rajadas.",
                    "C": "Verifica que la paleta base esté sólida y nivelada, alinea las paletas verticalmente respetando la altura máxima permitida por manual y mantiene los frentes ordenados.",
                    "D": "Empuja las paletas con la defensa del montacargas para apretarlas contra la pared del almacén."
                }
            },
            21: {
                "enunciado": "Al culminar el turno de trabajo y disponer el montacargas para su resguardo nocturno:",
                "opciones": {
                    "A": "Deja el montacargas atravesado en el pasillo principal con las uñas elevadas a un metro de altura.",
                    "B": "Deja la llave de encendido pegada en el suiche y el equipo encendido en neutro en el patio.",
                    "C": "Se marcha sin poner el freno de mano dejando la máquina sobre una pendiente.",
                    "D": "Estaciona en el área designada, baja las horquillas completamente al suelo, inclina el mástil hacia adelante, aplica el freno de mano, apaga el motor, retira la llave y entrega el reporte."
                }
            },
            22: {
                "enunciado": "En el patio de maniobras externo comienza a llover con fuerza y se requiere trasladar paletas de cartón corrugado hacia el almacén techado:",
                "opciones": {
                    "A": "Maneja a toda velocidad derrapando en las curvas mojadas para terminar antes de empaparse.",
                    "B": "Disminuye la velocidad a paso peatonal, incrementa la distancia de seguridad, protege la carga con cobertores plásticos y conduce con máxima precaución sobre piso húmedo.",
                    "C": "Deja las paletas de cartón abandonadas bajo la lluvia en el patio para no mojarse la ropa.",
                    "D": "Desconecta las luces del montacargas para evitar que se quemen con el agua de lluvia."
                }
            },
            23: {
                "enunciado": "Al inspeccionar el montacargas en la rutina diaria, nota que una de las cadenas de elevación del mástil está destensada o presenta un eslabón fisurado:",
                "opciones": {
                    "A": "Informa la anomalía de inmediato a Mantenimiento, no opera la función de elevación con peso y espera la sustitución o ajuste técnico antes de mover cargas pesadas.",
                    "B": "Le echa grasa espesa a la fisura para disimular la grieta y sigue trabajando normalmente.",
                    "C": "Amarra la cadena con un alambre dulce para evitar que se rompa durante el día.",
                    "D": "Ignora la falla argumentando que las máquinas tienen dos cadenas y con una es suficiente."
                }
            },
            24: {
                "enunciado": "Sobre el autocontrol y la tolerancia ante reclamos o llamados de atención en el patio:",
                "opciones": {
                    "A": "Si un transportista me grita porque tardo en descargarlo, bajo las uñas de golpe y me voy a pelear.",
                    "B": "He experimentado momentos de tensión con choferes impacientes en el andén, pero mantengo la compostura, la educación y ejecuto las maniobras con rigor técnico y seguridad.",
                    "C": "Poseo una serenidad sobrehumana inalterable; absolutamente ningún conflicto, calor extremo ni reclamo me ha causado molestia jamás.",
                    "D": "Cuando me enojo con un supervisor, golpeo las estanterías con el contrapeso del montacargas."
                }
            },
            25: {
                "enunciado": "Un supervisor de turno le pide que sobrecargue el montacargas con 500 kg por encima del límite nominal de la máquina para terminar de vaciar una gandola rápido:",
                "opciones": {
                    "A": "Acepta sobrecargar el equipo asumiendo el riesgo de volcarse o reventar los sellos hidráulicos.",
                    "B": "Pide dinero adicional al supervisor para arriesgarse a operar la máquina con sobrepeso.",
                    "C": "Intenta levantar la carga inclinando el mástil hacia adelante para ver si el montacargas aguanta.",
                    "D": "Explica con respeto técnico el riesgo inminente de accidente y daño a la maquinaria, y divide la carga respetando la capacidad nominal certificada del equipo."
                }
            },
            26: {
                "enunciado": "Durante la búsqueda y movimiento de paletas en el almacén, observa que una caja cayó al pasillo y bloquea la línea de tránsito de otros equipos móviles:",
                "opciones": {
                    "A": "Le pasa por encima con las ruedas del montacargas aplastando la caja y destruyendo el producto.",
                    "B": "Detiene la máquina en lugar seguro con freno aplicado, recoge la caja, verifica su estado, la coloca en su estiba y deja la vía de circulación libre de obstáculos.",
                    "C": "Patea la caja debajo de una estantería para que nadie la vea en el medio del pasillo.",
                    "D": "Pasa esquivando la caja a alta velocidad sin importarle que otro vehículo la tropiece."
                }
            },
            27: {
                "enunciado": "Se requiere extender la jornada 45 minutos para apoyar en el traslado y despeje de la zona de despacho previo a una auditoría operativa de la empresa:",
                "opciones": {
                    "A": "Se niega rotundamente a quedarse argumentando que su horario vence a las 5:00 p.m. en punto.",
                    "B": "Asume la labor con compromiso y sentido de colaboración, apoya el despeje del andén y deja los equipos en orden y resguardo seguro.",
                    "C": "Se queda en las instalaciones pero se sienta en el montacargas apagado a mirar el teléfono móvil.",
                    "D": "Se queja a gritos en el patio asegurando que la empresa abusa del personal operativo."
                }
            },
            28: {
                "enunciado": "Al acomodar cargas en la zona de despacho, se percata de que un palé tiene una tabla rota en la base que hace que la mercancía quede inclinada:",
                "opciones": {
                    "A": "Baja la carga con cuidado, solicita el traspaso a un palé en perfecto estado, asegura la mercancía y la ubica en el área de despacho sin riesgo de desplome.",
                    "B": "Deja la paleta inclinada en el andén y le dice a los ayudantes que la sostengan con las manos.",
                    "C": "Apuntala la paleta partida colocándole un pedazo de cartón doblado debajo de la madera rota.",
                    "D": "Monta la paleta inclinada en el camión esperando que el viaje termine de romperla."
                }
            },
            29: {
                "enunciado": "En su relación con otros operadores de montacargas y reconocimientos de la empresa:",
                "opciones": {
                    "A": "Jamás en toda mi vida profesional he sentido la mínima envidia, recelo o molestia cuando felicitan a otro operador por su destreza o cuidado del equipo.",
                    "B": "A veces he sentido sana emulación o deseo de destacar como el operador más pulcro y seguro, pero me enfoco en cuidar la máquina, evitar averías y trabajar con exactitud.",
                    "C": "Considero que cuando felicitan a un montacarguista en la empresa es únicamente por compadrazgo con los jefes.",
                    "D": "Prefiero no advertirle a los otros operadores cuando una máquina tiene fallas para que ellos queden mal."
                }
            },
            30: {
                "enunciado": "La Dirección le encomienda realizar una inspección reservada del estado mecánico y consumo real de combustible de los montacargas de los otros turnos ante sospechas de desvío:",
                "opciones": {
                    "A": "Le avisa a los otros operadores de turno para que arreglen las cifras antes de la revisión.",
                    "B": "Se niega a realizar la inspección argumentando que no le corresponde revisar máquinas ajenas.",
                    "C": "Ejecuta la inspección con absoluto sigilo profesional: audita horómetros, niveles de combustible, estado de uñas/cadenas y entrega el informe técnico reservado a la Dirección.",
                    "D": "Altera los datos del informe técnico para encubrir a compañeros de trabajo amigos."
                }
            }
        }
    },

    # =========================================================================
    # 27. VIGILANTE / SEGURIDAD INTEGRAL Y CONTROL DE ACCESOS (CJS-VIG)
    # =========================================================================
    "27_VIGILANTE": {
        "codigo": "CJS-VIG",
        "titulo": "EVALUACIÓN PSICOTÉCNICA EN SEGURIDAD INTEGRAL Y CONTROL DE ACCESOS",
        "instrucciones": "Lea con atención cada situación de resguardo, inspección en garita y rondas de seguridad. Marque con una equis [ X ] una sola opción (A, B, C o D) por pregunta. Responda con honestidad sobre su integridad, apego a las normas internas, firmeza y discreción. Dispone de un máximo de 45 minutos.",
        "preguntas": {
            1: {
                "enunciado": "Al finalizar la jornada a las 5:00 p.m., un trabajador de almacén intenta salir por la puerta peatonal llevando una caja de herramientas de la empresa en un morral, pero no presenta pase de salida ni factura:",
                "opciones": {
                    "A": "Lo deja salir sin revisar porque es un compañero antiguo y de confianza en la planta.",
                    "B": "Le pide al trabajador que le preste una herramienta a cambio de no decir nada.",
                    "C": "Le permite la salida y anota en el libro que la caja era de uso personal del empleado.",
                    "D": "Frena la salida, solicita el soporte formal o factura reglamentaria, retiene la herramienta en custodia y notifica la no conformidad al supervisor a cargo."
                }
            },
            2: {
                "enunciado": "Al momento de iniciar su turno de guardia a las 7:00 a.m., debe realizar la recepción del puesto junto al vigilante saliente:",
                "opciones": {
                    "A": "Firma el libro de novedades a ciegas en la entrada y se sienta en la garita a desayunar.",
                    "B": "Realiza el recorrido físico por todas las áreas asignadas, efectúa el inventario externo de vehículos y activos, y recibe verbalmente y por escrito las novedades y consignas.",
                    "C": "Deja que el vigilante saliente se marche sin hacer entrega física ni balance de llaves.",
                    "D": "Empieza su turno sin uniforme reglamentario diciendo que la dotación le incomoda."
                }
            },
            3: {
                "enunciado": "Durante su ronda periódica nocturna por el almacén, detecta olor a quemado y un recalentamiento con chispas en la brequera principal del tablero de iluminación:",
                "opciones": {
                    "A": "Aplica el procedimiento de seguridad: aísla la zona, baja la palanca de corte de la brequera con equipo dieléctrico, utiliza el extintor adecuado si hay llama y reporta de inmediato la avería.",
                    "B": "Le echa un tobo de agua fría directamente a la brequera con corriente para apagar el recalentamiento.",
                    "C": "Ignora las chispas y continúa su ronda diciendo que los problemas eléctricos le tocan a mantenimiento.",
                    "D": "Tapa la brequera con un trapo viejo para que el humo no se extienda por el almacén."
                }
            },
            4: {
                "enunciado": "En su trayectoria profesional y desempeño en puestos de vigilancia:",
                "opciones": {
                    "A": "Si un visitante no me saluda con respeto, le impido la entrada a la fuerza y lo insulto.",
                    "B": "En ocasiones he sentido fatiga o monotonía durante turnos largos de guardia o rondas a pie, pero mantengo la alerta visual, el porte del uniforme y el cumplimiento del reglamento.",
                    "C": "Jamás en toda mi vida he sentido sueño, cansancio ni he pestañeado un segundo durante un turno de vigilancia nocturna.",
                    "D": "Prefiero hacer las rondas sin linterna ni equipos de seguridad para no cargar peso extra."
                }
            },
            5: {
                "enunciado": "Son las 5:00 p.m. (su hora de salida), pero el vigilante que debe relevarlo en el turno entrante no ha llegado a la garita principal de acceso:",
                "opciones": {
                    "A": "Apaga las luces de la garita, deja los portones abiertos y se retira a su casa a la hora en punto.",
                    "B": "Le entrega las llaves de la empresa al chofer de un camión para que él cuide la puerta.",
                    "C": "Se marcha de las instalaciones dejando encargado a un transeúnte de la calle.",
                    "D": "Permanece en el puesto sin abandonar el área asignada, reporta el retraso al supervisor a cargo y espera la entrega física y el recorrido formal con el relevo."
                }
            },
            6: {
                "enunciado": "Un proveedor comercial llega a las instalaciones solicitando acceso en su vehículo particular para reunirse con la Gerencia Comercial:",
                "opciones": {
                    "A": "Lo deja entrar directamente al estacionamiento interno sin pedirle identificación ni registrarlo.",
                    "B": "Solicita identificación oficial, confirma la cita con la gerencia, registra datos en el libro de control de visitas y vehículos, inspecciona la maleta y entrega el pase de visitante.",
                    "C": "Le prohíbe el acceso a gritos al proveedor diciendo que en esa empresa no entra nadie.",
                    "D": "Le cobra una tarifa personal en efectivo al visitante para permitirle estacionar adentro."
                }
            },
            7: {
                "enunciado": "Durante la verificación final de las instalaciones al cerrar las oficinas administrativas a las 6:00 p.m.:",
                "opciones": {
                    "A": "Recorre el recinto cubriendo todas las áreas, constata que ventanas, puertas y otros accesos estén cerrados, apaga luces innecesarias y asegura candados perimetrales.",
                    "B": "Mira las oficinas desde la puerta principal sin caminar los pasillos y da por cerrado el turno.",
                    "C": "Deja abiertas las ventanas del área de facturación para que entre aire fresco en la noche.",
                    "D": "Fuerza las cerraduras de los escritorios para ver si los empleados guardaron dinero en efectivo."
                }
            },
            8: {
                "enunciado": "Son las 4:50 p.m. y el chofer de una gandola foránea exige retirar el camión de la planta apresuradamente, negándose a que le revisen la batea de carga:",
                "opciones": {
                    "A": "Mantiene la compostura y la autoridad preventiva: niega la apertura del portón hasta realizar la revisión selectiva y exhaustiva de la carga contra factura en mano.",
                    "B": "Abre el portón inmediatamente para evitar discusiones con el chofer foráneo.",
                    "C": "Insulta al chofer y le lanza piedras al parabrisas del camión para detenerlo.",
                    "D": "Se encierra en la garita y deja que el chofer empuje el portón con el camión si quiere."
                }
            },
            9: {
                "enunciado": "Respecto a la puntualidad y el cumplimiento de las consignas de vigilancia:",
                "opciones": {
                    "A": "Jamás en ninguno de mis empleos anteriores he llegado un solo segundo tarde a mi guardia ni he dejado de anotar una placa en el libro de control en toda mi vida.",
                    "B": "Considero que registrar la entrada y salida de los empleados de la empresa es una pérdida de tiempo innecesaria.",
                    "C": "Registro rigurosamente los ingresos y egresos de personas y vehículos, cumpliendo con disciplina los horarios y protocolos de seguridad integral.",
                    "D": "Si el libro de novedades se llena, prefiero no anotar nada durante varios días hasta que traigan otro."
                }
            },
            10: {
                "enunciado": "Un empleado del área de ventas con el que usted mantiene una estrecha relación de amistad le pide que le guarde un paquete en la garita sin revisarlo:",
                "opciones": {
                    "A": "Acepta guardarle el paquete sin revisar confiando en la amistad que tienen.",
                    "B": "Le propone al amigo esconder más mercancía en la garita para repartírsela al final de la semana.",
                    "C": "Se apropia del paquete de su amigo y se lo lleva a su casa al terminar el turno.",
                    "D": "Rechaza la petición con respeto, recuerda que el reglamento prohíbe relaciones personales que comprometan la función y exige la revisión y el pase de salida formal."
                }
            },
            11: {
                "enunciado": "Al realizar la revisión selectiva de salida a un vehículo de reparto de la empresa:",
                "opciones": {
                    "A": "Saluda al chofer desde la garita y le levanta la barrera sin verificar la mercancía ni la batea.",
                    "B": "Revisa solo la cabina del camión ignorando el furgón de carga por pereza de abrir la compuerta.",
                    "C": "Solicita las facturas y guías de despacho, abre la compuerta, constata que los bultos coincidan con los soportes y que no existan objetos no autorizados, firmando el control.",
                    "D": "Rompe las facturas del chofer para que el transporte no pueda salir a trabajar."
                }
            },
            12: {
                "enunciado": "Al verificar el llavero central de resguardo de los vehículos de la compañía bajo su custodia:",
                "opciones": {
                    "A": "Deja las llaves de todos los camiones puestas en los tableros de los vehículos en el patio abierto.",
                    "B": "Mantiene las llaves bajo llave en el tablero de seguridad de la garita, entregándolas exclusivamente al personal autorizado previa firma en el libro de control vehicular.",
                    "C": "Le entrega las llaves de un camión a un familiar de un chofer sin contar con autorización de la jefatura.",
                    "D": "Pierde el juego de llaves maestras de la empresa y no lo reporta a la administración por miedo."
                }
            },
            13: {
                "enunciado": "Durante el recorrido perimetral de la madrugada, observa a dos personas sospechosas merodeando la cerca trasera de las instalaciones:",
                "opciones": {
                    "A": "Activa de inmediato el protocolo de seguridad: ilumina la zona con la linterna, mantiene distancia prudencial de resguardo, alerta por radio a la base y comunica la novedad a los cuerpos policiales.",
                    "B": "Sale corriendo a la calle a enfrentarse solo y a golpes contra los dos sujetos armados.",
                    "C": "Se esconde en un depósito y apaga su radio para que nadie le pida que revise el perímetro.",
                    "D": "Dispara piedras contra la cerca sin verificar quiénes son las personas."
                }
            },
            14: {
                "enunciado": "En su relación con directivos y supervisores de seguridad en empleos previos:",
                "opciones": {
                    "A": "He tenido llamados de atención por demoras en la apertura de un acceso vehicular, pero acepté la corrección técnica, optimicé mi atención en garita y respeté la línea de mando.",
                    "B": "Los supervisores de seguridad siempre exigen estar de pie pero nunca colaboran con la vigilancia.",
                    "C": "No permito que nadie me supervise las rondas porque yo sé cuidar mejor que cualquiera.",
                    "D": "En todas las empresas donde he laborado he tenido supervisores de seguridad absolutamente perfectos que jamás me hicieron una sola observación."
                }
            },
            15: {
                "enunciado": "Al momento de registrar la asistencia de entrada del personal obrero en el portón a las 7:00 a.m.:",
                "opciones": {
                    "A": "Permite que los trabajadores entren sin registrarse diciendo que el reloj biométrico es suficiente.",
                    "B": "Anota hora de llegada puntual a trabajadores que llegaron media hora tarde a cambio de un refresco.",
                    "C": "Registra minuciosamente la hora real de ingreso de cada trabajador, verifica el porte del carnet y uniforme, y reporta las tardanzas con objetividad a Talento Humano.",
                    "D": "Discute a gritos con los trabajadores que llegan temprano impidiéndoles el paso al recinto."
                }
            },
            16: {
                "enunciado": "Un directivo de la compañía sale de la planta a las 8:00 p.m. en su vehículo y le pide que deje los portones principales abiertos porque regresará en 10 minutos:",
                "opciones": {
                    "A": "Deja los portones abiertos de par en par y se va a dormir a la garita durante los 10 minutos.",
                    "B": "Le dice al directivo que no le abre la puerta porque su turno ya terminó.",
                    "C": "Invita a vecinos de la calle a pasar a la empresa mientras el portón está abierto.",
                    "D": "Cierra y asegura los portones inmediatamente después de la salida del directivo, y permanece atento para abrir nuevamente cuando este retorne a la sede."
                }
            },
            17: {
                "enunciado": "Al efectuar el recorrido en el área de talleres y andenes de carga durante la noche:",
                "opciones": {
                    "A": "Verifica que no existan herramientas abandonadas, inspecciona equipos energizados innecesariamente, previene riesgos de incendio y reporta cualquier anomalía en el libro.",
                    "B": "Se apropia de cables de cobre y herramientas que hayan quedado sobre las mesas de trabajo.",
                    "C": "Desconecta las cámaras de seguridad del andén para que no graben sus movimientos nocturnos.",
                    "D": "Deja prendidas las máquinas pesadas del taller para ver si aguantan encendidas hasta el día siguiente."
                }
            },
            18: {
                "enunciado": "Un transportista le solicita permiso para pernoctar dentro de su camión en el patio de maniobras de la empresa sin contar con orden de estancia emitida por Logística:",
                "opciones": {
                    "A": "Le permite quedarse a cambio de que el transportista le pague una suma en dinero en efectivo.",
                    "B": "Verifica con el supervisor de guardia si existe autorización escrita; de no haberla, niega la permanencia en el recinto según el reglamento y orienta al chofer hacia zonas de descanso externas.",
                    "C": "Le permite pernoctar y además le entrega las llaves de las oficinas para que duerma adentro.",
                    "D": "Insulta al chofer y lo amenaza con llamar a la policía si no se marcha en un minuto."
                }
            },
            19: {
                "enunciado": "Sobre la honradez y la custodia de objetos olvidados o mercancía en los accesos de la empresa:",
                "opciones": {
                    "A": "Si encuentro un teléfono celular o dinero olvidado en la garita, me lo guardo en el bolsillo sin decir nada.",
                    "B": "Jamás en toda mi vida he sentido la mínima curiosidad por mirar un bolso ajeno ni he tomado un alfiler que no me pertenezca.",
                    "C": "Resguardo con estricta integridad cualquier pertenencia, paquete u objeto extraviado, registrándolo en el libro de novedades y entregándolo a la Gerencia o a su dueño.",
                    "D": "Vendo los objetos olvidados a otros empleados de la empresa para ganarme un dinero extra."
                }
            },
            20: {
                "enunciado": "Al revisar el área asignada al entrar a su turno, nota que el candado de la puerta trasera de un depósito secundario está violentado o forzado:",
                "opciones": {
                    "A": "Cambia el candado roto por uno nuevo de su bolsillo sin avisar a nadie para que no lo culpen.",
                    "B": "Entra al depósito a tomar productos antes de que los jefes se den cuenta de la rotura.",
                    "C": "No mueve la escena, asegura el perímetro exterior, notifica de inmediato al supervisor de seguridad y levanta la minuta detallada con registro fotográfico.",
                    "D": "Se marcha del puesto de guardia diciendo que él no cuida depósitos rotos."
                }
            },
            21: {
                "enunciado": "Al momento de llevar a cabo el control de entrada de un camión cisterna o de carga pesada:",
                "opciones": {
                    "A": "Abre los portones desde lejos sin revisar cabina ni pedir documentos al conductor.",
                    "B": "Le pide al chofer que le regale combustible de la cisterna para permitirle descargar.",
                    "C": "Deja el camión atravesado en la calle durante horas por puro capricho sin atenderlo.",
                    "D": "Realiza la inspección de seguridad: solicita guía de despacho, verifica placa y chofer, hace colocar tacos de seguridad (cuñas), inspecciona la unidad y guía el ingreso al andén."
                }
            },
            22: {
                "enunciado": "Durante su turno en la garita, se produce una falla eléctrica en las oficinas y el supervisor le solicita cambiar la brequera del circuito de computación:",
                "opciones": {
                    "A": "Realiza el cambio de brequera utilizando herramientas aisladas, verifica el amperaje correspondiente al circuito, baja el interruptor principal antes de intervenir y prueba el sistema.",
                    "B": "Coloca un cable de cobre directo sin brequera puenteando la caja eléctrica con riesgo de incendio.",
                    "C": "Se niega a colaborar diciendo que cambiar una brequera no le compete al personal de vigilancia.",
                    "D": "Golpea la caja de fusibles con un martillo para intentar reactivar la luz a la fuerza."
                }
            },
            23: {
                "enunciado": "Al momento de entregar el turno de vigilancia al relevo entrante:",
                "opciones": {
                    "A": "Efectúa el recorrido conjunto por todas las instalaciones, entrega el llavero vehicular completo, revisa el inventario externo de activos y asienta las novedades verbalmente y por escrito.",
                    "B": "Deja una nota arrugada sobre la mesa de la garita y se va corriendo antes de que llegue el relevo.",
                    "C": "Se marcha sin entregar novedades diciendo que en la noche nunca pasa nada importante.",
                    "D": "Le entrega el puesto a un empleado de limpieza que no tiene funciones de seguridad."
                }
            },
            24: {
                "enunciado": "Sobre el autocontrol emocional ante empleados o choferes que se niegan a ser revisados en la salida:",
                "opciones": {
                    "A": "Si un trabajador se resiste a que le revise el bolso, le saco un palo y me pongo a pelear en la puerta.",
                    "B": "He enfrentado trabajadores molestos ante las revisiones de rutina, pero mantengo la compostura, la educación y recuerdo con firmeza que la inspección es norma de la empresa.",
                    "C": "Poseo una paz mental celestial e inalterable; absolutamente ninguna ofensa, insulto ni amenaza ha provocado en mí la más mínima molestia en toda mi vida.",
                    "D": "Cuando un chofer me habla golpeado, le bajo la barrera metálica encima de la cabina del camión."
                }
            },
            25: {
                "enunciado": "Un empleado de confianza le pide que le permita salir de las instalaciones 2 horas antes de culminar su horario sin pase firmado por su supervisor:",
                "opciones": {
                    "A": "Lo deja salir por la puerta trasera pidiéndole que no le cuente a nadie.",
                    "B": "Le cobra una tarifa personal en efectivo al empleado para autorizarle la salida clandestina.",
                    "C": "Firma usted mismo el pase de salida haciéndose pasar por el gerente del empleado.",
                    "D": "Niega la salida sin el pase debidamente firmado por la jefatura autorizada, explicando que por reglamento interno toda salida anticipada debe estar soportada."
                }
            },
            26: {
                "enunciado": "Durante la noche, se activa una alarma sonora contra intrusos en el área del depósito de materias primas:",
                "opciones": {
                    "A": "Desconecta la alarma para que deje de hacer ruido y continúa durmiendo en la garita.",
                    "B": "Acude con linterna y equipo de protección con máxima precaución táctica, verifica si se trata de una falsa alarma o intrusión real, y reporta la situación de inmediato a la base.",
                    "C": "Se queda sentado en la garita esperando que los intrusos salgan por su propia cuenta.",
                    "D": "Lanza disparos al aire en la oscuridad sin saber qué causó la activación de la alarma."
                }
            },
            27: {
                "enunciado": "Se requiere extender su jornada de vigilancia 3 horas debido a que el relevo del turno de la noche sufrió un percance vial y viene en camino:",
                "opciones": {
                    "A": "Se niega rotundamente a quedarse y abandona el portón principal desprotegido a su hora de salida.",
                    "B": "Asume la extensión con compromiso y sentido del deber, mantiene el resguardo de las instalaciones y efectúa la entrega formal cuando arribe el compañero.",
                    "C": "Se queda en la garita pero se acuesta a dormir en el suelo dejando la empresa a oscuras.",
                    "D": "Se queja a gritos con los directores asegurando que el trabajo de seguridad es una esclavitud."
                }
            },
            28: {
                "enunciado": "Al momento de mantener la garita y su equipo de dotación asignado (linterna, radio transmisor, libros de control y botiquín):",
                "opciones": {
                    "A": "Mantiene limpio y en orden el equipo y sitio de trabajo, reporta cualquier anomalía técnica y asegura que las baterías de los radios y linternas queden cargadas.",
                    "B": "Deja la garita llena de restos de comida, envases vacíos y basura regada por el piso.",
                    "C": "Rompe el radio transmisor contra la mesa cuando se enoja por recibir una orden.",
                    "D": "Se lleva las linternas y radios de dotación para su casa sin permiso del supervisor."
                }
            },
            29: {
                "enunciado": "En su relación con otros vigilantes y evaluaciones del personal de seguridad:",
                "opciones": {
                    "A": "Jamás en toda mi vida laboral he sentido el menor recelo, molestia o envidia cuando felicitan a otro vigilante por haber frustrado un robo o por su disciplina.",
                    "B": "A veces he sentido sana emulación o deseo de destacar como el vigilante más alerta y puntual, pero me concentro en que mi área asignada esté 100% segura y sin pérdidas.",
                    "C": "Considero que cuando felicitan a un vigilante en la empresa es únicamente porque es un delator de los jefes.",
                    "D": "Prefiero no hablar con los otros vigilantes porque en los puestos de seguridad todos son desleales."
                }
            },
            30: {
                "enunciado": "La Gerencia le encomienda realizar un monitoreo reservado y confidencial sobre las salidas de vehículos de carga ante sospechas de complicidad interna en fugas de producto:",
                "opciones": {
                    "A": "Le avisa a los choferes y despachadores amigos para que no saquen mercancía durante su guardia.",
                    "B": "Se niega a realizar el monitoreo argumentando que vigilar a compañeros de trabajo es desleal.",
                    "C": "Ejecuta la vigilancia con absoluto sigilo profesional: inspecciona salidas, coteja facturas vs. mercancía física, anota irregularidades y entrega el informe reservado a Gerencia.",
                    "D": "Modifica las anotaciones en el libro de control vehicular para encubrir a trabajadores conocidos."
                }
            }
        }
    }
    }

def obtener_datos_test(perfil_key: str):
    """Retorna los datos del instrumento buscando por clave exacta o prefijo."""
    if not perfil_key:
        return None
    if perfil_key in BANCO_PREGUNTAS:
        return BANCO_PREGUNTAS[perfil_key]
    pk_clean = str(perfil_key).upper().strip()
    prefijo = pk_clean.split("_")[0]
    if prefijo.isdigit():
        p_num = f"{int(prefijo):02d}_"
        for k, v in BANCO_PREGUNTAS.items():
            if k.startswith(p_num) or k.startswith(f"{int(prefijo)}_"):
                return v
    for k, v in BANCO_PREGUNTAS.items():
        if any(palabra in k for palabra in pk_clean.split("_") if len(palabra) > 3):
            return v
    return None