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

print('titanic_df 데이터 건수: ', titanic_df.shape[0])
print('기본 설정인 dropna=True로 value_counts()')

# value_counts()는 디폴트로 dropna=True이므로 value_counts(dropna=True)와 동일
print(titanic_df['Embarked'].value_counts())
print(titanic_df['Embarked'].value_counts(dropna=False))
