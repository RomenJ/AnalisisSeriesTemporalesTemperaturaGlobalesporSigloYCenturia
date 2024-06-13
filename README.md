# Análisis de Series Temporales de Temperaturas Globales

Este proyecto realiza un análisis de series temporales de las temperaturas globales, utilizando visualizaciones de datos para países con alta frecuencia de registros. Se emplean herramientas como Python, pandas y seaborn para la manipulación y presentación de los datos.

## Descripción

El objetivo principal de este proyecto es analizar y visualizar las temperaturas medias anuales de diferentes países a lo largo del tiempo. El análisis se enfoca en países con un número alto de registros y permite observar las tendencias de temperatura en intervalos de 50 años.

## Estructura del Proyecto

- **load_and_inspect_data(filepath)**: Carga el dataset y muestra información básica.
- **filter_high_frequency_countries(data, threshold=3228)**: Filtra los países con alta frecuencia y elimina valores nulos.
- **add_time_intervals(data)**: Añade una columna para intervalos de 50 años.
- **plot_annual_temperature(data, countries)**: Grafica la temperatura media anual por país a lo largo del tiempo.
- **plot_stripplot(data, countries)**: Grafica utilizando stripplot con tonalidades por intervalos de 50 años.

## Requisitos

- Python 3.x
- pandas
- matplotlib
- seaborn

Puedes instalar los requisitos ejecutando:
```bash
pip install pandas matplotlib seaborn
