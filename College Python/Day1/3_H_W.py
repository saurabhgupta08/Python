days=int(input("Enter number of days "))
years=int(days/365)
month=int((days%365)/30)
day=(days%365)%30
print("Years:-",years,"month:-",month,"days:-",day)

