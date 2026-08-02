ar=[]
n=int(input("Enter trhe size of the array:"))
print("Enter the element of the array:")
for i in range(n):
    val=int(input())
    ar.append(val)
f_max=float('-inf')
for i in range(n):
    if(ar[i]>f_max):
        f_max=ar[i]
print("First maximum=",f_max)
s_max=float('-inf')
for i in range(n):
    if(ar[i]!=f_max and ar[i]>s_max):
        s_max=ar[i]
print("Second maximum=",s_max)
if(s_max==float('-inf')):
    print("No second maximum value.")
