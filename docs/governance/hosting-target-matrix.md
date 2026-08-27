# Matriz de destino de alojamiento

Estado: preparación. No autoriza conexión, compra ni despliegue en Hostinger.

## Inventario conocido

| Recurso | Identificador | Relación con Inmobia360 LATAM | Estado |
|---|---|---|---|
| VPS Hostinger KVM 2 | Identificador privado no versionado | Candidato para aplicación/API | No evaluado ni configurado |
| Dominio | `inmobia360.com` | Dominio principal del proyecto | Disponible según información de Juan |
| Email trial | `compracaptacion.com` | Fuera del alcance actual | No utilizar |

## Mapa previsto

| Superficie | Dominio | Destino técnico previsto | Confirmación necesaria |
|---|---|---|---|
| Landing institucional | `inmobia360.com` | WordPress + Bricks | Plan WordPress/hosting y método de publicación |
| Landing Perú | `inmobia360.com/pe/` | Misma instalación WordPress | Estructura de URLs, SEO y formularios |
| Aplicación | `app.inmobia360.com` | Next.js separado | Hosting Node.js/VPS y variables de entorno |
| Demo | `demo.inmobia360.com` | Entorno aislado de la aplicación | Aislamiento, acceso y datos sintéticos |
| Ayuda | `ayuda.inmobia360.com` | Sistema documental futuro | Herramienta y necesidad real |
| API/base de datos | Por definir | Servicio separado | Arquitectura, seguridad, copias y costes |

## Información requerida antes de configurar

- Plan de Hostinger contratado y producto disponible.
- Cuenta o proyecto de destino, sin incluir credenciales en el repositorio.
- Control actual del dominio y DNS.
- Servicio previsto para WordPress.
- Servicio previsto para Next.js, API y base de datos.
- Política de copias, restauración, monitorización y rollback.
- Presupuesto mensual aprobado.

## Hipótesis técnica pendiente

El KVM 2 podría alojar componentes técnicos separados de WordPress, como la aplicación Next.js, API o servicios auxiliares. Esto requiere comprobar capacidad, sistema operativo, seguridad, backups, costes y método de despliegue antes de aprobarlo.

## Puerta de autorización

No se conectará Hostinger hasta que exista una decisión explícita sobre el destino técnico, el coste, los permisos necesarios y el procedimiento de reversión. No se realizarán compras ni cambios DNS como parte de esta preparación.

