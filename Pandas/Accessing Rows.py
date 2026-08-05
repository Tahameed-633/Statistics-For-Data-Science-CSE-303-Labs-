import pandas as pd
student_data={
    "Name":["Shafin","Fatin","Farhan","Fariha","Irin","Jowa","Arif"],
    "Department":["CSE","IPE","ME","CSE","NAME","EEE","CE"],
    "CGPA":[3.06,3.25,3.50,2.78,3.79,3.35,3.95]
}
df=pd.DataFrame(student_data)
print(df[["Name","Department"]])
print(df[["Name","CGPA"]])
print("First Row:")
print(df.iloc[0])
print("Fourth Row:")
print(df.iloc[3])
print("6th Row:")
print(df.iloc[5])
print("Second to fifth row:")
print(df.iloc[1:4])
print("First to third row:")
print(df.iloc[0:3])
print("Fourth to sixth row:")
print(df.iloc[3:6])
print("Fourth to seventh row:")
print(df.iloc[4:7])
