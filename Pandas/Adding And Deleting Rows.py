import pandas as pd
student_data={
    "Name":["Shafin","Fatin","Farhan","Fariha","Irin","Jowa","Arif"],
    "Department":["CSE","IPE","ME","CSE","NAME","EEE","CE"],
    "CGPA":[3.06,3.25,3.50,2.78,3.79,3.35,3.95]
}
df=pd.DataFrame(student_data)
print("Student's Information:")
print(df)
new_row1={
    "Name":"Tahameed",
    "Department":"CSE",
    "CGPA":3.06
}
df.loc[len(df)]=new_row1
print("After adding new row:")
print(df.iloc[4:8])
df["Age"]=[21,20,22,23,20,24,21,19]
print("After Adding a new column:")
print(df)
new_row_2={
    "Name":"Rehnuma",
    "Department":"EEE",
    "CGPA":3.00,
    "Age":22
}
df.loc[len(df)]=new_row_2
print("After adding a new column and a new row:")
print(df)
print("Students with CGPA above 3.50:")
print(df[df["CGPA"]>3.50])
print("Students below age 20 and CGPA greater than or above 3.00:")
print(df[(df["Age"]<20) & (df["CGPA"]>=3.00)])
print("After deleting the 4th row:")
df=df.drop(3)
print(df)