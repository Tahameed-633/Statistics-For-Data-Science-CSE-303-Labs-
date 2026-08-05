import pandas as pd
student_data={
    "Name":["Shafin","Fatin","Farhan","Fariha","Irin","Jowa","Arif"],
    "Department":["CSE","IPE","ME","CSE","NAME","EEE","CE"],
    "CGPA":[3.06,3.25,3.50,2.78,3.79,3.65,3.95],
    "Credit":[10.5,60,35,25,30,98,27]
}
df=pd.DataFrame(student_data)
df.to_csv("student_data.csv",index=False)
print("CSV file created successfully!")
df=pd.read_csv("student_data.csv")
print(df)
df=pd.read_csv("student_data.csv")
print("Student with CGPA above 3.50 and credits above 90:")
print(df[(df["CGPA"]>=3.50) & (df["Credit"]>=90)])
df["Age"]=[19,21,23,20,24,23,22]
df.to_csv("student_data.csv",index=False)
df=pd.read_csv("student_data.csv")
print(df)
new_row={
    "Name":"Easha",
    "Department":"EEE",
    "CGPA":3.55,
    "Credit":100,
    "Age":21
}
df.loc[len(df)]=new_row
df.to_csv("student_data.csv",index=False)
df=pd.read_csv("student_data.csv")
print("Student with CGPA above 3.50,credits above 90 and age above 20:")
print(df[(df["CGPA"]>3.50) & (df["Credit"]>95) &(df["Age"]>20)])