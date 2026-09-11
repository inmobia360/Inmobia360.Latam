# Constitución SDD — Inmobia360 LATAM

Versión: 0.1.0
Estado: Activa

Esta constitución define las reglas superiores del desarrollo de Inmobia360 LATAM. Ninguna especificación, plan, tarea, skill o implementación puede contradecirla sin una decisión explícita registrada en gobernanza.

## Principios

1. **La especificación manda.** Ninguna funcionalidad nueva se implementa sin una spec activa y aprobada.
2. **No inventar requisitos.** Si una decisión necesaria no está definida, debe marcarse como `[NECESITA ACLARACIÓN]` o resolverse antes de implementar.
3. **Separación de responsabilidades.** Marketing WordPress, aplicación SaaS, datos, automatizaciones e integraciones mantienen fronteras explícitas.
4. **Privacidad y seguridad por diseño.** Toda funcionalidad que trate datos personales, autenticación, permisos, IA o integraciones debe definir riesgos, autorización y minimización de datos.
5. **Secretos fuera del repositorio.** Nunca se guardan tokens, contraseñas, claves API, datos personales reales ni credenciales de infraestructura.
6. **Testabilidad obligatoria.** Todo requisito verificable debe tener evidencia de validación; se priorizan tests automáticos cuando sean razonablemente posibles.
7. **Trazabilidad.** Cada requisito funcional debe relacionarse con plan, tareas, implementación y evidencia de validación.
8. **Cambios desde la spec.** Un requisito nuevo o modificado actualiza primero la spec; después se revisan plan, tareas y código.
9. **Compatibilidad multipaís.** La lógica común no debe incorporar reglas específicas de un país si puede resolverse mediante configuración o extensión regional.
10. **Producción protegida.** Los cambios deben pasar por revisión, tests aplicables, staging y aprobación antes de producción.
11. **Datos inmobiliarios estructurados.** `Property` y `Listing` son conceptos separados; cambios al modelo inmobiliario deben revisar el modelo de datos maestro.
12. **Una tarea coherente cada vez.** Los agentes implementan unidades pequeñas, verificables y acotadas; no expanden alcance durante la ejecución.

## Jerarquía documental

Cuando exista conflicto, prevalece este orden:

1. `docs/constitution.md`
2. decisiones aprobadas en `docs/governance/decision-log.md`
3. spec activa
4. plan de la spec
5. tareas de la spec
6. documentación técnica secundaria
7. prompts o instrucciones ad hoc

## Quality gates mínimos

Una spec no se considera cumplida hasta que:

- todos los requisitos funcionales estén resueltos o explícitamente retirados;
- cada RF tenga evidencia de validación;
- no existan contradicciones abiertas con esta constitución;
- los tests aplicables estén en verde;
- seguridad y privacidad hayan sido revisadas cuando corresponda;
- el cambio esté listo para revisión en staging cuando afecte producto ejecutable.

## Política de cambio

Cambiar esta constitución requiere:

1. propuesta explícita;
2. impacto documentado;
3. aprobación del propietario del proyecto;
4. registro en `docs/governance/decision-log.md`;
5. incremento de versión.
