# Write a Python program to convert temperatures to and from celsius, fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]


Tem=input("Enter your Temperature ")
a=Tem[-1]
# print(a)
value=float(Tem[:-1])
# print(value)
if(a.lower()=='f'):
    print("Temperature from farenheit to celcius=",(value-32)/1.8)
elif(a.lower()=='c'):
    print("Temperature from celcius to farenheit=",(value*1.8)+32)
else:
    print("Try again ")


