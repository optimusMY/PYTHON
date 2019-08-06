'''

A module allows you to logically organize your Python code.
Grouping related code into a module makes the code easier to
understand and use. A module is a Python object with arbitrarily
named attributes that you can bind and reference.
Simply, a module is a file consisting of Python code.
A module can define functions, classes and variables.
A module can also include runnable code.

Example
The Python code for a module named aname normally resides in
a file namedaname.py. Here is an example of a simple module, support.py −

def print_func( par ):
   print "Hello : ", par
   return
The import Statement
You can use any Python source file as a module by executing an import statement in
some other Python source file. The import has the following syntax −

import module1[, module2[,... moduleN]
When the interpreter encounters an import statement,
it imports the module if the module is present in the search path.
A search path is a list of directories that the interpreter searches before importing a module.
For example, to import the module hello.py,
you need to put the following command at the top of the script −

#!/usr/bin/python3

# Import module support
import support

# Now you can call defined function that module as follows
support.print_func("Zara")
When the above code is executed, it produces the following result −

Hello : Zara

A module is loaded only once, regardless of the number of times it is imported.
This prevents the module execution from happening repeatedly, if multiple imports occur.

The from...import Statement
Python's from statement lets you import specific attributes from a module into the current namespace.
 The from...import has the following syntax −

from modname import name1[, name2[, ... nameN]]
For example, to import the function fibonacci from the module fib, use the following statement −

#!/usr/bin/python3

# Fibonacci numbers module

def fib(n): # return Fibonacci series up to n
   result = []
   a, b = 0, 1
   while b < n:
      result.append(b)
      a, b = b, a + b
   return result

 from fib import fib
 fib(100)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
This statement does not import the entire module fib into the current namespace;
it just introduces the item fibonacci from the module fib into the
global symbol table of the importing module.

The from...import * Statement
It is also possible to import all the names from a module into the current namespace by
 using the following import statement −

from modname import *
This provides an easy way to import all the items from a module into the current namespace; however, this statement should be used sparingly.

Executing Modules as Scripts
Within a module, the module’s name (as a string) is available as the value of the global variable __name__. The code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__".

Add this code at the end of your module −

 Live Demo
#!/usr/bin/python3

# Fibonacci numbers module

def fib(n): # return Fibonacci series up to n
   result = []
   a, b = 0, 1
   while b < n:
      result.append(b)
      a, b = b, a + b
   return result
if __name__ == "__main__":
   f = fib(100)
   print(f)
When you run the above code, the following output will be displayed.

[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

Locating Modules
When you import a module, the Python interpreter searches for the module in the following sequences −
The current directory.

If the module is not found, Python then searches each directory in the shell variable PYTHONPATH.

If all else fails, Python checks the default path. On UNIX, this default path is normally /usr/local/lib/python3/.

The module search path is stored in the system module sys as the sys.path variable. The sys.path variable contains the current directory, PYTHONPATH, and the installation-dependent default.

The PYTHONPATH Variable
The PYTHONPATH is an environment variable, consisting of a list of directories. The syntax of PYTHONPATH is the same as that of the shell variable PATH.

Here is a typical PYTHONPATH from a Windows system −

set PYTHONPATH = c:\python34\lib;
And here is a typical PYTHONPATH from a UNIX system −

set PYTHONPATH = /usr/local/lib/python
Namespaces and Scoping
Variables are names (identifiers) that map to objects. A namespace is a dictionary of variable names (keys) and their corresponding objects (values).

A Python statement can access variables in a local namespace and in the global namespace. If a local and a global variable have the same name, the local variable shadows the global variable.

Each function has its own local namespace. Class methods follow the same scoping rule as ordinary functions.

Python makes educated guesses on whether variables are local or global. It assumes that any variable assigned a value in a function is local.

Therefore, in order to assign a value to a global variable within a function, you must first use the global statement.

The statement global VarName tells Python that VarName is a global variable. Python stops searching the local namespace for the variable.
For example, we define a variable Money in the global namespace. Within the function Money, we assign Money a value, therefore Python assumes Money as a local variable.

However, we accessed the value of the local variable Money before setting it, so an UnboundLocalError is the result. Uncommenting the global statement fixes the problem.

 Live Demo
#!/usr/bin/python3

Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   # global Money
   Money = Money + 1

print (Money)
AddMoney()
print (Money)
The dir( ) Function
The dir() built-in function returns a sorted list of strings containing the names defined by a module.

The list contains the names of all the modules, variables and functions that are defined in a module.
 Following is a simple example −

 Live Demo
#!/usr/bin/python3

# Import built-in module math
import math

content = dir(math)
print (content)
When the above code is executed, it produces the following result −

['__doc__', '__file__', '__name__', 'acos', 'asin', 'atan',
'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp',
'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log',
'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh',
'sqrt', 'tan', 'tanh']

Here, the special string variable __name__ is the module's name, and __file__ is
the filename from which the module was loaded.

The globals() and locals() Functions
The globals() and locals() functions can be used to return the
names in the global and local namespaces depending on the location from where they are called.

If locals() is called from within a function,
it will return all the names that can be accessed locally from that function.

If globals() is called from within a function,
it will return all the names that can be accessed globally from that function.

The return type of both these functions is dictionary.
Therefore, names can be extracted using the keys() function.

The reload() Function
When a module is imported into a script, the code in the top-level portion of a module is executed only once.

Therefore, if you want to reexecute the top-level code in a module, you can use the reload() function.
The reload() function imports a previously imported module again.
The syntax of the reload() function is this −

reload(module_name)
Here, module_name is the name of the module you want to reload and
not the string containing the module name. For example, to reload hello module, do the following −

reload(hello)
Packages in Python
A package is a hierarchical file directory structure that defines a
single Python application environment that consists of
modules and subpackages and sub-subpackages, and so on.

Consider a file Pots.py available in Phone directory. This file has the following line of source code −

def Pots():
print ("I'm Pots Phone")
Similar, we have other two files having different functions with the same name as above. They are −

Phone/Isdn.py file having function Isdn()

Phone/G3.py file having function G3()

Now, create one more file __init__.py in the Phone directory −

Phone/__init__.py
To make all of your functions available when you have imported Phone,
you need to put explicit import statements in __init__.py as follows −

from Pots import Pots
from Isdn import Isdn
from G3 import G3
After you add these lines to __init__.py, you have all of these classes available
when you import the Phone package.

#!/usr/bin/python3

# Now import your Phone Package.
import Phone

Phone.Pots()
Phone.Isdn()
Phone.G3()
When the above code is executed, it produces the following result −

I'm Pots Phone
I'm 3G Phone
I'm ISDN Phone
In the above example, we have taken example of a single function in each file,
but you can keep multiple functions in your files. You can also define different
Python classes in those files and then you can create your packages out of those classes.

'''

def hello(name):
    print("Hello " + name)
    return

def fibonacci(n): #
   """return Fibonacci series up to n"""
   result = []
   a, b = 0, 1
   while b < n:
       result.append(b)
       a, b = b, a + b
   return result

def calc(a, operation, b):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    elif operation == '%':
        return a % b
    elif operation == '^':
        return a ** b
    else:
        return 0
