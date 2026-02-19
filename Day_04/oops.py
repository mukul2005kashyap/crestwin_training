"""
OBJECT ORIENTED PROGRAMMING 

oops in python is programing approch or a  way to oragnaize the code through the objects and classes
          to represent the real world entities and their behaviour...
 or you can say that the oops is a paradigam that represent the reeal world entities in the form of objects 

# ! so ypu can say that the everything is an object in python 

or we can create the object in python so before directly creating the objects we have to create the class 
"""

# so here is also one more thing that is constructer 
#  construcrter is nothing but is __init__ () which is always being executed when the object is initiated
# like whereveer the class is created and it execute the constructer is always execute

#? parametrize constructer
class Traning:
    def __init__(self,name):
        # self.name=name         #--self parameter is the refernce of the current instance of the class 
                                   # and it is used it is used to access the variable belongs to the class.....
        print(self)

        """
        always in the constructer we have to pass the self parameter without that we got the error
        here the self is nothing but it shows the object or we can say that it pointing the object 
        """
t1 = Traning()
print(t1)


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

s1=Student("anish",(98,97,99))
print(s1.name,s1.marks)
        
# static method 

class Hello:
    @staticmethod
    def college():              
        print("svvv college")

        """
        if you create the function inside the class so it is called as methof or to execute that method you 
         have to use the self key as parameter 
          but if you want to use fun without the self key word that get that fun at the class level by making
           them the static method it is decoraatoe """

s1 = Hello()
s1.college()


# There are 4 pillars of oops--

# ? Abstracton--
"""
so abstraction is the process of hidding the implementation detail and showing only the necessary feature
to the users

"""
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


c = Car()
c.start()
c.stop()

# encapsulation 

"""
Encapsulation means wrapping data and methods inside a single unit (class).

It is used for data hiding and security.
"""

# inheritance 

"""
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a 
class (called a child or derived class) to inherit attributes and methods from another class
 (called a parent or base class). In this article, we'll explore inheritance in Python.
"""

class Animal:
    def __init__(self,name):
        self.name=name

class Dog(Animal):
    def sound_info(self):
        print(self.name,"baark")

d=Dog("buddy")
d.sound_info()
        
# polymorphism

"""
polymorphism means many form like a  same function or a attribute or a method behaves differently depending 
on the object it working with  """

class Anm:
    def sound(self):
        print("animals makes sound")

class Bob(Anm):
    def sound(self):
        print("bob barks")

class Cat(Anm):
    def sound(self):
        print("citty meow")

b=Bob()
c=Cat()
c.sound()

"""
OOP (Object-Oriented Programming) is a programming paradigm based on the concept of objects, 
    which can contain data (attributes) and code (methods/functions).
    OOP helps organize code, makes it more modular, reusable, and easier to maintain.
    
    -Dynamic Typing: Python classes and objects don't require explicit type declarations.

    -Everything is an object: Even basic data types (like integers, functions) are objects with attributes and methods.

    -Multiple Inheritance: Python supports inheriting from multiple classes, enabling complex class hierarchies.

    -Duck Typing: Python emphasizes behavior over type, allowing polymorphism without strict type hierarchies.

    -Built-in Magic Methods: Python uses special methods (like __init__, __str__, __len__) to customize object behavior,
                             enabling operator overloading and integration with Python syntax.


                             
?  What is the __init__ method in Python
        -The __init__ method in Python is a special constructor method that automatically runs when a new object of a class is created.
          It is used to initialize the object’s attributes with default or user-provided values.
            It is similar to constructors in other OOP languages like Java or C++.

?What is method overloading in Python?
In languages like Java or C++, method overloading allows multiple methods with the same name but different parameters.
 Python does not support true method overloading. If you define two methods with the same name,
   the latest one will overwrite the previous definition.


?What is method overriding in Python?
Method overriding allows a subclass to provide a specific implementation of a method that is already defined
 in its superclass. This means that the subclass can "override"the behavior of the method inherited
   from the parent class, providing a different version that is more suitable for the subclass.

?What are abstract classes in Python?
Abstract class is a class that serves as a blueprint for other classes. It defines a structure that derived
 classes must follow but does not provide full implementation, abstract classes cannot be instantiated 
 directly which means they are meant to be subclassed.  


"""
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

"""
?What is the Global Interpreter Lock (GIL) and its impact on Python OOP?
The Global Interpreter Lock (GIL) is a mutex that allows only one thread to execute Python bytecode at a time,
 even on multi-core systems.

It's impact:

        -For CPU-bound tasks, multithreading is limited by the GIL, so performance gains are minimal.
        -For I/O-bound tasks (like file handling, networking, databases), threads still help because the GIL
         is released during I/O operations.


? Explain Python’s MRO with an example.
Python’s Method Resolution Order (MRO) determines the order in which classes are searched 
when calling a method in the presence of multiple inheritance.

It follows the C3 linearization algorithm.

Example:

class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
​
print(D.mro())

            A
           / \ 
          B   c
           \ /
            D


[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
"""