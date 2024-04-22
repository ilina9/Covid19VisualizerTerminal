import pandas as pd
from data_loader import load_data

def calculate_summary_statistics(file_name):
    data = load_data(file_name)
    if data is None:
        return None 
    
    required_columns = ['date', 'country', 'confirmed_cases', 'deaths', 'recovered']
        
    # check if all columns are in dataset
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        print(f"Error: Columns {', '.join(missing_columns)} not found in the dataset.")
        return None  
    
    # Calculate summary statistics 
    total_confirmed_cases = data['confirmed_cases'].sum()
    total_deaths = data['deaths'].sum()
    total_recoveries = data['recovered'].sum()  
    
    try:
        fatality_rate = (total_deaths / total_confirmed_cases) * 100
    except ZeroDivisionError:
        fatality_rate = 0  # Handle divide by zero
    
    try:
        recovery_rate = (total_recoveries / total_confirmed_cases) * 100
    except ZeroDivisionError:
        recovery_rate = 0  # Handle divide by zero

    # Return summary statistics
    return {
        'Total Confirmed Cases': total_confirmed_cases,
        'Total Deaths': total_deaths,
        'Total Recoveries': total_recoveries,
        'Fatality Rate': fatality_rate,
        'Recovery Rate': recovery_rate
    }

# Example usage
summary_stats = calculate_summary_statistics('covid_data.csv')
if summary_stats is not None:
    # Print each statistic separately
    print("Summary Statistics:")
    print(f"Total Confirmed Cases: {summary_stats['Total Confirmed Cases']}")
    print(f"Total Deaths: {summary_stats['Total Deaths']}")
    print(f"Total Recoveries: {summary_stats['Total Recoveries']}")
    print(f"Fatality Rate: {summary_stats['Fatality Rate']}%")
    print(f"Recovery Rate: {summary_stats['Recovery Rate']}%")
