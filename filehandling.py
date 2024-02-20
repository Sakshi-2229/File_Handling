# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 03:23:00 2023

@author: sai
"""

"""
#File Handling
1. File is a Block of memory
"""

#Absolute path example
with open('pi_digits.txt') as file_object:
    #The open() function needs
    #one argument: the name of file you want to open.
    contents = file_object.read()
print(contents)
#observe the extra line at the end of output



#To remove the space at the end of output use rstrip() function.
with open('pi_digits.txt') as file_object:
    #The open() function needs
    #one argument: the name of file you want to open.
    contents = file_object.read()
print(contents.rstrip())

#rstrip()method removes, or strips, any whitespace
#characters from the right side of a string


"""
#Types of path
1. relative path- need to select working directory.
2. absolute path - not necessary to select working directory.

windows support back slash \ in path 
(for working in mac and python use front slash).

linux supports front slash / in path

"""


#absolute path example
file_path='C:/1-python/pi_digits.txt'
with open(file_path) as file_object:
    contents =  file_object.read()
print(contents.rstrip())

######################################################

#reading line by line
filename='pi_digits.txt'
#we assign the name of the file we're reading from to the variable
with open (filename) as file_object:
    #we again use the with syntax to
    #let python open and close
    #the file properly
    
    for line in file_object:
        print(line)
        
#######################################################

#These blank lines appear because an invisible newline
#character is at the end of each line in the text file.
#using rstrip() on each line in
#the print() call eliminates these extra blank lines

filename='pi_digits.txt'
with open (filename) as file_object:
   
    for line in file_object:
        print(line.rstrip())

##########################################################

#Working with a file's contents
#After you read file into memory,
#you can do whatever you want with the data

filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
    pi_string =''
    for line in lines:
        pi_string += line.rstrip()
        print(pi_string)
        print(len(pi_string))

#########################################################

#Writing to a file
#one of the simplest way to save data is to write it
#to a file. when you write text to a file,
# the output will still be available after
#you close the terminal containing your program's output

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I Love Programming")

############################################################

#writing multiple lines
#the write() function doesnt add newlines
#to the text you write. 


filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I Love Programming.")
    file_object.write(" I Love creating new games")

###########################################################

#each string appears on its own line
filename = 'programming.txt'
#WE use the 'w' argument to open the file in for writing
with open(filename, 'w') as file_object:
    file_object.write("I Love Programming.\n")
    file_object.write("I Love creating new games\n")

##########################################################

#Appending to a file
#If you want to add content to a file
#instead of writing over existing content,
#you can open the file in append mode.
#when you open the file in append mode, python doesnt erase 
#the contents of the file.
#before returning the file object.

filename = 'programming.txt'
with open(filename, 'a') as file_object:
#WE use the 'a' argument to open the file for appending
#rather than writing over the existing file.
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

######################################################################

#the error 
#Exceptions are handled with try_except block
#handling the ZeroDivisionError Exception
print(5/0)

#using try except block

try:
    print(5/0)
except ZeroDivisionError:
    print("You cant divide by zero!")

####################################################################

a=5
b=6
c=a=b
print(5/0)

#################################################################
a=5
b=6
c=a+b
#print(5/0)
try:
    print(5/0)
except ZeroDivisionError:
    print("You cant divide by zero!")
print(c)


#Handling the FileNotFoundError Exception










