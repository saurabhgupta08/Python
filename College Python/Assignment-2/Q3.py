# Given 2 strings, s1, and s2 return a new string made of the first, middle and
# last char each input string

def mixstring(s1,s2):
    l1=len(s1)//2
    l2=len(s2)//2
    str=s1[0]+s2[0]+s1[l1]+s2[l2]+s1[-1]+s2[-1]
    return str


str1="America"
str2="Japan"
print(mixstring(str1,str2))