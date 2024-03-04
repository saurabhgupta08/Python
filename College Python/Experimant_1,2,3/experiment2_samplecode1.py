n= int(input("Enter number of elemnets of first list "))
list1 = []

for i in range(n):
    a=int(input("Enter your number "))
    list1.append(a)

n= int(input("Enter number of elemnets of first list "))
list2 = []

for j in range(n):
    a=int(input("Enter your number "))
    list2.append(a)

g=len(list1)
h=len(list2)
for k in range(g):
    for l in range(h):
        if(list1[k]==list2[l]):
            print("the common element is ",list1[k])
            break
        

        
