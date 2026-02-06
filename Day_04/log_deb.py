"""
#! Debugging 
Debuging in python means finding and fixing the error or bug in code 

Types of errors:
--Syntax error :- error or mistake that you make while writing a code means you break the rule to write code

--Runtime error:-code crash or give the error while running

--Logical error:- logical error means Syntax bhi sahi, runtime bhi sahi, but logic wrong.
"""

# Debugging Techniques
"""
==Print Debugging (Beginner way)
Most common method.
-- print("value of x:", x)

==Debugger (Professional way)
in python there is a inbuilt debugger module pdb

===Debugging using Try-Except

#? Try-except is not debugging, but it helps handle crashes.

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
you can say that try catch is used to aavoid the prograamm crash not fix the bug


===Traceback Understanding (Very Important)

if any error encounter the python give the trackback:

Example:

File "app.py", line 10
ZeroDivisionError: division by zero


trackback shows you 3 
✅ file name
✅ line number
✅ error type
    

"""
class A:
    def __init__(self):
        pass

# LOGGING
"""
Logging is the process of keeping a record of what a program is doing while it runs,
 which helps developers understand program behavior and easily find and fix errors
 like invalid inputs or system failures.

#!  Python Logging Levels
    There are five built-in levels of the log message.            numeric value
                                                                 
Debug: Detailed information for diagnosing problems.                  10
Info: Confirms things are working as expected.                        20 
Warning: Indicates unexpected issues or potential future problems.    30
Error: A serious problem that prevents a function from running.       40
Critical: A severe error that may stop the program from running.      50

 """

import logging

# # logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.WARNING , filename="test.log")


# logging.debug("this is debug msg")
# logging.info("this is info msg")

# ---DEBUG:root:this is debug msg
# ---INFO:root:this is info msg


logger = logging.getLogger("crest_logger")
logger.setLevel(logging.WARNING)
formatter = logging.Formatter(" %(asctime)s - %(name)s - %(levelname)s - %(message)s ")
handler = logging.StreamHandler()         #---send message to the stream
handler.setFormatter(formatter)
logger.addHandler(handler)                # file handler -----send message to the file 



logger.debug("hello this is debbug msg")
logger.info("hello this is info msg")
logger.warning("hello this is warning msg")
logger.error("hello this is warning msg")

#----  2026-02-06 16:33:52,220 - crest_logger - INFO - hello this is info msg 
#----  2026-02-06 16:33:52,220 - crest_logger - DEBUG - hello this is debbug msg 
#----  2026-02-06 16:33:52,220 - crest_logger - WARNING - hello this is warning msg 
# 2026-02-06 16:46:49,389 - crest_logger - ERROR - hello this is warning msg 