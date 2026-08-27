# Benchmark funcional: onboarding guiado y asistente de acompañamiento

Fecha de análisis: 2026-08-27.

## Fuente observada

Carpeta de Drive `ONBOARDING NEW`, con materiales de bienvenida, checklist de incorporación, plan de onboarding, semanas de formación y versiones para formador y agente.

## Estructura observada

- `drive-download`: carpeta auxiliar.
- `PDF Eliseo`: material auxiliar.
- Carta de bienvenida.
- Checklist de incorporación de nuevo agente.
- Plan de onboarding inmobiliario.
- Semana 1: cimentación, identidad profesional y activación.
- Semana 2: conversión de oportunidades y valoración.
- Semana 3: marketing y representación del cliente.
- Semana 4: cierre, compradores y visión de futuro.

Los materiales detallados también plantean una progresión semanal con mentor/formador, sesiones, práctica de campo, deberes, resultados esperados, herramientas y revisiones de logros.

## Buenas prácticas aplicables

1. **Inicio con propósito:** bienvenida, expectativas, visión profesional y objetivos.
2. **Acceso operativo temprano:** perfil, permisos, herramientas, calendario, CRM y soporte.
3. **Checklist por hitos:** cada etapa tiene tareas, responsable, evidencia y estado.
4. **Progresión gradual:** fundamentos → prospección → visitas/valoración → marketing → cierre.
5. **Aprendizaje mixto:** contenido, práctica, role-play, mentoría, campo y reflexión.
6. **Resultados observables:** contactos, citas, materiales, propiedades, actividades y primeras oportunidades.
7. **Acompañamiento:** mentor, broker, compañeros y asistente como red de apoyo.
8. **Revisión periódica:** feedback, obstáculos, logros y siguiente semana.
9. **Conexión con el plan de negocio:** actividad del onboarding alimenta KPI, embudo y previsión.
10. **Adaptación por rol:** agente, mentor, broker, líder de equipo y administrador necesitan vistas diferentes.

## Asistente virtual propuesto

El asistente no debe ser un chatbot aislado. Debe ser una capa contextual sobre Academia, CRM, calendario, perfil y plan de negocio.

### Funciones candidatas

- Explicar el objetivo de cada etapa.
- Mostrar la siguiente tarea prioritaria.
- Recordar tareas pendientes y próximas sesiones.
- Detectar bloqueos declarados por el usuario.
- Recomendar una lección, checklist o recurso.
- Validar si existe evidencia de una tarea completada.
- Preparar una revisión semanal.
- Resumir progreso frente a objetivos.
- Escalar al mentor, líder o broker cuando corresponda.
- Proponer, pero no enviar, mensajes o acciones externas sin autorización.

### Máquina de estados candidata

`No iniciado → En curso → Evidencia pendiente → Completado → Revisado → Reforzar o avanzar`

Cada hito debería conservar usuario, rol, etapa, tarea, fecha objetivo, evidencia, responsable de revisión, estado, comentarios y auditoría.

## Diseño de experiencia

- Panel “Hoy”: tres prioridades máximas, bloqueos y próxima sesión.
- Ruta “Mi incorporación”: porcentaje de avance por etapa.
- Centro “Necesito ayuda”: preguntas frecuentes, recursos y escalado.
- Revisión semanal: logros, actividad, ratios, obstáculos y compromiso siguiente.
- Vista de mentor/broker: avance agregado sin exponer información innecesaria.
- Notificaciones configurables por canal y horario.

## Límites y adaptación

- La fuente contiene terminología, herramientas y referencias de una marca externa; no se reutilizarán literalmente.
- Los objetivos cuantitativos observados son ejemplos, no metas de Inmobia360.
- Los contenidos legales, fiscales, documentales y de herramientas deberán adaptarse a Perú y revisarse localmente.
- El asistente no aprobará contratos, precios, financiación, impuestos ni decisiones reguladas.
- No se usarán datos personales reales en el diseño o validación inicial.

## Pendientes

- Definir la duración y etapas del onboarding de Inmobia360.
- Aprobar roles, responsables y permisos.
- Definir evidencias de completitud y KPI.
- Diseñar las integraciones con CRM, calendario y Academia.
- Definir reglas de notificación, escalado y revisión humana.
