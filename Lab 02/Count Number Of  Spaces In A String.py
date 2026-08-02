str=input("Enter the string:");
spaces=[len(ch) for ch in str if ch==" "]
print("Number Of Spaces:")
count=sum([1 for ch in str if ch==" "])
print(count)