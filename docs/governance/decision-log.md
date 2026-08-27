# Registro de decisiones

Todas las decisiones de esta versión están fechadas el 2026-08-27.

## D-001 — Carpeta principal

- Estado: aprobada.
- Decisión: usar `C:\Users\Usuario\Documents\Inmobia360-LATAM` como carpeta principal.
- Evidencia: instrucción explícita de Juan.

## D-002 — Mercado inicial

- Estado: aprobada.
- Decisión: Perú como mercado inicial.
- Evidencia: instrucción explícita de Juan.

## D-003 — Ciudad piloto

- Estado: aprobada.
- Decisión: Lima como ciudad piloto.
- Evidencia: instrucción explícita de Juan.

## D-004 — Identidad responsable

- Estado: aprobada.
- Decisión: la identidad responsable es Inmobia-360; Juan es propietario y responsable final.
- Evidencia: instrucción explícita de Juan.

## D-005 — Objetivo del proyecto

- Estado: aprobada.
- Decisión: crear una plataforma SaaS inmobiliaria escalable para Latinoamérica.
- Evidencia: instrucción explícita de Juan.

## D-006 — Alcance MVP Perú

- Estado: aprobada.
- Decisión: limitar el MVP a las seis capacidades descritas en `project-charter.md`.
- Evidencia: instrucción explícita de Juan.

## D-007 — Arquitectura de superficies

- Estado: aprobada.
- Decisión: separar webs comerciales WordPress + Bricks de la aplicación SaaS Next.js y mantener los dominios definidos.
- Evidencia: instrucción explícita de Juan.

## D-008 — Fuera de alcance inicial

- Estado: aprobada.
- Decisión: no abrir pagos reales, expansión regional, MLS regional, automatizaciones avanzadas, integraciones costosas ni datos personales reales.
- Evidencia: instrucción explícita de Juan.

## D-009 — Skills

- Estado: aprobada como dirección futura.
- Decisión: `latam-real-estate` será la primera skill propia; las especialistas se desarrollarán posteriormente. No se construye ni se instalan skills externas en esta fase.
- Evidencia: instrucción explícita de Juan.

## D-010 — Fase 1 documental

- Estado: aprobada.
- Decisión: crear únicamente los nueve archivos de gobierno autorizados, conservando y comparando los existentes.
- Evidencia: aprobación explícita de Juan.

## D-011 — Sistema modular de skills

- Estado: aprobada.
- Fecha: 2026-08-27.
- Decisión: utilizar `latam-real-estate` como skill directora y mantener las skills especialistas como planificadas hasta que exista una necesidad validada.
- Evidencia: directrices y aprobación de Juan.

## D-012 — Admisión de skills externas

- Estado: aprobada.
- Fecha: 2026-08-27.
- Decisión: ninguna skill externa se instalará sin revisión de procedencia, contenido, scripts, auditorías, aislamiento, fijación de versión y aprobación de Juan. Si el riesgo no se resuelve, se construirá una versión propia.
- Evidencia: directriz explícita de Juan.

## D-013 — Skill directora v0.1.0

- Estado: implementada; validación de comportamiento pendiente.
- Fecha: 2026-08-27.
- Decisión: construir `latam-real-estate` con referencias, plantillas, puertas de calidad, derechos de decisión, enrutamiento de especialistas y política de admisión externa.
- Evidencia: autorización explícita de Juan y validación estructural satisfactoria.

## D-014 — Interfaz única de comunicación

- Estado: aprobada.
- Fecha: 2026-08-27.
- Decisión: Juan mantendrá comunicación activa únicamente con `latam-real-estate`; los perfiles especialistas trabajarán internamente y sus resultados serán consolidados por la skill directora.
- Evidencia: instrucción explícita de Juan.

## D-015 — Ruta de la landing comercial de Perú

- Estado: aprobada.
- Fecha: 2026-08-27.
- Decisión: utilizar `inmobia360.com/pe/` como ruta oficial de la landing comercial del mercado piloto de Perú. La ruta anterior `inmobia360.com/peru/` queda descartada.
- Evidencia: confirmación explícita de Juan.

## D-016 — Inicio de preparación de Fase 2

- Estado: aprobada para preparación documental.
- Fecha: 2026-08-27.
- Decisión: preparar la arquitectura de despliegue, matriz de entornos, política de Git/releases y controles de secretos/rollback antes de conectar Hostinger o comenzar el desarrollo.
- Restricciones: no instalar dependencias, no conectar servicios externos, no desplegar y no utilizar datos personales reales.
- Evidencia: instrucción de Juan de proceder con el siguiente paso recomendado.

## D-017 — Arquitectura de dominios y subdominios

- Estado: aprobada.
- Fecha: 2026-08-27.
- Decisión: utilizar `inmobia360.com` como landing institucional de presentación del negocio; mantener las landings comerciales por país en subdirectorios; reservar subdominios como `app.inmobia360.com`, `demo.inmobia360.com` y `ayuda.inmobia360.com` para aplicación, demostración y soporte global.
- Regla: cualquier subdominio nuevo deberá tener una función concreta, validada y documentada antes de crearse.
- Evidencia: confirmación explícita de Juan.

## D-018 — Preparación del destino de alojamiento

- Estado: aprobada para preparación documental.
- Fecha: 2026-08-27.
- Decisión: definir el destino técnico de cada dominio y subdominio antes de conectar Hostinger, modificar DNS, adquirir servicios o desplegar.
- Restricciones: no realizar compras, cambios DNS, conexiones externas ni despliegues durante esta preparación.
- Evidencia: instrucción de Juan de proseguir con el siguiente paso recomendado.

## D-020 — VPS como capa de orquestación de IA

- Estado: aprobada para diseño; implementación pendiente.
- Fecha: 2026-08-27.
- Decisión: evaluar el VPS KVM 2 como capa para orquestar agentes, subagentes, automatizaciones y acciones de IA, manteniendo inicialmente el modelo de IA como servicio cloud separado.
- Restricciones: no instalar modelos, runtimes ni automatizadores; no conectar servicios; no procesar datos personales reales; no ejecutar acciones irreversibles sin aprobación humana.
- Evidencia: instrucción explícita de Juan sobre el uso previsto del VPS.

## D-021 — Evaluación controlada de IA

- Estado: aprobada para diseño; proveedor e implementación pendientes.
- Fecha: 2026-08-27.
- Decisión: seleccionar el modelo y proveedor de IA mediante criterios documentados de seguridad, privacidad, coste, capacidad, portabilidad y operación. La primera fase se limitará a tareas no destructivas con datos sintéticos.
- Restricciones: no conectar proveedores, no enviar datos personales reales, no permitir cambios DNS, compras, mensajes externos ni acciones de producción automáticas.
- Evidencia: aplicación del flujo de decisión de `latam-real-estate` y autorización de Juan para proseguir.

## D-022 — Blueprint técnico inicial del MVP

- Estado: aprobado para diseño; implementación pendiente.
- Fecha: 2026-08-27.
- Decisión: estructurar funcional y técnicamente el MVP Perú antes de programar, manteniendo Lima como piloto, WhatsApp como canal prioritario y datos sintéticos.
- Restricciones: no iniciar desarrollo, no conectar IA, no activar integraciones externas ni ampliar el alcance aprobado.
- Evidencia: instrucción de Juan de proseguir con la estructura del proyecto.

## D-023 — Diseño conceptual del modelo de datos

- Estado: aprobado para diseño; implementación pendiente.
- Fecha: 2026-08-27.
- Decisión: estructurar entidades candidatas para leads, perfiles, propiedades, demandas, actividades, matches y eventos de canal, utilizando identificadores internos, datos sintéticos y trazabilidad.
- Restricciones: no crear tablas, migraciones ni operar con datos personales reales hasta validar campos, permisos, retención y requisitos legales.
- Evidencia: instrucción de Juan de proseguir con la estructura del proyecto.
