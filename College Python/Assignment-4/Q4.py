# Write a Python program to accept a filename from the user and print the extension of that
# file.

# Prompt the user to input a filename and store it in the 'filename' variable
filename = input("Input the Filename: ")

# Split the 'filename' string into a list using the period (.) as a separator and store it in the 'f_extns' variable
f_extns = filename.split(".")

# Print the extension of the file, which is the last element in the 'f_extns' list
print("The extension of the file is : ", f_extns[-1])
