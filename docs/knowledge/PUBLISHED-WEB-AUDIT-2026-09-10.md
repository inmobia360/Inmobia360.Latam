# Auditoría de la web publicada — 2026-09-10

Estado: referencia publicada autorizada para orientar futuras iniciativas;
no equivale por sí sola a una decisión de producto, una prueba de resultados
ni evidencia de que el código esté en este repositorio.

URL revisada: `https://inmobia360.com/`.

## Resumen ejecutivo

La web pública presenta una experiencia B2B inmobiliaria denominada
“RealEstate Connect” / “Habita B2B Real Estate Tech”, con una landing comercial
y un panel SaaS accesible desde `/app/dashboard/`. La experiencia publicada se
orienta actualmente a España y Canarias, mientras que la dirección aprobada de
Inmobia360 LATAM comienza en Perú y Lima.

Conclusión: la web es una referencia válida de experiencia, superficies y
capacidades que Juan quiere utilizar para futuros cambios, pero no está
sincronizada funcionalmente con el contenido del repositorio. El repositorio
actual documenta el proyecto y no contiene la implementación de esta web.

## Elementos observados en la landing

- Posicionamiento: plataforma SaaS B2B inmobiliaria con inteligencia artificial.
- Público visible: agencias y brokers de Madrid, Barcelona, Valencia, Sevilla
  y Canarias.
- Generación de fichas en múltiples formatos para portales, redes, WhatsApp,
  PDF y vídeo.
- Cálculo de Cap Rate, ROI neto y flujo de caja.
- Lead scoring predictivo y recomendación de tiempo de contacto.
- Landings públicas de propiedades y códigos QR.
- Flujo comercial mostrado: captación, ficha técnica, distribución multicanal,
  scoring de leads y cierre.
- Calculadora de ahorro operativo.
- Planes visibles: Starter 29 €/mes, Pro Agency 79 €/mes y Enterprise
  199 €/mes, con funciones distintas por plan.
- Preguntas frecuentes sobre IA, métricas financieras, marca, lead scoring y
  compatibilidad con plataformas de publicación.

## Elementos observados en el panel

- Panel general con propiedades publicadas, borradores, leads recibidos,
  leads prioritarios, impactos y visitas.
- Acciones rápidas para crear propiedad, usar el generador IA y revisar leads.
- Leads con ubicación, presupuesto, plazo, puntuación y próxima acción.
- Recomendaciones de contacto telefónico o WhatsApp.
- Cartera de propiedades con estado comercial, precio, superficie,
  habitaciones, baños y métricas de interacción.
- Navegación visible para propiedades/mapa, captación/scoring, generador
  multicanal y configuración/marca.
- Selector de idioma español/inglés.

## Datos y claims que no deben tratarse como hechos aprobados

Los precios, porcentajes de ahorro, volumen de inmuebles, valoraciones,
volumen de activos, testimonios, resultados de cierres, disponibilidad 24/7,
SLA 99.9 %, scoring predictivo y cualquier afirmación de precisión bancaria
requieren validación comercial, legal y técnica antes de incorporarse al
producto o a la documentación normativa.

Los teléfonos, correos, nombres, imágenes y propiedades visibles parecen datos
de demostración o placeholders. No deben reutilizarse como datos reales ni
incorporarse al repositorio como información operativa.

## Discrepancias frente al proyecto aprobado

| Tema | Web publicada | Proyecto aprobado |
|---|---|---|
| Mercado visible | España y Canarias | Perú |
| Piloto | Madrid y otras ciudades españolas | Lima |
| Moneda visible | Euro | Pendiente de definición comercial |
| Canal | WhatsApp, portales y redes | WhatsApp prioritario en Perú; integraciones pendientes |
| Estado técnico | Presenta landing y panel SaaS | App, WordPress y base de datos aún no implementados en este repositorio |
| Precios | Publica tres planes | Precios y margen pendientes |
| IA | Presenta generación, scoring y finanzas | Proveedor, permisos, coste e implementación pendientes |

Estas diferencias no se resuelven automáticamente. Cualquier adopción para
Perú debe pasar por una spec SDD y por la aprobación correspondiente.

## Uso autorizado como referencia

La web se utilizará como referencia para:

1. inventariar capacidades y superficies que Juan quiere considerar;
2. analizar la experiencia de landing, panel y flujo comercial;
3. identificar contenidos que necesitan localización para Perú;
4. preparar specs SDD de funcionalidades concretas;
5. comparar futuras implementaciones con la experiencia publicada.

No autoriza por sí sola:

- cambiar Perú por España como mercado inicial;
- aprobar precios, métricas, claims o testimonios;
- activar IA, scoring predictivo, pagos o integraciones;
- usar datos personales o de demostración como datos reales;
- afirmar que el código publicado está dentro de GitHub;
- desplegar cambios en la web.

## Siguiente paso recomendado

Crear una primera spec SDD de “experiencia base de la plataforma publicada”,
separando el núcleo funcional reutilizable de la localización para Perú,
los claims comerciales y las capacidades todavía fuera de alcance. La spec
deberá decidir qué partes se incorporan al MVP y cuáles permanecen como
evolución.
