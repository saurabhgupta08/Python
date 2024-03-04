# Given a string, return the sum and average of the digits that appear in the
# string, ignoring all other characters

def sum_ave_str(str):
    sum=0
    count=0
    for i in str:
        if(i.isdigit()):
            sum+=int(i)
            count+=1
    print("Sum = ",sum)
    print("Average = ",float(sum/count))

str="kd5cd5dcdc5cd5"
sum_ave_str(str)