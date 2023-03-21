from domain.student import Student
from domain.course import Course
import math

courses = [] #list
students = [] #list
marks = {} #dict
def input_num_students():
        x =  int(input("Enter the number of students: "))
        return x

def input_student_infor(i):
        print(f"------- Student No.{i} ------- ")
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth (DD-MM-YYYY): ")
        student = Student(student_id, student_name, student_dob)
        students.append(student)
    
def input_num_courses():
        y = int(input("Next, Enter the number of courses: "))
        return y
    
def input_course_infor(j):
        print(f"------- Course No.{j} --------")
        course_id = int(input("Enter course ID: "))
        course_name = input("Enter course name: ")
        course_credits = int(input("Enter credits of the course: "))
        course = Course(course_id, course_name, course_credits)
        courses.append(course)

def input_student_marks(course_id):
        for student in students:
            mark = float(input(f"Enter mark for student {student.name} in course {courses[course_id -1].name}: "))
            rounded_mark = math.floor(mark * 10) / 10 # round down to 1 decimal place
            marks[(student.student_id, course_id)] = rounded_mark