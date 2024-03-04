# Given a string of odd length greater 7, return a string made of the middle three
# chars of a given String

def getMiddleThreeChars(str):
    l=len(str)//2
    return str[l-1:l+2]
    

str=input("Enter your word ")
print("Middle three chars -->" ,getMiddleThreeChars(str))



