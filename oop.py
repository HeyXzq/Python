#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Employee:
    '所有员工的基类'
    empCount = 0
 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.patience = 3
        Employee.empCount += 1
   
    def displayCount(self):
        print( "Total Employee %d" % Employee.empCount)
 
    def displayEmployee(self):
        if self.patience <= 0:
            print('out')
            return
        else:
            print( "Name : ", self.name,  ", Salary: ", self.salary)
        self.patience -= 1
        print(self.patience)
      

#创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
print(Employee.empCount)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
print(Employee.empCount)

emp1.displayEmployee()
emp1.displayEmployee()
emp1.displayEmployee()
emp1.displayEmployee()

emp2.displayEmployee()

