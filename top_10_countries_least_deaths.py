import matplotlib.pyplot as plt
from data_loader import load_data

def top_10_countries_least_deaths(file_name):
    data = load_data(file_name)
    if data is None:
        return None  # Handle data loading error
    
    # Aggregate data by country and calculate total deaths
    country_data = data.groupby('country')['deaths'].sum().nsmallest(10)
    
    # Plot top 10 countries with the least deaths
    plt.figure(figsize=(10, 6))
    plt.bar(country_data.index, country_data.values, color='red')
    
    plt.xlabel('Country')
    plt.ylabel('Deaths')
    plt.title('Top 10 Countries with the Least Confirmed Deaths')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()


top_10_countries_least_deaths('covid_data.csv')