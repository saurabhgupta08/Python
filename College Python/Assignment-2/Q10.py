# Given an input string, count occurrences of all characters within a string

str1 = "Saurabh Gupta"

# create a result dictionary
char_dict = dict()

for char in str1:
    count = str1.count(char)
    # add / update the count of a character
    char_dict[char] = count
print('Result:', char_dict)