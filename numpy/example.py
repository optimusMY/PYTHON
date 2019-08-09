'''NUMPY is a MULTIDIMENSIONAL ARRAY LIB ALLOWS YOU TO WORK WITH MATRIX and MORE
if package is not installed yet, open cmd as admin-> type "pip install numpy" ->done
open pycharm and create new project then,
File->Settings->Project:numpy->Project Interpreter->Add button click with + ->type numpy -> install package->ok
now you can import the module
from numpy import *
'''

#import numpy as np
from numpy import *
from math import *


# if we copy with asignment like arr2 = arr1, you will see the adresses of arrays are the same, which means arr1 and arr2 is in the same physical adress
arr1 = array([0, 3, 7, 5, -1, 2])
arr2 = arr1

print("address arr1 :", id(arr1))
print("address arr2 :", id(arr2))

# if we copy without asignment like arr2 = arr1, you will see the adresses of arrays are not the same, so use always copy method
arr2 = arr1.copy()
print("address arr1 :", id(arr1))
print("address arr2 :", id(arr2))

'''linspace()--------------------------'''


'''logspace()--------------------------'''


'''arange()--------------------------'''
arr3 = arange(1, 15, 3)  # start, stop, step   from 1 to 15 go by +4
print("arr3 :", arr3)
arr4 = arange(20, 5, -3)  # start, stop, step   from 20 to 5 go by -3
print("arr4 :", arr4)


'''zeros()--------------------------'''
arr5 = zeros(10, int)  # array of zeros with length 10
print("arr5 :", arr5)


'''ones()--------------------------'''
arr6 = ones(12, int)  # array of zeros with length 12
print("arr6 :", arr6)





'''import array

arr1 = array.array('f', [1, 8, 5, 0, 7, 9, 5, 6, 3, 4])  # f float 4 byte
arr2 = array.array('d', [8, -1, 5, 15, 7, 6, 1, 9, 3, 2])  # d double 8 byte
arr3 = array.array('i', [8, -1, 5, 15, 7, 6, 1, 9, 3, 2])  # i signed int 2 byte
arr4 = array.array('l', [8, -1, 5, 15, 7, 6, 1, 9, 3, 2])  # l signed long 4 byte

print(arr1)

'''





https://www.youtube.com/watch?v=Blzp9iuhZqo&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=34











