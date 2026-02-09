# Decorators 
"""
Decorators in the python is function are the flexible way to changes or modify the behavious of another 
functions or method without changing their code actual code ..
"""

# A decorator is essentially a function that takes another function as an argument
# and returns a new function with enhanced functionality.

# Decorators are often used in scenarios such as logging, authentication and memorization,
# allowing us to add additional functionality to existing functions or methods in a clean, reusable way.

import logging

logging.basicConfig(level=logging.DEBUG ,filename="test.log")

def log_fun(fun):
    def decorated(*args , **kwargs):
        logging.info(f"calling {fun.__name__} with args={args} , kwargs={kwargs}")
        result=fun(*args, **kwargs)
        logging.debug(f"{fun.__name__} returned {result}")


        return result
    return decorated


@log_fun
def add(a,b):
    return a+b

add(4,8)


# what are the real life example of decorators 
"""
Mobile Phone Cover
Phone = Function
Cover = Decorator
        "Your phone works normally without cover."

            But when you add a cover:
                phone is protected
                phone looks better

Phone is same, but extra feature is added.


#?  lets move to the Real programming use case examples 

login authentication
        before functions run first check the user login or not 
            ex-- open profile is fun()
                 decorator check that login or not 


Logging tracking 
    Decorator can record:
        function called time
        function name
        input values

Used in real companies for debugging.


permission check
    only admin can delet the user
        fun--       to delete the user 
        decorator-- check first that if user is admin 

        then it call the fun

        
"""