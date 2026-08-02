ar=[]
s=int(input("Enter the size of the array:"))
print("Enter the elements of the list:")
total=0
ac_sum=s*(s+1)/2
for i in range(s-1):
    val=int(input())
    ar.append(val)
    total=total+val
m_num=ac_sum-total
print("Missing number=",m_num)     
