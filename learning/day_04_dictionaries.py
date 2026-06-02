print("Day 4: Dictionaries")
print("-------------------")

customer = {
    "name": "Rahul",
    "city": "Pune",
    "is_active": True,
}

print("Customer name:", customer["name"])
print("Customer city:", customer["city"])
print("Active customer:", customer["is_active"])

print()
print("Update dictionary values")
print("------------------------")

customer["city"] = "Mumbai"
customer["phone"] = "9876543210"

print(customer)

print()
print("Menu item dictionary")
print("--------------------")

menu_item = {
    "name": "Veg Thali",
    "price": 120,
    "is_available": True,
}

print("Food:", menu_item["name"])
print("Price:", menu_item["price"])

print()
print("List of order dictionaries")
print("--------------------------")

orders = [
    {"customer": "Rahul", "total": 480},
    {"customer": "Priya", "total": 850},
    {"customer": "Amit", "total": 300},
]

grand_total = 0

for order in orders:
    print(order["customer"], "ordered for", order["total"])
    grand_total = grand_total + order["total"]

print("Grand total:", grand_total)

print()
print("High value orders")
print("-----------------")

for order in orders:
    if order["total"] >= 700:
        print(order["customer"], "is a high value customer")
