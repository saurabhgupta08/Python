import math
n=int(input("Enter number "))
h=n
ans=0
while(n!=0):
    x=pow((n%10),3)
    ans=ans+x
    n=n//10
print(ans)

if(h==ans):
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")    