def main_menu():
    print("\nCOVID Data Analysis Tool")
    print("1. Calculate Summary Statistics")
    print("2. Visualize Summary Statistics")
    print("3. Plot Top 10 Countries with Highest Cases")
    print("4. Plot Top 10 Countries with Lowest Cases")
    print("5. Plot Top 10 Countries by Highest Confirmed Deaths")
    print("6. Plot Top 10 Countries by Lowest Confirmed Deaths")
    print("7. Plot Top 10 Countries by Highest Confirmed Recoveries")
    print("8. Check Correlation for Highest Number of Cases, Deaths, and Recoveries")
    print("9. Check Correlation for Top 10 Countries with Lowest Number of Cases and Deaths")
    print("10. Visualize Country Data")
    print("11. Exit")

if __name__ == "__main__":
    while True:
        main_menu()
        choice = input("\nEnter your choice (1-11): ")
        if choice == "1":
            from data_loader import load_data
            from data_analysis import calculate_summary_statistics
            file_name = "covid_data.csv"
            data = load_data(file_name)
            if data is not None:            
                summary_stats = calculate_summary_statistics(file_name)
                print("\nSummary Statistics:")
                print(summary_stats)
        elif choice == "2":
            from visualize_all_statistics import visualize_summary_statistics
            file_name = "covid_data.csv"
            visualize_summary_statistics(file_name)
        elif choice == "3":
            from top_10_countries_plot import top_10_countries_plot
            file_name = "covid_data.csv"
            top_10_countries_plot(file_name)
        elif choice == "4":
            from top_10_countries_least_cases import top_10_countries_least_cases
            file_name = "covid_data.csv"
            top_10_countries_least_cases(file_name)
        elif choice == "5":
            from top_10_countries_deaths import top_10_countries_confirmed_deaths
            file_name = "covid_data.csv"
            top_10_countries_confirmed_deaths(file_name)
        elif choice == "6":
            from top_10_countries_least_deaths import top_10_countries_least_deaths
            file_name = "covid_data.csv"
            top_10_countries_least_deaths(file_name)
        elif choice == "7":
            from top_10_countries_recoveries import top_10_countries_confirmed_recoveries
            file_name = "covid_data.csv"
            top_10_countries_confirmed_recoveries(file_name)
        elif choice == "8":
            from correlation_most_cases import check_correlation_and_significance
            file_name = "covid_data.csv"
            check_correlation_and_significance(file_name)
        elif choice == "9":
            from data_loader import load_data
            file_name = "covid_data.csv"
            data = load_data(file_name)
            if data is not None:
                from correlation_least_cases import format_matrices_as_tabular, check_correlation_least_cases_deaths
                correlation_matrix, significance_matrix = check_correlation_least_cases_deaths(file_name)
                formatted_message = format_matrices_as_tabular(correlation_matrix, significance_matrix)
                print(formatted_message)

        elif choice == "10":
            from country_data_search import visualize_country_data
            file_name = "covid_data.csv"
            while True:
                option = input("Enter '1' to enter a country's name or '2' to go back to the main menu: ")
                if option == "1":
                    country_name_input = input("Enter the country name: ")
                    visualize_country_data(file_name, country_name_input)
                elif option == "2":
                    break  # Exit the loop and go back to the main menu
                else:
                    print("Invalid option. Please enter '1' or '2'.")

        elif choice == "11":
            print("Exiting program.")
            exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")
