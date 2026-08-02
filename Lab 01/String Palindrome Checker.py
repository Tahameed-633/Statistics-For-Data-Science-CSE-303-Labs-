str1=input("Enter the string to check:")
l=0
for c in str1:
    l=l+1
str2=""
for i in range(l-1,-1,-1):
    str2=str2+str1[i]
if(str1==str2):
    print(str1,"is a palindrome!")
else:
    print(str1,"is not a palindrome!")
