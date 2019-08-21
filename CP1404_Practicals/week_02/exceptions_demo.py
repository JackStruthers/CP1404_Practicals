"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? when you put a letter in
2. When will a ZeroDivisionError occur? when the denominator = 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError? while loop for denominator
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("You cannot use 0 as a denominator")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
