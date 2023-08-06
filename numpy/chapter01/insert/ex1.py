# ndarray를 편리하게 생성하기 - arange, zeros, ones
import numpy as np


sequence_array = np.arange(10)
print(sequence_array)
print(sequence_array.dtype, sequence_array.shape)

zero_array = np.zeros((3, 2), dtype='int32')

print(zero_array)
print(zero_array.dtype, zero_array.shape)

one_array = np.ones((3, 2), dtype='int32')
print(one_array)
print(one_array.dtype, one_array.shape)