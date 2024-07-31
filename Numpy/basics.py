# import numpy
import numpy as np

arr = np.arange(1, 10)
print(arr)
arr = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])
arr3 = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print(np.diag(arr2))
print(np.diag(np.fliplr(arr2)))



print(arr.ndim)
print(arr2.ndim)
print(arr3.ndim)

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)      # z = [ 5  7  9 11]


# indexing =====================================
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])
print('Last element from 2nd dim: ', arr[1, -1])
print(arr[1, 1:4])
print(arr[0:2, 1:4])
print(arr.dtype)

# For List
lst = [[1,2,3,4,5], [6,7,8,9,10]]
print(lst[1][1:4])
print(lst[0:2][1:4])

# Datatype  ===================================
arr = np.array([1, 2, 0, 4], dtype='i4')

# Cast to Unicode string
newarr = arr.astype('U')

print(newarr)
print(newarr.dtype)

newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

# copy and view ===================================
x1 = arr.copy()
x2 = arr.view()
arr[0] = 42
print(x1)
print(x2)


# shape of array =====================================
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)


# Reshape 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)      # Reshape as 4*3 size. Reshape dimention n*m= size of element
# newarr = arr.reshape(3, 3)      # will raise error because 3*3 != 12
print(arr.reshape(2, 6).base)    # Reshaped array is the view of the original array


# Itterate============================================
# nditer is used to iterate over very lower dimentional element
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)    # 1,3,5,7

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

# ndenumerate is used to get the nd-index of element and lower dimentional element
for idx, x in np.ndenumerate(arr):
  print(idx, x)


# Join ===================================================
# joining arrays using concatenate
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)   # [[1 2 5 6][3 4 7 8]]


# joining arrays using stack function
arr = np.stack((arr1, arr2), axis=1)   # [[[1 2][5 6]][[3 4][7 8]]]

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis = 0)  # [[1 2 3][4 5 6]]      same as vstack
arr = np.stack((arr1, arr2), axis = 1)  # [[1 4][2 5][3 6]]     same as dstack
arr = np.hstack((arr1, arr2))           # [1 2 3 4 5 6]         same as concatenate
arr = np.vstack((arr1, arr2))           # [[1 2 3][4 5 6]]
arr = np.dstack((arr1, arr2))           # [[[1 4][2 5][3 6]]]


# Splitting  =======================================
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)         # [[1 2][3 4][5 6]]
newarr = np.array_split(arr, 4)         # [[1 2][3 4][5][6]]
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
newarr = np.array_split(arr, 2, axis=0)     # [[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]
newarr = np.array_split(arr, 2, axis=1)     # [[1, 2], [4, 5],[7, 8], [10, 11]][[ 3],[ 6],[ 9],[12]]


# Array searching =================================
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)                # [3,5,6]

x = np.where(arr%2 == 0)

# Find the indexes where the value 7 should be inserted in sorted array
arr = np.array([6, 7, 8, 9, 11])
x = np.searchsorted(arr, 7)
print(x)                                 # Prints 1

x = np.searchsorted(arr, 7, side='right')  # Prints 2

# Search for more than one value
x = np.searchsorted(arr, [6, 10, 12])     # Prints [0, 4, 6]


# Soting =============
newarr = np.sort(arr)


# Filtering ==================================
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)                       # Prints [41 43]

arr = np.array([1, 2, 3, 4, 5, 6, 7])
newarr = arr[arr % 2 == 0]
print(newarr)                       # Prints [2 4 6]