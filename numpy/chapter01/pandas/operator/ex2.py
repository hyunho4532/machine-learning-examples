import pandas as pd

data = {'Name': ['Chulmin', 'Eunkyung', 'Jinwoong', 'Soobeom'], 'Year': [2011, 2016, 2015, 2012], 'Gender': ['Male', 'Female', 'Female', 'Male']}

data_df = pd.DataFrame(data, index=['one', 'two', 'three', 'four'])
print(data_df)

print(data_df.iloc[2, 2])

print("\n 맨 마지막 칼럼 데이터 [:, -1] \n", data_df.iloc[:, -1])
print("\n 맨 마지막 칼럼을 제외한 모든 데이터 [:, :-1] \n", data_df.iloc[:, :-1])

print(data_df.loc['three', 'Name'])

print('위치기반 iloc slicing\n', data_df.iloc[0:1, 0], '\n')
print('명칭기반 loc slicing\n', data_df.loc['one':'two', 'Name' ])

print(data_df.loc['three', 'Name'])
print(data_df.loc['one':'two', [ 'Name', 'Year' ]])
print(data_df.loc['one':'three', 'Name':'Gender' ])
print(data_df.loc[:])
print(data_df.loc[data_df.Year >= 2014])
