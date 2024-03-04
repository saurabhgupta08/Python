# Write a Python program to test whether a passed letter is a vowel or not

vowels="aeiouAEIOU"
letter=input("Enter the letter: ")
if letter[0] in vowels:
    print("Vowels entered")
else:
    print("Not a vowels")