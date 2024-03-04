# Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of
# s1.

def appendMiddle(s1,s2):
    l=len(s1)//2
    nstr = s1[:l] + s2 + s1[l:]
    return nstr


str1="Saurab"
str2="YYYYYYY"
print(appendMiddle(str1,str2))