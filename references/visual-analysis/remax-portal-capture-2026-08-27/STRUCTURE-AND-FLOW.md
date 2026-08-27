# Inventario visual y funcional anonimizado

Fecha de captura: 2026-08-27
Fuente: portal observado en `https://remax.smbiotica.net/agente`
Uso: referencia interna de arquitectura funcional y patrones; no reutilizar marcas, logos, textos, imágenes ni activos de terceros.

## Superficie observada

- Portal de agente con navegación lateral.
- Cabecera con búsqueda, modo oscuro, carrito, notificaciones, asistente/IA y configuración.
- Área principal con título de sección, pestañas de categoría, acordeones, biblioteca de piezas y favoritos.
- Pie con copyright del proveedor observado.

## Navegación

- Creatividades
- Newsletter: Noticias, Ediciones
- Propiedades: Inmuebles, Email
- Formación: Formación, 12 pasos, Descargas, Equipo
- Calendario: Hoy, Mes, Semana, Día
- Favoritos
- IA: Dashboard de IA, Mi clave personal
- Datos de perfil
- Historial del carrito

## Categorías de biblioteca

### Corporativo

- Papelería: Tarjetas, Carpetas, Sobres, Hojas
- Carteles de venta
- Carteles de alquiler
- Carteles disponibles
- Carteles para escaparate
- Guías para vender, comprar, home staging y reclutar

### Posicionamiento

- Campañas de compradores online y offline
- Campañas de vendedores online y offline
- Campañas de reclutamiento online y offline
- Campañas online y offline de valoración

### Prospección

- Flyers de vendedores
- Flyers de reclutamiento
- Flyers de reclutamiento online
- Flyers de compradores
- Flyers de compradores online
- Dosieres de propiedades

### Colección o línea premium

- Corporativo
- Tarjetas
- Dosieres o guías
- Flyers
- Book de captación
- Carteles

## Patrón de campaña

1. Seleccionar categoría.
2. Abrir grupo de campaña.
3. Elegir versión textual o visual.
4. Consultar la previsualización.
5. Marcar como favorito o continuar con el producto.

## Arquitectura trasladable a Inmobia360

- `app.inmobia360.com`: autenticación, perfil, permisos y datos centrales del agente.
- `mk.inmobia360.com`: biblioteca, campañas, plantillas, personalización, previsualización, favoritos y exportación.
- Perfil reutilizable: nombre profesional, foto, logo, agencia, teléfono profesional, WhatsApp, email, web, redes y zona.
- Variables de perfil activables por pieza.
- Plantillas bloqueadas para elementos corporativos y editables para contenido comercial.
- Separación entre online/offline y entre objetivo, audiencia y canal.

## Criterio de producto y roadmap

La referencia visual no se trasladará como una copia de navegación. Se reinterpretará desde el objetivo aprobado de Inmobia360: reducir puntos de dolor del agente y aumentar su productividad.

### Puntos de dolor que debe resolver

- No saber qué campaña elegir para cada objetivo.
- Perder tiempo adaptando una misma pieza a varios canales.
- Repetir manualmente los datos de contacto del agente.
- Usar materiales desactualizados o inconsistentes.
- No poder encontrar rápidamente campañas anteriores.
- No tener claro cuál es la siguiente acción comercial.
- Separar campañas, propiedades, leads y seguimiento en herramientas distintas.

### Mejoras de productividad esperadas

- Asistente que recomiende objetivo, audiencia, canal y plantilla.
- Perfil único reutilizado automáticamente en los materiales.
- Adaptación multiformato desde una campaña base.
- Biblioteca con búsqueda, filtros, favoritos y recientes.
- Integración progresiva con propiedades, leads y actividades del espacio privado.
- Calendario de acciones y recordatorios comerciales.
- Previsualización y checklist antes de exportar.
- Registro de qué campaña se creó, para qué objetivo y con qué resultado.

### Exportación offline

- Toda pieza offline deberá exportarse como imagen y como PDF.
- Perfil “oficina local”: archivo sencillo, legible y compatible con impresoras habituales, con tamaño, orientación, resolución y márgenes definidos.
- Perfil “taller de imprenta”: PDF preparado para producción profesional, con tamaño final, sangrado y márgenes de seguridad cuando corresponda, imágenes a resolución de impresión y tipografías correctamente incorporadas según el flujo técnico aprobado.
- Las especificaciones exactas de color, resolución, sangrado y perfiles PDF deberán validarse con el proveedor de impresión y no se inventarán como estándar universal.

### Exportación digital

- Las campañas online deberán exportarse según las exigencias del canal de destino: redes sociales, email, webs, banners y otros medios de Internet.
- Cada canal tendrá presets versionados de proporción, dimensiones, resolución, formato, peso, compresión, zonas seguras y recorte.
- Se comprobarán legibilidad móvil, contraste, jerarquía, llamada a la acción, accesibilidad y conservación de los datos de contacto autorizados.
- El sistema deberá generar variantes desde una pieza base para reducir trabajo repetitivo del agente.
- Las especificaciones deberán mantenerse actualizables porque los requisitos de las plataformas pueden cambiar.

### Encaje con el roadmap

`mk` debe comenzar como capacidad del espacio privado del agente, dentro del MVP Lima, junto con propiedades, leads, asistente y seguimiento. La Red Profesional, el directorio público, la reputación, la expansión regional y las automatizaciones avanzadas quedan fuera de la primera entrega.

Cada función deberá justificar: punto de dolor resuelto, tiempo o pasos ahorrados, dependencia con el perfil o los datos centrales, métrica candidata y criterio de aceptación. Las métricas numéricas aún requieren aprobación.

## Límites de uso

- Este inventario no autoriza copiar diseños ni activos.
- No usar nombres, logos, slogans, fotografías, tipografías, paletas o composiciones identificables de terceros.
- Las campañas finales deben ser originales y utilizar únicamente la identidad aprobada de Inmobia360.
- No se han recogido credenciales, claves, datos personales ni contenido de clientes.
