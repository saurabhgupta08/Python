# Write a python script that display only those characters which are present at odd and
# even number index separately.
str=input("Enter your Word ")

l=len(str)

print("Characters at odd index")
for i in range(0,l,2):
    print(str[i],end="")
    
print("")

print("Characters at even index")
for i in range(1,l,2):
    print(str[i],end="")

print("")
