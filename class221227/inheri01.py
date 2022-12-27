# -*- coding : utf-8 -*-

class Employee:
    def __init__(self, name, salary):

            self.name = name
            self.salary = salary


if __name__ == "__main__":
    emp1 = Employee("HYUK", 100000)
    emp2 = Employee("Kim", 80000)
    print(emp1.name, emp1.salary)
    print(emp2.name, emp2.salary)
    