fo = open("foo.txt", "r+")
str = fo.read(10)
print("Rad String is : ", str)

position = fo.tell()
print("Current file position : ",  position)

position = fo.seek(0, 0)
str = fo.read(10)
print("Again read String is : ", str)
fo.close();
