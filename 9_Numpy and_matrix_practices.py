import numpy as np
import math

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

<<<<<<< HEAD
print("universal functions: ")
a = np.arange(3)
b = np.exp(a)
print(b)
c = np.sqrt(a)
print(c)
=======
print("\n Matrix Operations: \n")

A = np.array([[2, 4], [5, 6]])
B = np.array([[9, -3], [3, 6]])
C = A + B
print('Addition: \n', C)
>>>>>>> master

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

print("\n Slicing of a matrix: \n")
letters = np.array([1, 3, 5, 7, 9, 7, 5])
print(letters)

print("3rd to 5th elements: ", letters[2:5])        # Output: [5, 7, 9]

print("1st to 4th elements: ", letters[:-5])        # Output: [1, 3]

print("6th to last elements: ", letters[5:])         # Output:[7, 5]

print("1st to last elements: ", letters[:])          # Output:[1, 3, 5, 7, 9, 7, 5]

print("reversing a list: ", letters[::-1])          # Output:[5, 7, 9, 7, 5, 3, 1]

A = np.array([[1, 4, 5, 12, 14],
    [-5, 8, 9, 0, 17],
    [-6, 7, 11, 19, 21]])

print(A)
print("two rows, four columns: ", A[:2, :4])
print("first row, all columns: ", A[:1, ])
print("all rows, second column: ", A[:, 2])
print("all rows, third to the fifth column", A[:, 2:5])

print("use range function: ")
a = np.arange(10, 30, 5) # range between 10 to 30 and difference 5
b = np.arange(0, 2, 0.3)
print("A: {0}, type: {1}".format(a, type(a)))
print("B: ", b)

print("use linspace: ")
a = np.linspace(0, 2, 9)  # total 9 numbers from 0 to 2
print(a)

print("reshape of an array: ")
a = np.arange(12).reshape(3, 4) # for 2d as matrices
print(a)
b = np.arange(24).reshape(2, 3, 4) # for 3d as lists of matrices
print(b)

print("basic operations: ")
a = np.ones(3, dtype=np.int32)
print(a)

b = np.linspace(0, math.pi, 3)
print(b)
c = a+b
print(c)
d = np.exp(c*1j)
print(d)

print("random")
a = np.random.random((2, 3))
print(a)

