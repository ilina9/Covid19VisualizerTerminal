import matplotlib.pyplot as plt
from data_loader import load_data

def top_10_countries_least_cases(file_name):
    data = load_data(file_name)
    if data is None:
        return None
    
    country_data = data.groupby('country')['confirmed_cases'].sum().nsmallest(10)
    
    plt.figure(figsize=(10, 6))
    plt.plot(country_data.index, country_data.values, marker='o', color='blue', linestyle='-')
    
    plt.xlabel('Country')
    plt.ylabel('Confirmed Cases')
    plt.title('Top 10 Countries with the Least Confirmed Cases (Line Graph)')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.grid(True)
    plt.show()

top_10_countries_least_cases('covid_data.csv')
