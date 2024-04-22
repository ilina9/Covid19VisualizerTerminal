import matplotlib.pyplot as plt
from data_loader import load_data

def top_10_countries_confirmed_recoveries(file_name):
    data = load_data(file_name)
    if data is None:
        return None 
    
    country_data = data.groupby('country')['recovered'].sum().nlargest(10)
    
    plt.figure(figsize=(10, 6))
    plt.bar(country_data.index, country_data.values, color='green')
    
    plt.xlabel('Country')
    plt.ylabel('Confirmed Recoveries')
    plt.title('Top 10 Countries by Most Confirmed Recoveries')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

top_10_countries_confirmed_recoveries('covid_data.csv')
