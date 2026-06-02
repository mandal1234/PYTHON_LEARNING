print("Day 6: While Loops")
print("------------------")

print("Counter example")
print("---------------")

count = 1

while count <= 5:
    print("Count:", count)
    count = count + 1

print()
print("Process pending deliveries")
print("--------------------------")

pending_deliveries = 3

while pending_deliveries > 0:
    print("Delivery completed. Remaining:", pending_deliveries - 1)
    pending_deliveries = pending_deliveries - 1

print("All deliveries completed")

print()
print("Input validation idea")
print("---------------------")

sample_quantities = ["abc", "-2", "3"]
valid_quantity = None

for value in sample_quantities:
    print("Trying value:", value)

    try:
        quantity = int(value)

        if quantity > 0:
            valid_quantity = quantity
            print("Valid quantity found:", valid_quantity)
            break

        print("Quantity must be greater than 0")
    except ValueError:
        print("This is not a valid number")

print("Final valid quantity:", valid_quantity)
