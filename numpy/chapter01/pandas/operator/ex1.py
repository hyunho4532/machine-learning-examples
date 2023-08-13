import pandas as pd

titanic_df = pd.read_csv('data/train.csv')

print('단일 칼럼 데이터 추출:\n', titanic_df['Pclass'].head(3))
print('\n여러 칼럼의 데이터 추출:\n', titanic_df[['Survived', 'Pclass']].head(3))
# print('[] 안에 숫자 index는 KeyError 오류 발생:\n', titanic_df[0])

print(titanic_df[0:2])

print(titanic_df[ titanic_df['Pclass'] < 3].head(3))
