n1=int(input("Number of ele "))
list1=[]
for i in range (n1):
    x=int(input("Enter element"))
    list1.append(x)

n2=int(input("Number of ele "))
list2=[]
for j in range (n2):
    x=int(input("Enter element"))
    list2.append(x)

ans1=[]

for i in list1:
    for j in list2:
        if(i==j):
            ans1.append(i)
            break
        else:
            continue

print(ans1)