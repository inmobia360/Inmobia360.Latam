# Inmobia360 LATAM — Instrucciones del proyecto

## Identidad y responsabilidad

- Identidad responsable: Inmobia-360.
- Propietario y responsable final: Juan.

## Estado de la migración

Esta carpeta contiene una copia documental inicial de la base de conocimiento disponible en el chat compartido de Inmobia360 LATAM. El contenido no debe interpretarse como una especificación completa: los apartados sin evidencia están marcados como pendientes.

## Reglas

1. Leer este archivo y `docs/00-INDEX.md` antes de actuar.
2. Consultar `docs/CURRENT-STATE.md` y los registros de decisiones y riesgos.
3. No inventar datos de mercado, precios, entrevistas, resultados, arquitectura implementada ni decisiones aprobadas.
4. Separar hechos, hipótesis, estimaciones y recomendaciones.
5. No modificar el alcance, mercado inicial, presupuesto, precios o estrategia sin aprobación explícita.
6. No sobrescribir archivos existentes; ante conflicto, detenerse y documentarlo.
7. No programar ni instalar dependencias salvo autorización explícita.
8. No guardar credenciales, tokens, datos personales, direcciones protegidas ni infraestructura privada.
9. No desplegar ni cambiar permisos externos sin autorización.
10. Actualizar la documentación afectada cuando una decisión sea aprobada.

## Ámbito conocido

- Proyecto: Inmobia360 LATAM.
- Mercado inicial: Perú.
- Ciudad piloto: Lima.
- Objetivo: crear una plataforma SaaS inmobiliaria escalable para Latinoamérica.
- MVP aprobado: captación y centralización de leads; calificación de compradores y propietarios; seguimiento comercial; gestión básica de propiedades y demandas; matching básico; WhatsApp como canal prioritario para Perú.
- Arquitectura aprobada: webs comerciales en WordPress + Bricks; aplicación SaaS Next.js separada; dominios definidos en `docs/governance/project-charter.md`.
- Fuera de alcance inicial: pagos reales, expansión a otros países, MLS regional, automatizaciones avanzadas, integraciones costosas y datos personales reales.
