import matplotlib.pyplot as plt
from data_loader import load_data

def top_10_countries_least_cases(file_name):
    data = load_data(file_name)
    if data is None:
        return None
    
    # Aggregate data by country and calculate total confirmed cases
    country_data = data.groupby('country')['confirmed_cases'].sum().nsmallest(10)
    
    # Plot top 10 countries with the least cases
    plt.figure(figsize=(10, 6))
    plt.bar(country_data.index, country_data.values, color='blue')
    
    plt.xlabel('Country')
    plt.ylabel('Confirmed Cases')
    plt.title('Top 10 Countries with the Least Confirmed Cases')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()


top_10_countries_least_cases('covid_data.csv')