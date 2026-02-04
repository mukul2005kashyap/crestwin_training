"""
Docstring for Day_03.task_1_3
functions in python is resuable block of code that performs specific task ,
it improve, readibility and modularity and avoid repeatition 

# ? The idea is to put some commonly or repeatedly done task together and make a function so that instead 
# ?of writing the same code again and again for different inputs, we can do the function calls to reuse code
# ?contained in it over and over again.



functions are used for:
-Code reusability
-Better structure (modular programming)
-Easy debugging and maintenance
-Reducing redundancy

if talk about a functions so it is very necessary to understand about the parameters and arguments...
----Parameters are variables defined in function definition.
----Arguments are values passed while calling the function.

---argument ---A default argument is a parameter that assumes a default value
 if a value is not provided in the function call for that argument.

---n keyword arguments, values are passed by explicitly specifying the parameter names,
 so the order doesn’t matter.

---In positional arguments, values are assigned to parameters based on their order in the function call.


"""
def fun(a,b):
    return a*b

x=fun(3,5)
print(x)

#? this function returns the value 

def funt(a,b):
    print(a+b)
funt(9,8)
# ? this functions print the value 

# there a multiple of the inbuilt functions un python like 
# --print()
# --len()
# --sum()
# --type()

# ! and the functuions that created by using def keyword are catagorise as user defined functions 
# that defined by the users 

# ////////////////////////////////////////////////////////////////////////////////


"""so ther is also a case if you call function inside the same functions so it is called recursion....


 """

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    
y=fact(5)
print(y)

# -----------------------------------------------------------------------
# !  MODULES
"""
so models in python is nothing but a python file (.py) that contain the functions ,clases ,variables 
that we reuse many time in the different files or other programes by using "import keyword"
"""

import math as m
print(m.sqrt(5))

"""
What is the difference between module and package?
Module: single .py fle
Package: collection of modules inside a folder with __init__.py-----
like there is folder that contain multiple python file (modules) so it is called as package
"""

# ! VENV (VIRTUAL ENVIRONMENT) IN WINDOWS
"""
    if you run cmd to create virtual environment so windows initialy crate a folder like this ---
    venv/
  bin/
  lib/
  include/
  pyvenv.cfg

  and the pyvenv.cfg is the brain of the virtual environment--
  it stores 
Python ka original location kaha hai
global packages allow karne hain ya nahi
python version
"""