class Employee:
    empCount=0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self) :
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self) :
        print ("Name : ", self.name, ", Salary: ", self.salary)

emp1 = Employee("Kido", 100)
emp1.displayCount()
emp1.displayEmployee()

print("hasattr : ", hasattr(emp1, 'salary'))
print("getattr : ", getattr(emp1, 'salary'))
setattr(emp1, 'salary', 7000)
delattr(emp1, 'salary')
