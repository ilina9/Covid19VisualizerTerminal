import tkinter as tk
from tkinter import messagebox
from data_loader import load_data
import pandas as pd
from scipy.stats import pearsonr
from tabulate import tabulate

def check_correlation_least_cases_deaths(file_name, significance_level=0.05):
    data = load_data(file_name)
    if data is None:
        return None, None 
    
    # Select top 10 countries with the least cases and least deaths
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

# Format matrices as tabular string using tabulate
def format_matrices_as_tabular(correlation_matrix, significance_matrix, significance_level=0.05):
    # Filter non-significant correlations
    significant_correlations = significance_matrix[significance_matrix < significance_level]
    correlated_countries = significant_correlations.index.intersection(significant_correlations.columns)
    
    # Filter based on countries
    filtered_correlation_matrix = correlation_matrix.loc[correlated_countries, correlated_countries]
    filtered_significance_matrix = significance_matrix.loc[correlated_countries, correlated_countries]
    
    # Convert to tabular format
    correlation_table = tabulate(filtered_correlation_matrix, headers='keys', tablefmt='grid')
    significance_table = tabulate(filtered_significance_matrix, headers='keys', tablefmt='grid')

    # Combine the tables into a single formatted string
    formatted_str = f"Correlation Matrix:\n\n{correlation_table}\n\n"
    formatted_str += f"Statistically Significant Correlations:\n\n{significance_table}"

    return formatted_str


correlation_matrix_least, significance_matrix_least = check_correlation_least_cases_deaths('covid_data.csv')
formatted_message = format_matrices_as_tabular(correlation_matrix_least, significance_matrix_least)

# Create tk window and show the message box
window = tk.Tk()
window.withdraw()  # Hide the main window
messagebox.showinfo("Correlation and Significance Results", formatted_message)
window.mainloop()
