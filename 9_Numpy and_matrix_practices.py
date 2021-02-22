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

m_c = np.insert(m, [5], [[1], [2], [3], [4], [5], [6], [7]], 1) # 1 means column

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
A = np.arange(4)    # single array creating
print('A = ', A)

B = np.arange(12).reshape(3, 4)     # n-d array creating
print('B = ', B)




