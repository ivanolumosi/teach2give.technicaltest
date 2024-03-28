'''Question 3:
#program that takes an integer as input and returns true if the input is a power of two.Examples:8=> returns true 6=> returns false  

'''

# Get the integer from the user
number = int(input("Enter an integer: "))

# Check if the number is a power of two
if (number != 0) and (number & (number - 1)) == 0:
    print(f"{number} True")
else:
    print(f"{number} False")
