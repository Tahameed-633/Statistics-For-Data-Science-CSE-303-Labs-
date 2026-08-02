ar=[]
n=int(input("Enter the size of the array:"))
print("Enter the element of the array:")
for i in range(n):
    val=int(input())
    ar.append(val)
visited=[False]*n
for i in range(n):
    if(visited[i]):
        continue
    cnt=1
    for j in range(i+1,n):
        if(ar[i]==ar[j]):
            cnt=cnt+1
            visited[j]=True
    print("Frequency of ",ar[i],"=",cnt)
