ar=[]
n=int(input("Enter the size of the array:"))
print("Enter the element of the array:")
for i in range(n):
    val=int(input())
    ar.append(val)
max=float('-inf')
for i in range(n):
    if(ar[i]>max):
        max=ar[i]
print("Maximum value:",max)
