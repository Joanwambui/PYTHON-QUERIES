import sys

n = int(input())  # Read n (though it is not used)
s = 0  # Initialize sum of even numbers

for i in input().split():  # Read numbers
    x = int(i)  # Convert to integer
    if x % 2 == 0:  # Check if even
        s += x  # Add to sum

print(s)  # Print the final sum
