# Write a Python program to count the number of even and odd numbers from a series of numbers. 
 

n=int(input("Number of elements "))


list=[]

for i in range(n):
    x=int(input())
    list.append(x)

print(list) 

count_o=0
count_e=0
for i in list:
    if(i%2==0):
        count_e+=1
    else:
        count_o+=1

print("Number of even numbers :",count_e)
print("Number of odd numbers :",count_o)


    