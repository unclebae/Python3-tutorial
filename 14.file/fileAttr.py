fo = open("foo.txt", "wb")
print("Name of the file: ", fo.name)
print("Close or not: ", fo.closed)
print("Opening mode: ", fo.mode)
fo.close()

