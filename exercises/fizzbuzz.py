"""Print out 100 numbers, from 1 to 100 (both inclusive). But:
Instead of printing multiples of 3, print "Fizz"
Instead of printing multiples of 5, print "Buzz"
Instead of printing multiples of both 3 and 5, print "FizzBuzz".
"""
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)
