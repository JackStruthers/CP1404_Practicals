"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = int(input("Please enter the amount you sold, use a negative to leave the programme: "))
bonus = int

while sales >= 0:
    if 1000 > sales >= 0:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print("Your bonus is: ${:.2f}".format(bonus))
    sales = int(input("Please enter the amount you sold: "))

print("Thanks for using")
