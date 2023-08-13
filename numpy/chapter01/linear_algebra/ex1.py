import numpy as np

A = np.array( [[1, 2, 3], [4, 5, 6]] )
B = np.array( [[7, 8], [9, 10], [11, 12]])
C = np.array( [[2, 3], [4, 5], [6, 7]])

dot_product = np.dot(A, C)
print('행렬 내적 결과:\n', dot_product)

A = np.array( [[1, 2], [3, 4]])

transpose_matA = np.transpose(A)
print('A의 전치 행렬:\n', transpose_matA)

B = np.array( [[1, 2], [3, 4], [5, 6]])

transpose_matB = np.transpose(B)
print('B의 전치 행렬:\n', transpose_matB)