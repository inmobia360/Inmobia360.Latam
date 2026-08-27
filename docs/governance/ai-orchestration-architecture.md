# Arquitectura de orquestación de IA

Estado: propuesta aprobada para diseño. No autoriza instalaciones ni conexiones.

## Propósito

El VPS Hostinger KVM 2 se evaluará como capa técnica para gestionar acciones de IA, automatizaciones, agentes internos y tareas programadas del proyecto. No se presupone que el VPS aloje directamente un modelo grande.

## Flujo conceptual

```text
WordPress / aplicación / canales autorizados
                    ↓
              API segura de Inmobia360
                    ↓
          Orquestador de IA en el VPS
                    ↓
             Modelo de IA en la nube
                    ↓
      respuesta, tarea, alerta o actualización
```

## Responsabilidades del VPS

- Orquestación de agentes y subagentes.
- Colas y ejecución de tareas.
- Automatizaciones autorizadas.
- Registro de acciones y resultados.
- Controles de aprobación humana.
- Límites de coste, frecuencia y permisos.
- Integración segura con la aplicación y servicios aprobados.

## Límites iniciales

- No instalar todavía modelos, runtimes ni automatizadores.
- No ejecutar acciones irreversibles sin aprobación humana.
- No almacenar secretos en el repositorio.
- No procesar datos personales reales durante la fase de diseño.
- No exponer una API pública hasta definir autenticación, autorización, TLS, firewall y auditoría.

## Decisiones pendientes

- Proveedor y modelo cloud.
- Recursos reales del KVM 2: CPU, RAM, almacenamiento y sistema operativo.
- Acciones permitidas y acciones que siempre requieren aprobación de Juan.
- Política de datos, retención y anonimización.
- Presupuesto y límites de consumo.
- Estrategia de backups, monitorización y rollback.

