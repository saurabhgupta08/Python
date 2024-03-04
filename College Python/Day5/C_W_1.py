# Write a code to seprate odd and even number

size=int(input("Enter the size of list "))
list=[]
print("Enter elements")
for i in range(size):
    list.append(input())

odd=[]
even=[]


for j in range(size):
    if(int(list[j])%2==0):
        even.append(int(list[j]))
    else:
        odd.append(int(list[j]))


print("Even list ", even)
print("Odd  list ",odd)