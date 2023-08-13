import pandas as pd

titanic_df = pd.read_csv('data/train.csv')
titanic_boolean = titanic_df[titanic_df['Age'] > 60]
print(type(titanic_boolean))
print(titanic_boolean)

print(titanic_df[titanic_df['Age'] > 60][[ 'Name', 'Age' ]].head(3))
print(titanic_df.loc[titanic_df['Age'] > 60, [ 'Name', 'Age' ]].head(3))

# 나이가 60세 이상이고, 선실 등급이 1등급이며, 성별이 여성인 승객을 추출해 보겠다.
print(titanic_df[ (titanic_df['Age'] > 60) & (titanic_df['Pclass'] == 1) & (titanic_df['Sex'] == 'female') ])

cond1 = titanic_df['Age'] > 60
cond2 = titanic_df['Pclass'] == 1
cond3 = titanic_df['Sex'] == 'female'

print(titanic_df[ cond1 & cond2 & cond3 ])

titanic_sorted = titanic_df.sort_values(by=['Name'])
print(titanic_sorted.head(10))

titanic_sorted = titanic_sorted.sort_values(by=['Pclass', 'Name'], ascending=False)
print(titanic_sorted.head(3))

print(titanic_df.count())

print(titanic_df[[ 'Age', 'Fare' ]].mean())

titanic_groupby = titanic_df.groupby(by='Pclass')
print(type(titanic_groupby))

titanic_groupby = titanic_df.groupby('Pclass').count()
print(titanic_groupby)

titanic_groupby = titanic_df.groupby('Pclass')[['PassengerId', 'Survived']].count()
print(titanic_groupby)

print(titanic_df.groupby('Pclass')['Age'].agg([max, min]))

agg_format = { 'Age': 'max', 'SibSp': 'sum', 'Fare': 'mean' }
print(titanic_df.groupby('Pclass').agg(agg_format))
