# Mapa de estructura del proyecto

Estado: estructura base verificada. No implica que los componentes estén implementados.

## Directorios principales

| Ruta | Responsabilidad prevista | Estado |
|---|---|---|
| `docs/` | Conocimiento, producto y gobierno | Activo |
| `.agents/skills/` | Skills locales y soporte interno | Skill directora activa; especialistas pendientes |
| `.codex/` | Registros y configuración documental de Codex | Activo, sin secretos |
| `app/` | Futura aplicación SaaS Next.js | Reservado |
| `wordpress/` | Futura web comercial WordPress + Bricks | Reservado |
| `database/` | Futuro esquema, migraciones y documentación de datos | Reservado |
| `tests/` | Futuras pruebas automatizadas y criterios verificables | Reservado |

## Reglas de crecimiento

- No crear archivos de implementación hasta aprobar el diseño correspondiente.
- Mantener aplicación, WordPress, base de datos y pruebas separados.
- No almacenar credenciales, datos personales reales ni artefactos de producción.
- Cada nuevo directorio debe tener una responsabilidad concreta y documentada.
- Las decisiones que afecten la estructura se registrarán antes de ejecutarse.

## Estado actual

La estructura base está preparada para documentación, futura aplicación SaaS, web comercial, base de datos y pruebas. Los componentes técnicos todavía no están programados ni desplegados.

