food_cost = 79.25
tax = 6.54
tip = 12.00

total_due = food_cost + tax + tip
print(total_due)

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
# print("Tip is " + str(tip))
print("Tip is " + format(tip, ".2f"))
print("Total due is " + str(total_due))