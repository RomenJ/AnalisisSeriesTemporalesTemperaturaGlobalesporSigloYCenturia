import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset de temperaturas por país
dataGlobalbyCount = pd.read_csv('GlobalLandTemperaturesByCountry.csv', parse_dates=['dt'], index_col='dt')
print("Value Counts..........")

print(dataGlobalbyCount.head(5))
print("Info 2:")
print(dataGlobalbyCount.info())

print("Number of Values..........")
print(dataGlobalbyCount['Country'].value_counts())

# Filtrar países con alta frecuencia y eliminar filas con valores nulos en AverageTemperature
country_counts = dataGlobalbyCount['Country'].value_counts()
high_freq_countries = country_counts[country_counts > 3228].index
print(high_freq_countries)
HighFrecCountries = dataGlobalbyCount[dataGlobalbyCount['Country'].isin(high_freq_countries)]
HighFrecCountries = HighFrecCountries.dropna(subset=['AverageTemperature'])

# Seleccionar los países de interés
countries_to_add = ['Spain', 'Faroe Islands']
#countries_to_add = ['Serbia', 'Spain', 'Faroe Islands']
SHighFrecCountries = HighFrecCountries[HighFrecCountries['Country'].isin(countries_to_add)]


# Crear una nueva columna para el siglo
SHighFrecCountries['Century'] = (SHighFrecCountries.index.year // 100 + 1) * 100

# Graficar la temperatura media anual por país a lo largo del tiempo
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")
sns.lineplot(data=SHighFrecCountries, x=SHighFrecCountries.index, y='AverageTemperature', hue='Country', linewidth=2.5, alpha=0.5)

plt.title('Temperatura Media Anual por País')
plt.savefig('Temperatura Media por País con Tonalidades por Siglo.jpg')
plt.xlabel('País')
plt.xlabel('Fecha')
plt.ylabel('Temperatura Media (°C)')
plt.legend(title='País', loc='upper left')
plt.tight_layout()
plt.show()
plt.clf()

# Graficar utilizando stripplot con tonalidades por siglo

sns.stripplot(data=SHighFrecCountries, x='Country', y='AverageTemperature', hue='Century', palette='viridis')
plt.title('Temperatura Media por País con Tonalidades por Siglo')
plt.savefig('Temperatura Media por País con Tonalidades por Siglos.jpg')
plt.xlabel('País')
plt.ylabel('Temperatura Media (°C)')
plt.legend(title='Siglo', loc='upper right')
plt.tight_layout()
plt.show()
