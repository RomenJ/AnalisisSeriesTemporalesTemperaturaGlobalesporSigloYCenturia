import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_inspect_data(filepath):
    """Carga el dataset y muestra información básica."""
    data = pd.read_csv(filepath, parse_dates=['dt'], index_col='dt')
    print("Value Counts..........")
    print(data.head(5))
    print("Info 2:")
    print(data.info())
    print("Number of Values..........")
    print(data['Country'].value_counts())
    return data

def filter_high_frequency_countries(data, threshold=3228):
    """Filtra los países con frecuencia alta y elimina valores nulos en AverageTemperature."""
    country_counts = data['Country'].value_counts()
    high_freq_countries = country_counts[country_counts > threshold].index
    print("High frequency countries:", high_freq_countries)
    filtered_data = data[data['Country'].isin(high_freq_countries)]
    filtered_data = filtered_data.dropna(subset=['AverageTemperature'])
    return filtered_data

def add_time_intervals(data):
    """Añade una columna para intervalos de 50 años."""
    data = data.copy()
    data['HalfCentury'] = (data.index.year // 50) * 50
    return data

def plot_annual_temperature(data, countries):
    """Grafica la temperatura media anual por país a lo largo del tiempo."""
    selected_data = data[data['Country'].isin(countries)]
    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    sns.lineplot(data=selected_data, x=selected_data.index, y='AverageTemperature', hue='Country', linewidth=2.5, alpha=0.5)
    plt.title('Temperatura Media Anual por País')
    plt.savefig('Temperatura Media Anual por País.jpg')
    plt.xlabel('Fecha')
    plt.ylabel('Temperatura Media (°C)')
    plt.legend(title='País', loc='upper left')
    plt.tight_layout()
    plt.show()

def plot_stripplot(data, countries):
    """Grafica utilizando stripplot con tonalidades por intervalos de 50 años."""
    selected_data = data[data['Country'].isin(countries)]
    plt.figure(figsize=(12, 6))
    sns.stripplot(data=selected_data, x='Country', y='AverageTemperature', hue='HalfCentury', palette='viridis')
    plt.title('Temperatura Media por País con Tonalidades por Intervalos de 50 Años')
    plt.savefig('Temperatura Media por País con Tonalidades por Intervalos de 50 Años.jpg')
    plt.xlabel('País')
    plt.ylabel('Temperatura Media (°C)')
    plt.legend(title='Intervalo de 50 Años', loc='upper right')
    plt.tight_layout()
    plt.show()

def main():
    filepath = 'GlobalLandTemperaturesByCountry.csv'
    data = load_and_inspect_data(filepath)
    high_freq_data = filter_high_frequency_countries(data)
    high_freq_data = add_time_intervals(high_freq_data)
    
    countries_to_plot = ['Spain', 'Faroe Islands']
    plot_annual_temperature(high_freq_data, countries_to_plot)
    plot_stripplot(high_freq_data, countries_to_plot)

if __name__ == "__main__":
    main()
