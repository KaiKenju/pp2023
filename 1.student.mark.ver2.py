students = {} #/
courses = {} #/     stored information in set 
marks = {}  #/

#input student information
def input_students():
    num_students = int(input("Enter the number of students in the class: "))
    for i in range(num_students):
        print(f"------ Student No.{i+1} -------")
        student_id = input("Enter the student ID: ")
        student_name = input("Enter the student name: ")
        student_dob = input("Enter the student dob: ")
        students[student_id] = {"name": student_name, "dob": student_dob}    #dictionary ("key": student_name, "value": student_dob)

#input course information
def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    for j in range(num_courses):
        print(f"------ Course No.{j+1} -------")
        course_id = input("Enter the course ID: ")
        course_name = input("Enter the course name: ")
        courses[course_id] = {"name": course_name} #dictionary

#select a course and input marks for students
def input_marks():
    course_id = input("Next, Select a 'course ID' to prepare input marks: ")
    if course_id not in courses:
        print("Invalid course ID")
        return
    for student_id in students:
        mark = float(input(f"Enter the mark for {students[student_id]['name']}: "))  #key: "name"
        if student_id not in marks:
            marks[student_id] = {}
        marks[student_id][course_id] = mark

#list courses
def list_courses():
    print("ID | Course Name")
    for course_id in courses:
        print(f"{course_id}: {courses[course_id]['name']}")

#list students
def list_students():
    print("Student ID|Student Name")
    for student_id in students:
        print(f"{student_id}: {students[student_id]['name']}")

#show marks for a given course
def show_marks():
    course_id = input("Now, Enter the course ID: ")
    if course_id not in courses:
        print("Invalid course ID")
        return
    for student_id in students:
        if student_id in marks and course_id in marks[student_id]:
            print(f"{students[student_id]['name']}: {marks[student_id][course_id]}")     #{name}:{mark}
        else:
            print(f"{students[student_id]['name']}: N/A")

#main
def main():
    input_students()
    input_courses()

    while True:
        print("||**** Select an option ****||")
        print("0. Quit")
        print("1. Input marks for a course")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a given choice")
        choice = input("Enter your choice: ")
        if choice == "1":
            input_marks()
        elif choice == "2":
            list_courses()
        elif choice == "3":
            list_students()
        elif choice == "4":
            show_marks()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")
main()