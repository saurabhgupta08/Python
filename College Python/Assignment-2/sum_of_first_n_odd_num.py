n=int(input("Enter the n term "))
sum=0
count=1
i=1

while(count<=n):
    if(i%2!=0):
        sum=sum+i
        count=count+1
    i=i+1

print("Sum of first n odd number is ",sum)
        