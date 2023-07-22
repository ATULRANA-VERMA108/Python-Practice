""" seek()and tell() function: the seek() and tell() functions are used to work with
 file objects and their positions within a file. this is buildin function
 which provides a consistent interface for reading and writing to various file-like objects, 
 such as files, pipes, and in-memory buffers."""

 #seek function():allow to move in the current position within file in the specific position
 # position specified with byte and move either left or write 
with open('file.txt', 'r') as f:
  print(type)
  # Move to the 10th byte in the file
  f.seek(10)

  # Read the next 5 bytes
  data = f.read(5) 
  print(data)

# tell function(): tell function return the current postion with the file,in byte
 
with open('file.txt', 'r') as f:
  # Read the first 10 bytes
  data = f.read(10)

  # Save the current position
  current_position = f.tell()

  # Seek to the saved position
  print(f.seek(current_position))

#truncate() function: it is define the mode of opening file like as read(r),write(w),append(a)
with open('sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)

with open('sample.txt', 'r') as f:
  print(f.read())