import os

os.rename("test1.txt", "test2.txt")
print("Rename filename form test1.txt to test2.txt :");

os.rename("test2.txt", "test1.txt")
print("Rollback from modified filename")
