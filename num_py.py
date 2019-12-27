import numpy as np

my_list = [1,2,3,4,5]
np_array = np.array (my_list)
print(np_array)

np_array1 = np.array ([[7,8,9],[10,11,12]])
print(np_array1)

print(np_array1.shape) #Print Dimension

print("Range")
np_range = np.arange(0,36,2)
print(np_range)

print("Reshape to (3, 6)")
np_reshape = np_range.reshape(3,6)
print(np_reshape)

print("Line Space (0, 4, 9) with resize")
np_lnspc = np.linspace(0,4,9)
np_lnspc.resize(3,3)   #Resize updates same object.
print(np_lnspc)

print("Line Space (0, 4, 9) with reshape")
np_lnspc1 = np.linspace(0,4,9).reshape(3,3)  #Reshape creates a new object.
print(np_lnspc1)

print("One")
print(np.ones((3,3)))

print("Zeroe")
print(np.zeros((3,3)))

print("Eye")
print(np.eye(3))

print("Diag for 4,5,6,7")
print(np.diag(np.array([4,5,6,7])))

print("array with * operator")
print(np.array([4,5,6,7] * 3))

print("array with repeat")
print(np.repeat([4,5,6,7], 3))

print("Ones array and vertical stacking the same")
ones = np.ones([2,3], int)
print(ones)
vertical_stack = np.vstack([ones, ones * 2])
print(vertical_stack)

print("Ones array and horizontal stacking the same")
horizontal_stack = np.hstack([ones, ones * 2])
print(horizontal_stack)

x = np.array([[1,2],[1,2]])
y = np.array([[4,5],[4,5]])

print("Array X")
print(x)
print("Array Y")
print(y)
print("Array X * Y")
print(x * y)
print("Array X + Y")
print(x + y)

print("Array X**2")
print(x**2)

print("Array X DOT Y")
print(x.dot(y))

print("Transpose of an Array X")
print(x.transpose())

print("Data Type of X")
print(x.dtype)

print("Change Type of X to Float")
print(x.astype('f').dtype)

a=np.array([-4.,-2,1,3,5])
print ("Sum %d, Min %d, Max %d, Mean %f, Standard Deviation %f" %(a.sum(),a.min(),a.max(),a.mean(),a.std()))

print ("Max Index %d, Min Index %d" %(a.argmax(), a.argmin()))

squares = np.arange(0,13) ** 2
print(squares)
print(squares[0], squares[1], squares[0:3], squares[-4:])

two_d_array = np.arange(0,36).reshape([6,6])
print(two_d_array)

print(two_d_array[2, 2])    # Row 2 Column 2
print(two_d_array[3, 3:6])  # Third row and columns 3 to 5
print(two_d_array[-1, 3:6]) # Last row and columns 3 to 5
print(two_d_array[:2, :-1]) # First two rows and all columns except last.
print(two_d_array[-1, ::2]) # Every second element from last row
print(two_d_array[two_d_array > 25])   # Conditional check

two_d_array[two_d_array > 30] = 30
print(two_d_array)

array_slice = two_d_array[:3,:3]
array_slice[:] = 0   #It changes original array : two_d_array. 
print(array_slice)
print(two_d_array)

#To avoid accidental modification of original array create new copy.
print("New copy of array")
array_slice2 = two_d_array[3:,3:].copy()
print(array_slice2)
array_slice2[:]=0
print(array_slice2)
print(two_d_array)

print("Iterating Arrays with Enumerate : ")
two_d_array_copy = (two_d_array.copy() ** 2)[:,:3]

for i,row in enumerate(two_d_array):
    print(i,row)

for i,row in enumerate(zip(two_d_array, two_d_array_copy)):
    print(i,row)
