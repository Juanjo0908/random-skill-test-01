---
name: "titan-ml-logic"
description: "Analizador profesional de CSV con Machine Learning"
version: "1.0.0"

# AQUÍ DEFINES LA MONETIZACIÓN
pricing:
  type: "pay-per-use"    # O "subscription"
  currency: "USD"
  price: 0.10            # Cobras 10 centavos por cada ejecución
  free_tier: 5           # Las primeras 5 llamadas son gratis (para atraer clientes)

author: "Juanjo"
---
# Analizador Descriptivo de Datos
Esta skill permite a la IA entender rápidamente la estructura de cualquier dataset antes de entrenar un modelo.

## Cómo usar
El agente de IA debe ejecutar el script pasando la ruta del archivo CSV.
`python app.py --file data.csv`

## Requisitos
- Python 3.9+
- Pandas 
