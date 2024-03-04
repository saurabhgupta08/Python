# Write a python script to that ask user to enter two integer numbers return their
# product and if the product is greater than 1000, then return their sum.
a=int(input("Enter first number "))
b=int(input("Enter second number "))

product=a*b
print(a,"*",b,"=",product)

if(product>1000):
    sum=a+b
    print(a,"+",b,"=",sum)
