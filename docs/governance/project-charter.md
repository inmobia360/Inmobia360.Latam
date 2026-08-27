# Project charter — Inmobia360 LATAM

Fecha de aprobación de esta versión: 2026-08-27.

## Identidad y responsabilidad

- Identidad responsable: Inmobia-360.
- Propietario y responsable final: Juan.

## Objetivo

Crear una plataforma SaaS inmobiliaria escalable para Latinoamérica.

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

## Arquitectura de superficies aprobada

- `inmobia360.com`: web institucional LATAM.
- `inmobia360.com/pe/`: landing comercial de Perú.
- `inmobia360.com/co/`, `inmobia360.com/mx/` y `inmobia360.com/cl/`: futuras landings comerciales regionales, no publicadas en la fase inicial.
- `app.inmobia360.com`: aplicación SaaS.
- `demo.inmobia360.com`: entorno de demostración.
- `ayuda.inmobia360.com`: futura documentación y soporte.
- WordPress + Bricks: webs comerciales.
- Next.js separado: aplicación SaaS.

## Fuera de alcance inicial

- Pagos reales.
- Expansión a otros países.
- MLS regional.
- Automatizaciones avanzadas.
- Integraciones costosas.
- Datos personales reales.

## Hipótesis

La priorización de Lima y WhatsApp debe validarse con usuarios y operación real controlada, sin introducir datos personales reales durante esta fase.

