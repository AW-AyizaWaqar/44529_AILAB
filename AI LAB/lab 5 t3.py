class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

# Example usage:
student1 = Student("Charlie", 20, [90, 80, 85, 95])
print(student1.average_grade())  # Output: 87.5
