import time

time1=int(time.strftime('%H'))
print(time1)
print(type(time1))
if(time1<=12):
    print("Good Morning Sauarbh Gupta")
elif(time1<=15):
    print("Good Afternoon Saurabh Gupta")
elif(time1<=18):
    print("Good Evening Saurabh Gupta")
else:
    print("Good Night")
print(time.strftime('%H:%M:%S'))
print(time.strftime('%H'))

