name=input("Enter student's name:")
dept=input("Enter student's department:")
cgpa=float(input("Enter student's cgpa:"))
#Creating a dictionary
student={
    "Name":name,
    "Dept":dept,
    "CGPA":cgpa
}
print("Initial dictionary:")
#printing a dictionary
print(student)
#Access keys
print(student["Name"])
#Access keys using get()
print(student.get("CGPA"))
#Print keys
print("Keys:")
print(student.keys())
#Print values
print("Values:")
print(student.values())
#Access keys through loop
print("Traverse the initial dictionary:")
for key in student:
    print(key,student[key])
#Add new element
sem=input("Enter student's semester:")
student["Semester"]=sem
print("After adding semester:")
for keys in student:
    print(keys,student[keys])
#Copy Dictionary
student1=student.copy()
#Delete element
del student["CGPA"]
#Traverse Using Items
print("After deleting CGPA:")
for key, value in student.items():
  print(key,value)
print("Copied dictionary:")
for key, val in student1.items():
   print(key,val)