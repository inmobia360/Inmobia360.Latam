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
- La identidad corporativa cuenta con un manual maestro externo incorporado como referencia operativa en `docs/brand/BRAND-CONTEXT.md`.
- La dirección de producto contempla ahora espacio privado del agente, páginas públicas de propiedades, asistente guiado, Red Profesional y directorio/reputación como evoluciones.
- El contexto de producto se ha enriquecido con referencias funcionales externas sobre campañas, rendimiento de oficina, hubs de herramientas, colaboración profesional, formación y gestión de agentes; se conservan como benchmarks, no como especificaciones ni activos reutilizables.
- Se han definido como candidatos funcionales `mk.inmobia360.com` para marketing del agente, `red.inmobia360.com` para colaboración y `academia.inmobia360.com` para formación; ninguno está activado ni aprobado para despliegue.
- El staff propio incluye perfiles de diseño/publicidad, operaciones de broker/oficina, formación/políticas/soporte, integraciones/ecosistema y Red Profesional/colaboración.
- Se incorpora el perfil `inmobia360-business-planning` para planes de negocio, análisis comercial, KPI, previsiones, monedas y prorrateo de costes/beneficios por agente, equipo, agencia y broker.
- Se incorpora al contexto de Academia el benchmark formativo de liderazgo y crecimiento de oficina, con rutas candidatas para CEO de oficina, broker, líder de equipo y agente. Debe transformarse en contenido original, accionable y validado para Perú.
- Se incorpora al contexto de Academia el flujo candidato de captación en exclusiva: prospección, primera visita, cualificación, documentación, análisis de mercado, segunda visita, plan de marketing, decisión y seguimiento. Los contenidos legales y fiscales de la fuente quedan pendientes de adaptación local.
- Se incorpora al contexto de Academia el benchmark de onboarding guiado: bienvenida, activación, checklist, formación progresiva, práctica, mentoría, evidencias, revisión semanal y asistente contextual para soporte y seguimiento.
- Se incorpora al staff `inmobia360-onboarding-assistant`, especializado en rutas, estados, evidencias, recordatorios, bloqueos y escalado del onboarding por rol. Trabajará coordinado con Academia, Operaciones, Producto, Arquitectura, Datos y Planificación empresarial.

## No confirmado todavía

Siguen pendientes de validación: precios y margen, segmentos detallados, KPIs numéricos, fechas del roadmap, arquitectura técnica interna, modelo de datos completo, requisitos legales por país, reputación y ranking, marca blanca, responsabilidades hasta escritura, copy final de landings, pruebas independientes de comportamiento, diseño de las skills especialistas planificadas, alcance definitivo de Academia/Marketing Kit/Red Profesional, reglas de referidos y permisos de broker/oficina, vocabulario y fuentes de eventos comerciales, fórmulas de KPI, política de tipos de cambio y reglas de prorrateo de costes/beneficios, perfiles y KPI propios de liderazgo de oficina, criterios legales y metodología de captación en exclusiva para Perú, etapas, evidencias, responsables y notificaciones del onboarding asistido, rutas por rol, eventos de progreso y criterios de escalado.

## Hipótesis de trabajo

- El MVP debe validarse primero en Lima antes de considerar expansión.
- WhatsApp será el canal prioritario para la operación inicial en Perú.
- La separación entre webs comerciales y aplicación SaaS permitirá evolucionar cada superficie de forma independiente.

Estas hipótesis no sustituyen validación de usuarios, mercado, legalidad ni viabilidad técnica.

## Recursos de infraestructura informados por Juan

- Suscripción VPS Hostinger: KVM 2; identificador privado omitido de la documentación versionada.
- Dominio Hostinger: `inmobia360.com`.
- Suscripción `Starter Business Email Trial` asociada a `compracaptacion.com`; queda fuera del alcance actual de Inmobia360 LATAM.

Estos datos son un inventario informado. No implican autorización para acceder, configurar, modificar DNS o desplegar.

## Dirección técnica prevista para IA

- El VPS KVM 2 se evaluará como capa de orquestación de IA, automatizaciones y agentes internos.
- El modelo de IA se considera inicialmente un servicio cloud separado.
- El proveedor, modelo, permisos, costes y datos permitidos siguen pendientes de validación.
- El modelo de datos inmobiliarios cuenta con un diseño conceptual inicial; no existen tablas ni migraciones implementadas.
- La revisión de preparación del repositorio concluye `GO CONDICIONADO` para continuar la preparación documental y `NO-GO` para programar o desplegar: siguen pendientes la validación de Fase 2, el blueprint técnico, los contratos API, los roles/permisos, la seguridad, las pruebas y el plan de releases.
- Se propone `inmobia360-performance-marketing` como futura especialidad unificada para publicidad de pago, análisis social, atribución y formatos; no está implementada ni aprobada para conexiones externas.
- La investigación automatizada de competidores y portales queda como propuesta futura de `inmobia360-market-intelligence`, sujeta a límites legales, de privacidad y de seguridad.
