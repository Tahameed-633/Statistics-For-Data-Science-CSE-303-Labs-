ar=[]
n=int(input("Enter the size of the array:"))
print("Enter the element of the array:")
for i in range(n):
    val=int(input())
    ar.append(val)
cnt=0
for i in range(n):
    if(ar[i]>10):
        cnt=cnt+1
print("Number of elements greater than 10=",cnt)
