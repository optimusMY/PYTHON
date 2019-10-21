'''NUMPY is a MULTIDIMENSIONAL ARRAY LIB ALLOWS YOU TO WORK WITH MATRIX and MORE
if package is not installed yet, open cmd as admin-> type "pip install numpy" ->done
open pycharm and create new project then,
File->Settings->Project:numpy->Project Interpreter->Add button click with + ->type numpy -> install package->ok
now you can import the module
from numpy import *
'''

#TELUSKO NUMPY TUTORIAL   https://www.youtube.com/watch?v=Blzp9iuhZqo&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=34
#ProgrammingKnowledge TUTORIAL  https://www.youtube.com/watch?v=HAqMy9Usy00&list=PLS1QulWo1RIYWmvS03CzXh1MTSN9dbTnR&index=2


import numpy as np
#from numpy import *
from math import *

'''numpy.array is just a convenience function to create an ndarray; it is not a class itself.
You can also create an array using numpy.ndarray, but it is not the recommended way. From the docstring of numpy.ndarray:
Arrays should be constructed using array, zeros or empty ... 
The parameters given here refer to a low-level method (ndarray(...)) for instantiating an array.
'''

# if we copy with assignment like arr2 = arr1, you will see the addresses of arrays are the same, which means arr1 and arr2 is in the same physical address
arr1 = np.array([0, 3, 7, 5, -1, 2])
arr2 = arr1

print("address arr1 :", id(arr1))
print("address arr2 :", id(arr2))

# if we copy without assignment like arr2 = arr1, you will see the addresses of arrays are not the same, so use always copy method
arr2 = arr1.copy()
print("\n\naddress arr1 :", id(arr1))
print("address arr2 :", id(arr2))

'''linspace()--------------------------fills samples as linear '''

arrLin = np.linspace(1, 5, 10)  # 1=lowerbound  5=upperbound 10=num of samples in array
print("arrLin :", arrLin)


'''logspace()--------------------------'''


'''arange()--------------------------'''
arr3 = np.arange(1, 15, 3)  # start, stop, step   from 1 to 15 go by +4
print("arr3 :", arr3)
arr4 = np.arange(20, 5, -3)  # start, stop, step   from 20 to 5 go by -3
print("arr4 :", arr4)


'''zeros()--------------------------'''
arr5 = np.zeros(10, int)  # array of zeros with length 10
print("arr5 :", arr5)


'''ones()--------------------------'''
arr6 = np.ones(12, int)  # array of zeros with length 12
print("arr6 :", arr6)


# Two matrices are initialized by value
x = np.array([[1, 2], [4, 5]])
y = np.array([[7, 8], [9, 10]])
print("x :\n", x)
print("y :\n", y)
print("Addition of x and y: ")  #  add()is used to add matrices
print(np.add(x, y))
print("Subtraction of x and y : ")  # subtract()is used to subtract matrices
print(np.subtract(x, y))
print("Matrix Division : ")  # divide()is used to divide matrices
print(np.divide(x, y))
print("Multiplication of x and y: ")
print(np.multiply(x, y))
print("The product of x and y : ")
print(np.dot(x, y))
print("square root is : ")
print(np.sqrt(x))
print("The summation of elements : ")
print(np.sum(y))
print("The column wise summation  : ")
print(np.sum(y, axis=0))
print("The row wise summation: ")
print(np.sum(y, axis=1))
print("Matrix transposition : ")  # using "T" to transpose the matrix
print(x.T)


'''import array

arr1 = array.array('f', [1, 8, 5, 0, 7, 9, 5, 6, 3, 4])  # f float 4 byte
arr2 = array.array('d', [8, -1, 5, 15, 7, 6, 1, 9, 3, 2])  # d double 8 byte
arr3 = array.array('i', [8, -1, 5, 15, 7, 6, 1, 9, 3, 2])  # i signed int 2 byte
arr4 = array.array('l', [8, -1, 5, 15, 7, 6, 1, 9, 3, 2])  # l signed long 4 byte

print(arr1)

'''

List1 = [1, 2, 3, 4, 5]
NpArr = np.array(List1)
print("NpArr :", NpArr)

#for list datatype adding more elements
List1 = List1+[9, 10]  # this will make concatenation
print("List1 :", List1)
List1.append(11)  # this will make concatenation as well
print("List1 :", List1)
List1 = 2*List1  # this will make concatenation as well
print("List1 :", List1)
#in np.array , concatenation is not the same as lists
NpArr = NpArr + [6]
print("NpArr :", NpArr)

NpArr2 = np.array([1, 2, 3])
NpArr2 = NpArr2 + NpArr2   # vector operation handled in np array, so it wil be sum of each corresponding element
print("NpArr2 :", NpArr2)
NpArr2 = NpArr2**2   # vector operation handled in np array, so it will take square of each  element
print("NpArr2 :", NpArr2)
NpArr2 = np.sqrt(NpArr2)  # vector operation handled in np array, so it will take squareRoot of each  element
print("NpArr2 :", NpArr2)

NpArr2 = np.array([1, 2, 3])
NpArr2 = np.log(NpArr2)  # vector operation handled in np array, so it will take logaritma of each  element
print("NpArr2 :", NpArr2)
NpArr2 = np.array([1, 2, 3])
NpArr2 = np.exp(NpArr2)  # vector operation handled in np array, so it will take exponantialPower of each  element
print("NpArr2 :", NpArr2)


npA = np.array([1, 2, 3])  # 1 dimensional array
npB = np.array([[1, 2], [3, 4], [5, 6]])  # 2 dimensional array 3rows 2columns
print("npB :\n", npB)
print("npB[0] :", npB[0])
print("npB[0][0] :", npB[0][0])
print("npB[0,0] :", npB[0, 0])   # results in the same as npB[0][0]
print("Transpose of npB :", npB.T)
print("shape of  npB :", npB.shape)  # (rows , columns) of npB
print("num of dims of  npB :", npB.ndim)  # number of dimensions  of npB
print("num of all elements in  npB :", npB.size)  #num of all elements in  npB
print("npB datatype:", npB.dtype)  # datatype of the elements in npB

print("npB max :", npB.max())
print("npB min :", npB.min())
print("npB sum :", npB.sum())
print("npB vertical sum :", npB.sum(axis=0))  # returns sum of each columns as an array  (axis=0 is vertical sum)
print("npB horizontal sum :", npB.sum(axis=1))  # returns sum of each rows as an array  (axis=0 is horizontal sum)



npC = np.array([1, 2, 3], np.float64)  # 1 dimensional array
print("npC :\n", npC)
print("npC datatype :", npC.dtype)  # datatype of the elements in npC
print("npC datasize as bytes of the each elements :", npC.itemsize)  # datasize as bytes of the each elements in npC
npC = np.array([1, 2, 3], np.int32)  # 1 dimensional array
print("npC datasize as bytes of the each elements :", npC.itemsize)  # datasize as bytes of the each elements in npC


npD = np.zeros((2, 3), np.int32)
print("npD :\n", npD)
npD = np.ones((4, 2), np.int32)
print("npD :\n", npD)
npD = np.empty((5, 5), dtype=np.float)
print("npD :\n", npD)
npD = np.random.random((4, 3))  # it will create 4row3col 2Darray whose values are random between 0 and 1.0
print("npD :\n", npD)

npE = np.array([np.arange(1, 11, 1), np.arange(11, 21, 1), np.arange(21, 31, 1)])
print("npE :\n", npE)
print("npE[2, 3] :\n", npE[2, 3])

npE = npE.reshape((5, 6))
print("npE :\n", npE)
print("npE[2, 3] :\n", npE[2, 3])

npE = npE.reshape((3, -1))  # -1 means autoset the columnsize as to element number of array
print("npE :\n", npE)
print("npE[2, 3] :\n", npE[2, 3])

npK = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("npK 3x3:\n", npK)
npK = npK.flatten()
print("npK flatten :\n", npK)

npK = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("npK 3x3:\n", npK)
npK = npK.reshape((2, 2, 3))  # [array(2,3), array(2,3)] = 2 array_element array
print("npK reshaped 2,2,3 :\n", npK)



npF = np.zeros((3, 3))  # set 3x3 matrix filled with zeros
print("npF :\n", npF)
npG = np.ones((1, 3))  # set 1x3 matrix filled with ones
print("npG :\n", npG)
npV = np.vstack((npF, npG))  # combine two matrices in together vertically
print("npV :\n", npV)
npV = np.vstack((npG, npF))  # combine two matrices in together vertically
print("npV :\n", npV)
npI = np.array([3, 3, 3, 3]).reshape((4, 1))
print("npI :\n", npI)
npH = np.hstack((npV, npI))
print("npH :\n", npH)
npH = np.hstack((npI, npV))
print("npH :\n", npH)

npJ = np.hsplit(npH, 2)
print("npJ :\n", npJ)
npJ = np.vsplit(npH, 2)
print("npJ :\n", npJ)



''' YOU CAN NOT RESHAPE THE ARRAY BY SETTING SIZE WHICH EXCEEDS NUMBER OF ELEMENTS OF ARRAY
FOR EXAMPLE , npE is 30 element array, so you can reshape as 30x1 or 6x5 or 3x10 etc. but you can not set size as mxn !=30
if you try to reshape npE as  (8,4) it results in error.'''


'''
A = np.array([[1,-1,2],[3,2,0]])
Vectors are just arrays with a single column.


v = np.transpose(np.array([[2,1,3]]))  is equal with      v = np.array([[2],[1],[3]])
numpy overloads the array index and slicing notations to access parts of a matrix. For example, to print the bottom right entry in the matrix A we would do

print(A[1,2])

To slice out the second column in the A matrix we would do

col = A[:,1:2]


The first slice selects all rows in A, while the second slice selects just the middle entry in each row.

To do a matrix multiplication or a matrix-vector multiplication we use the np.dot() method.

w = np.dot(A,v)

numpy.vdot(vector_a, vector_b) returns the dot product of vectors a and b.
 If first argument is complex the complex conjugate of the 
 first argument(this is where vdot() differs working of dot() method) is used for the calculation of the dot product.



_______Solving systems of equations with numpy_______
We start by constructing the arrays for A and b.

A = np.array([[2,1,-2],[3,0,1],[1,1,-1]])
b = np.transpose(np.array([[-3,5,-2]])
To solve the system we do

x = np.linalg.solve(A,b)

'''
MA = np.array([[2, 1, -2], [3, 0, 1], [1, 1, -1]])
Mb = np.transpose(np.array([[-3, 5, -2]]))

Mx = np.linalg.solve(MA, Mb)
print(Mx)

#To do a matrix multiplication or a matrix-vector multiplication we use the np.dot() method.  w = np.dot(A,v)
#if Mx is multiplied by Ma , the result must be Mb
Mresult = np.dot(MA, Mx)
print("Mresult :\n", Mresult)




mxA = np.array([[1, -1, 2],[3, 2, 0]])
print("mxA :\n", mxA)
mxB = mxA[:, 1:2]  # second column of mxA
print("mxB is second column of mxA :\n", mxB)



















