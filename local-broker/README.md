# Broker local

Núcleo local inicial del asistente digital inmobiliario. Esta etapa contiene
solo el dominio de agencias, tenants y expedientes; no conecta servicios
externos ni representa todavía la aplicación SaaS de producción.

## Pruebas

Desde la raíz del repositorio:

```text
python -m unittest discover -s local-broker/tests -p "test_*.py"
```

La agencia sintética de prueba es `Inmobiliaria Demo Broker`.
