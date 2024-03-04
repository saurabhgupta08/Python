# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

row=int(input("Enter the number of row "))

i=1
while(i<=row):
    j=1
    while(j<=i):
        print(i,end="")
        j+=1
    i+=1
    print("")
