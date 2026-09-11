# SDD Workflow — Inmobia360 LATAM

Versión: 0.1.0

## Objetivo

Aplicar Specification-Driven Development (SDD) como proceso oficial para evolucionar Inmobia360 LATAM con agentes de IA y desarrollo humano controlado.

## Flujo oficial

1. **Idea / necesidad de negocio**
2. **Validación del problema** cuando corresponda
3. **Spec** — define QUÉ y POR QUÉ
4. **Clarificación QA** — detecta ambigüedades, contradicciones y casos límite sin programar
5. **Revisión de seguridad, privacidad y país** cuando aplique
6. **Plan** — define CÓMO
7. **Tasks** — divide el plan en unidades pequeñas y verificables
8. **Implementación** — una tarea coherente cada vez
9. **Tests y verificación**
10. **Code review**
11. **Validación RF por RF**
12. **Staging**
13. **Release guard / aprobación**
14. **Producción**
15. **Métricas y aprendizaje**

## Reglas por fase

### Spec

Debe contener únicamente comportamiento, actores, requisitos, casos límite, fuera de alcance, criterios de finalización y dudas abiertas. No debe decidir stack, archivos concretos ni detalles de implementación salvo que sean una restricción de producto aprobada.

Los requisitos funcionales deben expresarse preferentemente en EARS:

- `CUANDO <evento>, EL SISTEMA <respuesta>`
- `SI <condición>, ENTONCES EL SISTEMA <respuesta>`
- `MIENTRAS <estado>, EL SISTEMA <respuesta>`
- `EL SISTEMA <comportamiento permanente>`

### Clarificación

Un revisor distinto debe buscar:

- ambigüedades;
- contradicciones;
- casos límite ausentes;
- conflictos con `docs/constitution.md`;
- riesgos de seguridad y privacidad;
- problemas de multitenancy;
- dependencias específicas de país;
- requisitos no verificables.

No debe resolver silenciosamente las dudas detectadas.

### Plan

Debe incluir:

- arquitectura afectada;
- módulos y componentes;
- modelo de datos;
- APIs/contratos/eventos;
- seguridad y privacidad;
- configuración por país;
- migraciones;
- observabilidad;
- estrategia de tests;
- decisiones técnicas y alternativas descartadas;
- matriz RF → implementación/test.

### Tasks

Cada tarea debe:

- tener un ID;
- indicar RF cubiertos;
- declarar dependencias;
- ser pequeña y coherente;
- contener `Hecho cuando:` con criterio verificable.

### Implementación

El agente implementa solo la tarea asignada. No amplía alcance, no refactoriza áreas no necesarias y no añade dependencias sin justificación y autorización correspondiente.

### Validación

Se recorre la spec requisito por requisito. Para cada RF se registra:

- implementación relacionada;
- test/evidencia;
- resultado;
- estado.

Si un RF no tiene evidencia suficiente, la spec no está cumplida.

## Cambios de requisitos

Ante un requisito nuevo:

1. no tocar código;
2. actualizar la spec;
3. mostrar el impacto/diff;
4. revisar plan y tareas;
5. implementar después de aprobación.

## Relación entre SDD y skills

- **SDD** define qué construir y el proceso de construcción.
- **Skills** definen qué especialista sabe ejecutar o revisar cada parte.
- La skill directora `latam-real-estate` coordina especialistas, pero ninguna skill puede sustituir o contradecir una spec aprobada.

## Trazabilidad mínima

Cada spec debe poder responder:

`RF → Plan → Task → Código/Configuración → Test/Evidencia → Estado`
