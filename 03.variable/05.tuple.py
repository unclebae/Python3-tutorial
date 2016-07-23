#!/usr/local/bin/python3

tuple = ('abcd', 786, 2.23, 'john', 70.2 )
tinyTuple = (123,  'john')

#tuple is just read-only lists

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinyTuple * 2)
print(tuple + tinyTuple)
