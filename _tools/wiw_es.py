# Spanish (Spain) copy for the client city. Keys mirror wiw_content.P by "num".
DISTRICTS = {
    "old-town": ("Casco Antiguo", "Dueños y operaciones", "Negocios de servicios donde cada trabajo es un presupuesto nuevo, una obra nueva o un pedido nuevo. Aquí la IA tiene que aguantar la operativa real."),
    "business-district": ("Distrito Financiero", "Dirección y trabajo regulado", "Personas cuyas decisiones pesan: un CEO, una clínica, un auditor, un proyecto con riesgos de seguridad. Aquí la IA tiene que poder verificarse."),
    "market-square": ("Plaza del Mercado", "Marketing y ventas", "Gente que vive de la atención y del pipeline. Aquí la IA tiene que sonar humana y traer trabajo."),
    "the-station": ("La Estación", "Cambio de rumbo", "Para quien va hacia su próximo puesto. Aquí la IA construye el argumento de adónde ir."),
}

T = {}

T["01"] = dict(
    slug="empresas-de-eventos", persona="El Dueño con Mucha <em>Operativa</em>", persona_plain="El Dueño con Mucha Operativa",
    sector="Eventos y producción en vivo", country="Italia",
    h1="IA para empresas de eventos y producción en vivo",
    title="IA para Empresas de Eventos: Presupuestos y Briefings en Automático",
    desc="Cómo una empresa de producción de eventos automatizó el 85–90% de sus presupuestos y briefings con IA. Un día en la vida, qué se construyó y cómo empezar.",
    roles=["Dueño", "Jefe de operaciones", "Coordinador de equipo"],
    answer="Una empresa de eventos puede usar la IA para convertir la transcripción de una visita técnica en tres documentos a la vez: un briefing de logística, uno técnico y el presupuesto para el cliente. La clave es una tarifa y unas reglas de descuento por escrito que la IA pueda leer, no un prompt más largo.",
    story=[
        "Diriges un negocio de servicios donde cada trabajo es un presupuesto nuevo, un briefing nuevo y mil piezas en movimiento: especificaciones técnicas para tu equipo y una versión cuidada para el cliente. Le pasaste esto a la IA y se rompía en cuanto el encargo no era simple: formato equivocado, partidas que faltaban, documentos que tu equipo no podía usar.",
        "<strong>El problema nunca fue la herramienta. Era tratar un negocio de 400 eventos al año como un solo prompt.</strong> Cuando el trabajo se dividió en los documentos correctos para cada persona, con una tarifa real y reglas de descuento por escrito, el resultado cambió por completo.",
    ],
    result="El trabajo de presupuestos y briefings funciona ahora automatizado en un 85–90%. El dueño solo interviene en la estrategia y en los casos realmente especiales.",
    day=[
        ("08:00", "Las notas de voz de la visita de ayer siguen en el móvil.", "La transcripción entra en el proyecto. Tres borradores te esperan antes del café."),
        ("10:00", "Reescribes el mismo trabajo dos veces: para el equipo y para el cliente.", "Los briefings de logística y técnico llegan al equipo en su propio formato."),
        ("13:00", "El precio depende de quién pregunta. Está en tu cabeza.", "Las reglas de descuento por tipo de cliente están escritas. La IA las aplica y pregunta si duda."),
        ("16:00", "El presupuesto sale tarde y con una partida olvidada.", "El presupuesto sigue tu plantilla y tu tarifa reales. Tú revisas, no escribes."),
        ("19:00", "Sigues con el correo.", "Estás en el evento, donde de verdad pasa el negocio."),
    ],
    signals=[
        "He probado la IA para presupuestos y se desmonta en cuanto algo es complejo",
        "Mi equipo necesita información distinta que mis clientes y reescribo todo dos veces",
        "No tengo tiempo de convertirme en ingeniero de prompts. Necesito que funcione",
        "Nada está escrito en ningún sitio que la IA pueda usar",
    ],
    outcomes=[
        "Un sistema de documentos separados: uno para operaciones internas y otro para el cliente",
        "Un briefing escrito para cada rol del equipo, para que la IA deje de adivinar",
        "Un porcentaje de automatización realista para tu negocio, no una promesa vaga",
        "Una lista priorizada de qué delegar primero y qué seguir haciendo tú",
    ],
    faq=[
        ("¿Puede la IA hacer presupuestos para una empresa de eventos?", "Sí, si tiene tu tarifa real, tus reglas de descuento y dos o tres presupuestos de ejemplo. Sin eso adivina, y las adivinanzas son lo que se rompe en los trabajos complejos."),
        ("¿Tengo que cambiar de software?", "No. En este caso se usó el Google Drive que ya tenía el dueño y un proyecto de Claude. Lo nuevo fue poner por escrito reglas que solo existían en su cabeza."),
        ("¿Cuánto tarda en ahorrar tiempo?", "La primera prueba con una transcripción real dio un briefing y un presupuesto utilizables en las primeras clases. Después, casi todo el trabajo es rellenar huecos que la IA deja a la vista, como una tarifa de artistas que faltaba."),
    ],
)

T["02"] = dict(
    slug="ingenieria-infraestructuras", persona="El Especialista en Sectores <em>Regulados</em>", persona_plain="El Especialista en Sectores Regulados",
    sector="Permisos y cumplimiento en infraestructuras", country="Proyectos internacionales",
    h1="IA para ingeniería y cumplimiento normativo en infraestructuras",
    title="IA para Ingeniería e Infraestructuras: Sistemas Verificables, no Chatbots",
    desc="Cómo un coordinador de permisos de trabajo en proyectos internacionales construyó subsistemas de IA verificables sin pérdida de datos entre sedes.",
    roles=["Cumplimiento", "Responsable técnico", "Auditor"],
    answer="En ingeniería regulada, la IA es útil cuando se construye como agentes pequeños y verificables, con entradas y reglas definidas, no como una única ventana de chat. Cada agente hace un trabajo y una persona puede comprobar cada traspaso.",
    story=[
        "Trabajas donde un error tiene consecuencias reales: documentación de seguridad, permisos, coordinación entre varias obras, todo bajo inspección. No quieres un chatbot. Quieres un sistema que puedas verificar.",
        "<strong>No se trata de escribir mejores prompts. Se trata de construir un sistema de varios pasos</strong>: agentes que hacen partes concretas del trabajo, con reglas que puedes comprobar y sin pérdidas silenciosas de datos entre pasos.",
    ],
    result="Subsistemas verificados sin pérdida de datos entre sedes, ahora escalando hacia un sistema de coordinación completo. El cliente ha ampliado el proyecto por iniciativa propia.",
    day=[
        ("07:30", "Llegan permisos de tres obras en tres formatos distintos.", "Un agente de entrada los normaliza en un único formato revisado."),
        ("09:00", "Cruzas documentos a mano contra la normativa.", "Un agente de reglas marca lo que falta. Revisas las alertas, no cada página."),
        ("12:00", "Dos obras, dos husos horarios, una hoja de cálculo que se desincroniza.", "Cada traspaso queda registrado. Nada cambia entre sedes sin dejar rastro."),
        ("15:00", "Un auditor pregunta por qué se aprobó un permiso.", "El rastro está ahí: entrada, regla aplicada, quién firmó."),
        ("18:00", "Te quedas hasta tarde para que nada se escape.", "Te vas a casa sabiendo qué hizo el sistema y por qué."),
    ],
    signals=[
        "Necesito algo más riguroso que un chat en el que no confío del todo",
        "La coordinación entre obras se come horas cada semana",
        "No quiero solo resultados. Quiero verificar que son correctos",
        "Casi todos los consejos de IA para empresas son demasiado genéricos para trabajo crítico",
    ],
    outcomes=[
        "Un mapa de qué pasos se pueden automatizar con seguridad y cuáles necesitan revisión humana",
        "Un primer sistema verificable que funciona de verdad, no una demo",
        "Un método para pasar de una pieza que funciona a un sistema coordinado",
        "Saber exactamente qué hace el sistema en cada paso",
    ],
    faq=[
        ("¿Es segura la IA para permisos de trabajo y documentos de cumplimiento?", "Puede serlo si cada agente tiene reglas acotadas y cada resultado lo revisa una persona antes de darlo por bueno. La IA redacta y señala; la persona cualificada aprueba."),
        ("¿Deben los equipos regulados usar IA en su propio servidor?", "A menudo sí, por control de los datos. Los agentes en tu propio servidor mantienen los documentos fuera de las apps de chat y te dan un registro completo de lo que se ejecutó."),
        ("¿Por dónde se empieza?", "Por un subsistema con una entrada y una comprobación claras, como normalizar permisos de distintas obras. Lo demuestras y luego conectas el siguiente."),
    ],
)

T["03"] = dict(
    slug="equipos-de-marketing", persona="El Responsable de Marketing <em>Interno</em>", persona_plain="El Responsable de Marketing Interno",
    sector="Marketing corporativo y producción creativa", country="Italia",
    h1="Producción de vídeo con IA para equipos de marketing internos",
    title="Vídeo con IA para Equipos de Marketing: un Flujo de Producción Real",
    desc="Cómo un responsable de marketing interno montó un flujo de vídeo con IA coherente para una campaña de empresa: fichas de personajes y localizaciones, plan de cámara y entrega real.",
    roles=["Director creativo", "Responsable de contenidos", "Gestor de campañas"],
    answer="El vídeo con IA parece profesional cuando fijas personajes y localizaciones antes de generar nada y sigues un plan de cámara por escrito. Las fichas de coherencia y el plan de planos importan más que la herramienta de vídeo que elijas.",
    story=[
        "Eres responsable de lo que publica tu empresa, y eso ya incluye vídeo. Probaste herramientas de vídeo con IA y chocaste enseguida con el problema: personajes y lugares cambian de un plano a otro y nada tiene nivel para llevar la marca.",
        "<strong>La solución no es una herramienta mejor. Es la disciplina de una producción real</strong>: fijar primero la coherencia de personajes y localizaciones y rodar con un plan de cámara en lugar de prompts sueltos.",
    ],
    result="Flujo de producción completo: sistema de coherencia, plan de cámara y una pieza real usada en una campaña de la empresa en un gran evento del sector.",
    day=[
        ("09:00", "El encargo dice «un vídeo corto para el evento». Sin equipo ni presupuesto.", "Escribes el guion con IA y lo divides en planos."),
        ("10:30", "En cada clip la persona es un poco distinta.", "Las fichas de personajes y localizaciones fijan cómo se ve todo."),
        ("13:00", "Pruebas cinco herramientas y obtienes cinco estilos.", "Un plan de planos por escrito entra en la herramienta que mejor encaja con cada plano."),
        ("16:00", "Montar los clips queda amateur.", "Movimientos de cámara y luz están planificados, así que el montaje se sostiene."),
        ("18:00", "Dudas si está a la altura para enseñárselo al CEO.", "Entra en la campaña real."),
    ],
    signals=[
        "Genero clips, pero unirlos en algo coherente es un caos",
        "Mis personajes y escenarios cambian en cada plano",
        "Necesito algo con nivel para una campaña real",
        "No vengo de producción. Necesito un sistema que pueda seguir",
    ],
    outcomes=[
        "Un sistema de coherencia reutilizable para personajes y localizaciones",
        "Un plan de cámara por escrito que puedes dar a cualquier herramienta de vídeo con IA",
        "Una comparativa de las herramientas actuales, para dejar de adivinar",
        "Una pieza real de campaña, no solo técnicas",
    ],
    faq=[
        ("¿Cómo se mantienen coherentes los personajes en un vídeo con IA?", "Haz primero una ficha de referencia del personaje: vista de giro, primeros planos, expresiones, paleta y una lista de «no cambiar». Usa sus paneles como imágenes de referencia en cada prompt de plano."),
        ("¿Qué herramienta de vídeo con IA es mejor para marketing?", "Cambia cada pocos meses. Elige por plano: unas manejan mejor a las personas y otras el movimiento de cámara. Lo que mantiene la coherencia entre herramientas es el plan de planos escrito."),
        ("¿Puede hacerlo alguien de marketing sin experiencia en cine?", "Sí. Este caso empezó sin experiencia en producción. El método toma los pasos de una producción real y los convierte en listas de comprobación."),
    ],
)

T["04"] = dict(
    slug="freelancers-multicliente", persona="El Freelance <em>Multicliente</em>", persona_plain="El Freelance Multicliente",
    sector="Servicios freelance", country="Suiza y otros",
    h1="IA para freelancers que trabajan con varios clientes",
    title="IA para Freelancers con Varios Clientes: Informes y Administración",
    desc="Cómo los freelancers con varios clientes usan la IA para dejar de rehacer a mano los mismos informes y la misma administración: informes en vivo, facturas y listas de clientes.",
    roles=["Consultor", "Freelance", "Asistente virtual"],
    answer="Un freelance con varios clientes saca más partido a la IA construyendo un único sistema reutilizable alrededor del trabajo que repite cada mes, como informes, facturas y listas de clientes, conectado a datos reales en lugar de copiar y pegar.",
    story=[
        "Atiendes a varios clientes a la vez y gran parte de tu semana se va en trabajo que no hace crecer a nadie: el mismo resumen rehecho a mano, facturas, listas de clientes. Sabes que la IA debería encargarse. No has tenido tiempo de montarlo bien.",
        "<strong>La clave no es una herramienta de IA genérica. Es un sistema construido alrededor de tu forma real de trabajar</strong>, conectado a datos reales y reutilizado con cada cliente en lugar de empezar de cero cada mes.",
    ],
    result="Un freelance pasó de un informe mensual hecho a mano a un sistema de informes interactivo con datos en vivo, y ganó un cliente nuevo en parte gracias a él. Otro, en Suiza, está convirtiendo una herramienta de facturación hecha por él para un negocio de fitness en agentes que colaboran.",
    day=[
        ("08:30", "Lunes: cinco clientes quieren cinco informes.", "Los informes se actualizan con datos en vivo. Tú añades el comentario que solo tú puedes escribir."),
        ("11:00", "Las facturas se hacen una a una con una plantilla.", "Facturas y listas de clientes salen de un solo sitio, hecho con IA y sin suscripción."),
        ("14:00", "Un posible cliente pregunta cómo son tus informes.", "Le enseñas el sistema en vivo. Vende por ti."),
        ("16:00", "La administración se come las horas facturables.", "Pequeños agentes hacen el trabajo repetitivo y se pasan el siguiente paso."),
        ("18:00", "Más clientes significaría más noches.", "Más clientes significa más filas en el mismo sistema."),
    ],
    signals=[
        "Rehago el mismo informe cada mes para clientes distintos",
        "Sé que la IA podría acelerarlo, pero no tengo una forma estructurada de montarlo",
        "Mis clientes esperan informes más rápidos y mejores de lo que puedo hacer a mano",
        "Quiero más clientes, no más horas",
    ],
    outcomes=[
        "Un sistema de informes reutilizable, construido sobre tu forma de trabajar",
        "Un camino para conectar datos reales de clientes en lugar de copiar y pegar",
        "Entregables que los clientes notan y que ayudan a ganar el siguiente",
        "Horas libres cada mes para trabajo facturable",
    ],
    faq=[
        ("¿Cómo pueden los freelancers automatizar los informes con IA?", "Elige el informe que más rehaces, conéctalo a su fuente de datos y deja que la IA genere la estructura y los gráficos. Guárdate las dos o tres frases de análisis real."),
        ("¿Puedo sustituir un software de pago por algo hecho con IA?", "A menudo sí, en herramientas sencillas como facturación o listas de clientes. Antes, revisa lo que pierdes: copias de seguridad, normas fiscales y soporte siguen importando."),
        ("¿Qué son los agentes que colaboran?", "Pequeños ayudantes de IA que hacen cada uno un trabajo, como reservas, facturas o recordatorios, y pasan el resultado al siguiente. Más fáciles de arreglar que un gran asistente único."),
    ],
)

T["05"] = dict(
    slug="profesionales-de-ventas", persona="El Comercial que Busca <em>Ventaja</em>", persona_plain="El Comercial que Busca Ventaja",
    sector="Ventas y desarrollo de negocio", country="Europa",
    h1="IA para profesionales de ventas y desarrollo de negocio",
    title="IA para Comerciales: Prospección e Investigación sin Sonar a Robot",
    desc="Un flujo de IA para account executives, SDRs y consultores: prospección más inteligente, mensajes personalizados e investigación previa a la llamada en minutos.",
    roles=["Account executive", "SDR", "Consultor"],
    answer="Los comerciales sacan más partido a la IA en la investigación y la preparación: estudiar cuentas, preparar llamadas y primeros borradores de mensajes. Lo humano sigue siendo la relación y el criterio sobre qué decir.",
    story=[
        "Eres bueno en lo tuyo. Pero los mejores de tu entorno usan la IA para prospectar mejor, personalizar más rápido e investigar más a fondo, y la distancia crece cada trimestre.",
        "<strong>Tienes el instinto y las relaciones. Te faltan las herramientas adecuadas encima.</strong> No prompts genéricos: un flujo construido sobre cómo vendes tú.",
    ],
    result="Objetivo fijado en el trabajo conjunto: reducir la investigación previa a cada llamada de 45 minutos a 5.",
    day=[
        ("08:00", "Repasas LinkedIn buscando a quién llamar.", "Tienes una lista corta de cuentas con un motivo para llamar hoy."),
        ("09:30", "Cada correo empieza en blanco.", "Los primeros borradores usan detalles reales de la cuenta. Tú los haces tuyos."),
        ("12:00", "45 minutos de preparación antes de una llamada.", "Cinco minutos con una ficha de una página: empresa, persona, objeciones probables."),
        ("15:00", "Las notas se quedan en tu cabeza después de la llamada.", "El resumen y los próximos pasos se escriben solos en tu CRM."),
        ("17:30", "Te preguntas cómo lo hace el mejor del equipo.", "Ahora lo sabes."),
    ],
    signals=[
        "Quiero usar IA para prospectar sin sonar a robot",
        "Necesito que clientes y dirección me vean con soltura en IA",
        "Los mejores cierran más. Quiero saber exactamente cómo",
        "La investigación y la preparación me llevan demasiado",
    ],
    outcomes=[
        "Un flujo de prospección con IA adaptado a tu forma de vender",
        "Marcos de prompts para mensajes que no parecen generados",
        "Un sistema de investigación previa: 5 minutos en lugar de 45",
        "Una forma de presentar tu dominio de la IA ante los clientes",
    ],
    faq=[
        ("¿Cómo usan la IA los comerciales sin sonar robóticos?", "Usa la IA para investigar y estructurar, y escribe tú la primera frase y la petición. Los detalles concretos de la persona ganan a cualquier plantilla."),
        ("¿Cuál es la victoria más rápida de la IA en ventas?", "La investigación previa a la llamada. Una ficha de una página sobre la empresa y la persona, hecha con fuentes públicas, es lo que más tiempo ahorra la primera semana."),
        ("¿Necesito una herramienta de IA específica para ventas?", "No para empezar. Un asistente general con tu perfil de cliente ideal y ejemplos de tus mejores correos cubre la mayor parte."),
    ],
)

T["06"] = dict(
    slug="cambio-de-carrera", persona="La que Cambia de <em>Carrera</em>", persona_plain="La que Cambia de Carrera",
    sector="Transición entre sectores", country="España",
    h1="Coaching de carrera con IA para quien cambia de sector",
    title="Coaching de Carrera con IA: Convierte un Perfil Variado en un Argumento",
    desc="Cómo una persona que cambia de carrera usa la IA para una búsqueda de empleo basada en datos: salarios, empresas objetivo y posicionamiento en tres categorías de puesto.",
    roles=["Cambio de carrera", "Varios sectores", "Reposicionamiento"],
    answer="Quien cambia de carrera puede usar la IA para investigar cuánto pagan y qué piden los puestos objetivo, preparar una lista de empresas y reescribir un perfil variado como una sola historia clara. El valor está en los datos, no en un CV más bonito.",
    story=[
        "Has hecho trabajo de verdad en más de un mundo, y esa variedad es un activo. Nadie te ha enseñado a contarlo, así que se lee como dispersión en lugar de intención.",
        "<strong>No es un retoque del CV. Es construir un argumento con datos</strong>: qué pagan y qué piden esos puestos, y un posicionamiento que convierte tu trayectoria en tu ventaja.",
    ],
    result="Un argumento con datos en tres categorías de puesto, con salarios reales de referencia, listas de empresas objetivo, una web personal y un posicionamiento para cada una.",
    day=[
        ("09:00", "Te presentas a todo lo que se parece.", "Te presentas dentro de tres categorías claras con rangos salariales reales."),
        ("11:00", "Tu CV intenta decirlo todo.", "Una versión distinta por categoría cuenta una sola historia clara."),
        ("14:00", "Te llaman para una entrevista: tienes una tarde para prepararla.", "La investigación con IA sobre la empresa y el entrevistador está lista en una hora."),
        ("17:00", "Te preguntas si tu pasado tiene sentido para alguien.", "Una web personal lo muestra como un camino, no como un zigzag."),
        ("20:00", "Otra tarde mirando portales de empleo.", "Un plan de 30 días dice qué hacer mañana."),
    ],
    signals=[
        "Mi perfil no cabe en una casilla y no sé explicarlo como una fortaleza",
        "No quiero un CV más bonito. Quiero una estrategia de adónde ir",
        "No sé cuánto pagan ni qué piden de verdad estos puestos",
        "Todos dicen «usa la IA» en la búsqueda de empleo y nadie dice cómo",
    ],
    outcomes=[
        "Un relato que convierte un perfil variado en una historia clara",
        "Rangos salariales y requisitos de tus categorías objetivo",
        "Una lista de empresas que vale la pena atacar, con vías de contacto",
        "Un plan concreto para los próximos 30 días",
    ],
    faq=[
        ("¿Cómo me ayuda la IA a cambiar de carrera?", "Para investigar puestos y salarios, conectar tu experiencia con lo que piden esos puestos y preparar entrevistas. Acelera la investigación; la dirección la eliges tú."),
        ("¿Debo hacer un CV distinto para cada puesto?", "Sí, uno por categoría. Con la IA es rápido cuando toda tu trayectoria está en un proyecto del que puede tirar."),
        ("¿Es para quien busca su primer empleo?", "No. Funciona mejor para personas con experiencia real en más de un campo que necesitan explicar el hilo que lo une."),
    ],
)

T["07"] = dict(
    slug="electricistas-y-oficios", persona="El Dueño de una Empresa de <em>Oficios</em>", persona_plain="El Dueño de una Empresa de Oficios",
    sector="Instalaciones eléctricas", country="Australia",
    h1="IA para electricistas y empresas de oficios",
    title="IA para Electricistas y Empresas de Oficios: un Panel que Encuentra Dinero Perdido",
    desc="Cómo una empresa de instalaciones eléctricas en Australia conectó la IA a su gestión de trabajos y a su contabilidad para detectar trabajos sin cobrar y leads sin atender.",
    roles=["Dueño", "Director general", "Oficina"],
    answer="Una empresa de oficios puede conectar la IA a su software de gestión de trabajos y de contabilidad para detectar trabajos terminados sin cobrar, leads que nadie siguió y trabajos sin notas. El valor está en encontrar fugas, no en contar trabajos.",
    story=[
        "Tienes un equipo de técnicos en la calle y un equipo de oficina. Los leads llegan por correo, formulario web y WhatsApp; los trabajos viven en tu software y el dinero en tu contabilidad. Solo te enteras de que algo se escapó cuando un cliente se queja o falta caja.",
        "<strong>Un trabajo puede valer más que diez. Así que la pregunta no es cuántos trabajos hiciste.</strong> Es qué dinero está atascado, qué lead no llamó nadie y quién del equipo necesita ayuda.",
    ],
    result="En su primera prueba, el espacio de trabajo con IA detectó un pago vencido que el dueño no conocía; la siguiente encontró un lead que nadie había trabajado. Un informe semanal de trabajos de inmobiliarias pasó de unos cinco minutos a uno.",
    day=[
        ("06:30", "Los técnicos salen. No sabes si cada trabajo tiene notas.", "El repaso de la mañana marca los trabajos sin notas antes de que salgan las furgonetas."),
        ("09:00", "Las órdenes de trabajo llegan como correos y PDF.", "Cada una se convierte en un trabajo con el tipo de cliente asignado, para que los informes cuadren."),
        ("12:00", "Alguien dice que un cliente no ha pagado. ¿Cuál?", "Los trabajos terminados y sin cobrar están arriba del todo en el panel."),
        ("15:00", "Un lead de la semana pasada se enfrió.", "Los leads sin trabajar se marcan el mismo día."),
        ("21:00", "Vuelves a mirar el negocio desde el móvil.", "Un panel, en tu móvil, pensado para el dueño y el director."),
    ],
    signals=[
        "Solo me entero de los problemas cuando un cliente se queja",
        "Mi software lo tiene todo, pero no veo la foto completa",
        "No me importa cuántos trabajos hicimos. Me importa cuáles dieron dinero",
        "Llevo casi todo el negocio desde el móvil",
    ],
    outcomes=[
        "IA conectada a tu software de trabajos y de contabilidad",
        "Informes semanales guardados por tipo de cliente, en un minuto en lugar de cinco",
        "Un reglamento de categorías para que tus datos dejen de mentir",
        "Un panel visual para dueño y director, pensado para el móvil",
    ],
    faq=[
        ("¿Se puede conectar la IA a ServiceM8 y Xero?", "Sí. En este caso ambos se conectaron a Claude con conectores oficiales, así que los informes leen datos de trabajos y contabilidad en vivo en lugar de exportaciones."),
        ("¿Qué debería vigilar con IA una empresa de oficios?", "El dinero atascado entre «trabajo hecho» y «cobrado», los leads sin seguimiento, los trabajos sin notas y los trabajos sin tipo de cliente. El número de trabajos importa menos."),
        ("¿Necesito un programador?", "No para empezar. Los conectores y un proyecto bien escrito cubren los primeros meses. La automatización y las API llegan después, cuando sabes qué informes usas de verdad."),
    ],
)

T["08"] = dict(
    slug="empresas-de-construccion", persona="El Director de Operaciones de <em>Obra</em>", persona_plain="El Director de Operaciones de Obra",
    sector="Fachadas y revestimientos", country="Reino Unido",
    h1="IA para operaciones de construcción e informes de seguridad y salud",
    title="IA para Empresas de Construcción: Informes al Consejo, Incidentes y Visitas de Obra",
    desc="Cómo el director de operaciones de una empresa de fachadas del Reino Unido usa la IA para informes al consejo, incidentes sin daños, seguridad y salud, y actas de visita de obra.",
    roles=["Director de operaciones", "Responsable de seguridad", "Jefe de obra"],
    answer="Los equipos de construcción pueden usar la IA para convertir notas de voz de obra y registros de seguridad en informes, listas de acciones y resúmenes para el consejo. Funciona cuando la IA tiene las reglas y plantillas de tu empresa, configuradas una vez en un espacio compartido.",
    story=[
        "Un grupo más grande entró en el capital de tu empresa, y con él llegaron los informes corporativos: el dossier mensual del consejo, el registro de incidentes, las charlas de seguridad, los informes de obra. Intentaste arreglar un solo formulario de incidente con IA y perdiste once horas y doscientos prompts.",
        "<strong>El problema no era el esfuerzo. Era empezar cada chat de cero.</strong> Un espacio de trabajo que ya conoce tu empresa, tus plantillas y tus normas de seguridad convierte cada informe en una revisión corta en lugar de una pelea.",
    ],
    result="Hay un espacio de IA de empresa configurado con instrucciones y material de charlas de seguridad; ya funcionan el informe al consejo y los resúmenes de hilos de correo. Siguiente paso: el libro mensual de seguridad y salud convertido en un resumen listo para el consejo.",
    day=[
        ("07:00", "Tres obras, tres listas de problemas, un solo tú.", "Las notas de voz de la visita se convierten en un informe escrito y una lista de acciones en Excel."),
        ("10:00", "Hay que registrar bien un incidente sin daños.", "El formulario se rellena con tus notas, en el formato de la empresa."),
        ("13:00", "Un hilo de 40 correos que necesitas entender.", "Un resumen de una página: quién decidió qué y qué queda abierto."),
        ("16:00", "Toca el informe al consejo. Los números están repartidos en varios libros.", "El libro mensual de seguridad se convierte en el borrador del resumen."),
        ("19:00", "Escribes informes en la mesa de la cocina.", "Revisas y envías. Hecho antes de cenar."),
    ],
    signals=[
        "Llegaron los informes corporativos y nadie me dio más horas",
        "He pasado días enteros peleándome con la IA por un solo formulario",
        "No soy técnico. Lo necesito paso a paso",
        "Mis notas de obra nunca se convierten a tiempo en informes de verdad",
    ],
    outcomes=[
        "Un espacio de IA de empresa que conoce tus reglas, plantillas y términos",
        "De nota de voz a informe de obra más resumen de acciones en Excel",
        "Registros de incidentes y charlas de seguridad en tu formato",
        "Un informe mensual al consejo que editas en lugar de escribir",
    ],
    faq=[
        ("¿Puede la IA redactar informes de seguridad y salud en obra?", "Puede redactarlos a partir de tus notas, en el formato de tu empresa. Una persona competente sigue revisando y firmando. El ahorro está en escribir y dar formato."),
        ("¿Por qué falló la IA cuando la probé antes?", "Normalmente porque cada chat empezaba de cero. Un proyecto con tus plantillas, normas y ejemplos guardados le da a la IA el contexto que necesitaría un compañero nuevo."),
        ("¿Tengo que manejarme bien con el ordenador?", "No. Este trabajo va clic a clic. El objetivo es que lo uses tú solo, no que alguien lo haga por ti."),
    ],
)

T["09"] = dict(
    slug="asistente-ia-para-ceo", persona="El <em>CEO</em>", persona_plain="El CEO",
    sector="Dirección general", country="África",
    h1="Un asistente de IA para CEOs",
    title="Asistente de IA para CEOs: Informes de Ventas, Presentaciones y un Briefing Diario",
    desc="Cómo el CEO de una empresa de 60 personas en África usa la IA como jefe de gabinete: esquemas de diapositivas desde bocetos a mano, informes de ventas y vigilancia de competidores.",
    roles=["CEO", "Director general", "Fundador"],
    answer="Un CEO saca más partido a la IA como jefe de gabinete personal: un espacio de trabajo que conoce la empresa, convierte bocetos en esquemas de diapositivas, resume las ventas y vigila a la competencia. El CEO sigue tomando todas las decisiones.",
    story=[
        "Diriges una empresa de unas sesenta personas con un equipo comercial que se mueve cada día. Las presentaciones se comen tus noches. Los números de ventas que recibes dicen qué pasó, no quién rinde ni qué productos se mueven.",
        "<strong>No necesitas aprender a programar. Necesitas la IA en el centro de cómo diriges.</strong> Dos asistentes, configurados una vez, llevan el contexto de la empresa para que cada petición empiece desde lo que ya sabes.",
    ],
    result="En la primera clase el CEO creó dos asistentes: un Asistente de Presentaciones que convierte bocetos de diapositivas hechos a mano en esquemas, y un Asistente de CEO con el dossier de la empresa, el informe de ventas y el folleto. Siguiente: un informe diario de ventas por comercial y una vigilancia regional de la competencia.",
    day=[
        ("07:00", "Las ventas de ayer: un total, no una historia.", "Un briefing: quién vendió, qué se vendió, qué preguntar al equipo."),
        ("09:00", "Presentación al consejo esta noche. Diapositivas en blanco.", "Dibujas las diapositivas en papel. El asistente convierte la foto en un esquema."),
        ("12:00", "Un competidor lanzó algo. Te enteraste tarde.", "Una vigilancia semanal de tu región y tu sector."),
        ("15:00", "Un socio quiere la historia de la empresa en una página.", "El asistente ya conoce el dossier y el folleto. Un borrador y tus cambios."),
        ("20:00", "Otra vez diapositivas.", "Tiempo con tu familia."),
    ],
    signals=[
        "Las presentaciones se comen mis noches",
        "Mis informes dicen qué pasó, no por qué",
        "Quiero la IA en el centro de mi trabajo sin volverme técnico",
        "Me entero tarde de lo que hace la competencia",
    ],
    outcomes=[
        "Un asistente de CEO que conoce tu empresa",
        "Diapositivas a partir de tus propios bocetos, con tu estructura",
        "Un informe de ventas diario más rico: por persona y por producto",
        "Una vigilancia periódica de competencia y sector",
    ],
    faq=[
        ("¿Cómo puede un CEO usar la IA cada día?", "Empieza por las tareas que se comen tus noches, normalmente presentaciones e informes. Pon el dossier de la empresa y los informes recientes en un proyecto de IA para que cada petición tenga contexto."),
        ("¿Puede la IA convertir bocetos a mano en diapositivas?", "Sí. Haces una foto del boceto y un asistente con tus instrucciones lo convierte en un esquema diapositiva a diapositiva con tu estructura, listo para diseñar."),
        ("¿Están seguros los datos de mi empresa en un asistente de IA?", "Usa un plan de empresa que no entrene con tus datos y limita los archivos sensibles a lo que necesita cada asistente. Lo configuramos en la primera clase."),
    ],
)

T["10"] = dict(
    slug="agentes-inmobiliarios", persona="El Agente <em>Inmobiliario</em>", persona_plain="El Agente Inmobiliario",
    sector="Inmobiliaria residencial", country="Emiratos Árabes Unidos",
    h1="IA para agentes inmobiliarios",
    title="IA para Agentes Inmobiliarios: Ordena tus Datos y Luego Activa tus Contactos",
    desc="Cómo un agente inmobiliario en los Emiratos arregló la sincronización de leads e inmuebles entre hojas de cálculo e IA y convirtió 5.000 contactos en un plan de marketing.",
    roles=["Agente", "Jefe de equipo", "Gestor de inmuebles"],
    answer="Los agentes inmobiliarios sacan más partido a la IA cuando sus leads e inmuebles están limpios. Con un CRM ligero en hojas de cálculo conectado a un espacio de IA, el siguiente paso es el marketing a los contactos existentes: manual de marca, landing page y campañas de mensajes.",
    story=[
        "Tu pequeño equipo funciona con hojas de cálculo y un espacio de IA en lugar de un CRM. Los leads, los inmuebles y los paneles para dirección dejaron de cuadrar, y nadie se fiaba de los números.",
        "<strong>Hacer marketing a 5.000 contactos no funciona con datos rotos.</strong> Así que lo primero fue arreglar la sincronización. Lo segundo, convertir esos contactos en una campaña que la gente quiera leer.",
    ],
    result="Tras la primera sesión, la sincronización entre leads, inmuebles y paneles quedó prácticamente resuelta. El foco pasó al marketing a unos 5.000 contactos existentes: manual de marca, landing page y un canal social.",
    day=[
        ("09:00", "La hoja de leads y la de inmuebles no coinciden.", "Una única fuente de verdad, sincronizada con el espacio de IA."),
        ("11:00", "El resumen semanal para dirección lleva horas.", "Se construye desde las hojas, con números fiables."),
        ("13:00", "5.000 contactos y ningún plan.", "Contactos ordenados en compradores, vendedores e inquilinos, cada uno con su mensaje."),
        ("16:00", "Los mensajes no llevan a ninguna parte.", "Una landing sencilla recoge cada respuesta."),
        ("18:00", "Publicas cuando te acuerdas.", "Un canal social con un plan."),
    ],
    signals=[
        "Nuestras hojas y paneles no cuadran",
        "Tenemos miles de contactos y no hacemos nada con ellos",
        "No quiero pagar otra herramienta",
        "Dirección quiere números de los que no me fío",
    ],
    outcomes=[
        "Sincronización limpia entre leads, inmuebles e informes",
        "Contactos segmentados con un mensaje por segmento",
        "Un manual de marca y una landing para campañas",
        "Un reparto claro de qué va a IT, a marketing y a ti",
    ],
    faq=[
        ("¿Puede un agente inmobiliario usar la IA sin CRM?", "Sí, en un equipo pequeño. Google Sheets más un espacio de IA puede funcionar como CRM ligero, siempre que leads e inmuebles estén sincronizados."),
        ("¿Cómo hacer marketing a contactos antiguos?", "Segmenta en compradores, vendedores e inquilinos, escribe un mensaje útil por segmento y lleva a la gente a una página sencilla que recoja respuestas."),
        ("¿Cuál es el primer arreglo de IA en una agencia?", "Los datos. Si leads, inmuebles e informes no coinciden, cada resumen de la IA hereda el error."),
    ],
)

T["11"] = dict(
    slug="clinicas-dentales", persona="El Dueño de la <em>Clínica</em>", persona_plain="El Dueño de la Clínica",
    sector="Clínica dental", country="Estados Unidos",
    h1="IA para dueños de clínicas dentales",
    title="IA para Clínicas Dentales: Automatización Segura de Seguros, Protocolos y Reuniones",
    desc="Cómo el dueño de una clínica dental en EE. UU. planifica la IA para pagos de seguros, ajustes de cuenta, protocolos y reuniones, empezando con pacientes ficticios y la privacidad en mente.",
    roles=["Dueño de la clínica", "Gerente", "Responsable de equipo"],
    answer="Las clínicas dentales pueden usar ya la IA para resúmenes de reuniones, protocolos y manuales de formación. Escribir en el software de gestión, para pagos de seguros o ajustes, necesita antes una configuración segura: un acuerdo que cubra los datos de pacientes y pruebas con pacientes ficticios.",
    story=[
        "Tienes una clínica de doce personas que ya funciona con un sistema de gestión claro: reuniones semanales, cuadros de mando, objetivos. Usas la IA en el chat. Quieres que entre en el software de la clínica para registrar pagos de seguros y ajustes, sin arriesgar los datos de pacientes ni el propio sistema.",
        "<strong>La regla es simple: nada toca a pacientes reales hasta que funciona con pacientes ficticios.</strong> Por eso el primer proyecto es una prueba de concepto con datos inventados, y el acuerdo sobre datos de pacientes llega antes de poner nada en marcha.",
    ],
    result="Primer proyecto acordado: un panel de prueba con pacientes ficticios para probar con seguridad la API del software de la clínica, mientras la clínica cierra un acuerdo de datos de pacientes para sus herramientas de IA.",
    day=[
        ("07:30", "Reunión semanal del equipo: notas en una grabación que nadie escucha.", "Orden del día y resumen desde la transcripción, en tu formato de reunión."),
        ("10:00", "Pagos de seguros tecleados a mano.", "Previsto: la IA prepara las entradas y una persona las aprueba, con una conexión segura."),
        ("13:00", "Una nueva incorporación necesita los protocolos.", "Protocolos y manuales de formación redactados a partir de cómo trabajáis de verdad."),
        ("15:00", "Las cuentas vencidas en un informe que casi nunca abres.", "Previsto: un resumen semanal de vencidos y estado de reclamaciones."),
        ("18:00", "Te preguntas si la IA es segura para una clínica.", "Sabes qué toca datos de pacientes y qué no."),
    ],
    signals=[
        "Quiero IA en nuestro software, pero no a costa de los datos de pacientes",
        "Nuestras reuniones y protocolos viven en grabaciones y en cabezas",
        "Los seguros se comen horas de recepción",
        "Mi equipo todavía no usa IA",
    ],
    outcomes=[
        "Una línea clara entre lo que la IA puede hacer ya y lo que necesita un acuerdo de datos",
        "Una prueba de concepto con pacientes ficticios antes de tocar datos reales",
        "Órdenes del día, resúmenes, protocolos y manuales de formación",
        "Un plan para que el equipo se sume",
    ],
    faq=[
        ("¿Cumple la IA con HIPAA en una clínica dental?", "Depende del plan y del acuerdo, no del modelo. Usa un plan de empresa con un acuerdo firmado para datos de pacientes y mantén esos datos fuera de herramientas de consumo."),
        ("¿Puede la IA registrar pagos de seguros en el software de la clínica?", "Técnicamente sí, a través de la API del software. Hazlo solo tras probar con pacientes ficticios y con una persona aprobando cada escritura."),
        ("¿Para qué puede usar una clínica la IA hoy, con seguridad?", "Órdenes del día y resúmenes de reuniones, protocolos, descripciones de puesto y manuales de formación: todo lo que no lleva datos de pacientes."),
    ],
)

T["12"] = dict(
    slug="software-hosteleria", persona="La Hostelera que Construye un <em>SaaS</em>", persona_plain="La Hostelera que Construye un SaaS",
    sector="Software de gestión para hostelería", country="España",
    h1="IA para hosteleros que construyen su propio software",
    title="IA para Hostelería: Construye y Ten en Propiedad tu Software de Gestión de Bares",
    desc="Cómo una profesional de la hostelería en España está sacando su app de gestión de bares de una plataforma no-code cara y convirtiéndola en un SaaS para otros bares.",
    roles=["Operadora", "Consultora", "Fundadora"],
    answer="Los hosteleros pueden construir su propio software de gestión con IA, pero las plataformas no-code se encarecen al crecer el uso. El camino habitual es reconstruir un módulo cada vez en un stack propio y después empaquetarlo para otros locales.",
    story=[
        "Llevas las operaciones y la contabilidad de varios bares y construiste una app para gestionarlos: finanzas, presupuestos, personal, temas legales, pedidos a proveedores. Funciona y la gente la usa a diario. Pero la plataforma no-code donde vive cuesta más cada mes y la lógica se ha ido enredando.",
        "<strong>El objetivo no es solo un alojamiento más barato. Es ser dueña del producto</strong>, para que pueda convertirse en un software por el que otros bares paguen, junto con la experiencia que hay detrás.",
    ],
    result="Una primera app ya funciona con su propio alojamiento y base de datos, fuera de la plataforma no-code. El plan: reducir a la mitad el coste mensual, reconstruir los módulos uno a uno y empaquetar un plan de entrada para otros bares.",
    day=[
        ("08:00", "La caja de anoche, en tres sistemas.", "Ventas y costes llegan a un informe semanal por bar."),
        ("11:00", "Cada encargado pide sus propios números.", "Cada encargado ve solo su bar. Tú lo ves todo."),
        ("14:00", "Llega la factura del no-code.", "Los módulos pasan a tu stack, uno a uno."),
        ("17:00", "Otro dueño de bar pregunta qué usáis.", "Hay una versión que puedes venderle."),
        ("23:00", "Servicio. El móvil vibra con preguntas.", "La app responde las de rutina."),
    ],
    signals=[
        "Mi app no-code funciona, pero la factura no para de crecer",
        "La reconstruiría si supiera por dónde empezar",
        "Otros locales quieren lo que tenemos",
        "Los datos económicos de los clientes deben seguir siendo privados",
    ],
    outcomes=[
        "Un plan de migración módulo a módulo, no una reconstrucción arriesgada de golpe",
        "Tu propio alojamiento y base de datos",
        "Un plan de producto que otros locales pueden comprar",
        "Reglas de privacidad para los datos económicos de los clientes",
    ],
    faq=[
        ("¿Puedo construir un software de gestión de bares con IA?", "Sí. Una app que funcione para finanzas, personal y pedidos es realista. Piensa pronto en la propiedad: alojamiento, base de datos y permisos de acceso."),
        ("¿Debo dejar mi plataforma no-code?", "Cuando el coste mensual y la lógica enredada pesan más que la velocidad. Mueve un módulo cada vez para que los bares no dejen de funcionar."),
        ("¿Cómo convierto una herramienta interna en un SaaS?", "Empieza por el módulo que más preguntan otros locales, pon precio a un plan de entrada y deja tu consultoría como capa premium."),
    ],
)

T["13"] = dict(
    slug="contables", persona="La <em>Contable</em>", persona_plain="La Contable",
    sector="Contabilidad y auditoría", country="Europa",
    h1="IA para contables que construyen sus propias herramientas de auditoría",
    title="IA para Contables: de Copiar y Pegar Prompts a tu Propio Software de Auditoría",
    desc="Cómo una contable europea está pasando de pegar prompts entre herramientas de IA a construir un MVP estructurado de su propio software de auditoría legal.",
    roles=["Contable", "Auditora", "Socia de despacho"],
    answer="Los contables pueden usar la IA para construir sus propias herramientas, como listas de comprobación de auditoría y detección de anomalías, sin ser programadores. El paso que importa es pasar de copiar prompts entre chats a un proyecto estructurado con un MVP claro.",
    story=[
        "Quieres dedicar menos tiempo a la rutina y más a clientes nuevos. Ya construiste una herramienta de escritorio que funciona para auditorías legales escribiendo prompts en una IA y pegándolos en otra.",
        "<strong>Funciona, pero no escala.</strong> El siguiente paso es estructura: un único sitio para la lógica, un MVP definido y una IA que señala anomalías mientras tú firmas la auditoría.",
    ],
    result="Las primeras clases definen el objetivo del software y la estructura del MVP, para que la herramienta crezca con intención y no a base de copiar y pegar.",
    day=[
        ("09:00", "Libros que revisar, línea a línea.", "La herramienta marca anomalías. Tú revisas las alertas."),
        ("11:00", "Un prompt escrito en una IA y pegado en otra.", "Un proyecto reúne la lógica, las versiones y las pruebas."),
        ("14:00", "Un cliente hace la misma pregunta rutinaria por tercera vez.", "Una respuesta redactada y revisada por ti."),
        ("16:00", "No hay tiempo para clientes nuevos.", "La rutina se reduce. Crecen las horas para clientes nuevos."),
        ("18:00", "Tu software vive en un solo ordenador.", "Un MVP que puedes enseñar y mejorar."),
    ],
    signals=[
        "He construido algo con IA, pero se sostiene a base de copiar y pegar",
        "Quiero pasar de usar la IA como un compañero más a construir con código",
        "La rutina no me deja tiempo para clientes nuevos",
        "Firma la profesional, no la IA",
    ],
    outcomes=[
        "Un MVP claro para tu software",
        "Un proyecto estructurado en lugar de prompts pegados",
        "Una IA que señala y tú que apruebas",
        "Un camino de herramienta de escritorio a producto",
    ],
    faq=[
        ("¿Pueden los contables crear software con IA sin programar?", "Sí, hasta una herramienta que funcione. Importa más la estructura que el código: un objetivo definido, un MVP y un proyecto donde viva la lógica."),
        ("¿Puede la IA hacer una auditoría?", "No. Puede señalar anomalías y preparar papeles de trabajo. La contable revisa y firma."),
        ("¿Qué es un MVP para una herramienta de auditoría?", "La versión más pequeña que hace una comprobación de principio a fin con archivos reales, como cuadrar el mayor con los extractos bancarios."),
    ],
)
