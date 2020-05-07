import os 

# extract the current working directory
def current_directory():
    cwd = os.getcwd()
    print(cwd) 

# retrieves the path of another file 
# There is the absolute & relative path name.
# abosolute - stright from the drive 
#relative - to the the current directory. 
def file_path(filename):
    path = os.path.abspath((filename))
    print(path)


#current_directory()
file = "sample.txt"
file_path(file)