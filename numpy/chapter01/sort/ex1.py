import numpy as np

org_array = np.array([3, 1, 9, 5])
print('원본 행렬: ', org_array)

sort_array1 = np.sort(org_array)
print('np.sort( ) 호출 후 반환된 정렬 행렬: ', sort_array1)

print('np.sort( ) 호출 후 원본 정렬: ', org_array)

sort_array2 = org_array.sort()
print('org_array.sort( ) 호출 후 반환된 행렬: ', sort_array2)
print('org_array.sort( ) 호출 후 원본 행렬: ', org_array)

sort_array1_desc = np.sort(org_array)[::-1]
print('내림차순으로 정렬: ', sort_array1_desc)

array2d = np.array([[8, 12], [7, 1]])

sort_array2d_axis0 = np.sort(array2d, axis=0)
print('로우 방향으로 정렬:\n', sort_array2d_axis0)

sort_array2d_axis1 = np.sort(array2d, axis=1)
print('칼럼 방향으로 정렬:\n', sort_array2d_axis1)

org_array = np.array([3, 1, 9, 5])
sort_indeices = np.argsort(org_array)
print(type(sort_indeices))
print('행렬 정렬 시 원본 행렬의 인덱스: ', sort_indeices)

org_array = np.array([3, 1, 9, 5])
sort_indeices_desc = np.argsort(org_array)[::-1]
print('행렬 내림차순 정렬 시 원본 행렬의 인덱스: ', sort_indeices_desc)

name_array = np.array([ 'John', 'Mike', 'Saren', 'Kate', 'Samuel' ])
score_array = np.array([ 70, 85, 94, 78, 40])

sort_indeices_asc = np.argsort(score_array)
print('성적 오름차순 정렬 시 score_array의 인덱스: ', sort_indeices_asc)
print('성적 오름차순으로 name_array의 이름 출력: ', name_array[sort_indeices_asc])