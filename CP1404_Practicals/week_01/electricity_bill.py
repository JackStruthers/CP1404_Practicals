TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
print("Electricity bill Estimator 2.0")

tariff_choice = int(input("Please select either tariff 11 or 31"))
while tariff_choice != 11 and tariff_choice != 31:
    tariff_choice = int(input("Please select either tariff 11 or 31"))

daily_usage = float(input("Enter daily use in kWh"))
billing_period = int(input("Enter the number of billing days"))

if tariff_choice == 11:
    estimated_bill = TARIFF_11 * daily_usage * billing_period
else:
    estimated_bill = TARIFF_31 * daily_usage * billing_period

print("Estimated bill ${:.2f}".format(estimated_bill))
