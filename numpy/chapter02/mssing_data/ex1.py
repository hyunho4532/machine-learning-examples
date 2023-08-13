import pandas as pd

titanic_df = pd.read_csv('data/train.csv')

print(titanic_df.isna().head(3))
print(titanic_df.isna().sum())

titanic_df['Cabin'] = titanic_df['Cabin'].fillna('C000')
print(titanic_df.head(3))

# Age 칼럼의 NaN 값을 평균 나이로, Embarked 칼럼의 NaN 값을 S로 대체
titanic_df['Age'] = titanic_df['Age'].fillna(titanic_df['Age'].mean())
titanic_df['Embarked'] = titanic_df['Embarked'].fillna('S')
print(titanic_df.isna().sum())