import numpy as np

a = np.array([['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
              ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
              ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
              ['Sun', 13, 15, 19, 16]])

m = np.reshape(a, (7, 5))

print("Matrix and its specific values: \n")
print(m)
print("column of 2 values: ", m[2])
print("values of m[4][3]: ", m[4][3])

print("\nAdd rows in a matrix\n")

m_r = np.append(m, [['Avg', 12, 15, 13, 11]], 0)  # 0 means row

print(m_r)

print("\nAdd column in a matrix\n")

m_c = np.insert(m, [5], [[1], [2], [3], [4], [5], [6], [7]], 1)  # 1 means column

print(m_c)

print("Deleting a row from matrix: ")

m = np.delete(m, [2], 0)
print(m)

print("Deleting a column from matrix: ")

m = np.delete(m, [2], 1)
print(m)

print("Update a row in a matrix: ")

m[2] = ['Thu', 0, 0, 0]
print(m)

print("\n Create array of zeros and ones: \n")

zeros_array = np.zeros((2, 3), dtype=np.int32)
print(zeros_array)

ones_array = np.ones((3, 5), dtype=np.int32)
print(ones_array)

print(" use arrange() and shape(): ")
A = np.arange(4)  # single array creating
print('A = ', A)

B = np.arange(12).reshape(3, 4)  # n-d array creating
print('B = ', B)

print("\n Matrix Operations: \n")

A = np.array([[2, 4], [5, 6]])
B = np.array([[9, -3], [3, 6]])
C = A + B
print('Addition: \n', C)

A = np.array([[3, 6, 7], [5, -3, 0]])
B = np.array([[1, 1], [2, 1], [3, -3]])
C = A.dot(B)
print('Multiplication: \n', C)

print('Transpose: Convert row to column and column to row \n')
A = np.array([[1, 1], [2, 1], [3, -3]])
print(A.transpose())

print("Access rows of a matrix: ")

A = np.array([[1, 4, 5, 12],
              [-5, 8, 9, 0],
              [-6, 7, 11, 19]])
print(A)

print("Row data: ")
print("A[0] =", A[0])   # First Row
print("A[2] =", A[2])   # Third Row
print("A[-1] =", A[-1]) # Last Row (3rd row in this case)

print("\ncolumn data: ")
print("A[:,0] =", A[:, 0])    # First Column
print("A[:,3] =", A[:, 3])    # Fourth Column
print("A[:,-1] =", A[:, -1])  # Last Column (4th column in this case)


