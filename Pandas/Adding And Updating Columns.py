import pandas as pd
student_data={
    "Name":["Shafin","Fatin","Farhan","Fariha","Irin","Jowa","Arif"],
    "Department":["CSE","IPE","ME","CSE","NAME","EEE","CE"],
    "CGPA":[3.06,3.25,3.50,2.78,3.79,3.35,3.95]
}
df=pd.DataFrame(student_data)
print(df)
print("Student's name with CGPA:")
print(df[["Name","CGPA"]])
df["Semester"]=["1st","2nd","3rd","5th","7th","6th","4th"]
print("Student with with CGPA and semester:")
print(df[["Name","CGPA","Semester"]])
print("Third student's information","Name:",df.loc[2,"Name"],"Semester:",df.loc[2,"Semester"],"CGPA:",df.loc[2,"CGPA"])
df["CGPA"]=df["CGPA"]+0.01
print("Student name with updated CGPA:")
print(df[["Name","CGPA"]])