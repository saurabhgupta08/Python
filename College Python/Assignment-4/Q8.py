# Write a Python program to calculate number of days between two dates. Ask the user to enter
# the first and last date.


# Import the 'date' class from the 'datetime' module
from datetime import date

# Define a start date as July 2, 2014
f_date = date(2014, 7, 2)

# Define an end date as July 11, 2014
l_date = date(2014, 7, 11)

# Calculate the difference between the end date and start date
delta = l_date - f_date

# Print the number of days in the time difference
print(delta.days)
