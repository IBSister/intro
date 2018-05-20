#Opening a File
fo = open("foo.txt", "wb")
print("Name of file: ", fo.name)
print("Closed or not: ", fo.closed)
print("Opening mode: ", fo.mode)
#Closing a file
fo.close()

#Writing to a file
fo = open("foo.txt", "w")
fo.write("Hey")
fo.close()

#Reading from file
fo = open("foo.txt", "r+")
str = fo.read(10);
print("Reading String is: ", str)
fo.close()