# Matriz de entornos

Estado: propuesta de preparación.

| Entorno | Propósito | Datos permitidos | Publicación | Estado |
|---|---|---|---|---|
| Local | Desarrollo y documentación | Datos sintéticos | No pública | Disponible |
| Preview | Revisión de cambios | Datos sintéticos | Acceso restringido | Pendiente |
| Demo | Demostración pública controlada | Datos sintéticos | Pública y aislada | Pendiente |
| Producción | Operación aprobada | Solo tras validación de privacidad | Pública | Pendiente |

## Reglas de promoción

1. Un cambio debe revisarse antes de llegar a `main`.
2. Las validaciones deben completarse antes de publicar.
3. La promoción a producción requiere aprobación explícita de Juan.
4. Todo despliegue debe tener una reversión documentada.
5. No se usarán datos personales reales durante el MVP documental o de demostración.

