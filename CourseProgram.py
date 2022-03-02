"""
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH 
student in the students list using a For loop.
3) Print out the student name, course name, 
CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
"""

from CourseClass import Register
import CourseClass as cc


def main():

    name = "MIS 4322 - Advanced Python"
    crn = "250309"
    seats = 4
    status = "open"
    students = ["John", "James", "Jill", "Jack", "Joanne"]


student = cc.Course(students, crn, seats, status)
register = Register(studentname)

for name in student:
    student.get_name()
    register.get_studentname
    print("Student Name: ", register.get_studentname())
    print("Course name: ", student.get_name())
    print("CRN:", student.get_crn())
    print("Seats Left: ", student.get_status())
    if student.get_status() <= 1:
        print(
            "Sorry",
            register.get_studentname(),
            "registration is closed for MIS 4322 - Advanced Python",
        ),
    else:
        student.get_status() - 1


main()
