from functools import reduce

sum=lambda a,b:a+b
l=[1,2,3,4,5,6,7,8,9]

newl=reduce(sum,l)
print(newl)