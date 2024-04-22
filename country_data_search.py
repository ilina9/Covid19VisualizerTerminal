import tkinter as tk
from tkinter import messagebox
from data_loader import load_data
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def visualize_country_data(file_name, country_name_input):
    data = load_data(file_name)
    if data is None:
        return None 
    country_name = country_name_input.lower()
    country_data = data[data['country'].str.lower() == country_name]
    
    if country_data.empty:
        messagebox.showinfo("Country Data Unavailable", f"No data available for {country_name_input}.")
        return None
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(country_data['date'], country_data['confirmed_cases'], label='Confirmed Cases', color='blue')
    ax.plot(country_data['date'], country_data['deaths'], label='Deaths', color='red')
    ax.plot(country_data['date'], country_data['recovered'], label='Recoveries', color='green')
    
    ax.set_xlabel('Date')
    ax.set_ylabel('Count')
    ax.set_title(f'COVID-19 Trajectory for {country_name_input}')
    ax.legend()
    
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

def show_country_data():
    country_name_input = country_entry.get()
    visualize_country_data('covid_data.csv', country_name_input)

window = tk.Tk()
window.title("COVID Data Analysis Tool")

country_entry = tk.Entry(window, width=30)
country_entry.pack()

visualize_button = tk.Button(window, text="Visualize Country Data", font=("Arial", 14), height=2, command=show_country_data)
visualize_button.pack()

window.mainloop()
