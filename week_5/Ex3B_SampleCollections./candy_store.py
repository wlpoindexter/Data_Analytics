candies = ("Skittles", "Starburst", "Jolly Ranchers")
flavors = ("mango-chili", "lychee", "blueberry lavender", "watermelon")

candy_combos = set()
candy_combos.add(candies[0] + " - " + flavors[0])
candy_combos.add(candies[0] + " - " + flavors[2])
candy_combos.add(candies[1] + " - " + flavors[1])
candy_combos.add(candies[1] + " - " + flavors[3])
candy_combos.add(candies[2] + " - " + flavors[0])
candy_combos.add(candies[2] + " - " + flavors[2])

print("Today's candy options include:")
print(candy_combos)
print("Today's candy options include:")
print(candy_combos)
print("Today's candy options include:")
print(candy_combos)

# The order may appear different each run because sets are unordered. Python makes no guarantee about the print order of set items.