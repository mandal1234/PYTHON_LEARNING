print("Day 2: User Input and Decisions")
print("---------------------------------")

# input() lets the user type a value in the terminal.
customer_name = input("Customer name: ")

# input() always returns text, so convert number inputs before doing math.
meals_per_day = int(input("Meals per day: "))
days = int(input("Number of days: "))
price_per_meal = int(input("Price per meal: "))

subtotal = meals_per_day * days * price_per_meal

print()
print("Order summary")
print("-------------")
print("Customer:", customer_name)
print("Meals per day:", meals_per_day)
print("Days:", days)
print("Price per meal:", price_per_meal)
print("Subtotal:", subtotal)

# A program can make decisions using if, elif, and else.
if days >= 30:
    discount_percent = 10
elif days >= 7:
    discount_percent = 5
else:
    discount_percent = 0

discount_amount = subtotal * discount_percent / 100
final_total = subtotal - discount_amount

print("Discount percent:", discount_percent)
print("Discount amount:", discount_amount)
print("Final total:", final_total)

print()
print("Business decision")
print("-----------------")

if final_total >= 5000:
    print("This is a high value customer.")
elif final_total >= 2000:
    print("This is a regular monthly customer.")
else:
    print("This is a small order.")
