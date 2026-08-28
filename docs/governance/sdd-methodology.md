# Metodología Spec-Driven Development (SDD)

Estado: aprobada para preparación documental y uso en iniciativas autorizadas.

## Propósito

Convertir cada iniciativa de producto en un contrato verificable antes de
programar. La metodología reduce ambigüedades, evita ampliar el alcance sin
aprobación y mantiene trazabilidad entre necesidad, requisito, diseño, tarea,
prueba y entrega.

## Jerarquía de fuentes

1. Decisiones aprobadas por Juan y el `project-charter`.
2. `AGENTS.md`, `CURRENT-STATE.md`, riesgos y políticas de seguridad/release.
3. La spec aprobada de la iniciativa.
4. El plan técnico aprobado.
5. Las tareas y la implementación.

Una spec no puede contradecir una decisión superior. Si aparece un conflicto,
se detiene la iniciativa y se eleva una decisión; no se resuelve por intuición.

## Flujo obligatorio

1. **Constitución y contexto:** confirmar objetivo, usuarios, país, fase,
   restricciones, datos permitidos y criterios de éxito.
2. **Spec:** documentar el qué y el porqué, historias, requisitos EARS,
   casos límite, fuera de alcance y dudas abiertas. No incluir stack,
   arquitectura, nombres de archivos ni algoritmos.
3. **Clarificación:** revisar ambigüedades, contradicciones, huecos, riesgos y
   conflictos con la gobernanza. No implementar mientras queden dudas críticas.
4. **Plan:** definir arquitectura, modelo de datos, contratos, decisiones
   técnicas, alternativas descartadas, seguridad y estrategia de pruebas.
5. **Tareas:** dividir el plan en unidades pequeñas, dependientes y
   verificables, vinculadas a requisitos.
6. **Implementación:** trabajar en una rama aislada y una tarea cada vez;
   escribir pruebas antes del código cuando sea aplicable.
7. **Validación:** recorrer cada requisito funcional, evidenciar sus pruebas,
   comprobar criterios de finalización y documentar fallos o excepciones.
8. **Cambio:** modificar primero la spec, mostrar el alcance afectado y
   obtener aprobación antes de modificar plan, tareas o código.

## Convenciones

- Iniciativas en `specs/NNN-nombre-en-kebab-case/`.
- Requisitos funcionales numerados `RF-1`, `RF-2`, etc.
- Criterios de aceptación en notación EARS: evento, estado, condición no
  deseada, característica opcional o comportamiento ubicuo.
- Cada requisito debe poder verificarse sin interpretación subjetiva.
- Toda duda se marca como `[NECESITA ACLARACIÓN: pregunta concreta]`.
- Cada tarea incluye requisitos cubiertos y una línea `Hecho cuando:`.
- Ninguna tarea se declara completada sin evidencia de validación.

## Adaptación a Inmobia360

- `docs/` sigue siendo la fuente de gobierno, negocio y contexto regional.
- `specs/` contiene contratos de iniciativas concretas; no sustituye el
  charter, el modelo conceptual ni las decisiones de producto.
- Las primeras iniciativas usarán Lima, Perú y datos sintéticos.
- No se implementan pagos, expansión regional, datos personales reales,
  automatizaciones avanzadas ni integraciones costosas sin decisión específica.
- Producto, arquitectura, seguridad y QA revisan desde responsabilidades
  separadas; quien implementa no es la única persona que aprueba.

## Puertas de calidad

- **Spec:** objetivo, usuarios, alcance, RF, límites y dudas identificados.
- **Plan:** todos los RF tienen diseño y estrategia de prueba.
- **Implementación:** las tareas están trazadas y las pruebas relevantes pasan.
- **Release:** validación RF por RF, seguridad, rollback, aprobador y entorno
  registrados.

Las salidas son `GO`, `GO CONDICIONADO`, `NO-GO` o `INFORMACIÓN INSUFICIENTE`,
según las puertas de calidad de `latam-real-estate`.
