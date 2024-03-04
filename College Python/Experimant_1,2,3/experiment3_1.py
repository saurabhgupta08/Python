n=int(input("Enter number of row "))

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()


for k in range(n+1):
    for l in range(n-k+1):
        print("*",end=" ")
    print()