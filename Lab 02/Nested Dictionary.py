name=input("Enter student's name:")
dept=input("Enter student's department:")
cgpa=float(input("Enter student's CGPA:"))
name1=input("Enter student's name:")
dept1=input("Enter student's department:")
cgpa1=float(input("Enter student's CGPA:"))
#Creating the nested dictionary
students={
101:{"Name":name,"Dept":dept,"CGPA":cgpa},
102:{"Name":name1,"Dept":dept1,"CGPA":cgpa1}
}
#Print the dictionary
print(students)
#Access the elements
print("Access Elements:")
print(students[101]["Name"])
print(students[102]["CGPA"])
print("Access student:")
print(students[102])
print("Traversing The Dictionary:")
for id in students:
    print(id,students[id])
#Adding new student
name2=input("Enter student's name:")
dept2=input("Enter student's department:")
cgpa2=float(input("Enter student's CGPA:"))
students[103]={
    "Name":name2,
    "Dept":dept2,
    "CGPA":cgpa2
}
print("After Adding new student:")
for id, info in students.items():
    print("Student ID:",id)
    for key,value in info.items():
        print(key,":",value)
print("Updade student's  CGPA with student ID 101:")
students[101]["CGPA"]=3.50
print("New CGPA:",students[101]["CGPA"])
print("Add a new field in student ID 103:")
sem=input("Enter student's semester:")
students[103]["Semester"]=sem
print(students[103])
print("Delete student with student ID 103:")
del students[103]
for id,info in students.items():
    print("Student ID:",id)
    for key,value in info.items():
        print(key,":",value)