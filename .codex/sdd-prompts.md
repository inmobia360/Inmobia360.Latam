# Prompts SDD — Inmobia360 LATAM

Usar estos prompts como guía operativa. No sustituyen `docs/constitution.md`, las decisiones aprobadas ni la spec activa.

| Fase | Prompt esencial |
|---|---|
| Constitución | "Lee `docs/constitution.md`. Detecta si la solicitud entra en conflicto con algún principio. No programes todavía." |
| Spec | "NO escribas código. Convierte la necesidad en una spec usando `specs/_templates/spec.md`. Define solo QUÉ y POR QUÉ. Usa RF numerados en EARS, casos límite, fuera de alcance y criterios de finalización." |
| Clarificación | "Revisa la spec como QA independiente. Detecta ambigüedades, contradicciones, casos límite ausentes, conflictos con la Constitución, riesgos de seguridad/privacidad, multitenancy y país. Solo detecta; no resuelvas silenciosamente." |
| Plan | "Lee Constitución, decisiones y spec. Sin implementar código, crea `plan.md` con arquitectura afectada, datos, contratos, seguridad, país, observabilidad, decisiones técnicas y estrategia de tests. Mapea cada parte a sus RF." |
| Tareas | "Divide el plan en tareas pequeñas, ordenadas por dependencia. Cada tarea debe indicar RF, dependencia, trabajo, `Hecho cuando:` y evidencia esperada." |
| Implementación | "Implementa SOLO la tarea Tn de la spec activa. No amplíes alcance. Ejecuta los tests aplicables, registra evidencia, actualiza la tarea y detente." |
| Validación | "Recorre la spec RF por RF. Para cada requisito muestra implementación, test/evidencia y resultado. Da veredicto: cumplida / no cumplida." |
| Cambio | "Nuevo requisito: <X>. NO toques código. Actualiza primero la spec, explica impacto en plan/tareas y muestra el cambio antes de implementar." |
| Release | "Comprueba tests, seguridad/privacidad, staging, rollback, migraciones y trazabilidad RF antes de declarar el cambio listo para producción." |

## Regla de parada

Si falta una decisión que cambia producto, alcance, seguridad, arquitectura principal, presupuesto o regulación, marcar `[NECESITA ACLARACIÓN]` y no inventarla.
