import math 
import numpy as np
#contructer of Student
class Student:  
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

#contructer of Course
class Course:
    def __init__(self,course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

##contructer of Mark
class MarkStudent:
    def __init__(self):
        self.students = [] #list
        self.courses = [] #list
        self.marks = {} #dict
        self.creditss = [] #list

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
    
    def input_course_infor(self, j):
        print(f"------- Course No.{j} --------")
        course_id = int(input("Enter course ID: "))
        course_name = input("Enter course name: ")
        course_credits = int(input("Enter credits of the course: "))
        course = Course(course_id, course_name, course_credits)
        self.courses.append(course)

    #input mark
    def input_student_marks(self, course_id):
        for student in self.students:
            mark = float(input(f"Enter mark for student {student.name} in course {self.courses[course_id -1].name}: "))
            rounded_mark = math.floor(mark * 10) / 10 # round down to 1 decimal place
            self.marks[(student.student_id, course_id)] = rounded_mark
    
    #list of students
    def list_student(self):
        print("List of students:")
        print(f"| {'ID Student': <10} | {'Name Student': <20} | {'DOB': <15} |")
        print("-" * 55)
        for student in self.students:
            print(f"| {student.student_id:10} | {student.name:20} | {student.dob:15} |")
          
    
   #information coursecourse
    def show_course(self):
        print("List of courses: ")
        print(f"| {'ID Course': <10} | {'Name Course': <20} | {'Credit': <10} |")
        print("-" * 50)
        for course in self.courses:
            print(f"| {course.course_id:10} | {course.name:20} | {course.credits:10} |")
            self.creditss.append(course.credits)
    
    #total credits
    def total_cre(self):
        k = 0
        for course in self.courses:
            k += course.credits
        return k
    
    def main(self):
        num_students = self.input_num_students()
        for i in range(num_students):
            self.input_student_infor(i+1)
        
        num_courses = self.input_num_courses()
        for j in range(num_courses):
            self.input_course_infor(j+1)
        
        #self.list_courses()
        self.list_student()
        self.show_course() # show credits

        for choice in range(1, num_courses+1):
            course_id = choice
            self.input_student_marks(course_id)
            
        new_list_mark = [] #list of mark ('value') of the dictionary
        sort_list_gpa = [] #list gpa to descending
        for myvalue in self.marks.values():
            new_list_mark.append(myvalue)

        arr = np.array(new_list_mark) # [10 11 12 13]
        arr1 = np.array(self.creditss) # [4,3]
        jin = self.total_cre()

        print(f"| {'Name Student': <10} | {'GPA': <10} |")
        print("-" * 26)
        def gpa(temp):
            back = []
            x = 0
            a = arr[temp:len(arr):num_courses] #[10 12] and [11 13]
            for i in range(0,len(a)):
                for j in range(0,len(arr1)):
                    if i == j:
                        x += a[i]*arr1[j] / jin     #10*4+12*3 / (4+3)   and  11*4+13*3 / 7
        
            test =math.floor(x*10)/10
            for student in self.students:
                z = student.name
                back.append(z)
            back1 = back.pop(temp) #pop first student and so on
            print(f"| {back1:10} | {test:10} |")
            sort_list_gpa.append(test) # take the "test" to the 'sort_list_gpa'

            if temp+1 < num_students:
                return gpa(temp+1)
            else:
                pass
        
        gpa(0)
        print("Sort student list by GPA descending: ")
        sort_list_gpa.sort(reverse=True)
        print(sort_list_gpa)
        
kai = MarkStudent()
kai.main()

