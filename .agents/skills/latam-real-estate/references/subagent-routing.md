# Enrutamiento de especialistas

Activar solo los perfiles necesarios:

| Perfil | Usar para | Revisión independiente |
|---|---|---|
| Producto | Problema, usuarios, alcance, MVP y roadmap | Dirección / Juan |
| Viabilidad y finanzas | Mercado, costes, ingresos y precios | Dirección / Juan |
| Investigación por país | Competencia, cultura, terminología y contexto local | Producto / legal |
| Arquitectura | SaaS, APIs, persistencia y escalabilidad | Seguridad / QA |
| Datos inmobiliarios | Property, Listing, Lead, Demand, matching y duplicados | Arquitectura / seguridad |
| Legal y privacidad | Normativa, contratos, consentimiento y transferencias | Juan |
| Marketing y crecimiento | Landings, posicionamiento, SEO y métricas | Producto |
| Diseño gráfico y publicidad | Sistema visual, piezas online/offline, campañas, plantillas y personalización para agentes | Marca / Producto / Seguridad y calidad |
| Operaciones de broker y oficina | Brokers, oficinas, equipos, agentes, rendimiento, operaciones y productividad | Producto / Arquitectura / Datos / Legal y privacidad / Seguridad y calidad |
| Formación, políticas y soporte | Centro de recursos, onboarding, checklists, políticas y atención de incidencias | Producto / Legal y privacidad / Seguridad y calidad |
| Integraciones y ecosistema | Catálogo de herramientas, proveedores, permisos, datos y dependencias | Arquitectura / Seguridad y calidad / Legal y privacidad / Juan |
| Red Profesional y colaboración | Feed de oportunidades, propiedades, demandas, referidos, perfiles y actividad verificable | Producto / Operaciones / Datos / Legal y privacidad / Seguridad y calidad |
| Planificación empresarial y análisis comercial | Planes de negocio, KPI, embudo, previsiones, monedas, costes/beneficios y acciones para agentes, equipos y agencias | Producto / Arquitectura / Datos / Operaciones / Investigación por país / Seguridad y calidad |
| Academia y liderazgo de oficina | Rutas para CEO de oficina, brokers y líderes de equipo; formación accionable, cultura, reclutamiento, desarrollo, servicio, retención y productividad | Producto / Planificación empresarial / Operaciones / Formación / Investigación por país / Legal y privacidad / Seguridad y calidad |
| Captación y exclusivas | Curso, guiones, role-play, primera/segunda visita, cualificación, ACM, plan de marketing, objeciones y seguimiento | Academia / Datos inmobiliarios / Planificación empresarial / Marketing / Investigación por país / Legal y privacidad / Seguridad y calidad |
| Onboarding y asistente de acompañamiento | Ruta de incorporación, checklist, evidencias, mentoría, progreso, recordatorios, bloqueos y escalado | Academia / Producto / Planificación empresarial / Operaciones / Arquitectura / Seguridad y calidad |
| Onboarding asistido | Estados, evidencias, tareas, notificaciones, soporte contextual y escalado por rol | Academia / Producto / Operaciones / Arquitectura / Datos / Planificación empresarial / Seguridad y calidad |
| Seguridad y calidad | Amenazas, pruebas, dependencias, release y rollback | Juan / revisión independiente |

## Handoff específico para `mk.inmobia360.com`

La skill directora debe coordinar, según la fase, los siguientes handoffs:

| Necesidad | Subagente responsable | Resultado esperado |
|---|---|---|
| Puntos de dolor, alcance y prioridad | Producto | Flujo priorizado para agentes de Lima y criterios de éxito |
| Campañas, plantillas y formatos | Diseño gráfico y publicidad | Sistema original de piezas online/offline y reglas de personalización |
| Sesión compartida, perfil y exportación | Arquitectura | Contratos, permisos, integración y estrategia de formatos |
| Perfil, propiedades, leads y actividades | Datos inmobiliarios | Entidades, referencias y trazabilidad sin duplicar datos |
| Uso de foto, logo y contactos | Legal y privacidad | Consentimiento, visibilidad, retención y límites por dato |
| Adaptación por canal y medición | Marketing y crecimiento | Presets, eventos analíticos y recomendaciones de conversión |
| QA visual, accesibilidad y releases | Seguridad y calidad | Pruebas, controles, rollback y validación independiente |

Los perfiles anteriores que figuran como planificados no se considerarán creados hasta disponer de sus definiciones y validación correspondientes. Ningún handoff autoriza por sí mismo desarrollo, publicación, cambios DNS o despliegue.

## Contexto compartido de rendimiento y productividad

El equipo debe considerar como referencia funcional el patrón de Performance Office: dashboard, rendimiento individual y de oficina, periodos mensual/anual/parcial/acumulado, captaciones, volumen de negocio, equipo, evolución del agente, operaciones, cierres, presupuestos, formación, soporte y gestión del ciclo del agente.

La traducción a Inmobia360 debe resolver puntos de dolor y aumentar productividad. Cada subagente deberá identificar qué decisión o acción habilita cada métrica y evitar paneles decorativos.

| Subagente | Contexto que debe incorporar |
|---|---|
| Producto | Priorizar siguiente acción, tareas pendientes, leads, campañas, propiedades, actividades y evolución del agente; separar MVP Lima de funciones posteriores. |
| Diseño gráfico y publicidad | Relacionar campañas y exportaciones con objetivos, actividades, leads y resultados; reducir tiempo de preparación. |
| Arquitectura | Diseñar permisos y agregaciones por agente, equipo, agencia y periodo; mantener perfil, actividad y métricas trazables. |
| Datos inmobiliarios | Relacionar agente, agencia, equipo, propiedad, lead, campaña, actividad, operación y resultado con identificadores internos. |
| Marketing y crecimiento | Definir eventos analíticos no sensibles para medir uso de campañas, conversiones y productividad por canal. |
| Legal y privacidad | Revisar visibilidad, consentimiento, rankings, comparativas, facturación y datos individuales o de oficina. |
| Seguridad y calidad | Probar aislamiento entre oficinas, permisos por rol, exactitud de periodos, auditoría y rollback. |
| Formación, políticas y soporte | Convertir estándares y procesos en onboarding, checklists, ayuda contextual, responsables y escalado de incidencias. |
| Integraciones y ecosistema | Catalogar herramientas por función, permisos, datos tratados, dependencias, soporte y estrategia de salida. |
| Planificación empresarial y análisis comercial | Convertir visión y objetivos en actividad diaria, registrar llamadas, contactos, visitas, ofertas, cierres y rechazadas; mantener trazabilidad de moneda local, conversión regional, costes y reglas de reparto. |
| Academia y liderazgo de oficina | Convertir prácticas de liderazgo y operación en cursos, checklists, ejercicios, planes de acción y KPI por rol; usar referencias externas solo como benchmark y mantener contenido original de Inmobia360. |
| Captación y exclusivas | Convertir el flujo contacto → visita → valoración → plan de marketing → decisión en acciones verificables del CRM, con adaptación legal por país y sin técnicas manipulativas. |
| Onboarding y asistente de acompañamiento | Convertir cada etapa en una tarea con estado, evidencia, responsable, fecha objetivo y siguiente acción; el asistente recomienda y escala, pero no ejecuta acciones sensibles sin autorización. |
| Onboarding asistido | Diseñar rutas específicas por rol, controlar transición de estados, definir eventos de progreso y evitar que una recomendación se convierta en acción externa sin aprobación. |

Los rankings, presupuestos, liquidaciones y facturación son referencias funcionales; no quedan aprobados para el MVP por esta incorporación.

## Reglas

- No activar todos los perfiles por defecto.
- No tratar perfiles como agentes permanentes con autoridad propia.
- La comunicación externa con Juan pasa exclusivamente por `latam-real-estate`.
- Un especialista recomienda; la skill directora consolida; Juan decide lo reservado.
- Un perfil no puede ser la única aprobación de su propio resultado.
- Los especialistas no contactan terceros, no solicitan aprobaciones directamente y no entregan conclusiones finales fuera de la skill directora.
- `inmobia360-country-market-researcher` es el perfil operativo para Investigación por país. Debe activarse con país, ciudad, audiencia y pregunta definidos; su salida es evidencia y recomendaciones para la skill directora, no una decisión aprobada.
