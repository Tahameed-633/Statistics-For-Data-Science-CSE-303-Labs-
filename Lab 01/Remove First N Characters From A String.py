str1=input("Enter the string:")
n=int(input("Enter the value of n:"))
l=0
for ch in str1:
    l=l+1
if(n>l or n<=0):
    print("Invalid input!")
else:
    str2=""
    for i in range(n,l):
        str2=str2+str1[i]
print(str2)
