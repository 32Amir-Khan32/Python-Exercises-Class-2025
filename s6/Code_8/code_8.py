class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major
    
    def __str__(self):
        return f"Student: {self.name} (ID: {self.student_id}, Major: {self.major})"

student1 = Student("AmirKhan", "S12345", "Computer Science")
student2 = Student("Sara", "S67890", "Mathematics")

print(student1)
print(student2)