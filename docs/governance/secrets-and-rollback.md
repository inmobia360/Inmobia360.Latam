# Secretos, seguridad y rollback

Estado: controles de preparación. No contiene secretos reales.

## Secretos

- Mantener secretos fuera del repositorio, incluidos repositorios públicos.
- Usar variables protegidas del sistema de CI/CD y del proveedor de ejecución.
- Separar secretos por entorno.
- Aplicar mínimo privilegio y rotación documentada.
- Revocar inmediatamente cualquier secreto expuesto.

## Rollback mínimo

Antes de cada publicación se debe conservar:

- commit exacto desplegado;
- copia verificable de la configuración no secreta;
- copia de seguridad cuando exista base de datos o contenido mutable;
- procedimiento probado para volver a la versión anterior;
- responsable y criterio de decisión.

## Bloqueos actuales

- No hay aplicación ni infraestructura implementada.
- No hay credenciales de despliegue configuradas.
- No se ha confirmado el producto Hostinger que alojará cada superficie.
- No se autoriza todavía ninguna compra, conexión externa o despliegue.
