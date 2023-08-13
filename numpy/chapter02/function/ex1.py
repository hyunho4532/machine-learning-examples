import pandas as pd

def get_square(a):
    return a ** 2

print('3의 제곱은:', get_square(3))

lambda_square = lambda x : x ** 2

print('3의 제곱은:', lambda_square(3))

a = [1, 2, 3]
squares = map(lambda x : x ** 2, a)

print(list(squares))


titanic_df = pd.read_csv('data/train.csv')

titanic_df['Name_len'] = titanic_df['Name'].apply(lambda x : len(x))
print(titanic_df[[ 'Name', 'Name_len' ]].head(3))

titanic_df['Child_Adult'] = titanic_df['Age'].apply(lambda x : 'Child' if x <= 15 else 'Adult')
print(titanic_df[['Age', 'Child_Adult']].head(8))

titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x : 'Child' if x <= 15 else ('Adult' if x <= 60 else 'Elderly'))
print(titanic_df['Age_cat'].value_counts)