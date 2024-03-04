# Write a python script to enter a number, Iterate from start number to the end number
# and print the sum of the current number and previous number. 
num=int(input("Enter a number"))

i=1
while(i<=num):
    print(i+(i-1))
    i=i+1
