fo = open("foo.txt", "r+")
str = fo.read(10)
print("Read ten bytes from file :", str)
fo.close()
