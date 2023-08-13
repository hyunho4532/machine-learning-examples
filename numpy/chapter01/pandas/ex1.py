import pandas as pd

titanic_df = pd.read_csv(r'data/train.csv')
print('titanic 변수 type: ', type(titanic_df))
print(titanic_df)

print(titanic_df.head(3))

print('DataFrame 크기: ', titanic_df.shape)


print(titanic_df.info())

print(titanic_df.describe())

print(titanic_df.count())

value_counts = titanic_df['Pclass'].value_counts()
print(value_counts)

titanic_pclass = titanic_df['Pclass']
print(type(titanic_pclass))

print(titanic_pclass.head())

