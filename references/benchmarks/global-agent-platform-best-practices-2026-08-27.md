# Benchmark funcional anonimizado — plataforma global para agentes

Fecha: 2026-08-27
Uso: extraer buenas prácticas de producto y arquitectura para Inmobia360. No copiar marca, textos, nombres, imágenes, diseño ni activos.

## Arquitectura de navegación observada

- Dashboard.
- Apps & Tools.
- Find & Refer.
- Resources.
- New Chat y búsqueda/historial de chats.
- Menú de cuenta.
- Acceso a un sistema legado separado.

## Dashboard y asistente

- Asistente conversacional como punto de entrada.
- Mensaje de bienvenida y orientación a crecimiento/productividad.
- Aviso visible de que la IA puede equivocarse.
- Acciones sugeridas para acelerar tareas frecuentes.
- Acciones observadas: descripción de inmueble, ideas para redes, referidos, branding y acceso a grupos/aplicaciones.

## Catálogo de aplicaciones

- Vista “All” y “Favorites”.
- Filtro por categoría.
- Orden alfabético.
- Fichas con nombre, propósito y acceso.
- Aplicaciones para portal de oficina, soporte, referidos, recursos, SSO, formación, engagement, reclutamiento, marketing, premios, comercio, noticias, URL/QR, hub de agentes, vídeo/social y videoconferencia.

## Find & Refer

- Pestañas Affiliates, Offices y Favorites.
- Filtros por ubicación y búsqueda por nombre o email.
- Filtros avanzados.
- Tabla de resultados con perfil, ubicación, experiencia, especialidad y acción de referir.
- Favoritos por persona.
- Paginación y contador de resultados.
- Perfiles individuales y acción de referral separadas.

## Resources

- Pestañas Announcements y Content Hubs.
- Noticias y actualizaciones.
- Eventos virtuales y presenciales.
- Artículos con fecha, resumen, llamada a la acción y enlace externo.
- Hub específico de recursos para agentes y brokers.

## Buenas prácticas aplicables

- Un único punto de entrada para operaciones, herramientas, recursos y asistencia.
- Asistente guiado con límites y aviso de incertidumbre.
- Acciones rápidas basadas en tareas reales.
- Catálogo de herramientas con propósito antes de abrirlas.
- Favoritos y búsqueda para reducir fricción.
- Directorio con filtros y acción contextual.
- Separación entre perfil, referir y favoritos.
- Recursos con fecha, resumen y siguiente acción.
- Compatibilidad con sistemas heredados sin mezclar su navegación con el núcleo nuevo.
- SSO como principio de reducción de duplicidad.

## Traducción a Inmobia360

- Dashboard del agente: siguiente acción, leads, campañas, propiedades, actividades y productividad.
- Apps y herramientas: catálogo con permisos, datos tratados, responsable, estado y soporte.
- Red Profesional: búsqueda de agentes, oficinas y partners; referidos con consentimiento y trazabilidad.
- Centro de recursos: anuncios, formación, guías, políticas y hubs por audiencia.
- Asistente: ayuda para campañas, descripciones, seguimiento y decisiones; siempre revisable.
- Favoritos, historial, búsqueda y filtros como funciones transversales.

## Límites y decisiones pendientes

- No replicar rankings, referrals, asistentes, SSO o integraciones sin definir privacidad, roles, metodología y responsabilidades.
- No usar datos reales de personas para pruebas.
- Las métricas, costes, proveedores, integraciones y reglas legales deben validarse por separado.

## Catálogo de Apps & Tools verificado

- Portal de oficina: pagos y gestión de oficina.
- Soporte: tickets y servicios de producto.
- Referidos globales.
- Recursos globales.
- SSO para herramientas y aplicaciones.
- Portal de ideas de producto.
- Aprendizaje y educación.
- Engagement y contenido social.
- Reclutamiento, coaching y reconocimiento.
- Referidos locales y globales.
- Servicios hipotecarios.
- Plantillas y creación rápida de contenido.
- Premios y reconocimientos.
- Recursos para brokers comerciales.
- Marketplace de proveedores aprobados.
- Noticias.
- Acortador de URL, códigos QR y analítica de vistas.
- Hub de marca, logos y plantillas.
- Vídeo, infografías y contenido social.
- Videoconferencia.

## Patrón de plataforma trasladable

El catálogo no debe ser una lista de enlaces. Cada herramienta de Inmobia360 debería tener: nombre, propósito, audiencia, problema que resuelve, permisos, datos tratados, propietario, estado, soporte, dependencia, última revisión y siguiente acción. Las integraciones deben abrirse mediante identidad compartida cuando sea posible y mantener una estrategia de salida.

## Cobertura de investigación

### Verificado en esta investigación

- Dashboard y asistente de entrada.
- Apps & Tools en vista All.
- Controles de favoritos, categorías, búsqueda y ordenación identificados.
- Find & Refer en vista Affiliates.
- Filtros por ubicación, nombre/email y filtros avanzados identificados.
- Paginación, favoritos, perfiles y acción Refer identificados.
- Resources en vista Announcements.
- Pestaña Content Hubs identificada.
- Navegación principal, historial de chats, cuenta, privacidad y acceso legado.

### Pendiente de verificación directa

- Contenido resultante de Apps & Tools > Favorites.
- Valores y categorías concretas de All Categories.
- Contenido completo de Find & Refer > Offices y Favorites.
- Comportamiento y campos de Advanced Filters.
- Contenido completo de Resources > Content Hubs.
- Menú de cuenta y acciones internas del asistente.
- Estados de error, ausencia de resultados y filtros combinados.

No se considera exhaustivo el contenido de estas superficies pendientes. La arquitectura y las buenas prácticas documentadas se basan solo en estados observados directamente.

## Verificaciones adicionales

- Apps & Tools > Favorites muestra un estado vacío explícito cuando no hay favoritos.
- Find & Refer > Offices muestra resultados por oficina con ubicación, número de afiliados, especialidad y acción Contact.
- El directorio de oficinas ofrece paginación y contador de resultados.
- Find & Refer > Advanced Filters expone Language, Specialty, Subspecialty, Years of Experience y Must have photo, además de CLEAR.
- Resources > Content Hubs agrupa bibliotecas por región y especialidad, incluyendo recursos de agentes/brokers, recursos globales, comercial, reclutamiento y noticias.

Estos estados refuerzan para Inmobia360 la necesidad de diseñar estados vacíos útiles, filtros combinables, paginación, contadores, clasificación por región/especialidad y acciones contextuales (referir, contactar, abrir recurso).
