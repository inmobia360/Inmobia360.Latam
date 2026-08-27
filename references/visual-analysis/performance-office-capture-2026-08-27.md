# Inventario funcional anonimizado — Performance Office

Fecha de captura: 2026-08-27
Fuente observada: portal de rendimiento de oficina accesible mediante URL proporcionada por Juan.
Uso: referencia interna de flujos y arquitectura funcional. No copiar marcas, nombres, textos, activos ni datos de la fuente.

## Estructura principal observada

- Dashboard
- Informe de rendimiento
- Performance de oficina
- Oficina
- Accountability
- Agentes
- Consulta de facturas
- Ventas e ingresos
- Informes
- Plataforma de e-learning
- Site corporativo
- Soporte
- Intranet de propiedades
- Finanzas e hipotecas
- Servicio de gestión inmobiliaria
- Correo

## Subcategorías observadas

### Informe de rendimiento

- Rendimiento de la oficina
- Agentes de la oficina
- Agentes rookies de la oficina
- Equipos de la oficina
- Gráfico parcial o acumulado

### Performance de oficina

- Oficina anual
- Oficina mensual
- Captaciones
- Volumen de negocio
- Equipo

### Accountability

- Presupuestos

### Agentes

- Alta de agente
- Ficha de asociados
- Baja de agente
- Validar agentes
- Detalle de equipos
- Administración de equipos

### Consulta de facturas

- Facturas CDC

### Ventas e ingresos

- Cierre de operaciones
- Cierre del mes
- Consulta de liquidaciones

### Informes

- Evolución del agente
- Rankings
- Roster

### Ventas

- Acceso independiente observado en navegación lateral.

## Patrones funcionales reutilizables para Inmobia360

- Dashboard con entrada rápida a áreas operativas.
- Separación entre visión de oficina, visión de agente, equipos y evolución temporal.
- Filtros o selector de contexto organizativo en cabecera.
- Métricas comparables por año, mes, parcial y acumulado.
- Seguimiento de captaciones, volumen de negocio, cierres e ingresos.
- Gestión del ciclo de agentes: alta, ficha, validación, equipos y baja.
- Informes y rankings como herramientas de seguimiento, con especial cuidado de privacidad y posibles sesgos.
- Módulos auxiliares separados: formación, soporte, propiedades, finanzas y correo.

## Traducción a Inmobia360

- Dashboard del agente: siguiente acción, campañas, leads, propiedades, actividades y productividad.
- Dashboard de agencia: visión agregada por equipo, periodo, canal y objetivo.
- Métricas de campañas: piezas creadas, tiempo de preparación, exportaciones, leads asociados y acciones posteriores.
- Comparativas temporales: mensual, anual, parcial y acumulada.
- Perfil central: agente, agencia, equipo, permisos y datos de contacto autorizados.
- Flujo de incorporación: alta, perfil incompleto, validación y activación.
- Informes: evolución individual y de equipo; cualquier ranking requerirá metodología, privacidad y aprobación específica.
- Integración futura con `mk.inmobia360.com`: campañas → actividad → lead → seguimiento → resultado.

## Requisitos de productividad

Cada panel deberá responder a una decisión o acción del agente y evitar métricas decorativas. Debe mostrar qué hacer después, qué tareas están pendientes, qué campañas necesitan adaptación y qué resultados requieren seguimiento.

## Límites

- No se recogieron ni conservaron credenciales, claves, datos personales de agentes ni cifras privadas.
- Los identificadores de oficina observados se excluyen de esta documentación.
- La fuente no autoriza copiar la aplicación ni replicar su marca.
- La activación de rankings, facturación, presupuestos o funcionalidades reguladas requiere revisión legal, de privacidad, seguridad y producto.

## Procedimiento futuro de replicación en Inmobia360

Cuando se autorice la construcción, `latam-real-estate` seguirá este orden:

1. **Definir el objetivo operativo**: concretar qué problemas del broker, oficina, equipo y agente se quieren resolver y qué decisiones debe facilitar el dashboard.
2. **Definir roles y contexto**: broker, responsable de agencia, coordinador, agente y administrador; establecer el alcance de oficina, agencia, equipo y periodo.
3. **Convertir el inventario en requisitos propios**: usar la estructura observada como referencia abstracta, nunca copiar marca, textos, activos ni diseño identificable.
4. **Diseñar el modelo de datos**: relacionar agentes, perfiles, oficinas, equipos, propiedades, leads, campañas, actividades, operaciones, cierres, ingresos, objetivos, periodos e informes.
5. **Diseñar permisos y privacidad**: definir qué puede ver y hacer cada rol, aislamiento entre oficinas y tratamiento de datos personales, financieros y comparativos.
6. **Diseñar el dashboard de acciones**: priorizar siguiente acción, tareas pendientes, bloqueos, leads, campañas, propiedades y resultados; evitar métricas sin uso operativo.
7. **Diseñar las vistas de análisis**: rendimiento individual, equipo y oficina; periodos mensual, anual, parcial y acumulado; captaciones, operaciones, ingresos y evolución.
8. **Conectar productividad y marketing**: enlazar campañas de `mk.inmobia360.com` con actividades, leads, propiedades, seguimientos y resultados.
9. **Definir métricas y fórmulas**: documentar fuentes, filtros, fechas de corte, estados, agregaciones y reglas; no inventar valores ni rankings.
10. **Diseñar estados y excepciones**: cero datos, datos incompletos, permisos insuficientes, oficina sin equipo, periodos cerrados y errores de sincronización.
11. **Diseñar UX y responsive**: interfaz original Inmobia360, mobile-first, accesible y orientada a lectura rápida y acción.
12. **Prototipar con datos sintéticos**: validar flujos y cálculos sin credenciales ni datos reales.
13. **Revisión independiente**: producto valida alcance; arquitectura valida integración; datos valida consistencia; legal/privacidad valida exposición; seguridad/calidad valida aislamiento y pruebas.
14. **Validación con usuarios autorizados**: comprobar comprensión, utilidad y reducción de trabajo antes de activar producción.
15. **Preparar despliegue reversible**: staging, observabilidad, control de cambios, rollback y aprobación expresa de Juan antes de producción.

### Resultado esperado

La réplica no será una copia visual de la fuente. Será una infraestructura propia de gestión de brokers y oficinas que conserve los patrones funcionales útiles y los convierta en acciones concretas para aumentar productividad.
