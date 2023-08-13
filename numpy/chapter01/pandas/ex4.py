import pandas as pd

# 원본 파일 다시 로딩
titanic_of = pd.read_csv('data/train.csv')

# Index 객체 추출
indexes = titanic_of.index
print(indexes)

# Index 객체를 실제 값 array로 변환
print('Index 객체 array값: \n', indexes.value_counts())

print(type(indexes.values))
print(indexes.values.shape)
print(indexes[:5].values)
print(indexes.values[:5])
print(indexes[6])

series_fair = titanic_of['Fare']
print('Fair Series max 값:\n', series_fair.max())
print('Fair Series sum 값:\n', series_fair.sum())
print('sum() Fair Series:\n', sum(series_fair))
print('Fair Series + 3:\n', (series_fair + 3).head(3))

titanic_reset_of = titanic_of.reset_index(inplace=False)
print(titanic_reset_of.head(3))

print('#### before reset_index ####')
value_counts = titanic_of['Pclass'].value_counts()
print(value_counts)
print('value_counts 객체 변수 타입: ', type(value_counts))

new_value_counts = value_counts.reset_index(inplace=False)
print('#### after reset_index ####')
print(new_value_counts)
print('new_value.counts 객체 변수 타입: ', type(new_value_counts))
