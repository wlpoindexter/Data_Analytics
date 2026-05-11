import math

num_tourists = 38
seats_per_van = 15
cost_per_van = 250.00

vans_needed = math.ceil(num_tourists / seats_per_van)
total_cost = vans_needed * cost_per_van
cost_per_person = total_cost / num_tourists

print(f"Tourists: {num_tourists}")
print(f"Vans needed: {vans_needed}")
print(f"Total van rental cost: ${format(total_cost, '.2f')}")
print(f"Cost per person: ${format(cost_per_person, '.2f')}")

# a) Cost per person = $750 / 38 = ~$19.74
# b) 38 × $19.74 = $750.12 collected
# c) Vans cost $750.00
# d) Leftover ~$0.12 because cost per person rounds up slightly, so multiplying across all 38 people over collects by a few cents.