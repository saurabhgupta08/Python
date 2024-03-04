# Reverse a given number and return true if it is the same as the original number

num=input("Enter the number ")

rev=num[::-1]

if(num==rev):
    print("True")
else:
    print("False")