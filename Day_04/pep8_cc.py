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

# linux process

"""
Processes in Linux
A process is simply a program that is currently running on your system.
Whenever you execute a command in Linux,
the operating system creates a process to run that command.

for example :-- you issued a cmd un linux like pwd -- so os creates a processs to execute that cmd that is used to show the 
location of the current working directory in which currently user in 

there is a 5 digit number that unix or linux keeps an account of the processes means that 5 digit number is the id 
of the process and each process have the unique id of unique number 

there is not any possibility in any case that two different processses having the same process id because 
os use that process id to track all the process

"""

# so here is the some of the command that are related to the processes 
"""
ps ---- to show status of the running process in the system

ps -ef -----  to show all the current running process in the system

ps aux --- a: Shows processes for all users, including those not owned by the current user.
"""
