#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
You can use an if statement to determine which is larger, or use the
max() function to determine the larger of the two
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
import math

number1 = int(input("enter a number: "))
number2 = int(input("enter a second number: "))
if number1 >= number2 and number1 % number2 == 0:
    print(f"{number2} is a factor of {number1}")
elif number1 >= number2 and number1 % number2 >= 1:
    print(f"{number2} is not a factor if {number1}")
    
if number2 >= number1 and number2 % number1 == 0:
    print(f"{number1} is a factor of {number2}")
elif number2 >= number1 and number2 % number1 >= 1:
    print(f"{number2} is not a factor if {number1}")