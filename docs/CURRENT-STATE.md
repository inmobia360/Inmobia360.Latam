# Estado actual

Fecha de actualización: 2026-08-27.

## Repositorio local

La carpeta estaba vacía antes de esta migración. No existían archivos, directorios ni `.git`; por tanto, no hubo sobrescrituras ni conflictos físicos.

## Conocimiento confirmado en la fuente accesible

- Identidad responsable: Inmobia-360.
- Propietario y responsable final: Juan.
- Nombre del proyecto: Inmobia360 LATAM.
- Mercado inicial aprobado: Perú.
- Ciudad piloto aprobada: Lima.
- Objetivo aprobado: crear una plataforma SaaS inmobiliaria escalable para Latinoamérica.
- MVP aprobado: captación y centralización de leads; calificación de compradores y propietarios; seguimiento comercial; gestión básica de propiedades y demandas; matching básico; WhatsApp como canal prioritario para Perú.
- Arquitectura aprobada: `inmobia360.com` institucional LATAM; `inmobia360.com/pe/` landing comercial Perú; `app.inmobia360.com` aplicación SaaS; `demo.inmobia360.com` demo; WordPress + Bricks para webs comerciales; Next.js separado para la aplicación.
- Arquitectura regional prevista: futuras landings comerciales mediante `/co/`, `/mx/` y `/cl/`; `ayuda.inmobia360.com` queda reservado para documentación y soporte.
- Principio de dominios aprobado: `inmobia360.com` será la landing institucional de presentación del negocio; los subdominios se reservarán para aplicación, demo, ayuda y futuras funciones globales validadas.
- Skill directora construida: `latam-real-estate` versión `0.1.0`, con flujo ejecutivo, enrutamiento, derechos de decisión, puertas de calidad, admisión de externas y plantillas.
- Skills especialistas previstas: `inmobia360-product-architecture`, `inmobia360-real-estate-data`, `inmobia360-security-privacy`, `inmobia360-country-landing`, `inmobia360-wordpress-bricks` e `inmobia360-release-guard`.

## No confirmado todavía

Siguen pendientes de validación: precios, segmentos detallados, KPIs numéricos, fechas del roadmap, arquitectura técnica interna, modelo de datos completo, requisitos legales por país, copy final de landings, pruebas independientes de comportamiento y diseño de las skills especialistas.

## Hipótesis de trabajo

- El MVP debe validarse primero en Lima antes de considerar expansión.
- WhatsApp será el canal prioritario para la operación inicial en Perú.
- La separación entre webs comerciales y aplicación SaaS permitirá evolucionar cada superficie de forma independiente.

Estas hipótesis no sustituyen validación de usuarios, mercado, legalidad ni viabilidad técnica.
