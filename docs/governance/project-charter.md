# Project charter — Inmobia360 LATAM

Fecha de aprobación de esta versión: 2026-08-27.

## Identidad y responsabilidad

- Identidad responsable: Inmobia-360.
- Propietario y responsable final: Juan.

## Objetivo

Crear una plataforma PropTech regional que ayude a agentes y pequeñas agencias a crear su presencia digital, gestionar propiedades y leads, mejorar su productividad, colaborar con profesionales y acompañar operaciones inmobiliarias con confianza y trazabilidad.

## Mercado y piloto

- Mercado inicial aprobado: Perú.
- Ciudad piloto aprobada: Lima.

## Alcance inicial aprobado

El MVP validará primero:

1. Captación y centralización de leads.
2. Calificación de compradores y propietarios.
3. Seguimiento comercial.
4. Gestión básica de propiedades y demandas.
5. Matching básico entre demandas y propiedades.
6. WhatsApp como canal prioritario para Perú.
7. Asistente guiado para reducir la barrera de entrada y la curva de aprendizaje.

## Arquitectura de superficies aprobada

- `inmobia360.com`: web institucional LATAM.
- `inmobia360.com/pe/`: landing comercial de Perú.
- `inmobia360.com/co/`, `inmobia360.com/mx/` y `inmobia360.com/cl/`: futuras landings comerciales regionales, no publicadas en la fase inicial.
- `app.inmobia360.com`: aplicación SaaS.
- `demo.inmobia360.com`: entorno de demostración.
- `ayuda.inmobia360.com`: futura documentación y soporte.
- `red.inmobia360.com`: subdominio candidato para la Red Profesional regional; pendiente de validación y activación.
- `agentes.inmobia360.com`: subdominio candidato para el directorio público y perfiles de agentes; pendiente de validación y activación.
- Los nuevos subdominios solo se crearán cuando exista una función concreta, validada y documentada; no se crearán anticipadamente.
- WordPress + Bricks: webs comerciales.
- Next.js separado: aplicación SaaS.

## Fuera de alcance inicial

- Pagos reales.
- Expansión a otros países.
- Red regional de colaboración como producto público completo.
- Ranking público y reputación de agentes.
- Marca blanca completa para agencias.
- Acompañamiento regulado hasta escritura sin definir responsables y marco legal local.
- Automatizaciones avanzadas.
- Integraciones costosas.
- Datos personales reales.

## Hipótesis

La priorización de Lima y WhatsApp debe validarse con usuarios y operación real controlada, sin introducir datos personales reales durante esta fase.
