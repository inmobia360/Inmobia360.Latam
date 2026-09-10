# Tareas — Spec 001

- [x] T1. Registrar decisiones de stack local, límites y estructura técnica.
  (RF: RF-013, RF-014) Hecho cuando: las decisiones están documentadas y no
  introducen dependencias sin autorización.
- [ ] T2. Crear el dominio de agencia, tenant y expediente con estados.
  (RF: RF-001..RF-003) Hecho cuando: las pruebas de identificación, estados y
  aislamiento sintético pasan.
- [ ] T3. Crear el contrato común de especialistas y el orquestador BROKER.
  (RF: RF-004..RF-006) Hecho cuando: una necesidad se enruta y ningún
  especialista puede escribir memoria canónica.
- [ ] T4. Implementar registro de fuentes y controles de ingesta local.
  (RF: RF-007, RF-008) Hecho cuando: URL válida, URL no válida y datos
  sensibles tienen el comportamiento especificado.
- [ ] T5. Implementar propuestas de conocimiento y estados de revisión.
  (RF: RF-009) Hecho cuando: ninguna propuesta pasa a memoria aprobada sin
  calidad y autorización.
- [ ] T6. Implementar CONTROL DE CALIDAD y cierre de expediente.
  (RF: RF-010..RF-012) Hecho cuando: rechazo y aprobación son reproducibles y
  el cierre exige todos los indicadores.
- [ ] T7. Exponer el backend local y preparar persistencia provisional.
  (RF: RF-001..RF-014) Hecho cuando: las operaciones del dominio son accesibles
  localmente y no exponen datos fuera del tenant.
- [ ] T8. Crear la interfaz web local para la agencia Demo Broker.
  (RF: RF-001..RF-012) Hecho cuando: se recorre el flujo completo desde la UI.
- [ ] T9. Ejecutar pruebas de aislamiento, privacidad, regresión y UI.
  (RF: RF-001..RF-014) Hecho cuando: las pruebas relevantes pasan y se
  documentan sus resultados.
- [ ] T10. Completar validación RF por RF y revisión independiente.
  (RF: RF-001..RF-014) Hecho cuando: `validation.md` tiene evidencia y
  decisión de calidad.

## Reglas de ejecución

- Implementar una sola tarea cada vez.
- Escribir tests antes del código cuando sea aplicable.
- Detenerse si aparece una decisión nueva de alcance, arquitectura, coste,
  datos o integración.
- No activar MCP ni servicios externos durante esta iniciativa.
