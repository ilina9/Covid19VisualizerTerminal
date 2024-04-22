import pandas as pd
#just loading the data here
def load_data(file_name):
    try:
        data = pd.read_csv(file_name)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

data = load_data('covid_data.csv')
if data is not None:  
    print('Covid data loaded') #print that the specific file is loaded
