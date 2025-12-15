class Student:
    total_students = 0
    
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        Student.total_students += 1
    
    @classmethod
    def get_total_students(cls):
        return cls.total_students
    
    @classmethod
    def create_from_string(cls, student_string):
        """Alternative constructor from string like 'AmirKhan:S12345'"""
        name, student_id = student_string.split(":")
        return cls(name, student_id)
    
    @staticmethod
    def is_valid_student_id(student_id):
        """Check if student ID follows pattern SXXXXX"""
        return student_id.startswith('S') and student_id[1:].isdigit()
    
    @staticmethod
    def get_university_name():
        return "Tech University"
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Valid ID: {self.is_valid_student_id(self.student_id)}")

# Create students
student1 = Student("AmirKhan", "S12345")
student2 = Student.create_from_string("Sara:S67890")

print("Student Information:")
print("-" * 30)
student1.display_info()
print()
student2.display_info()

print(f"\nTotal students: {Student.get_total_students()}")
print(f"University: {Student.get_university_name()}")
print(f"Is 'S12345' valid? {Student.is_valid_student_id('S12345')}")
print(f"Is '12345' valid? {Student.is_valid_student_id('12345')}")