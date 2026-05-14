import pandas as pd
# Load the dataset
data = pd.read_csv('ksinha_aggregated.csv')
print(data.head())
print(data.shape)
print(data.info())
print(data.describe())