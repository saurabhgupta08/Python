# . Write a Python program that accepts a string and calculate the number of digits and letters. 

str=input("Enter string ")

count_l=0
count_d=0
for i in str:
    if i.isalpha():
        count_l+=1
    elif i.isdigit():
        count_d+=1

print("Digits : ",count_d," letters :",count_l)