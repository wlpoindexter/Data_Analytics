def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(f"{city}, {state} {zip}")

def add_numbers(*numbers):
    total = sum(numbers)
    equation = " + ".join(str(num) for num in numbers)
    print(f"{equation} = {total}")

def display_receipt(total_due, amount_paid):
    change = amount_paid - total_due

    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")

    if change >= 0:
        print(f"Change Due: ${change:.2f}")
    else:
        print(f"Remaining Balance: ${abs(change):.2f}")

    print()

display_mailing_label(
    "Will Poindexter",
    "123 Main St",
    "Chicago",
    "IL",
    "60601")

print()

display_mailing_label(
    "John Smith",
    "456 Oak Ave",
    "Naperville",
    "IL",
    "60540")

print()

add_numbers(5)
add_numbers(5, 10)
add_numbers(5, 10, 15, 20)

print()

display_receipt(50, 60)
display_receipt(50, 50)
display_receipt(50, 40)