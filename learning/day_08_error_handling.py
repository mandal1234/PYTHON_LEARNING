print("Day 8: Error Handling")
print("---------------------")

sample_values = ["10", "abc", "25", "", "5"]

valid_numbers = []

for value in sample_values:
    try:
        number = int(value)
        valid_numbers.append(number)
        print(value, "converted to", number)
    except ValueError:
        print(value, "is not a valid number")

print()
print("Valid numbers:", valid_numbers)

total = 0

for number in valid_numbers:
    total = total + number

print("Total:", total)

print()
print("Safe division")
print("-------------")

orders = 0
revenue = 5000

try:
    average = revenue / orders
    print("Average order value:", average)
except ZeroDivisionError:
    print("Cannot calculate average because orders are zero")
