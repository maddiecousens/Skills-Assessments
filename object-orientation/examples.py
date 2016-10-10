#####################################################################
# - How to increment a Class Attribute with every instance
# - How to get the Class name of an object as a string:
#     --> object.__class__.__name__
#####################################################################

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
#Employee Count increments
print "Total Employee %d" % Employee.empCount
# How to get name of class of an object
print emp2.__class__.__name__

#####################################################################
# - Proof that changing a Class Attribute adjusts that attribute for
#     all instances
# - issublass(SubClass, ParentClass)
# - isisntance(instance, Class)
#####################################################################

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

class Child(Parent): # define child class
   def __init__(self):
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'

c = Child()          # instance of child
c.setAttr(500)       # change parentAttr
d = Child()          # create another instance of Child
d.getAttr()          # returns 500 because we set to parent level
Parent.parentAttr = 700 # c, d now have .parentAttr set to 700

issubclass(Child, Parent) # Returns True
#issubclass(Child, Hello) # Returns NameError: 'Hello' is not defined
isinstance(c, Child)    # Returns True
isinstance(c, Parent)   # Returns True

#####################################################################
# OVERLOADING OPERATORS
# - how to redefine operator functionality so it can be used on
#     objects. Would otherwise error out
# - __str__ overrides what is printed to console when you write
#     'print object'
# - __repr__ overrides what is printed to consol when you just write
#     'object'
#####################################################################
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)

   def __repr__(self):
      return 'Vector!! (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2

#####################################################################
# Hiding Attributes
# - write with double underscore
# - to call, must use Classname preceded with single underscore
#     --> object._Classname__secretattribute
#####################################################################

class JustCounter:
   __secretCount = 0 #double underscore
  
   def count(self):
      self.__secretCount += 1
      print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
#print counter.__secretCount # This errors out
counter._JustCounter__secretCount

#####################################################################
# Copying an Object
# - import Copy
# - obj2 = copy.copy(obj2)
# >>> p1 is p2
# False
# >>> p1 == p2
# False
# the default behavior of the == operator is the same as the is operator; 
#     it checks object identity, not object equivalence
#####################################################################

class Point(object):
    """Represents a point in 2-D space."""

class Rectangle(object):
    """Represents a rectangle. 

    attributes: width, height, corner.
    """
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

import copy
box2 = copy.copy(box)















