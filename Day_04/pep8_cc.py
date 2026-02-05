"""
PEP 8 -- PEP  stands for (Python Enhancement Proposal 8) are python style guide

this are the several style guide or a instructions that are set or define by the python to make your code easy 
to maintain and redable and professional

1. Indentation
Indentation in Python organizes code into blocks and defines the program’s structure
. PEP 8 recommends using 4 spaces per level to maintain readability and consistency.

2. Docstrings
Use docstrings to describe functions or modules
, while multi-line explanations use triple quotes spanning several lines.

3. Spaces Around Operators
Use spaces around operators and after commas for readability,
 but avoid spaces immediately inside parentheses, brackets, or braces.

4, Naming Conventions
Follow consistent naming conventions: use CamelCase for classes, lower_case_with_underscores for functions and variables,
 and all uppercase with underscores for constants.

5.Class and Function Arguments
Always use self as the first argument in instance methods and cls as the first argument in class methods.

6. Line length 
 in python max line length is 79 characters it recommend max 79 charater in one line 



"""

# Clean Code principles
# you can say that the clean code principle are the instruction specify to make your code 
# easily to understand .simple, readable,and easily modify 
"""
# ?1. Meaningful variable names
Bad:
x = 100

Good:
total_price = 100

#? 2.Avoid repetition (DRY)

DRY = Don't Repeat Yourself
Bad:
print("Welcome Mukul")
print("Welcome Aman")

Good:
def welcome(name):
    print(f"Welcome {name}")

welcome("mukul")
welcome("anand")

#? Proper comments (only when needed)
Bad:
x = x + 1  # increment x by 1

Good:
attempt_count += 1

"""