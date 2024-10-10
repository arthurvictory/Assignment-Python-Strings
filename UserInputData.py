# Objective: The aim of this assignment is to process and format user input data.
# Task 1: Input Length Validator Write a script that asks for and checks the length 
# of the user's first name and last name. Both should be at least 2 characters long. 
# If not, print an error message.

def length_validator(name, name_type):
    if len(name) < 2:
        print(f"Error: {name_type} must be at least 2 characters long.")
        return False
    return True

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    if length_validator(first_name, "First name") and length_validator(last_name, "Last name"):
        print("Both names are valid.")
    else:
        print("Please enter valid names.")

main()