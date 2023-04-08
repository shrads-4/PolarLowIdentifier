import pandas as pd

data = pd.read_csv('pkl_file.csv')
data.to_pickle('pkl_file.pkl')