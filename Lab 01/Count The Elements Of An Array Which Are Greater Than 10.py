ar=[]
n=int(input("Enter the size of the array:"))
print("Enter the element of the array:")

for i in range(n):
    val=int(input())
    ar.append(val)
flag=1
for i in range(n-1):
    if(ar[i]>=ar[i+1]):
        flag=0
if(flag==0):
    print("The array is not in increasing order.")
else:
    print("The array is  in increasing order.")
