# Arquitectura de despliegue

Estado: propuesta de preparación. No autoriza despliegues.

## Superficies previstas

| Superficie | Dirección | Tecnología prevista | Estado |
|---|---|---|---|
| Landing LATAM | `inmobia360.com` | WordPress + Bricks | No implementada |
| Landing Perú | `inmobia360.com/pe/` | WordPress + Bricks | No implementada |
| Aplicación SaaS | `app.inmobia360.com` | Next.js separado | No implementada |
| Demo | `demo.inmobia360.com` | Aplicación aislada | No implementada |
| Ayuda | `ayuda.inmobia360.com` | Futuro sistema documental | Reservada |

## Principios

- `inmobia360.com` se reserva para la presentación institucional del negocio.
- Las landings comerciales regionales se organizan mediante subdirectorios del dominio principal.
- Los subdominios se reservan para aplicaciones, demo, ayuda y servicios globales con una función validada.
- No se crearán subdominios anticipadamente ni se expondrán APIs internas sin una necesidad justificada.
- Marketing y aplicación deben poder desplegarse y revertirse por separado.
- La demo no debe utilizar datos personales reales ni exponer controles internos.
- Los secretos deben residir en el proveedor de CI/CD o en el entorno de ejecución, nunca en Git.
- Cada entorno debe tener credenciales y datos de prueba separados.
- No se elegirá un servicio de Hostinger hasta confirmar el plan contratado y sus capacidades.

## Pendientes de validación

- Plan y modalidad exacta de Hostinger.
- Ubicación de API y base de datos.
- Método de despliegue para WordPress.
- Método de despliegue para Next.js.
- Gestión de DNS, SSL, copias de seguridad y rollback.
- Registro de subdominios, responsables, entornos, datos tratados y controles de seguridad.

