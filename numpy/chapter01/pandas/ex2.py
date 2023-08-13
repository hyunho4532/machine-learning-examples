import numpy as np
import pandas as pd

col_name1 = ['col1']
list1 = [1, 2, 3]
array1 = np.array(list1)
print('array1 shape: ', array1.shape)

df_list1 = pd.DataFrame(list1, columns=col_name1)
print('1차원 리스트로 만든 DataFrame:\n', df_list1)

df_array1 = pd.DataFrame(array1, columns=col_name1)
print('1차원 ndarray로 만든 DataFrame:\n', df_array1)


# 2차원 형태의 데이터를 기반으로 DataFrame 생성
col_name2 = [ 'col1', 'col2', 'col3' ]

list2 = [[1, 2, 3], [11, 12, 13]]

array2 = np.array(list2)
print('array2 shape: ', array2.shape)
df_list2 = pd.DataFrame(list2, columns=col_name2)
print('2차원 리스트로 만든 DataFrame: \n', df_list2)

df_array2 = pd.DataFrame(array2, columns=col_name2)
print('2차원 ndarray로 만든 DataFrame:\n', df_array2)

dict1 = { 'col1': [1, 11], 'col2': [2, 22], 'col3': [3, 33] }
df_dict = pd.DataFrame(dict1)
print('딕셔너리로 만든 DataFrame: \n', df_dict)

array3 = df_dict.values
print('df_dict.values 타입:', type(array3), 'df_dict.values shape: ', array3.shape)
print(array3)

# DataFrame을 리스트로 변환
list3 = df_dict.values.tolist()
print('df_dict.values.tolist() 타입:', type(list3))
print(list3)

# DataFrame을 딕셔너리로 변환
dict3 = df_dict.to_dict('list')
print('\n df_dict.to_dict() 타입: ', type(dict3))
print(dict3)
