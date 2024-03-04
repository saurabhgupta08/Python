# Write a python script that ask for entering a string and an integer number n, remove
# characters from a string starting from zero up to n and return a new string. Modify the same
# script to remove the n number of character from the end of the string.

str=input("Enter string ")
num=int(input("Enter the number "))

str_front=str[num:]
str_end=str[:-num]

print("String after remove char from front ",str_front)
print("String after remove char from end ",str_end)