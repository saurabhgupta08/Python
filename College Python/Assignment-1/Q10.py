# Given a two list of numbers create a new list such that new list should contain only
# odd numbers from the first list and even numbers from the second list.

list1=[1,2,3,5,6,8,7,9,66]
list2=[11,22,55,6,4,88,9,10]

list=[]

for i in list1:
    if(i%2!=0):
        list.append(i)
    

for i in list2:
    if(i%2==0):
        list.append(i)

print("New list --> ", list)