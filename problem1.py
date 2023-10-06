#! python3
 
"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue

Enter a number: 36
36 is frue

Enter a number: 16
16 is not frue
"""

answer = int(input("enter a number: "))
if answer % 6 == 0:
    if answer % 8 >= 1:
        print(f"{answer} is frue")
    else:
        print(f"{answer} is not frue")