#Input number of student
def input_num_students():
    x = int(input("Enter the number of students: "))
    return x

#data for student
def input_student_info(i):
    print(f"------- Student No.{i} ------- ")
    student_id = int(input("Enter student ID: "))
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth (DD-MM-YYYY): ")
    return (student_id, student_name, student_dob)

#number of courses
def input_num_courses():
    y = int(input("Next, Enter the number of courses: "))
    return y 

#date of course
def input_course_info(j):
    print(f"------- Course No.{j} --------")
    course_id = int(input("Enter course ID: "))
    course_name = input("Enter course name: ")
    return (course_id, course_name)

#input mark for students
def input_student_marks(students, courses, course_id):
    marks = {}
    for student in students:
        marks[student[0]] = float(input(f"Enter mark for student {student[1]} in course {courses[course_id-1][1]}: "))
    return marks


#list of courses
def list_courses(courses):
    print("List of courses:")
    for course in courses:
        print(f"{course[0]}: {course[1]}")

#list of students
def list_students(students):
    print("List of students:")
    for student in students:
        print(f"{student[0]}: {student[1]} (DoB: {student[2]})")  #id - name - dob

#show students marks and name
def show_student_marks(students, marks):
    print(f"Student marks for  given course : ")
    for student in students:
        if student[0] in marks:
            print(f"{student[1]}: {marks[student[0]]}")
        else:
            print(f"{student[1]}: N/A")

def main():
    num_students = input_num_students() #num of students
    students = [input_student_info(i+1) for i in range(num_students)] #ex: range(2) = 0 1 --> i+1
    num_courses = input_num_courses() #num of courses
    courses = [input_course_info(j+1) for j in range(num_courses)]
    print("\n")
    list_courses(courses)
    print("\n")
    list_students(students)
    
    choice = int(input("Select a course to input marks (numerical order of list of courses): "))
    
    if choice in range(1, num_courses+1):
        course_id = choice
        marks = input_student_marks(students, courses, course_id)
        course_name = courses[course_id-1][1]
        print(f"Marks for {course_name}: {marks}")
        

    show_student_marks(students, marks) #display marks

main()
