import csv

with open("CSVpre.csv","w") as f:
    file=csv.writer(f)
    for i in range(3):
        name=input("Enter the name ")
        mark=input("Enter the marks ")
        file.writerow([name,mark])


read=csv.DictReader(open("CSVpre.csv",))
for i in read:
    print(i)


