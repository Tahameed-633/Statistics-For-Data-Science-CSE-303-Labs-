ar=[]
n=int(input("Enter the size of the array:"))
print("Enter the elements of the array:")
for i in range(n):
    val=int(input())
    ar.append(val)
f_min=float('inf')
for i in range(n):
    if(ar[i]<f_min):
        f_min=ar[i]
print("First minimum value:=",f_min)
s_min=float('inf')
for i in range(n):
  if(ar[i]!=f_min and ar[i]<s_min):
      s_min=ar[i]
print("Second minimum value:=",s_min)
if(s_min==float('inf')):
    print("No second minimum.")
