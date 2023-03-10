#contructer of Student
class Student:  
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

#contructer of Course
class Course:
    def __init__(self,course_id, name):
        self.course_id = course_id
        self.name = name

##contructer of Mark
class MarkStudent:
    def __init__(self):
        self.students = [] #list
        self.courses = [] #list
        self.marks = {} 

    def input_num_students(self):
        x =  int(input("Enter the number of students: "))
        return x

    def input_student_infor(self, i):
        print(f"------- Student No.{i} ------- ")
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth (DD-MM-YYYY): ")
        student = Student(student_id, student_name, student_dob)
        self.students.append(student)
    
    def input_num_courses(self):
        y = int(input("Next, Enter the number of courses: "))
        return y
    
    #data course
    def input_course_infor(self, j):
        print(f"------- Course No.{j} --------")
        course_id = int(input("Enter course ID: "))
        course_name = input("Enter course name: ")
        course = Course(course_id, course_name)
        self.courses.append(course)

    #input mark
    def input_student_marks(self, course_id):
        for student in self.students:
            mark = float(input(f"Enter mark for student {student.name} in course {self.courses[course_id -1].name}: "))
            self.marks[(student.student_id, course_id)] = mark
    
   #show course
    def list_courses(self):
        print("Information of courses: ")
        print(f"| {'STT': <10} | {'ID Course': <10} | {'Name Course': <10} | ")
        print("-" * 40)
        temp = 0
        for course in self.courses:
            temp +=1
            print(f"| {temp:10} | {course.course_id:10} | {course.name:10} |")
        print("-" * 40)
    
    #show data student
    def list_student(self):
        print("Information of students:")
        print(f"| {'ID Student': <10} | {'Name Student': <10} | {'DOB': <10} |")
        print("-" * 42)
        for student in self.students:
            print(f"| {student.student_id:10} | {student.name:12} | {student.dob:10} |")
        print("-" * 42)

    #show mark
    def show_mark(self,course_id):
        print("Mark of student: ")
        print(f"| {'Student Name': <10} | {'Course': <10} | {'Mark': <10} |")
        print("-" *40)
        for student in self.students:
            if (student.student_id, course_id) in self.marks:
                mark = self.marks[(student.student_id, course_id)]
                print(f"| {student.name:10} | {self.courses[course_id-1].name:12} | {mark:10} |")
            else:
                print(f"| {student.name:10} | {self.courses[course_id-1].name:12} | {'N/A':10} |")
    
    def main(self):
        num_students = self.input_num_students()
        for i in range(num_students):
            self.input_student_infor(i+1)
        
        num_courses = self.input_num_courses()
        for j in range(num_courses):
            self.input_course_infor(j+1)

        self.list_student()
        self.list_courses()

        choice = int(input("Select a course to input marks (numerical order of list of courses): "))
        if choice in range(1, num_courses+1):
            course_id = choice
            self.input_student_marks(course_id)
            self.show_mark(course_id)

kai = MarkStudent()
kai.main()