print("Day 1: Python Basics")
print("--------------------")

# A variable is a name that stores a value.
customer_name = "Amit"
city = "Pune"
meal_plan = "Monthly Veg Plan"

print("Customer name:", customer_name)
print("City:", city)
print("Meal plan:", meal_plan)

print()
print("Numbers and calculations")
print("------------------------")

meals_per_day = 2
number_of_days = 30
price_per_meal = 80

total_meals = meals_per_day * number_of_days
total_price = total_meals * price_per_meal

print("Meals per day:", meals_per_day)
print("Number of days:", number_of_days)
print("Price per meal:", price_per_meal)
print("Total meals:", total_meals)
print("Total price:", total_price)

print()
print("True / False values")
print("-------------------")

is_active_subscription = True
has_discount = False

print("Active subscription:", is_active_subscription)
print("Has discount:", has_discount)

print()
print("Small decision")
print("--------------")

if total_price >= 4000:
    print("This is a high value monthly order.")
else:
    print("This is a small order.")

print()
print("Your experiment")
print("---------------")
print("Change customer_name, city, meals_per_day, and price_per_meal.")
print("Then run this file again and see what changes.")
