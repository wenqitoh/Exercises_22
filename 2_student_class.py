"""New class practice exercise - students"""


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # integer 1-100

    # method to return student grade
    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = [] # blank list to hold student details

    # method to add students to a course
    def add_student(self, student):
        # test that there is room in the class
        if len(self.students) < self.max_students:
            self.students.append(student) # add to class if room
            return True # if student added successfully
        return False # if student not added to course

    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade() # using a method from the Student
            # class. Could use student.grade above but using the function is
            # more effective and is more future-proof - eg. in the event of a
            # grade being determined in a different way
            return total / len(self.students)


# main routine


# instantiate 3 student objects
s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Caleb", 19, 65)

# instantiate course object
course1 = Course("Computer Science", 2)

# add students to course
course1.add_student(s1)
course1.add_student(s2)
print(course1.add_student(s3))

# Get the average grade of all students in a course
print(f"The average grade in {course1.name} is {course1.get_average_grade()}")
