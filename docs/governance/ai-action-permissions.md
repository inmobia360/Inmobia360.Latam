# Catálogo de acciones de IA y permisos

Estado: marco de control. No autoriza ejecuciones.

## Niveles

| Nivel | Tipo de acción | Regla |
|---|---|---|
| A0 | Lectura de documentación pública o sintética | Permitida en entorno controlado |
| A1 | Clasificación, resumen o propuesta sin efectos externos | Revisión operativa |
| A2 | Crear borradores, tareas o registros internos | Requiere trazabilidad y revisión |
| A3 | Enviar mensajes, cambiar datos o activar integraciones | Aprobación explícita previa |
| A4 | Compras, cambios DNS, producción, borrado o acciones irreversibles | No permitido automáticamente; aprobación específica de Juan |

## Controles mínimos

- Identidad del agente y origen de la solicitud.
- Alcance de herramientas permitido por tarea.
- Registro de entrada, salida, decisión y resultado.
- Límites de tiempo, coste y frecuencia.
- Idempotencia o mecanismo de reintento seguro.
- Detención manual y procedimiento de rollback.
- Separación entre propuesta de IA y ejecución aprobada.

## Primera fase propuesta

Limitar la IA a lectura de documentación del proyecto, clasificación de información sintética, generación de borradores y recomendaciones. No se habilitarán mensajes externos, cambios de infraestructura, compras, DNS ni producción.
