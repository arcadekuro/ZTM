# A module in python is simply a file that contains accesible code with functions and statements. 
"""
Common modules for scripting include:
1. sys 
2. os 
3. subprocess
4. Math 
5. Random 
6. Datetime
7. JSON
"""

import sys
import os # for interacting with your
import math 

"""
Sys
provides information about constants, functions and methods of the Python interpreter
    - it is the system specific parameters and functions. Responsible for controlling and interacting with the interpreter. (e.g. info on operating system or python version. )
    .stdin 
    .stdout
    .exit - exit the python interpreter. 
"""

print(sys.version) # version of python
print(sys.argv) # list containing the CLI arguments passed to our script (script name & path)

"""
os module 
interact with operating system, for moving folders,
or something to do with working directory.
"""
def changes_os():
    print(os.getcwd()) #prints current working directory. 
    #os.chdir() #change directory & give path. then you can print the cwd. only double backslash or 1 front slask works
    os.mkdir("/Users/arcadekwaku/udemy/scripting") #makes directory.
    os.rmdir() # remove directory
    os.remove() # remove file
    os.path.join()
    print(os.path.split("/Users/arcadekwaku/udemy/scripting"))
    
# Does the path exist? will give a boolean operator,
print(os.path.exists("/Users/arcadekwaku/udemy/scripting"))


"""

Subprocess module methods for the os object. 
lets you interact with the  operating system to create new processes to pass the information
into and out of them and get the return codes so it ca be used by using the coil function
so you.
system administrastor tasks. for accessing system commands. Runs a command? 

"""
print(math.pi) # prints the value for pi 
print(math.e) # prints a constant 
print(math.degrees(0.1)) # converts to degrees. 
print(math.acos(0.5)) #the cosine vlue. 
print(math.asin(0.5))
print(math.atan(5))
print(math.cos(3))
print(math.exp(2))