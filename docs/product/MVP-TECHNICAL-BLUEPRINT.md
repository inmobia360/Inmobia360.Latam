# Blueprint técnico del MVP Perú

Estado: diseño inicial; pendiente de validación y aprobación técnica. No es una especificación de implementación.

## Objetivo

Definir la primera estructura funcional y técnica para validar el MVP en Lima, manteniendo WhatsApp como canal prioritario y sin datos personales reales.

## Módulos funcionales candidatos

1. Captación y centralización de leads.
2. Calificación de compradores y propietarios.
3. Seguimiento comercial y actividades.
4. Gestión básica de propiedades.
5. Gestión básica de demandas.
6. Matching inicial entre demandas y propiedades.
7. Bandeja o registro de conversaciones de WhatsApp, sin automatización avanzada.
8. Creación de una página pública asociada al agente y sus propiedades.
9. Asistente guiado contextual para completar datos y orientar la siguiente acción.

Son módulos candidatos derivados del alcance aprobado; el orden y profundidad deben validarse.

## Superficies

- WordPress: presentación, landings y formularios de captación.
- Aplicación SaaS: operación interna, usuarios autorizados y seguimiento.
- Demo: experiencia aislada con datos sintéticos.
- API: contrato pendiente entre web, aplicación y servicios autorizados.
- VPS: candidato para servicios técnicos y orquestación futura; no se implementa todavía.
- Directorio público de agentes y Red Profesional: superficies futuras, no parte del primer flujo técnico.

## Entidades candidatas

- Lead.
- Persona o perfil comercial sintético.
- Propiedad.
- Demanda.
- Actividad o seguimiento.
- Match.
- Conversación o evento de canal.
- Perfil público de agente.
- Actividad guiada del asistente.

Los campos, relaciones, estados, permisos, auditoría y reglas de deduplicación quedan pendientes de diseño de datos.

## Flujo mínimo a validar

1. Un lead llega desde una landing.
2. Se registra con origen y consentimiento simulado.
3. Se clasifica como comprador, propietario u otro estado definido.
4. Se registra una actividad de seguimiento.
5. Se relaciona con una propiedad o demanda compatible.
6. Un usuario autorizado revisa el resultado y decide la siguiente acción.

## Criterios de aceptación preliminares

- El flujo puede recorrerse con datos sintéticos de Lima.
- Cada registro tiene estado, origen y trazabilidad básica.
- Un usuario autorizado puede revisar y corregir la clasificación.
- El matching muestra criterios comprensibles y no ejecuta acciones externas.
- Los fallos no exponen secretos ni datos sensibles.
- El flujo puede detenerse y revertirse sin pérdida no controlada.

## Fuera de alcance

- Pagos reales.
- Red Profesional regional completa.
- Expansión a otros países.
- Automatizaciones avanzadas.
- Integraciones costosas.
- Datos personales reales.
- Modelo cloud de IA conectado.

## Decisiones pendientes

- Roles de usuario y permisos.
- Contratos API.
- Modelo de datos y tecnología de persistencia.
- Proveedor de autenticación.
- Canal WhatsApp y nivel de integración.
- KPIs y umbrales de éxito.
- Requisitos legales y de privacidad aplicables.
- Reglas de reputación, opiniones verificadas y ranking público.
- Modelo de colaboración regional y responsabilidades hasta hitos de cierre.
