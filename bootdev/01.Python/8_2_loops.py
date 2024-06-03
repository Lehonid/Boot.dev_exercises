"""
As a reminder, a "for loop" in Python is written like this:

for i in range(0, 10):
    print(i)

In English, the code says:

Start with i equals 0. (i in range(0)
If i is greater than or equal to 10 (range(0, 10)), exit the loop.
Print i to the console. (print(i))
Add 1 to i. (range defaults to incrementing by 1)
Go back to step 2
The result is that the numbers 0-9 are logged to the console in order.
"""

for i in range(0, 10):
    print(i)


# 8_8
def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total

# somme des nombres impairs
def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
    return total

