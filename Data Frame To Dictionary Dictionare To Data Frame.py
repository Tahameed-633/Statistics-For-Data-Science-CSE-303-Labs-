import pandas as pd
student_data={
    "Name":["Shafin","Fatin","Farhan","Fariha","Irin","Jowa","Arif"],
    "Department":["CSE","IPE","ME","CSE","NAME","EEE","CE"],
    "CGPA":[3.06,3.25,3.50,2.78,3.79,3.65,3.95],
    "Credit":[10.5,60,35,25,30,98,27]
}
df=pd.DataFrame(student_data)
print("Data Frame:")
print(df)
dic=df.to_dict("records")
print("Data Frame To Dictionary:")
print(dic)
new_df=pd.DataFrame(dic)
print("Dictionary To Data Frame:")
print(new_df)