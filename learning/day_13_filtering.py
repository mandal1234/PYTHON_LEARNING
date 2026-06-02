print("Day 13: Filtering And List Comprehensions")
print("-----------------------------------------")

order_totals = [250, 500, 800, 1200, 300, 950]

print("All orders:", order_totals)

print()
print("Filter using a normal loop")
print("--------------------------")

high_orders = []

for total in order_totals:
    if total >= 700:
        high_orders.append(total)

print("High orders:", high_orders)

print()
print("Filter using list comprehension")
print("-------------------------------")

small_orders = [total for total in order_totals if total < 700]
print("Small orders:", small_orders)

print()
print("Filter dictionaries")
print("-------------------")

customers = [
    {"name": "Rahul", "is_active": True},
    {"name": "Priya", "is_active": False},
    {"name": "Amit", "is_active": True},
]

active_customers = [
    customer for customer in customers if customer["is_active"] is True
]

for customer in active_customers:
    print("Active customer:", customer["name"])
