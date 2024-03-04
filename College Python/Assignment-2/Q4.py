# arrange String characters such that lowercase letters should come first
# Given input String of combination of the lower and upper case arrange characters in such
# a way that all lowercase letters should come first.

def sepLowUpp(str):
    lower=""
    upper=""
    for i in str:
        if(i.islower()):
            lower=lower+i
        if(i.isupper()):
            upper=upper+i
    return lower+upper


str="QWryuIOLKjh"
print(sepLowUpp(str))