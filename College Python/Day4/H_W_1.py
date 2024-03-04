# Find list of intersection of a and b list
a=[23,45,55,66,10,30]
b=[44,45,66,55,3,4]

ans1=[]

x=len(a)
y=len(b)

for i in range(x):
    for j in range(y):
        if(a[i]==b[j]):
            ans1.append(a[i])
            break
        else:
            continue

print("ans1 = ",ans1)

##############################################
ans_a=a

z=len(ans1)
for k in range(z):
    ans_a.remove(ans1[k])

print("ans_a = ",ans_a)
##############################################
ans_b=b

w=len(ans1)
for h in range(w):
    ans_b.remove(ans1[h])

print("ans_b = ", ans_b)

##############################################
ans3=ans1 + ans_a + ans_b
print("ans3 = ",ans3)
