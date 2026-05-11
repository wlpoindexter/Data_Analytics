favorites = ["tacos", "ramen", "jerk chicken", "injera", "pierogi"]

for index, item in enumerate(favorites, start=1):
    if index == 1:
        print(f"{index}. {item} <- top pick!")
    else:
        print(f"{index}. {item}")

# BONUS: reverse order, still numbered 1–5
print("\nReversed:")
for index, item in enumerate(reversed(favorites), start=1):
    print(f"{index}. {item}")