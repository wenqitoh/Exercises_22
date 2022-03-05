"""Create a student system - exercise
Wen-Qi Toh
28/2/22"""


# classes & functions
class Student:
    def __init__(self, name, age, ph_num, form_class, subjects, is_male):
        self.name = name
        self.age = age
        self.ph_num = ph_num
        self.form_class = form_class
        self.subjects = subjects
        self.is_male = is_male
        self.enrolled = True
        student_list.append(self)
        subject_list.append(self.subjects)

    def display_info(self):
        print("\n######################\n")
        print("student name: ", self.name)
        print("student age: ",self.age)
        print("student phone number: ", self.ph_num)
        print("student form class: ", self.form_class)
        print("student subject/s: ", self.subjects)
        print("student is male: ", self.is_male)
        print("student is enrolled: ", self.enrolled)


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        teacher_list.append(self)
        teacher_subject.append(self.subject)

    def display_info(self):
        print("\n######################\n")
        print("teacher name: ", self.name)
        print("teacher subject: ", self.subject)


def add_student():
    print("adding a new student: ")
    name = input("student full name: ")
    age = int_check("student age: ")
    ph_num = int_check("student phone number: ")
    form_class = input("student form class: ")
    subjects = enter_classes()
    is_male = get_gender()
    enrolled = True
    Student(name, age, ph_num, form_class, subjects, is_male)
    print(f"\n{name} has been added to the student database\n")


def get_gender():
    valid_gender = False
    while not valid_gender:
        gender = input("Enter student gender ('M' or 'F'): ").upper()
        if gender == "M":
            return True
        elif gender == "F":
            return False
        else:
            print("Whoops... gender can only be 'M' or 'F'")


def enter_classes():
    subject = ""
    subject_list_2 = []
    while subject != "Q":
        subject = input("Enter the 3 character code for a class/subject. "
                        "Enter 'Q' to stop: ").upper()
        if subject == "Q":
            break
        else:
            subject_list_2.append(subject)
            return','.join(subject_list_2)


def delete_student():
    name = input("\nWhat is the student's name? ").title()
    found = False
    for student in student_list:
        if name == student.name:
            confirmation = input("Are you sure you want to remove this student from the records?"
                                 "(enter 'Yes'/'No'): ").title()
            if confirmation == "Yes":
                found = True
                student_list.remove(student)
                print("\n* student removed *")

    if not found:
        print("Student not found.")


def print_student_details():
    for student in student_list:
        student.display_info()


def select_student_age():
    counter = 1
    ask_age = int_check("Please enter an age: ")
    for student in student_list:
        if student.age > ask_age:
            student.display_info()
            counter += 1
    print(f"\nTotal number of students older than {ask_age}: {counter} students")


def count_students():
    find_class = input("What class are you looking for? ").upper()
    counter = 0

    for subjects in subject_list:
        class_list = subjects.split(", ")
        for classes in class_list:
            if find_class == classes:
                counter += 1
    for teacher in teacher_list:
        if find_class == teacher.subject:
            print(f"\n**Teacher of {find_class} is {teacher.name}**")
            print(f"\nThere are currently {counter} students enrolled in this class.")
    if counter == 0:
        print("\nNo student currently enrolled in this class.")


def find_student():
    find_stu = input("Which student are you looking for? ").title()
    found = False
    for student in student_list:
        if find_stu == student.name:
            student.display_info()
            print("\n######################\n")
            found = True
    if not found:
        print("\nStudent not found.")


def generate_students():
    # available form classes are: "BAKER", "MORGAN", "MCNICOL", "GRAHAM", "BELL", "NIMMO", "BARKER"
    # available classes are: "ART", "ENG", "MAT", "GRA", "DTC", "PHY", "BIO"
    import csv
    with open('random_students.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter='|')
        for line in filereader:
            if line[5] == "True":
                is_male = True
            else:
                is_male = False
            Student(line[0], int(line[1]), line[2], line[3], line[4], is_male)


def int_check(text):
    valid = False
    while not valid:
        try:
            number_to_check = int(input(text))
            if isinstance(number_to_check, int):
                valid = True
                return number_to_check
        except ValueError:
            print("Whoops, entry must be an integer...")


def print_teacher_details():
    for teacher in teacher_list:
        teacher.display_info()


def gender():
    count_m = 0
    count_f = 0
    which_gender = input("Which gender would you like to find of students? "
                         "(enter 'M' for male, 'F' for female): ").title()
    for student in student_list:
        if which_gender == "M" and student.is_male is True:
            print(student.name)
            count_m += 1

        elif which_gender == "F" and student.is_male is False:
            print(student.name)
            count_f += 1
        else:
            print("Error! Please enter either 'M' for male of 'F' for female. "
                  "Returning user back to main menu.")
            return
    if count_m > 0:
        print("\n*** total male students: ", count_m)
    else:
        print("\n*** total female students: ", count_f)


def menu():
    stop = False
    while not stop:
        print("\n***** Main Menu *****")
        print("1. Count students taking a particular subject")
        print("2. Print a full list of all students")
        print("3. Print a list of students above a particular age")
        print("4. Get details of a particular student")
        print("5. Add new student")
        print("6. Delete student from records")
        print("7. Print teacher information")
        print("8. Find male/female students")
        choice = input("\nWhat would you like to do?"
                       "\n- enter a number or 'Q' to exit: ")
        if choice == "1":
            count_students()
        elif choice == "2":
            print_student_details()
        elif choice == "3":
            select_student_age()
        elif choice == "4":
            find_student()
        elif choice == "5":
            add_student()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            print_teacher_details()
        elif choice == "8":
            gender()
        elif choice == 'Q':
            stop = True
            print("Goodbye!")


# main routine
student_list = []
teacher_list = []
subject_list = []
teacher_subject = []

Teacher("Mr Bowater", "GRA")
Teacher("Miss Wallace", "MAT")
Teacher("Mr Vannoort", "CHE")
Teacher("Mr BAKER(is super cool)", "DTC")
Teacher("Mr Harris", "PHY")
Teacher("Mr Glover", "ART")
Teacher("Mr McConnell", "ENG")

generate_students()
menu()
gender()

