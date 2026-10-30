import pandas as pd
import numpy as np

data=pd.read_csv("student.csv")
df=pd.DataFrame(data)
# print(df)
# =================  total marks  =========================
df["total_marks"]=df[["Python","Maths","DBMS","English"]].sum(axis=1)
# =================   percentage  ==========================
df["percentage"]=(df["total_marks"])/4

# =================   grade  =============================
def grade(percentage):
    if percentage>=90:
        return  ("A+")
    elif percentage>=80:
        return  ("A")
    elif percentage>=70:
        return ("B")
    elif percentage>=60:
        return ("C")
    elif percentage>=50:
        return ("D")
    elif percentage<50:
        return ("F")

df["grade"]=df["percentage"].apply(grade)

# ==============  Rank  =================================
df["Rank"]=df["percentage"].rank(ascending=False).astype(int)

# ===============  Status ===============================
def status(percentage):
    if percentage>=90:
        return  ("Excellent")
    elif percentage>=80:
        return  ("Very good")
    elif percentage>=70:
        return ("Good")
    elif percentage>=60:
        return ("Pass")
    elif percentage>=50:
        return ("Pass")
    elif percentage<50:
        return ("Fail")

df["Status"]=df["percentage"].apply(status)

# =======================  Questions  =============================
print("=======================================")
print("    Student Performance System")
print("=======================================")
print("1. Show all students")
print("2. Search student")
print("3. Show topper")
print("4. Show average marks")
print("5. Show passed students")
print("6. Show failed students")
print("7. Show attendance shortage")
print("8. Show class statistics")
print("9. Exit")

print("========= All student's Report ===========\n")

while True:
    user=input("Choose the option:")
    

    if user=="1":
        print(df,"\n")
    elif user=="2":
        name =input("enter the name:")

        s=df[df["Name"].str.lower()==name.lower()]
        if s.empty:
            print("Student not found")
        else:
            print("========== STUDENT DETAIL ===========\n")
            print()
            print (s.T.to_string(header=False))

    elif user=="3":
        print("============= Topper Student =============\n")
        topper=df[df["percentage"]==df["percentage"].max()]
        print(topper.T.to_string(header=False))

    elif user=="4":
        print("============= Average Marks =============\n")
        average_marks=df["total_marks"].mean()
        print("average_marks :",average_marks)

    elif user=="5":
        print("============== Passed Students ==============\n")
        pass_student=df[df["percentage"]>=50][["Name","total_marks","grade","Status"]]
        print(pass_student)

    elif user=="6":
        print("================ Failed Sudents =============\n")
        failed_student=df[df["percentage"]<50][["Name","total_marks","grade","Status"]]
        print(failed_student.to_string(index=False))

    elif user=="7":
        print("================ Attendance Shortage ============\n")
        short_attendance=df[df["Attendance"]<75][["Name","Attendance"]]
        print(short_attendance.to_string(index=False))

    elif user=="8":
        print("================ Class Statistics =============\n")
        total_students=len(df)
        print("Total_students :",total_students)
        male_students=df[df["Gender"]=="M"]["Name"].count()
        print("Total_Male_students :",male_students)
        female_students=df[df["Gender"]=="F"]["Name"].count()
        print("Total_Female_students :",female_students,"\n")

        Highest_percentage=df["percentage"].max()
        print("Highest_percentage :",Highest_percentage)
        lowest_percentage=df["percentage"].min()
        print("lowest_percentage :",lowest_percentage,"\n")

        average_percentage=df["percentage"].mean()
        print("Average_percentage :",average_percentage)
        average_attendance=df["Attendance"].mean()
        print("Average_Attendance :",average_attendance,"\n")

        passed_students=df[df["percentage"]>=50]["Name"].count()
        print("Passed Students :",passed_students)
        fail_students=df[df["percentage"]<50]["Name"].count()
        print("Failed Students :",fail_students,"\n")

        Attendance_shortage=df[df["Attendance"]<75]["Name"].count()
        print("Attendance_shortage :",Attendance_shortage)

        topper=df[df["percentage"]==df["percentage"].max()]["Name"]
        print("Topper :",topper.to_string(index=False),"\n")
        print("===================================================\n")

    elif user=="9":
        print("Exit")
