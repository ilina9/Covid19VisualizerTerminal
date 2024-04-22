import tkinter as tk


# Define function to handle button click and plot top 10 countries
def plot_top_10_countries():
    from top_10_countries_plot import top_10_countries_plot
    file_name = "covid_data.csv"  # Example file name, modify as needed
    top_10_countries_plot(file_name)

# Create the main window
window = tk.Tk()
window.title("COVID Data Analysis Tool")

# Create a command wrapper to ensure the function is not executed prematurely
def command_wrapper(func):
    return lambda: func()

# Create button to plot top 10 countries
plot_button = tk.Button(window, text="Plot Top 10 Countries", command=command_wrapper(plot_top_10_countries))
plot_button.pack()

# Start the GUI event loop
window.mainloop()
