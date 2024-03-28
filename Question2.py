'''Question 2:
program to generate the Fibonacci sequence up to 100.
'''

# Initialize the first two numbers of the sequence
x, y = 0, 1

# generating the numbers while the last number generated is less than or equal to 100
while y <= 100:
    # Print the current number
    print(y)
    
    # Update x and y to generate the next Fibonacci number
    x, y = y, x + y
