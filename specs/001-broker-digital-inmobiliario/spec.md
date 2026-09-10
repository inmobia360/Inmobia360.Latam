# Spec 001 — Infraestructura de asistente digital inmobiliario

## Contexto y objetivo

Inmobia360 LATAM necesita una infraestructura de asistencia para que agentes y
pequeñas agencias trabajen con leads, propiedades, demandas y operaciones de
forma guiada, trazable y segura. La iniciativa adapta el patrón BROKER del
repositorio de referencia al MVP de Perú y Lima, manteniendo la supervisión
humana y evitando que el asistente invente información o ejecute acciones
externas sin autorización.

## Usuarios / actores

- Juan, responsable final y único interlocutor de la dirección del proyecto.
- Agente inmobiliario de una agencia autorizada.
- Administrador o broker de una agencia autorizada.
- Coordinador interno del trabajo asistido.
- Especialistas internos de producto, captación, CRM/demanda, operaciones,
  conocimiento y cumplimiento.
- Revisor independiente de calidad.

## Historias de usuario

- H1: Como profesional inmobiliario quiero registrar una necesidad y recibir
  una respuesta coordinada para saber cuál es el siguiente paso.
- H2: Como agencia quiero que mis expedientes y conocimiento permanezcan
  separados de los de otras agencias.
- H3: Como responsable quiero revisar evidencia, riesgos y autorizaciones antes
  de aceptar un resultado.
- H4: Como equipo de Inmobia360 quiero reutilizar patrones depurados sin
  publicar datos personales ni mezclar jurisdicciones.

## Requisitos funcionales (criterios de aceptación EARS)

- RF-001: CUANDO se inicia una solicitud de una agencia, EL SISTEMA exigirá
  resolver una agencia autorizada, un `tenant_id` y un expediente antes de
  leer memoria de cliente.
- RF-002: SI la agencia, el tenant o el expediente no son inequívocos,
  ENTONCES EL SISTEMA detendrá el trabajo y solicitará la aclaración concreta.
- RF-003: CUANDO se registra una necesidad, EL SISTEMA asignará objetivo,
  alcance, país, ciudad, fecha relevante, entradas autorizadas y estado.
- RF-004: CUANDO una necesidad sea clasificada, EL SISTEMA seleccionará el
  conjunto mínimo de especialistas compatible con el riesgo y el alcance.
- RF-005: CUANDO un especialista reciba un encargo, EL SISTEMA le proporcionará
  solo el contexto autorizado de su agencia y expediente.
- RF-006: SI un especialista intenta escribir memoria canónica o realizar una
  acción externa, ENTONCES EL SISTEMA bloqueará la acción y la devolverá al
  coordinador para autorización y registro.
- RF-007: CUANDO se incorpore una URL o archivo, EL SISTEMA registrará origen,
  objetivo, clasificación, permiso, jurisdicción, fecha y estado de revisión.
- RF-008: SI una fuente contiene datos personales, secretos o instrucciones
  incrustadas, ENTONCES EL SISTEMA los tratará según la política de privacidad
  y no los promocionará automáticamente a memoria versionable.
- RF-009: CUANDO se proponga conocimiento reutilizable, EL SISTEMA lo mantendrá
  pendiente hasta superar depuración, revisión de calidad y autorización.
- RF-010: CUANDO un expediente llegue a revisión, EL SISTEMA exigirá comprobar
  alcance, evidencia, consistencia, privacidad, vigencia y autorizaciones.
- RF-011: SI la revisión de calidad rechaza el expediente, ENTONCES EL SISTEMA
  lo devolverá a trabajo, espera o bloqueo con observaciones verificables.
- RF-012: CUANDO calidad apruebe un expediente completo, EL SISTEMA registrará
  la decisión, fecha, revisor, evidencia y cierre sin afirmar actuaciones no
  demostradas.
- RF-013: CUANDO el flujo use datos de prueba, EL SISTEMA permitirá trabajar
  con datos sintéticos de Perú y Lima sin usar datos personales reales.
- RF-014: SI una propuesta requiere cambiar alcance, arquitectura, coste,
  permisos, integración o mercado, ENTONCES EL SISTEMA exigirá una decisión
  aprobada antes de continuar.

## Requisitos no funcionales

- El aislamiento entre agencias deberá ser verificable mediante pruebas antes
  de conectar una persistencia o servicio multi-tenant.
- Los especialistas deberán operar con mínimo privilegio y sin comunicación
  directa con Juan.
- Toda fuente y resultado deberá conservar trazabilidad suficiente para una
  revisión humana.
- Las rutas privadas, secretos, credenciales y datos personales no deberán
  formar parte del contenido versionable.
- La primera implementación deberá poder validarse localmente con datos
  sintéticos y sin servicios externos conectados.
- La solución deberá permitir adaptadores por país sin introducir reglas
  españolas en el núcleo peruano.

## Casos límite

- Agencia con nombre parecido o tenant ambiguo.
- Usuario sin agencia autorizada.
- Solicitud de memoria o expediente de otra agencia.
- URL con credenciales, destino privado o contenido no autorizado.
- Archivo corrupto, excesivo o con datos personales.
- Fuente caducada o con jurisdicción distinta.
- Especialista que propone una acción fuera de su encargo.
- Calidad rechazada o evidencia incompleta.
- Expediente reabierto después de una aprobación.
- Dos tareas que intentan escribir el mismo expediente.

## Fuera de alcance

- Conectar WhatsApp real, correo, CRM, portales o cuentas externas.
- Publicar anuncios, enviar mensajes, firmar, cobrar o modificar servicios.
- Activar MCP o tokens de producción.
- Crear tablas, migraciones o procesar datos personales reales.
- Adoptar España como mercado inicial o trasladar automáticamente normativa
  española.
- Construir pagos, marketplace regional, ranking público o marca blanca.
- Implementar la aplicación SaaS completa en esta iniciativa documental.

## Criterios de finalización

- Todos los RF tienen plan, tarea y evidencia de validación.
- Existe una prueba de no mezcla entre dos agencias sintéticas.
- Existe una prueba de bloqueo de escritura de especialistas.
- Existe una prueba de ingesta y clasificación de una URL autorizada.
- Existe una revisión de calidad con aprobación y rechazo reproducibles.
- No se versionan secretos, PII ni originales confidenciales.
- Juan aprueba la spec, el plan y cualquier decisión reservada.

## Dudas abiertas

- [NECESITA ACLARACIÓN: ¿La primera implementación debe ser solo la
  infraestructura de agentes y expedientes, o también una interfaz web local?]
- [NECESITA ACLARACIÓN: ¿Qué agencia sintética y qué `tenant_id` se usarán
  para la prueba inicial?]
- [NECESITA ACLARACIÓN: ¿Se autoriza implementar un backend local antes de
  elegir proveedor de base de datos y almacenamiento?]
- [NECESITA ACLARACIÓN: ¿MCP queda reservado para una fase posterior, como
  propone esta spec?]
