import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data

def visualize_summary_statistics(file_name):
    data = load_data(file_name)
    if data is None:
        return None  # Handle data loading error
    
    required_columns = ['date', 'country', 'confirmed_cases', 'deaths', 'recovered']
        
    # Check if all required columns exist in dataset
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        print(f"Error: Columns {', '.join(missing_columns)} not found in the dataset.")
        return None  # Handle missing column/s error
    
    # Make sure 'date' column is parsed as datetime
    data['date'] = pd.to_datetime(data['date'])
    
    # Aggregate data by date
    date_data = data.groupby('date').agg({
        'confirmed_cases': 'sum',
        'deaths': 'sum',
        'recovered': 'sum'
    }).reset_index()
    
    # Plot data as a stacked bar chart
    plt.figure(figsize=(12, 8))
    plt.bar(date_data['date'], date_data['recovered'], label='Recovered', color='green')
    plt.bar(date_data['date'], date_data['deaths'], bottom=date_data['recovered'], label='Deaths', color='red')
    plt.bar(date_data['date'], date_data['confirmed_cases'], bottom=date_data['recovered'] + date_data['deaths'], label='Confirmed Cases', color='blue')
    
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title('COVID-19 Cases, Deaths, and Recoveries Over Time')
    plt.xticks(rotation=45)
    plt.legend()
    
    plt.tight_layout()
    plt.show()

# Example usage
visualize_summary_statistics('covid_data.csv')




