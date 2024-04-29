Solution

Feature 1 – Dataset Loading

 	Dataset Loading is implemented in the data_loader.py file through the function “load_data(file_name)” which is further used to load the data in the rest of the program.
 	We are using a try-except block to handle the data loading, i.e. to make sure that the data is loaded without any issues, specifically targeting the scenario of the data not existing.
 	If the data is loaded successfully, we will see the output “Covid data loaded” in the terminal – otherwise, we will get the output “Error: File 'covid_data.csv' not found.”. 
 	Ensures clear feedback on whether the data is loaded or not.

Feature 2 – Summary Statistics Overview

 	Summary Statistics Overview is achieved through the function “calculate_summary_statistics()” in the file data_analysis.py
 	Error and data handling through ensuring that the data is loaded as well as hat there are no missing columns.
 	Summary statistics are performed using the .sum() function for each of the relevant columns (confirmed cases, deaths and recovered).
 	Implemented additional functionality – Fatality and Recovery rates, i.e. how many of the confirmed cases resulted in death and how many resulted in recovery.

Feature 3 - Daily Cases Plotting

 	Daily cases plotting feature is implemented through the “visualize_summary_statistics()” function in visualize_all_statistics.py
 	Data loading and column presence validation.
 	Converting date to datetime objects in pandas for an accurate timeline plot.
 	Data for each date is aggregated using .agg() in order to be able to see the overall trend instead of the individual entries per country.
 	Each line for cases, recoveries and deaths has a separate color.

Feature 4 - Top 10 Countries Plot

 	Implemented through “top_10_countries_plot()” function in the top_10_countries_plot.py file.
 	Data is grouped by the country column and the total confirmed cases are summed up for each country.
 	Data is filtered based on the top 10 largest confirmed cases.
 	As per the requirements, a bar chart from matplotlib is used to represent the data, where the height of the bar indicates the number of the confirmed cases.

Feature 5 - Country-wise Search

 	The visualization functionality is encapsulated within the function visualize_country_data(file_name, country_name_input) in the file country_data_search.py
 	The function focuses on loading, filtering, and plotting data with line plots on the same graph for records of confirmed cases, deaths and recoveries for a specific country based on the user’s input.
 	Implemented functionality to convert all input to lower case, finding the country no matter how the user typed it, as well as checking in case there is no data for the specified country upon which a terminal message will be thrown to notify the user.

Feature 6 – Exit Option

 	Selecting the specific main menu option in the terminal when running main.py terminates the loop used in the application using the “exit()” function, printing a goodbye message and exiting the program.

Feature 0 - How it all comes together in main.py

 	Menu driven functionality through the terminal
 	Each option is clearly numbered and described, allowing users to choose the specific analysis or visualization they need
 	If-elif-else statements are the central structure of the menu functionality, where depending on the number chosen by the user, the appropriate block of code that matches the input with its related function will be executed.

Feature 7 – Implement Additional Functionality

Feature 7.1 and 7.2 – Plot 10 Countries with Lowest Cases, Deaths

 	Plotting top 10 countries with the least amount of cases and plot 10 countries with least amount of deaths in separate files, being top_10_countries_least_cases.py and top_10_countries_least_deaths.py.
 	Groups data by country aggregates data for cases and deaths, respectively.
 	Use “nsmallest(10)” to find the lowest numbers.
 	Plots a bar chart where the x-axis are countries, while the y-axis are cases/deaths.

Feature 7.3 - Plot Top 10 Countries by Highest Confirmed Recoveries

 	Plotting top 10 countries with the most recoveries in the top_10_countries_confirmed_recoveries.py file.
 	Groups data by country and calculates the sum of recoveries for each country.
 	Creates a bar chart for the data using matplotlib.

Feature 7.4 – Tabulated correlations

	Correlation for Highest Number of Cases, Deaths, and Recoveries
	Correlation for Top 10 Countries with Lowest Number of Cases and Deaths

 	Correlations are calculated in the correlation_most_cases.py and correlation_least_cases.py files.
 	Computes the p-values of statistical significance using Pearson correlation coefficient for the top 10 countries with highest numbers of cases, deaths and recoveries and lowest number of cases and deaths.
 	Determines which correlations are statistically significant
 	Prints correlation matrix and formats it using tabulate.
 	Printed table contains information indicating significant or not significant correlations.

Feature 7.5 – Correlation Plot for Cases and Deaths

 	Implemented in the file death_confirmed_cases.py. 
 	Variables a and b implemented with their respective values (cases and deaths) due to possibility of changing the attributes which will be represented on the plot.
 	Scatter plot is shown to visualize the relationship between confirmed cases and deaths.

General Features

 	Overall error handling throughout all files
 	Modularity of the code in separate functions and separate files
 	Solution regularly updated on GitHub
 	Other version with GUI in progress using Tkinter, where every functionality of the main menu has its button.
o	Each file’s necessary function is added to the main.py file from which the functions will be linked to their respective buttons.
 
Errors and problems

	Some of the matplotlib visualizations are displayed twice when the user calls the visualization from the terminal. This does not occur when the functions are executed in their separate files. This calls for additional troubleshooting.
