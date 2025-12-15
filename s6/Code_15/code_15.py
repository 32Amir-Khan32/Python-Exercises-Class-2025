class University:
    def __init__(self, name):
        self.name = name
        self.departments = []
    
    def add_department(self, department_name):
        dept = self.Department(department_name)
        self.departments.append(dept)
        return dept
    
    class Department:
        def __init__(self, name):
            self.name = name
            self.courses = []
            self.professors = []
        
        def add_course(self, course_code, course_name):
            course = self.Course(course_code, course_name)
            self.courses.append(course)
            return course
        
        def add_professor(self, name, specialization):
            prof = self.Professor(name, specialization)
            self.professors.append(prof)
            return prof
        
        def display_info(self):
            print(f"\nDepartment: {self.name}")
            print(f"Courses ({len(self.courses)}):")
            for course in self.courses:
                print(f"  - {course.course_code}: {course.course_name}")
            
            print(f"Professors ({len(self.professors)}):")
            for prof in self.professors:
                print(f"  - {prof.name} ({prof.specialization})")
        
        class Course:
            def __init__(self, course_code, course_name):
                self.course_code = course_code
                self.course_name = course_name
        
        class Professor:
            def __init__(self, name, specialization):
                self.name = name
                self.specialization = specialization

# Create university system
uni = University("Tech University")

# Add departments
cs_dept = uni.add_department("Computer Science")
math_dept = uni.add_department("Mathematics")

# Add courses to CS department
cs_dept.add_course("CS101", "Introduction to Programming")
cs_dept.add_course("CS201", "Data Structures")
cs_dept.add_course("CS301", "Algorithms")

# Add professors to CS department
cs_dept.add_professor("Dr. Smith", "Artificial Intelligence")
cs_dept.add_professor("Dr. Johnson", "Database Systems")

# Add courses to Math department
math_dept.add_course("MATH101", "Calculus I")
math_dept.add_course("MATH201", "Linear Algebra")

# Add professors to Math department
math_dept.add_professor("Dr. Brown", "Pure Mathematics")
math_dept.add_professor("Dr. Davis", "Applied Mathematics")

print(f"University: {uni.name}")
print("-" * 40)

# Display department information
cs_dept.display_info()
math_dept.display_info()