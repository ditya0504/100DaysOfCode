from array import array

array1: object = array.array('i', [0, 1])
array2 = array.array('i', [2, 3, 4])

array1.extend(array2)
print(array1)  # array('i', [0, 1, 2, 3, 4])

print(array2)  # array('i', [2, 3, 4])
array2.extend([1, 2])
print(array2)  # array('i', [2, 3, 4, 1, 2])

array1 = array.array('i', [1])
array1.extend(set([0, 0, 0, 2]))
print(array1)  # array('i', [1, 0, 2])v