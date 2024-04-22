import tkinter as tk
from tkinter import messagebox

if __name__ == '__main__':
    def calculate_and_show_summary():
        from data_analysis import calculate_summary_statistics
        file_name = "covid_data.csv"
        summary_stats = calculate_summary_statistics(file_name)
        if summary_stats is not None:
            messagebox.showinfo("Summary Statistics", summary_stats)

    def visualize_summary_statistics():
        from visualize_all_statistics import visualize_summary_statistics  # Corrected import
        file_name = "covid_data.csv"
        visualize_summary_statistics(file_name)  # Call the correct function

    def plot_top_10_countries():
        from top_10_countries_plot import top_10_countries_plot
        file_name = "covid_data.csv"
        top_10_countries_plot(file_name)

    def plot_top_10_countries_deaths():
        from top_10_countries_deaths import top_10_countries_confirmed_deaths
        file_name = "covid_data.csv"
        top_10_countries_confirmed_deaths(file_name)
    
    def plot_top_10_countries_recoveries():
        from top_10_countries_recoveries import top_10_countries_confirmed_recoveries
        file_name = "covid_data.csv"
        top_10_countries_confirmed_recoveries(file_name)

    def check_correlation_highest_cases():
        from correlation_most_cases import check_correlation_and_significance
        file_name = "covid_data.csv"
        correlation_highest = check_correlation_and_significance(file_name)
        if correlation_highest is not None:
            # Create Tkinter window
            window = tk.Tk()
            window.title("Correlation data")

            # Create label to display the correlation data
            label = tk.Label(window, text=correlation_highest)
            label.pack()

    window = tk.Tk()
    window.title("COVID Data Analysis Tool")

    summary_button = tk.Button(window, text="Calculate Summary Statistics", font=("Arial", 14), height=2, command=calculate_and_show_summary)
    summary_button.pack()

    visualize_button = tk.Button(window, text="Visualize Summary Statistics", font=("Arial", 14), height=2, command=visualize_summary_statistics)
    visualize_button.pack()

    top_10_countries_button = tk.Button(window, text="Plot Top 10 Countries", font=("Arial", 14), height=2, command=plot_top_10_countries)
    top_10_countries_button.pack()

    top_10_countries_deaths_button = tk.Button(window, text="Plot Top 10 Countries by Confirmed Deaths", font=("Arial", 14), height=2, command=plot_top_10_countries_deaths)
    top_10_countries_deaths_button.pack()

    top_10_countries_deaths_button = tk.Button(window, text="Plot Top 10 Countries by Confirmed Recoveries", font=("Arial", 14), height=2, command=plot_top_10_countries_recoveries)
    top_10_countries_deaths_button.pack()

    top_10_countries_deaths_button = tk.Button(window, text="Check Correlation for Highest Number of Cases, Deaths and Recoveries", font=("Arial", 14), height=2, command=check_correlation_highest_cases)
    top_10_countries_deaths_button.pack()

    window.mainloop()
