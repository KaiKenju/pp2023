import math
import numpy as np
from input import *
from output import *

def main():
        num_students = input_num_students()
        for i in range(num_students):
            input_student_infor(i+1)
        
        num_courses = input_num_courses()
        for j in range(num_courses):
            input_course_infor(j+1)
        
        list_student()
        show_course() # show credits

        for choice in range(1, num_courses+1):
            course_id = choice
            input_student_marks(course_id)
            
        new_list_mark = [] #list of mark ('value') of the dictionary
        sort_list_gpa = [] #list gpa to descending
        for myvalue in marks.values():
            new_list_mark.append(myvalue)

        arr = np.array(new_list_mark) # [10 11 12 13]
        arr1 = np.array(creditss) # [4,3]
        jin = total_cre()

        print(f"| {'Name Student': <10} | {'GPA': <10} |")
        print("-" * 30)
        def gpa(temp):
            back = []
            x = 0
            a = arr[temp:len(arr):num_courses] #[10 12] and [11 13]
            for i in range(0,len(a)):
                for j in range(0,len(arr1)):
                    if i == j:
                        x += a[i]*arr1[j] / jin     #10*4+12*3 / (4+3)   and  11*4+13*3 / 7
        
            test =math.floor(x*10)/10
            for student in students:
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
        
if __name__ == "__main__":
    main()
