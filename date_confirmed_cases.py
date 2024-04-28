from matplotlib import style
import matplotlib.pyplot as plt
from data_loader import load_data

def date_confirmed_cases_correlation(file_name):
    data = load_data(file_name)
    style.use("ggplot")
    p = "confirmed_cases"
    plt.scatter(data[p], data["confirmed_cases"])
    plt.xlabel(p)
    plt.ylabel("Correlation with confirmed cases")
    plt.show()

date_confirmed_cases_correlation("covid_data.csv")