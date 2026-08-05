import pandas as pd
student_data={
    "Math": 90,
    "Physics":88,
    "Chemistry":92
}
print("Dictionary:")
print(student_data)
data=pd.Series(student_data)
print("Pandas series:")
print(data)
print("Number of subjects:",data.count())
print("Average Number:",data.mean())
print("Highest Number:",data.max())
print("Lowest Number:",data.min())
print("Update number got in Physics:")
data["Physics"]=95
student_data["Physics"]=95
print("Dictionary:")
for key in student_data:
    print(key,student_data[key])
print("Pandas Series:")
print(data)
print("Index:")
print(data.index)