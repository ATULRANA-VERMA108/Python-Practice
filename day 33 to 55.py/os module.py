#  os module in python
 
# some common task by the os module : reading and writting the file the os module

import os

# Open the file in read-only mode
f = os.open("myfile.txt", os.O_RDONLY)

# Read the contents of the file
contents = os.read(f, 1024)

# Close the file
os.close(f)


# to open the file for the writting use the os.O_WRONGLY flag:

import os

# Open the file in write-only mode
f = os.open("myfile.txt", os.O_WRONLY)

# Write to the file
os.write(f, b"Hello, world!")

# Close the file
os.close(f)


# interactive with the file system :

import os

# Get a list of the files in the current directory
files = os.listdir(".")
print(files)  # Output: ['myfile.txt', 'otherfile.txt']


# create a new directory:
import os

# Create a new directory
os.mkdir("newdir")

# running system commands:

import os

# Run the "ls" command and print the output
output = os.system("ls")
print(output)  # Output: ['myfile.txt', 'otherfile.txt']

#You can also use the os.popen function to run a command and get the output as a file-like object:

import os

# Run the "ls" command and get the output as a file-like object
f = os.popen("ls")

# Read the contents of the output
output = f.read()
print(output)  # Output: ['myfile.txt', 'otherfile.txt']

# Close the file-like object
f.close()


# for more information for the os module access by using of google....