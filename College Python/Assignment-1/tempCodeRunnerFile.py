lst=[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

for i in range(1,6):
    for j in range(i):
        print(lst[i+j],end=" ")
    print("")
