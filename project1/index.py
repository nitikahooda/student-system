Python=int(input("enter the marks of python:"))
Maths=int(input("enter the marks of maths:"))
Dbms=int(input("enter the marks of dbms:"))
English=int(input("enter the marks of english:"))

def calculate_total(Python,Maths,Dbms,English):
    return Python+Maths+Dbms+English

total_marks=calculate_total(Python,Maths,Dbms,English)
print("total marks:",total_marks)

def calculate_percentage(total_marks):
    return (total_marks/400)*100

total_percentage=calculate_percentage(total_marks)
print("total percentage :",total_percentage)


def get_grade(total_percentage):
    if total_percentage >=90:
        print("Grade : A+ grade")
    elif 90>total_percentage >=80:
        print("Grade : A grade")
    elif 80>total_percentage >=70:
        print("Grade : B grade")
    elif 70>total_percentage >=60:
        print("Grade : C grade")
    elif 60>total_percentage >=50:
        print("Grade : D grade")
    elif total_percentage <50:
        print("fail")

get_grade(total_percentage)

def get_status(total_percentage):
    if total_percentage>=75:
        print("status : Excellent")
    elif 75> total_percentage>=60:
        print("status : Good")
    elif 60> total_percentage>=40:
        print("status : pass")
    elif total_percentage<40 :
        print("status : fail")

get_status(total_percentage)


