import matplotlib.pyplot as plt
from data_loader import load_data
import pandas as pd
from scipy.stats import pearsonr


def top_10_countries_least_cases(file_name):
    data = load_data(file_name)
    if data is None:
        return None  # Handle data loading error
    
    # Aggregate data by country and calculate total confirmed cases
    country_data = data.groupby('country')['confirmed_cases'].sum().nsmallest(10)
    
    # Plotting the top 10 countries with the least cases
    plt.figure(figsize=(10, 6))
    plt.bar(country_data.index, country_data.values, color='blue')
    
    plt.xlabel('Country')
    plt.ylabel('Confirmed Cases')
    plt.title('Top 10 Countries with the Least Confirmed Cases')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

# Example usage
top_10_countries_least_cases('covid_data.csv')

def top_10_countries_least_deaths(file_name):
    data = load_data(file_name)
    if data is None:
        return None  # Handle data loading error
    
    # Aggregate data by country and calculate total deaths
    country_data = data.groupby('country')['deaths'].sum().nsmallest(10)
    
    # Plotting the top 10 countries with the least deaths
    plt.figure(figsize=(10, 6))
    plt.bar(country_data.index, country_data.values, color='red')
    
    plt.xlabel('Country')
    plt.ylabel('Deaths')
    plt.title('Top 10 Countries with the Least Confirmed Deaths')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

# Example usage
top_10_countries_least_deaths('covid_data.csv')

import pandas as pd
from scipy.stats import pearsonr

def check_correlation_least_cases_deaths(file_name, significance_level=0.05):
    data = load_data(file_name)
    if data is None:
        return None  # Handle data loading error
    
    # Select the top 10 countries with the least cases and least deaths
    top_10_least_cases = data.groupby('country')['confirmed_cases'].sum().nsmallest(10).index
    top_10_least_deaths = data.groupby('country')['deaths'].sum().nsmallest(10).index
    
    # Filter data for these top 10 countries with least cases and deaths
    top_10_least_cases_data = data[data['country'].isin(top_10_least_cases)]
    top_10_least_deaths_data = data[data['country'].isin(top_10_least_deaths)]
    
    # Calculate correlation between cases and deaths for these countries
    correlation_matrix = pd.DataFrame(index=top_10_least_cases, columns=top_10_least_deaths)
    significance_matrix = pd.DataFrame(index=top_10_least_cases, columns=top_10_least_deaths)
    for country_cases in top_10_least_cases:
        for country_deaths in top_10_least_deaths:
            cases_data = top_10_least_cases_data[top_10_least_cases_data['country'] == country_cases]['confirmed_cases']
            deaths_data = top_10_least_deaths_data[top_10_least_deaths_data['country'] == country_deaths]['deaths']
            
            # Calculate correlation coefficient and p-value
            correlation_coefficient, p_value = pearsonr(cases_data, deaths_data)
            correlation_matrix.loc[country_cases, country_deaths] = correlation_coefficient
            significance_matrix.loc[country_cases, country_deaths] = p_value < significance_level
    
    return correlation_matrix, significance_matrix


correlation_matrix_least, significance_matrix_least = check_correlation_least_cases_deaths('covid_data.csv')
print("Correlation Matrix between Top 10 Countries with Least Cases and Least Deaths:")
print(correlation_matrix_least)
print("\nStatistical Significance Matrix:")
print(significance_matrix_least)
