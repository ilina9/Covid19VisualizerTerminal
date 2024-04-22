import matplotlib.pyplot as plt
from data_loader import load_data

def visualize_country_data(file_name, country_name_input):
    data = load_data(file_name)
    if data is None:
        return None  

    country_name = country_name_input.lower()

    country_data = data[data['country'].str.lower() == country_name]

    if country_data.empty:
        print(f"No data available for {country_name_input}.")
        return None

    plt.figure(figsize=(10, 6))
    plt.plot(country_data['date'], country_data['confirmed_cases'], label='Confirmed Cases', color='blue')
    plt.plot(country_data['date'], country_data['deaths'], label='Deaths', color='red')
    plt.plot(country_data['date'], country_data['recovered'], label='Recoveries', color='green')

    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title(f'COVID-19 Trajectory for {country_name_input}')
    plt.xticks(rotation=45)
    plt.legend()

    plt.tight_layout()
    plt.show()

country_name_input = input("Enter a country's name: ")
visualize_country_data('covid_data.csv', country_name_input.lower())
