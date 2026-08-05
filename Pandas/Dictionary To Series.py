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