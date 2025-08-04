import numpy as np

# Array Creation
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Array 1: {array1}")  # [1 2 3 4 5]
print(f"Array 2: {array2}")  # [[1 2 3] [4 5 6]]
print(f"Shape of Array 1: {array1.shape}")  # (5,)

# Array operations
print(f"Array 1 Transpose: {array1.T}")  # [1 2 3 4 5] (1D array remains unchanged)
print(f"Array 2 transpose:{array2.T}")  # [[1 4] [2 5] [3 6]]
print(f"Array 1 Reshape: {array1.reshape(5,1)}")  
# [[1] [2] [3] [4] [5]]
print(f"result {array1*2}")  # [ 2  4  6  8 10]
print(f"result {array2**2}")  
# [[ 1  4  9]
#  [16 25 36]]
# print(f"result {array1+array2}")  # ❌ Can't broadcast together
print(f"result {array1/2}")  # [0.5 1.  1.5 2.  2.5]
print(f"result {array2/2}")  
# [[0.5 1.  1.5]
#  [2.  2.5 3. ]]
print(f"result {array1-2}")  # [-1  0  1  2  3]

# Mathematical functions
srt = np.sort(array1)
print(f"Sorted Array 1: {srt}")  # [1 2 3 4 5]
mean = np.mean(array2)
print(f"Mean of Array 2: {mean}")  # 3.5
sqrt = np.sqrt(array2)
print(f"Square Root of Array 2: {sqrt}")  
# [[1.         1.41421356 1.73205081]
#  [2.         2.23606798 2.44948974]]
cube = np.power(array1, 3)
print(f"Cube of Array 1: {cube}")  # [  1   8  27  64 125]
Stdd = np.std(array2)
print(f"Standard Deviation of Array 2: {Stdd}")  # 1.707825127659933
print(f"Sum of Array 1: {np.sum(array1)}")  # 15

# Array Indexing and Slicing
print(f"Element at index 2 in Array 1: {array1[2]}")  # 3
print(f"Elements from index 1 to 3 in Array 1: {array1[1:4]}")  # [2 3 4]
print(f"Last elements ao array2:{array2[-1]}")  # [4 5 6]

# 2D array indexing
print(f"element at row 0,col1 :{array2[0,1]}")  # 2
print(f"element at row 1,col2 :{array2[1,2]}")  # 6
print(f"First row: {array2[0, :]}")  # [1 2 3]
print(f"First column: {array2[:, 0]}")  # [1 4]

# Useful array creation functions
zeros = np.zeros((2, 3))
print(f"zeros array: {zeros}")  
# [[0. 0. 0.]
#  [0. 0. 0.]]
ones = np.ones((2, 3))
print(f"ones array: {ones}")  
# [[1. 1. 1.]
#  [1. 1. 1.]]
rang = np.arange(0, 10, 2)
print(f"Range array: {rang}")  # [0 2 4 6 8]
linspace = np.linspace(1, 5, 5)
print(f"Linspace array: {linspace}")  # [1. 2. 3. 4. 5.]

# Broadcasting
arr1 = np.array([1, 2]).reshape(2, 1)
arr2 = np.array([[4, 5, 6], [8, 9, 10]])
res = arr1 + arr2
print(res)  
# [[ 5  6  7]
#  [10 11 12]]

# Stacking and Concatenation
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
stacked = np.vstack((arr3, arr4))
print(f"Stacked Array:\n{stacked}")  
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
concatenated = np.concatenate((arr3, arr4), axis=0)
print(f"Concatenated Array:\n{concatenated}")  
# Same as stacked

# Boolean indexing
arr = np.array([1, 2, 3, 4, 5])
bool_idx = arr > 2
print(f"Boolean Indexing Result: {arr[bool_idx]}")  # [3 4 5]

# np.where
arr5 = np.array([1, 2, 3, 4, 5])
print(np.where(arr5 > 3, "High", "Low"))  
# ['Low' 'Low' 'Low' 'High' 'High']

# np.unique
arr6 = np.array([1, 2, 2, 3, 4, 4, 5])
unique_elements = np.unique(arr6)
print(f"Unique elements in arr6: {unique_elements}")  # [1 2 3 4 5]

array2 = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(array2, axis=0))  # [5 7 9]
print(np.sum(array2, axis=1))  # [ 6 15]

# np.dot
array3 = np.array([[1, 2], [3, 4]])
array4 = np.array([[5, 6], [7, 8]])
dot_product = np.dot(array3, array4)
print(f"Dot product of array3 and array4:\n{dot_product}")  
# [[19 22]
#  [43 50]]

# random module
np.random.seed(0)
random_array = np.random.rand(3, 3)
print(f"Random Array:\n{random_array}")  
# [[0.5488135  0.71518937 0.60276338]
#  [0.54488318 0.4236548  0.64589411]
#  [0.43758721 0.891773   0.96366276]]
