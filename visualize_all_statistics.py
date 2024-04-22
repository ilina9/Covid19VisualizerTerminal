import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data

def visualize_summary_statistics(file_name):
    data = load_data(file_name)
    if data is None:
        return None   
    
    required_columns = ['date', 'country', 'confirmed_cases', 'deaths', 'recovered']
        
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        print(f"Error: Columns {', '.join(missing_columns)} not found in the dataset.")
        return None   
    
    data['date'] = pd.to_datetime(data['date'])
    
    date_data = data.groupby('date').agg({
        'confirmed_cases': 'sum',
        'deaths': 'sum',
        'recovered': 'sum'
    }).reset_index()
    
    plt.figure(figsize=(12, 8))
    plt.plot(date_data['date'], date_data['recovered'], label='Recovered', color='green')
    plt.plot(date_data['date'], date_data['deaths'], label='Deaths', color='red')
    plt.plot(date_data['date'], date_data['confirmed_cases'], label='Confirmed Cases', color='blue')
    
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title('COVID-19 Cases, Deaths, and Recoveries Over Time (Line Graph)')
    plt.xticks(rotation=45)
    plt.legend()
    
    plt.tight_layout()
    plt.show()

visualize_summary_statistics('covid_data.csv')
