import pandas as pd

data = {'Name': ['Chulmin', 'Eunkyung', 'Jinwoong', 'Soobeom'], 'Year': [2011, 2016, 2015, 2012], 'Gender': ['Male', 'Female', 'Female', 'Male']}

data_df = pd.DataFrame(data, index=['one', 'two', 'three', 'four'])
print(data_df)

print(data_df.iloc[2, 2])

print("\n 맨 마지막 칼럼 데이터 [:, -1] \n", data_df.iloc[:, -1])
print("\n 맨 마지막 칼럼을 제외한 모든 데이터 [:, :-1] \n", data_df.iloc[:, :-1])

