"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():

    score = float(input("Enter score: "))
    grade = determine_grade(score)
    print(grade)


def determine_grade(score):

    if score <= 0 or score >= 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
