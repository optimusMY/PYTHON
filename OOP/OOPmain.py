import math



class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)



emp1 = Employee("Zara", 2000)  # This would create first object of Employee class"
emp2 = Employee("Manni", 5000)  # This would create second object of Employee class"
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)


emp1.salary = 7000  # Add an 'salary' attribute.
emp1.name = 'xyz'  # Modify 'name' attribute.
emp1.displayEmployee()
del emp1.salary  # Delete 'salary' attribute.
print("after deleting salary attribute we created new salary attribute: ")
setattr(emp1, 'salary', 7000)  # Set attribute 'salary' at 7000, If attribute does not exist, then it would be created.
if hasattr(emp1, 'salary'):  # Returns true if 'salary' attribute exists
    print(getattr(emp1, 'salary'))  # Returns value of 'salary' attribute

emp1.displayEmployee()

print()
delattr(emp1, 'salary')    # Delete attribute 'salary'




''''''

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
print("Employee.__doc__:", Employee.__doc__)  # Class documentation string or if undefined then none will be returned .
print("Employee.__name__:", Employee.__name__)  # Class name.
print("Employee.__module__:", Employee.__module__)  # Module name in which the class is defined. This attribute is "__main__" in interactive mode.
print("Employee.__bases__:", Employee.__bases__)  # A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.
print("Employee.__dict__:", Employee.__dict__)  # Dictionary containing the class's namespace.



class Point:
    def __init__(self, x=0, y=0):
       self.x = x
       self.y = y
    def __del__(self):
       class_name = self.__class__.__name__
       print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))   # prints the ids of the obejcts
del pt1
del pt2
del pt3

'''Note − Ideally, you should define your classes in a separate file,
 then you should import them in your main program file using import statement.'''






'''INHERITANCE
Instead of starting from a scratch, you can create a class by deriving it from 
a pre-existing class by listing the parent class in parentheses after the new class name.
The child class inherits the attributes of its parent class,
and you can use those attributes as if they were defined in the child class. 
A child class can also override data members and methods from the parent.
Syntax-Derived classes are declared much like their parent class; however,
a list of base classes to inherit from is given after the class name −

class SubClassName (ParentClass1[, ParentClass2, ...]):
   'Optional class documentation string'
   class_suite
'''
class Parent:  # define parent class
    parentAttr = 100
    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print('Calling parent method')

    def setAttr(self, attr):
       Parent.parentAttr = attr

    def getAttr(self):
       print("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
    def __init__(self):
        # if needed you can use super().__init__() constructor method here, super() is parent class here
        print("Calling child constructor")

    def childMethod(self):
        print('Calling child method')


# usage of the parent and child classes
c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method


'''
In a similar way, you can drive a class from multiple parent classes as follows 

class A:        # define your class A
   def __init__(self):
      print ("Calling classA constructor")

class B:         # define your class B
   def __init__(self):
      print ("Calling classB constructor")

class C(A, B):   # subclass of A and B
   def __init__(self):
      super().__init__()   # it will invoke the classA __init__() method because in definition C(A,B)  A is first one of the super classes (this is called MethodResolutionOrder 
      print ("Calling classB constructor")

'''




'''INHERITANCE AND METHOD OVERRIDING
You can always override your parent class methods. 
One reason for overriding parent's methods is 
that you may want special or different functionality in your subclass.
'''

class ParentClass:        # define parent class
    def myMethod(self):
        print('\nCalling parent method')

class Child(ParentClass):  # define child class
    def myMethod(self):
        print('\nCalling child method')

    def myAnotherMethod(self):
        print("I am different method which is already not in parent class")

c = Child()          # instance of child
c.myMethod()         # child calls overridden method




'''Data Hiding
An object's attributes may or may not be visible outside the class definition. 
You need to name attributes with a double underscore prefix, 
and those attributes then will not be directly visible to outsiders.

Python protects those members by internally changing the name to include the class name. 
You can access such attributes as object._className__attrName.
If you would replace your last line as following, then it works for you −

.........................
print (counter._JustCounter__secretCount)


'''

class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
counter.count()
# print(counter.__secretCount)  it throws an exception
print("directly secretCount value: ", counter._JustCounter__secretCount)  # runs without exception



'''
decorator example
@classmethod  is a decorator which enables following method to be static class method
when you declare a method like this, then you have to access with classname
you can not use instance name for accessing this method
'''

class Position:

    city = "istanbul"   # this is a class variable

    def __init__(self, posX, posY):   # consturctor
        self.px1 = posX               # these are instance variables
        self.py1 = posY

    def howfar(self, anotherPos):     # instance method (no decorator and param can be anything)
        distance = math.sqrt((anotherPos.px1 - self.px1)**2 + (anotherPos.py1 - self.py1)**2)
        print("distance:", str(distance))

    @classmethod
    def ClassCity(cls):     #class method (decorator is classmethod and param is class)
        return cls.city

    @staticmethod
    def MyStaticMethod(): # dosnt work with instance variable or class variable
        print("hi i am static method of the position class")




print(Position.ClassCity())  # this Position.ClassCity() method is static method of class Position and you can not access this method via instance.ClassCity() it wouldnt work

pos1 = Position(3, 5)   #creating new instance with initial px=3 and py=5 values
pos2 = Position(4, 12)   #creating new instance with initial px=4 and py=12 values

pos1.howfar(pos2)

Position.MyStaticMethod()



'''INNER CLASS
it is not inheritance property
this is just defining a class in a  outer class
'''

class MyTriangle:
    def __init__(self, Ax, Ay, Bx, By, Cx, Cy):
        self.pA = MyTriangle.MyPoint(Ax, Ay)
        self.pB = MyTriangle.MyPoint(Bx, By)
        self.pC = MyTriangle.MyPoint(Cx, Cy)

    def getPerimeterLength(self):
        lenAB = self.pA.distance(self.pB)
        lenBC = self.pB.distance(self.pC)
        lenCA = self.pC.distance(self.pA)
        return lenAB + lenBC + lenCA

    class MyPoint:

        def __init__(self, posX, posY):
            self.posx = posX
            self.posy = posY

        def distance(self, anotherPoint):
            return math.sqrt((anotherPoint.posx - self.posx) ** 2 + (anotherPoint.posy - self.posy) ** 2)


position1 = MyTriangle.MyPoint(3, 7)
position2 = MyTriangle.MyPoint(6, 2)
lenp1p2 = position1.distance(position2)
print("len p1 to p2:", lenp1p2)


triangle1 = MyTriangle(3, 4, 5, 5, 12, 13)
print("perimeter length of triangle1 :" + str(triangle1.getPerimeterLength()))



'''OPERATOR OVERLOADING
Suppose you have created a Vector class to represent two-dimensional vectors. 
What happens when you use the plus operator to add them? Most likely Python will yell at you.

You could, however, define the __add__ method in your class to 
perform vector addition and then the plus operator would behave as per expectation −
'''

class  Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
'''OPERATOR OVERLOADING ANOTHER EXAMPLE
'''
class MyPoint:

    def __init__(self, posX, posY):
        self.posx = posX
        self.posy = posY

    def distance(self, anotherPoint):
        return math.sqrt((anotherPoint.posx - self.posx) ** 2 + (anotherPoint.posy - self.posy) ** 2)

    def __add__(self, other):       # overloading "+" operator
        sumx = self.posx + other.posx
        sumy = self.posy + other.posy
        result = MyPoint(sumx, sumy)
        return result

    # def __gt__(self, other):   overloading grather than operator '>'    usage: p1 > p2    returns True or False
    # def __ge__(self, other):   overloading grather or equal  operator '>='    usage: p1 >= p2    returns True or False
    # def __sub__(self, other):   overloading subtract operator  '-'     usage: p3 = p2 - p1
    def __str__(self):          #  overloading print feature of toString
        return 'p(x,y)={},{}'.format(self.posx, self.posy)  # building and returning a customized string in the method


p1 = MyPoint(3, 5)
p2 = MyPoint(5, 12)
p3 = p2 + p1
print(p3.posx, p3.posy)
print(p3)


'''POLY MORPHISM BY   METHOD OVERLOADING
'''
class numbers:
    def __init__(self, num1, num2):
        self.n1 = num1
        self.n2 = num2

    def average(self, number1=None, number2=None, number3=None):
        if (number1 is not None) and (number2 is not None) and (number3 is not None):
            return (number1 + number2 + number3)/3
        elif (number1 is not None) and (number2 is not None):
            return (number1 + number2) / 2
        else:
            return number1


nu1 = numbers(0, 0)
print(nu1.average(3, 5, 7))
print(nu1.average(3, 5))
print(nu1.average(3))



