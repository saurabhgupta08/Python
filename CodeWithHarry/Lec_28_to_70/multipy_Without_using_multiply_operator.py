# multiplication without * operator

a=float(input("Enter first number "))
b=float(input("Enter second number "))

#first method
# print(f"The product of {a} and {b} is equal to {a/(1/b)}")

#second method
def mul(a,b):
    m=0
    for i in range(int(b)):
        m=m+a
    print(f"The product of {a} and {b} is {m}")

mul(a,b)



################################################################
# # sum without + operator
# c=float(input("Enter first number "))
# d=float(input("Enter second number "))
# print(f"The product of {c} and {d} is equal to {c-(-d)}")

