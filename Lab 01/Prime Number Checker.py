def prime_find():
    num=int(input("Enter the number to check:"))
    if(num==0 or num==1):
        print(num,"is not a prime number:")
    else:
        flag=0
    for i in range(2,num):
     if(num%i==0):
        flag=1
    if(flag==1):
         print(num,"is not a prime number!")
    else:
         print(num,"is a prime number!")
prime_find()
