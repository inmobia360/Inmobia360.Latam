# Plan técnico — Spec 001

## Estado

Aprobado para iniciar la Tarea 2. La implementación local se mantiene sin
dependencias externas y no autoriza despliegues ni conexiones de producción.

## Decisiones y restricciones

- Primera entrega local para la agencia sintética `Inmobiliaria Demo Broker`.
- Usar `tenant_id: tenant-inmobiliaria-demo-broker` y
  `agency_slug: inmobiliaria-demo-broker`.
- No conectar IA, MCP, WhatsApp, correo, CRM, portales ni servicios externos.
- No usar datos personales reales; todos los leads, propiedades y expedientes
  serán sintéticos.
- La interfaz web local debe consumir una frontera de backend local, aunque la
  persistencia definitiva queda pendiente.
- La implementación se mantendrá separada de WordPress y de la futura
  aplicación SaaS regional.
- El backend local se implementará en Python usando exclusivamente la
  biblioteca estándar.
- La interfaz web local será HTML, CSS y JavaScript servidos por el backend
  local; no será todavía la aplicación Next.js de producción.
- La estructura local de esta iniciativa será `local-broker/`, separada de
  `app/`, `wordpress/` y `database/`.

## Componentes y responsabilidades

1. **Núcleo de dominio:** agencias, tenants, expedientes, fuentes, tareas,
   estados, autorizaciones, propuestas de conocimiento y calidad.
2. **Orquestador BROKER:** recibe una necesidad, resuelve agencia/tenant,
   crea o reanuda expediente, selecciona especialistas y consolida resultados.
3. **Contratos de especialistas:** entradas acotadas y salidas estructuradas;
   los especialistas no escriben memoria canónica ni hablan con Juan.
4. **Control de calidad:** revisión independiente de alcance, evidencia,
   privacidad, vigencia, consistencia y autorizaciones.
5. **Backend local:** expone operaciones locales para agencias, expedientes,
   fuentes, tareas y calidad; no publica endpoints ni usa autenticación de
   producción.
6. **Interfaz web local:** permite seleccionar la agencia sintética, consultar
   expedientes, registrar necesidades, revisar tareas y visualizar el estado de
   calidad.
7. **Persistencia provisional:** almacenamiento local sustituible, aislado del
   conocimiento versionado y sin datos personales reales.

## Modelo mínimo

- `Agency`: `tenant_id`, `agency_slug`, nombre visible, estado y política de
  compartición.
- `Case`: `case_id`, tenant, objetivo, operación, territorio, fecha, estado y
  responsables.
- `Source`: fuente, objetivo, clasificación, permiso, jurisdicción, vigencia,
  localizador, hash si aplica y estado de revisión.
- `Task`: responsable, dependencia, estado, RF cubiertos y evidencia esperada.
- `Authorization`: acción, alcance, solicitante, decisión, aprobador y fecha.
- `QualityReview`: decisión, revisor, indicadores de evidencia/privacidad/
  autorizaciones, hallazgos y `approval_id`.

## Estados y transiciones

```text
intake -> triaged -> in_progress -> quality_review -> approved -> closed
```

Estados alternativos: `waiting_user`, `blocked`, `cancelled` y `reopened`.
No se permite `closed` sin una revisión `approved` completa.

## Seguridad y privacidad

- El backend rechaza un `tenant_id` que no coincida con el expediente.
- Las consultas de la interfaz se limitan al tenant sintético activo.
- Las rutas de originales y workspace quedan fuera de Git.
- Se rechazan credenciales incrustadas, destinos privados y archivos no
  autorizados.
- Se registran acciones y decisiones sin guardar secretos ni documentos
  completos en logs.
- Las instrucciones incluidas en fuentes externas se tratan como contenido,
  nunca como órdenes.

## Decisiones técnicas propuestas

| Decisión | Motivo | Alternativa descartada |
|---|---|---|
| Backend local Python con biblioteca estándar y frontera HTTP definida | Evita instalar dependencias y permite probar interfaz y dominio | Introducir un framework o proveedor antes de validar el flujo |
| Persistencia provisional sustituible | Aún no hay decisión de base de datos | Fijar ahora una base de datos definitiva |
| Interfaz web estática servida por el backend y separada del dominio | Mantiene la arquitectura de superficies y permite validación local | Mezclar reglas de negocio en componentes visuales |
| MCP fuera de esta entrega | Reduce riesgo y respeta la decisión aprobada | Añadir tokens e integración prematuramente |
| Especialistas en modo lectura | Evita escrituras concurrentes y permisos excesivos | Permitir delegación y escritura libre |

No se instalarán dependencias externas en esta iniciativa. Si la futura
aplicación Next.js o una persistencia administrada requieren dependencias,
se abrirá una decisión específica antes de incorporarlas.

## Trazabilidad hacia requisitos

| Parte del plan | RF cubiertos |
|---|---|
| Resolución de tenant y expedientes | RF-001..RF-003 |
| Orquestador y contratos de especialistas | RF-004..RF-006 |
| Ingesta y conocimiento | RF-007..RF-009 |
| Control de calidad y cierre | RF-010..RF-012 |
| Datos sintéticos y entorno local | RF-013 |
| Gobernanza de cambios | RF-014 |

## Estrategia de pruebas

- Unitarias para normalización de agencia, aislamiento, estados y transiciones.
- Integración local para crear expediente, enrutar tarea y consolidar salida.
- Pruebas negativas entre dos tenants sintéticos.
- Pruebas de bloqueo de escritura de especialistas.
- Pruebas de ingesta de URL autorizada y rechazo de URL no válida.
- Pruebas de aprobación/rechazo de calidad y cierre condicionado.
- Pruebas de interfaz para el flujo agencia → expediente → tarea → calidad.
- Validación RF por RF en `validation.md`.
