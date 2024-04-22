import matplotlib.pyplot as plt
from data_loader import load_data

def top_10_countries_confirmed_deaths(file_name):
    data = load_data(file_name)
    if data is None:
        return None  # Handle data loading error
    
    # Aggregate data by country and calculate total confirmed deaths
    country_data = data.groupby('country')['deaths'].sum().nlargest(10)
    
    # Plotting the top 10 countries by confirmed deaths
    plt.figure(figsize=(10, 6))
    plt.bar(country_data.index, country_data.values, color='red')
    
    plt.xlabel('Country')
    plt.ylabel('Confirmed Deaths')
    plt.title('Top 10 Countries by Most Confirmed Deaths')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

# Example usage
top_10_countries_confirmed_deaths('covid_data.csv')