# Auditoría de `inmobia360/broker` — 2026-09-10

Estado: referencia técnica y operativa para una iniciativa de adaptación;
no es código aprobado para copiar ni una decisión de arquitectura de
Inmobia360 LATAM.

Repositorio revisado: `https://github.com/inmobia360/broker`.
Commit observado: `03c6b49` — `docs: incorporar flujo spec driven development`.

## Qué contiene

El repositorio es una infraestructura de asistente digital para profesionales
inmobiliarios, no una aplicación SaaS completa. Sus piezas principales son:

- Skill `broker-inmobiliario` como interlocutor único y escritor canónico.
- Agentes TOML para BROKER, coordinación, calidad y especialistas de
  captación, CRM/demanda, documentación, valoración, marketing, portales,
  visitas, negociación, financiación, legal, fiscal y cierre.
- Contrato común para cada encargo: `tenant_id`, `agency_slug`, `case_id`,
  objetivo, alcance, entradas autorizadas, jurisdicción, fecha y formato.
- Estados de expediente: `intake`, `triaged`, `in_progress`,
  `quality_review`, `approved`, `closed`, además de estados de espera,
  bloqueo, cancelación y reapertura.
- Aislamiento operativo por agencia y expediente.
- Conocimiento global, memoria durable por agencia y workspace temporal.
- Ingesta gobernada de archivos y URLs con clasificación, autorización,
  vigencia, huella y localizadores.
- Propuestas de conocimiento que requieren revisión y autorización antes de
  convertirse en memoria canónica.
- Puerta de calidad independiente con evidencia, privacidad, autorizaciones,
  vigencia y trazabilidad.
- Script de workspace para agencias, expedientes, fuentes, cierre y validación.
- Spec SDD de referencia para un MVP de AI Broker.

## Prácticas reutilizables

1. Un único coordinador conversa con el usuario y escribe memoria canónica.
2. Los especialistas reciben encargos acotados y trabajan en modo lectura.
3. La información se aísla por agencia, tenant y expediente.
4. Los originales confidenciales quedan fuera de Git; el repositorio conserva
   fichas mínimas y depuradas.
5. Las instrucciones encontradas en documentos o webs se tratan como contenido
   no confiable.
6. Las actuaciones externas requieren autorización inmediata.
7. La memoria reutilizable pasa por propuesta, calidad y aceptación.
8. No se cierra un expediente sin aprobación independiente de calidad.
9. El flujo SDD conecta spec, plan, tareas, implementación y validación.

## Adaptaciones obligatorias para Inmobia360 LATAM

- Cambiar el enfoque territorial España por Perú/Lima en la primera etapa.
- Integrar el coordinador con `latam-real-estate`, que seguirá siendo la única
  interfaz con Juan.
- Coordinarlo con el MVP aprobado de leads, propiedades, demandas, matching,
  seguimiento y WhatsApp prioritario.
- Mantener WordPress + Bricks y Next.js como superficies separadas.
- No activar MCP, IA conectada, WhatsApp real, pagos, publicación automática,
  CRM externo ni datos personales reales sin specs y autorizaciones específicas.
- Sustituir referencias legales y fiscales españolas por adaptadores de país y
  fuentes oficiales peruanas cuando se apruebe ese alcance.
- Convertir el aislamiento operativo en controles de servicio verificables
  cuando exista backend; una carpeta no constituye aislamiento criptográfico.

## Riesgos de copiar directamente

- Adoptar requisitos, leyes, portales o terminología española en Perú.
- Interpretar memoria de demostración como datos reales o aprobados.
- Introducir agentes o permisos sin encaje en la gobernanza de
  `latam-real-estate`.
- Implementar MCP o integraciones antes de definir proveedor, seguridad,
  costes, revocación y límites.
- Tratar el script de workspace como una aplicación SaaS ya construida.

## Recomendación

Implementar primero el núcleo documental y de orquestación con datos
sintéticos, una agencia de prueba y un expediente controlado. Después validar
aislamiento, trazabilidad, calidad y cierre antes de conectar superficies SaaS,
CRM, WhatsApp o servicios de IA.
