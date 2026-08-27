# Arquitectura del producto

## Orientación conocida

La arquitectura de producto se organizará por capas: espacio privado del agente, páginas públicas de propiedades, asistente guiado, Red Profesional, directorio de agentes y servicios regionales configurables por país.

## Capas funcionales previstas

- **Espacio privado:** propiedades, demandas, leads, actividades, contenidos, métricas y asistente.
- **Página pública:** sección de propiedades del agente, fichas, formularios y contacto consentido.
- **Red Profesional:** oportunidades publicadas voluntariamente, matching, solicitudes y acceso gradual.
- **Directorio:** perfiles públicos, especialidades, cobertura y reputación con opiniones verificadas.
- **Operación:** checklist, hitos y coordinación; no implica prestar servicios regulados sin validación local.

## Núcleo común y adaptación por país

El núcleo común debe cubrir propiedad, demanda, lead, agente, agencia, actividad, match, colaboración, reputación y auditoría. Cada país debe aportar configuración de moneda, geografía, terminología, campos, consentimientos, documentos, integraciones y reglas legales.

## No definido

La arquitectura técnica concreta, contratos API, autenticación, persistencia, observabilidad y despliegue siguen pendientes de validación. Este documento no autoriza implementación.
