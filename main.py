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

    def top_10_countries_least_cases():
        from top_10_countries_least_cases import top_10_countries_least_cases
        file_name = "covid_data.csv"
        top_10_countries_least_cases(file_name)

    def top_10_countries_least_deaths():
        from top_10_countries_least_deaths import top_10_countries_least_deaths
        file_name = "covid_data.csv"
        top_10_countries_least_deaths(file_name)

    def check_correlation_highest_cases():
        from correlation_most_cases import check_correlation_and_significance
        file_name = "covid_data.csv"
        check_correlation_and_significance(file_name)

    def check_correlation_lowest_cases():
        from correlation_least_cases import format_matrices_as_tabular
        file_name = "covid_data.csv"
        format_matrices_as_tabular(file_name)
        
    def gui_window_search_country(): 
        from country_data_search import show_country_data    
        # Create GUI window
        window = tk.Tk()
        window.title("COVID Data Analysis Tool")
        # Country name input
        country_entry = tk.Entry(window, width=30)
        country_entry.pack(show_country_data)

    def exit_program():
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            window.destroy()

    def add_padding():
        space_label = tk.Label(window, text="", pady=0.1) 
        space_label.pack()


    #Create GUI buttons for each function
    window = tk.Tk()
    window.title("COVID Data Analysis Tool")

    summary_button = tk.Button(window, text="Calculate Summary Statistics", font=("Arial", 14), height=2, command=calculate_and_show_summary)
    summary_button.pack()
 
    visualize_button = tk.Button(window, text="Visualize Summary Statistics", font=("Arial", 14), height=2, command=visualize_summary_statistics)
    visualize_button.pack()
 

    top_10_countries_button = tk.Button(window, text="Plot Top 10 Countries with Highest Cases", font=("Arial", 14), height=2, command=plot_top_10_countries)
    top_10_countries_button.pack()


    top_10_countries_button = tk.Button(window, text="Plot Top 10 Countries with Lowest Cases", font=("Arial", 14), height=2, command=top_10_countries_least_cases)
    top_10_countries_button.pack()
 

    top_10_countries_deaths_button = tk.Button(window, text="Plot Top 10 Countries by Highest Confirmed Deaths", font=("Arial", 14), height=2, command=plot_top_10_countries_deaths)
    top_10_countries_deaths_button.pack()


    top_10_countries_deaths_button = tk.Button(window, text="Plot Top 10 Countries by Lowest Confirmed Deaths", font=("Arial", 14), height=2, command=top_10_countries_least_deaths)
    top_10_countries_deaths_button.pack()
  

    top_10_countries_deaths_button = tk.Button(window, text="Plot Top 10 Countries by Highest Confirmed Recoveries", font=("Arial", 14), height=2, command=plot_top_10_countries_recoveries)
    top_10_countries_deaths_button.pack()
 

    top_10_countries_deaths_button = tk.Button(window, text="Check Correlation for Highest Number of Cases, Deaths and Recoveries", font=("Arial", 14), height=2, command=check_correlation_highest_cases)
    top_10_countries_deaths_button.pack()
 

    top_10_countries_deaths_button = tk.Button(window, text="Check Correlation for Top 10 Countries with Lowest Number of Cases and Deaths", font=("Arial", 14), height=2, command=check_correlation_lowest_cases)
    top_10_countries_deaths_button.pack()

    visualize_button = tk.Button(window, text="Visualize Country Data", font=("Arial", 14), height=2, command=gui_window_search_country)
    visualize_button.pack()
    add_padding()
    exit_button = tk.Button(window, text="Exit", font=("Arial", 12), height=2, command=exit_program, bd=0, bg="red", fg="white", borderwidth=0, highlightthickness=0, activebackground="darkred")
    exit_button.configure(relief="solid", width=8, border=0, padx=10, pady=5, borderwidth=0, highlightthickness=0)
    exit_button.pack()

    window.mainloop()
