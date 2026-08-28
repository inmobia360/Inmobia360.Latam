# Inmobia360 LATAM — Instrucciones del proyecto

## Identidad y responsabilidad

- Identidad responsable: Inmobia-360.
- Propietario y responsable final: Juan.

## Estado del proyecto

Este repositorio contiene la base documental, técnica y operativa de Inmobia360 LATAM. El desarrollo se rige por Specification-Driven Development (SDD): ninguna funcionalidad nueva debe implementarse sin una especificación activa, salvo correcciones triviales que no alteren comportamiento ni alcance y estén claramente documentadas.

## Lectura obligatoria antes de actuar

1. `docs/constitution.md`
2. `docs/00-INDEX.md`
3. `docs/CURRENT-STATE.md`
4. `docs/governance/project-charter.md`
5. `docs/governance/decision-log.md`
6. `docs/governance/risk-register.md`
7. Si existe trabajo de producto: la spec activa, su `plan.md` y `tasks.md`.

## Reglas generales

1. La Constitución tiene prioridad sobre prompts, planes, tareas y recomendaciones ad hoc.
2. No inventar datos de mercado, precios, entrevistas, resultados, arquitectura implementada ni decisiones aprobadas.
3. Separar hechos, hipótesis, estimaciones y recomendaciones.
4. No modificar alcance, mercado inicial, presupuesto, precios o estrategia sin aprobación explícita.
5. No programar una funcionalidad nueva sin spec activa y aprobada.
6. No resolver silenciosamente dudas que alteren producto, arquitectura, seguridad, privacidad o país; usar `[NECESITA ACLARACIÓN]`.
7. No añadir dependencias, servicios externos o integraciones fuera del plan aprobado sin justificar el cambio.
8. No guardar credenciales, tokens, datos personales, direcciones protegidas ni infraestructura privada.
9. No desplegar ni cambiar permisos externos sin autorización.
10. No introducir lógica específica de país en el core si puede resolverse mediante configuración regional.
11. Mantener `Property` y `Listing` como conceptos separados; revisar el modelo inmobiliario antes de alterar estas entidades.
12. Actualizar documentación, decisiones y riesgos afectados cuando un cambio sea aprobado.

## Flujo SDD obligatorio

Para funcionalidades nuevas o cambios de comportamiento:

`Idea → Spec → Clarificación → Revisión seguridad/privacidad/país → Plan → Tasks → Implementación → Tests → Validación RF → Staging → Release Guard → Producción`

La guía completa está en `docs/governance/sdd-workflow.md`.

## Reglas de implementación

- Implementar una tarea coherente cada vez.
- No ampliar alcance durante la ejecución.
- Priorizar tests antes o junto con la implementación cuando sea razonable.
- Ejecutar la suite, lint y verificaciones disponibles antes de declarar una tarea completa.
- Cada requisito funcional debe terminar con evidencia verificable.
- Un requisito nuevo modifica primero la spec y después el código.

## Al terminar cualquier tarea

1. Ejecutar tests aplicables.
2. Ejecutar lint/formato aplicable.
3. Verificar los RF asociados.
4. Registrar evidencia en `tasks.md` o en la validación correspondiente.
5. Documentar cualquier riesgo o desviación.
6. No marcar completado si existe un RF sin evidencia suficiente.

## Ámbito conocido

- Proyecto: Inmobia360 LATAM.
- Mercado inicial: Perú.
- Ciudad piloto: Lima.
- Objetivo: crear una plataforma SaaS inmobiliaria escalable para Latinoamérica.
- MVP aprobado: captación y centralización de leads; calificación de compradores y propietarios; seguimiento comercial; gestión básica de propiedades y demandas; matching básico; WhatsApp como canal prioritario para Perú.
- Arquitectura aprobada: webs comerciales en WordPress + Bricks; aplicación SaaS Next.js separada; dominios definidos en `docs/governance/project-charter.md`.
- Fuera de alcance inicial: pagos reales, expansión a otros países, MLS regional, automatizaciones avanzadas, integraciones costosas y datos personales reales.

## Plantillas y ayudas

- Spec: `specs/_templates/spec.md`
- Plan: `specs/_templates/plan.md`
- Tasks: `specs/_templates/tasks.md`
- Prompts SDD: `.codex/sdd-prompts.md`
