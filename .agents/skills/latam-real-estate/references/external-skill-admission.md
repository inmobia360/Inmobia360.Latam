# Admisión de skills externas

Una skill externa no se instala directamente en el proyecto. Primero se evalúa y se registra.

## Gate obligatorio

1. Definir la necesidad funcional y alternativas propias.
2. Consultar skills.sh y ordenar candidatas por descargas.
3. Priorizar fuente oficial o mantenedor verificable, sin confundir popularidad con seguridad.
4. Obtener la ficha, árbol completo y commit/hash de la fuente.
5. Leer `SKILL.md`, scripts, referencias y archivos auxiliares.
6. Revisar auditorías disponibles: cualquier `fail`, riesgo alto/crítico o `warn` no resuelto bloquea la admisión.
7. Revisar comandos, descargas dinámicas, red, credenciales, telemetría, escritura de archivos y acciones destructivas.
8. Probar en entorno aislado, sin credenciales, datos reales, producción ni red innecesaria.
9. Registrar procedencia, hash, auditorías, revisión de archivos, alcance permitido, riesgos y resultado en `.codex/vendor-lock.yaml`.
10. Obtener aprobación explícita de Juan.
11. Copiar solo la versión aprobada a `.agents/skills/vendor-reviewed/` o construir una alternativa propia.

## Regla de sustitución

Si la función es necesaria pero el contexto, scripts, permisos o procedencia no son suficientemente seguros, no se instala. Se construye una versión interna mínima, revisable y limitada al proyecto.

## Revisión continua

Revisar una skill externa cuando cambie el commit, sus archivos, su alcance o sus dependencias. Una auditoría positiva no elimina la obligación de revisión local.

