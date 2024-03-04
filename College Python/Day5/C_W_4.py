n=int(input("Enter number "))
rev_n=0
while(n!=0):
    digit=n%10
    rev_n = rev_n * 10 +digit
    n=n//10

print(rev_n)

    