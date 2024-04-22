import tkinter as tk
from tkinter import messagebox
from data_loader import load_data
import pandas as pd
from scipy.stats import pearsonr
from tabulate import tabulate

def check_correlation_and_significance(file_name, significance_level=0.05):
    data = load_data(file_name)
    if data is None:
        return None
    
    top_10_cases = data.groupby('country')['confirmed_cases'].sum().nlargest(10).index
    top_10_deaths = data.groupby('country')['deaths'].sum().nlargest(10).index
    top_10_recoveries = data.groupby('country')['recovered'].sum().nlargest(10).index
    
    top_10_data = data[data['country'].isin(top_10_cases.union(top_10_deaths).union(top_10_recoveries))]
    
    correlation_matrix = top_10_data[['confirmed_cases', 'deaths', 'recovered']].corr()
    p_values = pd.DataFrame(index=['confirmed_cases', 'deaths', 'recovered'], columns=['confirmed_cases', 'deaths', 'recovered'])
    significance_matrix = pd.DataFrame(index=['confirmed_cases', 'deaths', 'recovered'], columns=['confirmed_cases', 'deaths', 'recovered'])
    
    for col1 in correlation_matrix.columns:
        for col2 in correlation_matrix.index:
            if col1 != col2:
                correlation_coefficient, p_value = pearsonr(top_10_data[col1], top_10_data[col2])
                p_values.loc[col1, col2] = p_value
                significance_matrix.loc[col1, col2] = p_value < significance_level

    correlation_table = tabulate(correlation_matrix, headers='keys', tablefmt='grid')
    significant_correlations = p_values[p_values < significance_level]
    significant_table = tabulate(significant_correlations, headers='keys', tablefmt='grid') if not significant_correlations.empty else "No statistically significant correlations."

    message = f"Correlation Matrix:\n\n{correlation_table}\n\n"
    message += f"Statistically Significant Correlations:\n\n{significant_table}"

    window = tk.Tk()
    window.withdraw()
    messagebox.showinfo("Correlation and Significance Results", message)
    window.mainloop()

check_correlation_and_significance('covid_data.csv')
