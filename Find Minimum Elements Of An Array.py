ar=[]
n=int(input("Enter the size of the array:"))
print("Enter the element of the array:")
for i in range(n):
    val=int(input())
    ar.append(val)
min=float('inf')
for i in range(n):
    if(ar[i]<min):
        min=ar[i]
print("Minimum value:",min)
