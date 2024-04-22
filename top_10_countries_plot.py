
import matplotlib.pyplot as plt
from data_loader import load_data

def top_10_countries_plot(file_name):
    data = load_data(file_name)
    if data is None:
        return None  
    
    country_data = data.groupby('country')['confirmed_cases'].sum().reset_index()
    
    top_10_countries = country_data.nlargest(10, 'confirmed_cases')
    
    plt.figure(figsize=(10, 6))
    plt.bar(top_10_countries['country'], top_10_countries['confirmed_cases'], color='blue')
    
    plt.xlabel('Country')
    plt.ylabel('Confirmed Cases')
    plt.title('Top 10 Countries with Highest Confirmed Cases Count')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

top_10_countries_plot('covid_data.csv')