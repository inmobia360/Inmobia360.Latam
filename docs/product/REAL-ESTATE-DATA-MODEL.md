# Modelo de datos inmobiliarios

Estado: diseño conceptual inicial; pendiente de validación. No crea tablas ni migraciones.

## Principios

- Usar identificadores internos y estados explícitos.
- Separar datos sintéticos de cualquier dato operativo futuro.
- Registrar origen, fecha de creación, última actualización y responsable de cada registro.
- Mantener historial de cambios relevantes sin sobrescribir decisiones comerciales.
- Minimizar datos personales y aplicar finalidad, acceso, retención y eliminación.

## Entidades candidatas

### Lead

Representa una oportunidad captada desde una landing o canal autorizado.

Campos candidatos: identificador interno, tipo de interés, origen, estado, prioridad, fecha de entrada, consentimiento simulado, responsable y referencia a una demanda o propiedad.

### Perfil comercial

Representa de forma controlada a un comprador, propietario u otro participante.

Campos candidatos: identificador interno, tipo de perfil, preferencias mínimas, zona general, estado de validación y referencias de contacto sintéticas.

No se deben introducir nombres, teléfonos, documentos ni direcciones personales reales durante esta fase.

### Propiedad

Representa un inmueble disponible o en gestión.

Campos candidatos: identificador interno, tipo, operación, zona general, rango de precio, características estructuradas, estado, fuente y responsable.

La dirección exacta y documentos quedan fuera del diseño inicial hasta revisar privacidad y permisos.

### Demanda

Representa una necesidad inmobiliaria de compra o alquiler.

Campos candidatos: identificador interno, operación, tipo de inmueble, zona general, rango presupuestario, características, estado, origen y responsable.

### Actividad

Registra una acción de seguimiento, nota, tarea o resultado operativo.

Campos candidatos: identificador, tipo, estado, fecha prevista, fecha realizada, resultado, autor y entidad relacionada.

### Match

Representa una relación propuesta entre una demanda y una propiedad.

Campos candidatos: identificador, demanda, propiedad, criterios coincidentes, puntuación explicable, estado de revisión, autor y fecha.

El match no debe ejecutar mensajes ni cambios externos automáticamente.

### Evento de canal

Registra la recepción o clasificación de un evento de WhatsApp u otro canal autorizado.

Campos candidatos: identificador, canal, tipo de evento, referencia sintética, dirección del evento, estado de procesamiento y fecha.

El contenido completo de conversaciones requiere una decisión específica de privacidad y retención.

## Relaciones conceptuales

```text
Perfil ──< Lead >── Demanda
Perfil ──< Lead >── Propiedad
Demanda ──< Match >── Propiedad
Lead / Demanda / Propiedad ──< Actividad
Lead / Perfil ──< Evento de canal
```

## Estados mínimos candidatos

- Lead: recibido, por calificar, calificado, en seguimiento, convertido, descartado.
- Propiedad: borrador, disponible, reservada, no disponible, archivada.
- Demanda: borrador, activa, pausada, atendida, archivada.
- Match: propuesto, revisado, aceptado, rechazado, vencido.

Los valores finales deben validarse con el proceso comercial de Lima.

## Reglas de calidad de datos

- Validar campos obligatorios en el backend cuando exista implementación.
- Evitar duplicados mediante reglas documentadas, no mediante coincidencias arbitrarias.
- No mezclar fuente observada, estimación y recomendación.
- Mantener trazabilidad de importaciones y correcciones.
- Diseñar exportación y eliminación antes de operar con datos reales.

## Pendientes

- Campos definitivos y tipos de datos.
- Relaciones y cardinalidades.
- Roles y permisos por entidad.
- Política de retención y consentimiento.
- Geografía y normalización de zonas de Lima.
- Tecnología de persistencia y migraciones.
