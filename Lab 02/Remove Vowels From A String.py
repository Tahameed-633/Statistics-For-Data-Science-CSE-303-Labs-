str=input("Enter the string:")
s=[ch for ch in str if ch.lower() not in "aeiou"]
result="".join(s)
print(result)