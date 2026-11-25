class Employee:
    total_employees = 0

    def __init__(self, name):
        self.name = name
        Employee.total_employees += 1

employee1 = Employee("Amit")
employee2 = Employee("Priya")
employee3 = Employee("Rahul")
employee4 = Employee("Neha")
employee4 = Employee("Nehal")
print("Total employees:", Employee.total_employees)
