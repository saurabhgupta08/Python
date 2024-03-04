# Write a Python program to calculate the sum of three given numbers, if the values are equal
# then return three times of their sum.
n1=int(input("Enter n1 "))
n2=int(input("Enter n2 "))
n3=int(input("Enter n3 "))



sum=n1+n2+n3
if(n1==n2==n3):
    print(sum*3)
else:
    print(sum)