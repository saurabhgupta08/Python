print("Enter the 10 number ")

even=[]
odd=[]
evenC=0
oddC=0

for i in range (10):
    a=int(input("Enter the element "))
    if(a%2==0):
        even.append(a)
        evenC=evenC+1
        
    else:
        odd.append(a)
        oddC=oddC+1


print("Even list is ",even)
print("Count of even number " ,evenC)

print("odd list is ",odd)
print("Count of odd number " ,oddC)