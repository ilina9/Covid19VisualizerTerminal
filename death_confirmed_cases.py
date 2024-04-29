from matplotlib import style
import matplotlib.pyplot as plt
from data_loader import load_data
import pandas as pd
import sklearn
from sklearn import linear_model

def date_confirmed_cases_correlation(file_name):
    data = load_data(file_name)
    style.use("ggplot")
    a = "confirmed_cases"
    b = "deaths"
    plt.scatter(data[a], data[b])
    plt.xlabel(a)
    plt.ylabel(b)
    plt.show()
date_confirmed_cases_correlation("covid_data.csv")