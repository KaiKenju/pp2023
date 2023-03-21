from domain.course import Course
from input import *
 #list of students

creditss = [] #list
def list_student():
        print("List of students:")
        print(f"| {'ID Student': <10} | {'Name Student': <20} | {'DOB': <15} |")
        print("-" * 55)
        for student in students:
            print(f"| {student.student_id:10} | {student.name:20} | {student.dob:15} |")
          
    
   #information coursecourse
def show_course():
        print("List of courses: ")
        print(f"| {'ID Course': <10} | {'Name Course': <20} | {'Credit': <10} |")
        print("-" * 50)
        for course in courses:
            print(f"| {course.course_id:10} | {course.name:20} | {course.credits:10} |")
            creditss.append(course.credits)
    
    #total credits
def total_cre():
        k = 0
        for course in courses:
            k += course.credits
        return k