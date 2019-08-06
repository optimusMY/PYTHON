strx = 'Hello World!'

print(strx)  # Prints complete string
print(strx[0])  # Prints first character of the string
print(strx[2:5])  # Prints characters starting from 3rd to 5th
print(strx[2:])  # Prints string starting from 3rd character
print(strx * 2)  # Prints string two times
print(strx + "TEST")  # Prints concatenated string

print('C:\\nowhere')  # result  C:\nowhere
print(r'C:\\nowhere')  # result C:\\nowhere

var1 = 'Hello World!'
var2 = "Python Programming"
print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

var1 = 'Hello World!'
print("Updated String :- ", var1[:6] + 'Python')

print("\nMy name is %s and weight is %d kg!" % ('Zara', 21))

person1 = "ali"
person2 = "AYSE"
person3 = "mustafa yetis"

print(person1 + " " + person2 + "'yi seviyor \n")

print(person1.upper() + '\n')
print(person2.lower() + '\n')

print(person2.islower())

print(person1.index('l'))
print(person2.index('S'))

print(person3.index("yetis"))

print(person3.replace("mustafa", "salih ertugrul"))

print(len(person3))

print(person3[5])

# ---------------------------------------------------------------------------------
print(3 * 4 - 5 + 12.5 / 2.5)

sayi1 = 123.66
sayi2 = -125.77

print(sayi1 - sayi2)
print(abs(sayi2))
print(pow(sayi1, 2))
print(round(sayi2))

from math import *

print(floor(sayi1))
print(ceil(sayi1))
print(sqrt(36))

# ---------------------------------------------------------------------------------
# name = input("what is your name?")
# print("nice to meet you " + name)

# age = input("how old are you?")
# print(name + " is " + age + " years old")


# ---------------------------------------------------------------------------------
# multiline statement
item_one = 1.5
item_two = 2.5
item_three = 3
total = item_one + \
        item_two * \
        item_three
print(total)

paragraph = """This is a paragraph. 
            It is made up of multiple lines and sentences."""
print(paragraph)

'''
This is a multiline
comment.
'''

'''The semicolon ( ; ) allows multiple statements on a single line 
given that no statement starts a new code block.'''
import sys;

x = 'foo';
sys.stdout.write(x + '\n')

# ------------------------------------------------------------------------------------
# Python allows you to assign a single value to several variables simultaneously.
a = b = c = 1
print(a, b, c)  # comma ','  used to add a space betweeen terms in string

# ---------------------------------------------------------------------------------
'''Lists are the most versatile of Python's compound data types.
A list contains items separated by commas and enclosed within square brackets ([]).
To some extent, lists are similar to arrays in C.
One of the differences between them is 
that all the items belonging to a list can be of different data type.
The values stored in a list can be accessed using the slice operator ([ ] and [:]) 
with indexes starting at 0 in the beginning of the list and working their way to end -1. 
The plus (+) sign is the list concatenation operator, 
and the asterisk (*) is the repetition operator.'''
list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)  # Prints complete list
print(list[0])  # Prints first element of the list
print(list[1:3])  # Prints elements starting from 2nd till 3rd
print(list[2:])  # Prints elements starting from 3rd element
print(tinylist * 2)  # Prints list two times
print(list + tinylist)  # Prints concatenated lists

# ------------------------------------------------------------------------------------
'''A tuple is another sequence data type that is similar to the list.
A tuple consists of a number of values separated by commas. 
Unlike lists, however, tuples are enclosed within parenthesis.
The main difference between lists and tuples are 
− Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed,
while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. 
Tuples can be thought of as read-only lists.'''
tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print('\n\n')
print(tuple)  # Prints complete tuple
print(tuple[0])  # Prints first element of the tuple
print(tuple[1:3])  # Prints elements starting from 2nd till 3rd
print(tuple[2:])  # Prints elements starting from 3rd element
print(tinytuple * 2)  # Prints tuple two times
print(tuple + tinytuple)  # Prints concatenated tuple

# ---------------------------------------------------------------------------------------
'''Python's dictionaries are kind of hash-table type.
They work like associative arrays or hashes found in Perl and 
consist of key-value pairs. A dictionary key can be almost any Python type,
but are usually numbers or strings. 
Values, on the other hand, can be any arbitrary Python object.
Dictionaries are enclosed by curly braces ({ }) 
and values can be assigned and accessed using square braces ([]).'''
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print('\n\n')
print(dict['one'])  # Prints value for 'one' key
print(dict[2])  # Prints value for 2 key
print(tinydict)  # Prints complete dictionary
print(tinydict.keys())  # Prints all the keys
print(tinydict.values())  # Prints all the values

# ---------------------------------------------------------------------------------
'''Data Type Conversion
you may need to perform conversions between the built-in types. To convert between types,
you simply use the type-names as a function.
There are several built-in functions to perform conversion from one data type to another.
These functions return a new object representing the converted value.

int(x [,base]) Converts x to an integer. The base specifies the base if x is a string.

float(x) Converts x to a floating-point number.

complex(real [,imag]) Creates a complex number.

str(x) Converts object x to a string representation.

repr(x) Converts object x to an expression string.

eval(str) Evaluates a string and returns an object.

tuple(s) Converts s to a tuple.

list(s) Converts s to a list.

set(s) Converts s to a set.

dict(d) Creates a dictionary. d must be a sequence of (key,value) tuples.

frozenset(s) Converts s to a frozen set.

chr(x) Converts an integer to a character.

unichr(x) Converts an integer to a Unicode character.

ord(x) Converts a single character to its integer value.

hex(x) Converts an integer to a hexadecimal string.

oct(x) Converts an integer to an octal string. '''

print('\n\n')
str_fp = "0.707"
fp = 1 / float(str_fp)
print(fp)

comp1 = complex(fp, 3)
print(comp1)

# ---------------------------------------------------------------------------------
''' OPERATORS
Arithmatic Operators
standart + - * / % are similar to C lang
** is exponent operator
x**y is  x^y operation gives same result with pow(x,y)
// is floor division operator
x//y  gives same result with floor(x/y)


Comparison Operators
standart == != < > <= >= are similar to C lang


Assignment operators
c += a is equivalent to c = c + a
c -= a is equivalent to c = c - a
c *= a is equivalent to c = c * a
c /= a is equivalent to c = c / a
c %= a is equivalent to c = c % a
c **= a is equivalent to c = c ** a
c //= a is equivalent to c = c // a


Bitwise Operators
& is AND operator
| is OR operator
^ is XOR operator
~ is TOGGLE operator
<< is Left Shift Operator
>> is Right Shift Operator


Logical Operators
and   is Logical AND  ,   (True and False) returns  False
or   is Logical OR  ,   (True or False) returns  True
not  is Logical NOT,    not(True) returns  False


Membership Operators (for string List or Tuple)
in  operator returns True when the value found in the sequence(list String or Tuple)
not in operator returns True when the value NOT found in the sequence(list String or Tuple)

Identity Operators
Identity operators compare the memory locations of two objects.
is       returns True if the variables on either side of the operator point to the same object and false otherwise.
is not   returns False if the variables on either side of the operator point to the same object and true otherwise.

x is y, here is returns 1 if id(x) equals id(y).

'''
foolean1 = True
foolean2 = False

print('\n\n')
num1 = 36
print('decimal:', num1)
print('hexadecimal:', hex(num1))
print('octal:', oct(num1))
print('binary:', bin(num1))
print('right shift by 2 step:', bin(num1 >> 2))
print('left shift by 2 step:', bin(num1 << 2))
print('toggle :', bin(~num1))

tmplist = ['bir', 1, 'iki', 2.0]
print('bir' in tmplist)  # returns True if 'bir' exist in the tmplist
print('iki' not in tmplist)  # returns False because 'iki' exist in the tmplist
print('dort' in tmplist)  # returns False because 'dort' not exist in the tmplist
print(3 not in tmplist)  # returns True because 3 not exist in the tmplist

# ---------------------------------------------------------------------------------
'''decision making
if expression:
   statement(s)

else:
   statement(s)

---------------------
if expression1:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   else
      statement(s)
elif expression4:
   statement(s)
else:
   statement(s)   


LOOPS

while expression:
   statement(s)

count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1

print ("Good bye!")   


The range() function
The built-in function range() is the right function to iterate over a sequence of numbers.
It generates an iterator of arithmetic progressions.
Example
>>> range(5)
range(0, 5)
>>> list(range(5))
[0, 1, 2, 3, 4] 

Example
range() generates an iterator to progress integers starting with 0 upto n-1.
 To obtain a list object of the sequence, it is typecasted to list(). 
 Now this list can be iterated using the for statement.

>>> for var in list(range(5)):
   print (var)  

for letter in 'Python':     # traversal of a string sequence
   print ('Current Letter :', letter)
print()
fruits = ['banana', 'apple',  'mango']

for fruit in fruits:        # traversal of List sequence
   print ('Current fruit :', fruit)

print ("Good bye!")

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('Current fruit :', fruits[index])

print ("Good bye!")  


Using else Statement with Loops
Python supports having an else statement associated with a loop statement.

If the else statement is used with a for loop, the else block is executed 
only if for loops terminates normally (and not by encountering break statement).

If the else statement is used with a while loop, 
the else statement is executed when the condition becomes false.

Example
The following example illustrates the combination of an else statement with a 
for statement that searches for even number in given list.


numbers = [11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
   if num%2 == 0:
      print ('the list contains an even number')
      break
else:
   print ('the list doesnot contain even number')


Iterator and Generator
Iterator is an object which allows a programmer to traverse through all the elements of a collection, regardless of its specific implementation. In Python, an iterator object implements two methods, iter() and next().

String, List or Tuple objects can be used to create an Iterator.

list = [1,2,3,4]
it = iter(list) # this builds an iterator object
print (next(it)) #prints next available element in iterator
Iterator object can be traversed using regular for statement
!usr/bin/python3
for x in it:
   print (x, end=" ")
or using next() function
while True:
   try:
      print (next(it))
   except StopIteration:
      sys.exit() #you have to import sys module for this
A generator is a function that produces or yields a sequence of values using yield method.

When a generator function is called, it returns a generator object without even beginning execution of the function. When the next() method is called for the first time, the function starts executing until it reaches the yield statement, which returns the yielded value. The yield keeps track i.e. remembers the last execution and the second next() call continues from previous value.

Example
The following example defines a generator, which generates an iterator for all the Fibonacci numbers.

#!usr/bin/python3

import sys
def fibonacci(n): #generator function
   a, b, counter = 0, 1, 0
   while True:
      if (counter > n): 
         return
      yield a
      a, b = b, a + b
      counter += 1
f = fibonacci(5) #f is iterator object

while True:
   try:
      print (next(f), end=" ")
   except StopIteration:
      sys.exit()


'''

# ---------------------------------------------------------------------------------
friends = ['ali', 'veli', 'deli']
family = ['camila', 'salah', 'ramadan']
print(friends)
print(family)
print(len(family))  # Length

family.extend(friends)
print(family)
family = family + friends  # concenation  adding friends list at the end of family
print(family)
family = family * 2  # repetition adding family list at the end of family for 1 time
print(family)
family.sort()  # sorting
print(family)

family.append("ertugrul")
print(family)

family.insert(2, 'ahmad')
print(family)

family.remove("camila")
print(family)

family.pop()
print(family)

print(family.index("ramadan"))

family.append("ramadan")
print(family)
print(family.count('ramadan'))
print(family.count('ali'))
print(family.count('camila'))

family.reverse()
print(family)

family2 = family.copy()
family.clear()
print(family)

# ------------------------------------------------------------------------------------
# FUNCTIONS
'''
def functionname( parameters ):
   "function_documentationstring"
   function_suite
   return [expression]

-------------------------------------
# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinfo( age = 50, name = "miki" )  # parameter order is not important if you use like this

   ----------------------------------------------------------------------------------

   Pass by Reference vs Value
All parameters (arguments) in the Python language are passed by reference. It means if you change what a parameter refers to within a function, the change also reflects back in the calling function. For example −

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   print ("Values inside the function before change: ", mylist)

   mylist[2]=50
   print ("Values inside the function after change: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)

Here, we are maintaining reference of the passed object and appending values in the same object. 
Therefore, this would produce the following result −
Values inside the function before change:  [10, 20, 30]
Values inside the function after change:  [10, 20, 50]
Values outside the function:  [10, 20, 50]

--------------------------------------------------------------
Variable-length Arguments
You may need to process a function for more arguments than you specified while defining the function. These arguments are called variable-length arguments and are not named in the function definition, unlike required and default arguments.

Syntax for a function with non-keyword variable arguments is given below −

def functionname([formal_args,] *var_args_tuple ):
   "function_docstring"
   function_suite
   return [expression]

An asterisk (*) is placed before the variable name that holds the values of all 
nonkeyword variable arguments. This tuple remains empty if no additional arguments are specified during 
the function call. Following is a simple example −

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)

   for var in vartuple:
      print (var)
   return

# Now you can call printinfo function
When the code is executed, it produces the following result −

printinfo( 10 )
Output is:
10

printinfo( 70, 60, 50 )
Output is:
70
60
50
-------------------------------------------------------------------------------
Namespaces and Scoping
Variables are names (identifiers) that map to objects. A namespace is a dictionary of variable names (keys)
 and their corresponding objects (values).
A Python statement can access variables in a local namespace and in the global namespace. If a local and
 a global variable have the same name, the local variable shadows the global variable.
Each function has its own local namespace. Class methods follow the same scoping rule as ordinary functions.
Python makes educated guesses on whether variables are local or global. 
It assumes that any variable assigned a value in a function is local.
Therefore, in order to assign a value to a global variable within a function,
 you must first use the global statement.
The statement global VarName tells Python that VarName is a global variable. 
Python stops searching the local namespace for the variable.
For example, we define a variable Money in the global namespace. 
Within the function Money, we assign Money a value, therefore Python assumes Money as a local variable.
However, we accessed the value of the local variable Money before setting it,
 so an UnboundLocalError is the result. Uncommenting the global statement fixes the problem.

Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   # global Money
   Money = Money + 1


'''


def topla(x, y):
    "iki objenin toplamini verir, sayi icin aritmetik sonuc verir +\
    ayrica diger veri turleri icin concatenation yapar yani birlestirerek return eder"
    return x + y


print(topla(3, -2.5))

print(topla('ali ', 'veli'))

''' Importing modules

import testmodule
f = testmodule.fibonacci(400)

from testmodule import fibonacci
f = fibonacci(300)

from modname import name1,name2,name3...
a= name1()
b= name2()
c= name3()
...

import all defined function and variables and classes from the module
from modulename import *

'''

from testmodule import fibonacci, hello  # only includes fibonacci and hello functions from the testmodule module

hello("World!")
f = fibonacci(300)
print(f)

from testmodule import *

result = calc(3, '^', 4)
print("3^4=", str(result))
result = calc(4, '%', 3)
print("4%3=", str(result))

'''FILE IO-----------------------------------------------------------------------------------------------------
https://www.tutorialspoint.com/python3/file_methods.htm
'''
# Open a file
fo = open("foo.txt", "w")
print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
fo.write("hello\nworld\nmustafa yetis\npython3")
fo.close() #file closed
print("after fclose Closed or not : ", fo.closed, "\n\n")


# -----------------------------------------------------------
# Open a file
fo = open("foo.txt", "r+")
string1 = fo.read(10)
print("Read String is : ", string1)

# Check current position
position = fo.tell()
print("Current file position : ", position)

string1 = fo.read()
print("Read all String is from last position : ", string1)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)#  seek(offset[, from])
string1 = fo.read()
print("after seek Again readall String is :\n", string1)  #  seek(0, 0) from 0 position goto 0 times next byte (goto beginning)

# Close opened file
fo.close()

# --------------------------------------------
# Open a file
fo = open("foo.txt", "r")
print("Name of the file: ", fo.name)

for index in range(4):
   linex = next(fo)
   print("Line No %d - %s" % (index, linex))

# Close opened file
fo.close()

# --------------------------------------------
# Open a file
fo = open("foo.txt", "r+")
print("\nName of the file: ", fo.name)

linex = fo.readline()
print("Read Line: %s" % (linex))
linex = fo.readline()
print("Read Line: %s" % (linex))
linex = fo.readline(10)
print("Read Line: %s" % (linex))
linex = fo.readline()
print("Read Line: %s" % (linex))  # mustafa yetis satiri tam okunmadigi icin kaldigi yerden newline a kadar olan kısmı line olarak alır
linex = fo.readline()
print("Read Line: %s" % (linex))

# Close opened file
fo.close()
# --------------------------------------------
# Open a file
fo = open("foo.txt", "r+")
print("Name of the file: ", fo.name)

linelist = fo.readlines(10)  # 10 bytes hangi satira denk gelirse o satır dahil listeye ekler (sayiyi degistirip gorebilirsiniz)
print("Read Line: %s" % (linelist))

linelist = fo.readlines()    # bir onceki readlines okuduğu son satırdan sonraki satır ve devamını listeye ekler
print("Read Line: %s" % (linelist))

# Close opened file
fo.close()


'''DIRECTORY OPERATIONS
https://www.tutorialspoint.com/python3/os_file_methods.htm

import os

# Rename a file from test1.txt to test2.txt
os.rename( "test1.txt", "test2.txt" )

# Delete file test2.txt
os.remove("text2.txt")

# Create a directory "test"
os.mkdir("test")

# Changing a directory to "/home/newdir"
os.chdir("/home/newdir")

# This would give location of the current directory
os.getcwd()

# This would  remove "/tmp/test"  directory.
os.rmdir( "/tmp/test"  )

'''





