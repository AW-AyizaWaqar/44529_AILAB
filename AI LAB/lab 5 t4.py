class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print(f"Programming Language: {self.programming_language}")

# Example usage:
manager1 = Manager("Diana", 80000, "HR")
developer1 = Developer("Eve", 75000, "Python")

manager1.display_details()  # Output: Name: Diana, Salary: 80000, Department: HR
developer1.display_details()  # Output: Name: Eve, Salary: 75000, Programming Language: Python
