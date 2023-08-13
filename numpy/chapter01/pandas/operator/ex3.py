import pandas as pd

data_df = pd.read_csv('data/train.csv')

print(data_df.loc['one', 'Name'])
