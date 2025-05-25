import os
import sys
os.chdir("E:\\python intermediate project")
print(os.getcwd())#get current working directory
os.chdir('..')#change directory to the parent directory
print(os.getcwd())
w = os.name
print(w)
os.chdir("E:\\python intermediate project\\exam\\.venv\\Scripts")
print(os.listdir())#list the file and directory inside the current directory as a list
print(sys.argv)#returns a list of command line arguments passed to a python script
                #at index 0 it will always contain the name of the script
print(sys.path)#returns the path for all python module by searching the environment variable
print(sys.maxsize)#returns the largest integer a variable can take

sys.exit()#this causes the current script to exit back to the command prompt or python console used to exit safely if an exception occurs

