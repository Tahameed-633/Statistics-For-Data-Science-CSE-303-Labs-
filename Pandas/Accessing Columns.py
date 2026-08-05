import pandas as pd
data={
    "Name":["Safin","Fatin","Irin","Tasnim"],
    "Department":["CSE","ME","EEE","NAME"],
    "CGPA":[3.06,3.24,3.50,3.35]

}
df=pd.DataFrame(data)

print(df["Name"])
print(df[["Name","Department"]])
print(df[["Name","CGPA"]])