# Política de Git y releases

Estado: propuesta de preparación.

## Repositorio

- Repositorio canónico: `https://github.com/inmobia360/Inmobia360.Latam`.
- `main`: cambios aprobados y candidatos a producción.
- Ramas de trabajo: cambios aislados y revisables.
- No se deben incluir credenciales, tokens, dumps de bases de datos ni datos personales.

## Flujo recomendado

1. Crear una rama de trabajo descriptiva.
2. Actualizar documentación o código con alcance limitado.
3. Ejecutar validaciones automáticas y revisión de seguridad.
4. Abrir una revisión hacia `main`.
5. Fusionar solo tras cumplir los criterios de aceptación.
6. Registrar decisiones, riesgos y resultado del despliegue.

## Releases

Cada release deberá indicar alcance, commit, entorno, validaciones, aprobador, riesgos conocidos y procedimiento de rollback. Todavía no se ha definido una herramienta ni una convención de versionado definitiva.

