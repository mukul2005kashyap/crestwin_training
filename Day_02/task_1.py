"""
Docstring for Day_02.task_2
python Data types:
python data types are the way to classify the data items , or we can say that is represent the kind of value ,
 which determines what operations can be performed on that data. Since everything is an object in Python programming, Python data types are classes and variables are instances (objects) of these classes.

The following are standard or built-in data types in Python:

Numeric: int, float, complex
Sequence Type: string, list, tuple
Mapping Type: dict
Boolean: bool
Set Type: set


"""

# int
x=50
y=60
print(x+y)

# float
a=10.6
b=20.4
print(a*b)

""" Strings in Python can be created using single quotes, 
 double quotes or even triple quotes.
  We can access individual characters of a String using index."""
# str
h="hello"
print(h)

# list ----allows indexing
l1=[10,20,30,"hello",10.2]
print(l1)

# tuple
t1=(10,20,30,"hello")

# boolean
print(a==b)
print(a is b)
c=10
x=c
print(x is c)
print(c is x)

# set -- set is uorderd collection kof elements which can store only unique values

set={10,10,20,30,3,3,4,67}
print(set)

# dictionary ---stores the data into key values pairs 

dict={1:"mukul",2:"gyan",3:"anand"}
print(dict)


