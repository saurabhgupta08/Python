# Write a code to remove b element from list
a=[33,22,55,44,22,99,22,88,77,44,22]
b=22
print("My list :",a)
cnt=a.count(b)
print(cnt)
for i in range(cnt):
    a.remove(b)

print("New list after removing :",a)