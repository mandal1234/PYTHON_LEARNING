from tiffin_utils import calculate_delivery_fee, calculate_total, format_money

print("Day 10: Modules And Imports")
print("---------------------------")

price_per_meal = 80
number_of_meals = 10

order_total = calculate_total(price_per_meal, number_of_meals)
delivery_fee = calculate_delivery_fee(order_total)
final_total = order_total + delivery_fee

print("Order total:", format_money(order_total))
print("Delivery fee:", format_money(delivery_fee))
print("Final total:", format_money(final_total))

print()
print("Why this matters")
print("----------------")
print("The calculation functions live in tiffin_utils.py.")
print("This file imports and uses them.")
