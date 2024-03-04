# from functools import reduce

# cub= lambda n : n*n*n

# def is_even(n):
#     if(n%2==0):
#         return True
#     else:
#         return False
    
# list1=[1,2,3,4,5,6,7,8,9]

# sqr=list(map(lambda a:a*a,list1))
# print(sqr)

# max=reduce(lambda a,b:a if a>b else b,list1)
# print(max)


####################

# from datetime impor

# from datetime import datetime

# today=datetime.now()

# print(today.hour)
# print(today.month)


# f=open('myfile1.txt','r')
# print(f.read())
# f.close()

# g=open('myfile1.txt','r')
# print(g.read())
# g.close()

# f=open('myfile2.txt','a')
# f.write("Yooo Yoooo\n")
# f.close()

f1=open("myfile1.txt","r")
f2=open("myfile2.txt","w")

for i in f1:
    print(i)
    f2.write(i)

f1.close()
f2.close()
