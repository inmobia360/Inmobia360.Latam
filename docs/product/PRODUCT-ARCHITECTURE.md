# Arquitectura del producto

## Orientación conocida

La arquitectura de producto se organizará por capas: espacio privado del agente, páginas públicas de propiedades, asistente guiado, Red Profesional, directorio de agentes y servicios regionales configurables por país.

## Capas funcionales previstas

- **Espacio privado:** propiedades, demandas, leads, actividades, contenidos, métricas y asistente.
- **Página pública:** sección de propiedades del agente, fichas, formularios y contacto consentido.
- **Red Profesional:** oportunidades publicadas voluntariamente, matching, solicitudes y acceso gradual.
- **Directorio:** perfiles públicos, especialidades, cobertura y reputación con opiniones verificadas.
- **Operación:** checklist, hitos y coordinación; no implica prestar servicios regulados sin validación local.
- **Marketing Kit candidato:** campañas online/offline, plantillas, personalización desde el perfil, exportación para impresión y presets digitales por canal; debe medir productividad y enlazar progresivamente campañas con leads, propiedades y actividades.
- **Academia candidata:** formación por rol, rutas, cursos, guías, checklists, progreso, favoritos, evaluaciones, certificaciones internas, soporte y analítica de aprendizaje.
- **Academia de liderazgo candidata:** rutas diferenciadas para CEO de oficina, broker, líder de equipo y agente; visión, reclutamiento, desarrollo, servicio, productividad, cultura, retención, costes compartidos y planes de acción.
- **Onboarding asistido candidato:** ruta de incorporación por etapas con checklist, evidencias, mentoría, progreso, recordatorios, bloqueos y escalado contextual mediante el asistente.
- **Servicio de onboarding candidato:** componente especializado para estados, evidencias, responsables, eventos de progreso, notificaciones y escalados por rol; coordinado con Academia, CRM, calendario y plan de negocio.
- **Centro de herramientas candidato:** catálogo de aplicaciones e integraciones con propósito, audiencia, permisos, datos tratados, responsable, estado, soporte y estrategia de salida.
- **Red Profesional candidata:** feed de oportunidades, propiedades, demandas, referidos, perfiles, comentarios y actividad verificable con visibilidad por ámbito.
- **Plan de negocio candidato:** visión del agente, objetivos económicos y comerciales, embudo de actividad, ratios, proyección, alertas y siguiente acción; con vistas separadas para agente, equipo, agencia y broker.
- **Captación en exclusiva candidata:** flujo guiado de contacto propietario, primera visita, cualificación, expediente, análisis de mercado, segunda visita, plan de marketing, decisión y seguimiento, conectado con leads, propiedades y actividades.
- **Contabilidad operativa candidata:** costes y beneficios por ámbito con reglas de reparto versionadas, moneda funcional local y conversión regional documentada; no sustituye la contabilidad oficial.

## Núcleo común y adaptación por país

El núcleo común debe cubrir propiedad, demanda, lead, agente, agencia, actividad, match, colaboración, reputación y auditoría. Cada país debe aportar configuración de moneda, geografía, terminología, campos, consentimientos, documentos, integraciones y reglas legales.

El núcleo deberá tratar las actividades comerciales como eventos trazables —llamadas, contactos, visitas, ofertas, cierres, rechazadas y seguimientos— y conservar periodo, fuente, estado y relación con el objetivo. La consolidación regional deberá conservar importe local, moneda funcional, tipo de cambio, fecha/fuente e importe convertido.

## No definido

La arquitectura técnica concreta, contratos API, autenticación, persistencia, observabilidad y despliegue siguen pendientes de validación. Este documento no autoriza implementación.

## Principio transversal de productividad

Cada panel, recurso, campaña, formación, publicación o integración debe resolver un punto de dolor del agente o broker y habilitar una siguiente acción. Las referencias externas sirven para descubrir patrones; la solución debe ser original, coherente con Inmobia360 y validada con datos sintéticos.
