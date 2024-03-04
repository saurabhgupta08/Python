min11=int(input("Enter the minutes "))
hor=0
min=0
while(min11>=60):
    hor=hor+1
    min11=min11-60
    min=min11

print(hor,"Hour :",min,"Minutes")