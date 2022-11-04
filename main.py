def main():
    print("___WELCOME TO FIDA ACADEMY___")
    print("\t1)To Get Student Details")
    print("\t2)To Add New Student")
    print("\t3)To Remove Student")
    print("\t4)To Update Student Details")
    print("\t5)To Update Academy Name")
    print("\t6)To Get Number of Students")
    print("\t7)To Get All Student Details")
    print("\t8)To Get any Course Student Details")


    option=input("Enter AAny Above Given Option :")
    print()

    if option=="1":
        New_Student=Student()
        Student.Student_Dictionary[New_Student.Register_Number]=New_Student
    elif option=="2":
        pass
    elif option=="3":
        pass
    elif option=="4":
        pass
    elif option=="5":
        pass
class student:
    Student_Dictionary={}

    def __init__(self,Student_Name,Register_No,Mobile_No,A):
        self.Student_Name=input("\tEnter the student Name :")
        self.Register_No=input("\tEnter the Register number :")
        self.Mobile_No=input("\tEnter the Mobile Number :")
        self.Address=input("\tEnter the Address :")
        course=input("\tEnter the Course :"[Ex: JAVA,Python,C,RUST,Data_Science,Devops])
        self.Fees=input("\tEnter the actual Fees :")



        if course in course.field:
            course.field[course].courselist.append(self)
        else:
            new_course=field(course)
            new_course.courselist.append(self)
            course.field[course]=new_course

        self.course=course.field[course]

        print("\nStudent Added successfully")

    def getStudents(self):
        print("\n---Steudent Details---\n")
        print("\tStudent Name:",self.StudentName)
        print("\tRegister Number:",self.RegisterNumber)
        print("\tMobile Number:",self.MobileNumber)
        print("\tAddress:",self.Address)
        print("\tCourse:",self.Course)
        print("\tActual fees:",self.Actualfees)






        class course:
            field={}

