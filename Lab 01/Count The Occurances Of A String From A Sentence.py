str1=input("Enter a string:")
l=0
for c in str1:
    l=l+1
cnt=0
for i in range(l-5):
    if(str1[i]=='C' and str1[i+1]=='S' and str1[i+2]=='E' and str1[i+3]=='3' and str1[i+4]=='0' and str1[i+5]=='3'):
        cnt=cnt+1
print("CSE303 appears",cnt,"times in the string!")
