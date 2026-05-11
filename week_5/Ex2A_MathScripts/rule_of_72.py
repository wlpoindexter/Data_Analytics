current_savings = 5000.00
interest_rate = 0.06

years_to_double = 72 / (interest_rate * 100)
doubled_balance = current_savings * 2

print("Your current savings is " + format(current_savings, ".2f") + ".")
print(f"At a {format(interest_rate, '.0%')} interest rate, your savings account will be "
      f"worth {format(doubled_balance, '.2f')} in {format(years_to_double, '.1f')} years")

bill_amount    = input("What was your restaurant bill total? $")
tip_percentage = input("How much do you want to tip? (e.g. 0.20 for 20%): ")

# Pitfall: input() always returns a string. Must convert to float before math.
# If user types something non-numeric, float() will crash with a ValueError.

bill_amount    = float(bill_amount)
tip_percentage = float(tip_percentage)

tip_amount = bill_amount * tip_percentage

print(f"The tip on a ${format(bill_amount, '.2f')} restaurant bill is ${format(tip_amount, '.2f')}")