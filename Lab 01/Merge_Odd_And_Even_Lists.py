l1=[1,2,4,6,3,8,9]
l2=[2,6,9,5,3,7,4]
l3=[]
for i in range(len(l1)):
 if(l1[i]%2!=0):
   l3.append(l1[i])
     
for i in range(len(l2)):
  if(l2[i]%2==0):
    l3.append(l2[i])
     
print(l3)
