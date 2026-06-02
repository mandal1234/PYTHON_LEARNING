print("Day 3: Lists And Loops")
print("----------------------")

# A list stores many values in one variable.
menu_items = ["Dal Rice", "Paneer Rice", "Veg Thali"]

print("Menu items:")
print(menu_items)

print()
print("Read items by index")
print("-------------------")

# Python list indexes start from 0.
print("First item:", menu_items[0])
print("Second item:", menu_items[1])
print("Third item:", menu_items[2])

print()
print("Add a new item")
print("--------------")

menu_items.append("Curd Rice")
print("Updated menu:", menu_items)
print("Total menu items:", len(menu_items))

print()
print("Print menu using a loop")
print("-----------------------")

for item in menu_items:
    print("Food item:", item)

print()
print("Order totals")
print("------------")

order_totals = [250, 500, 800, 1200]

grand_total = 0

for total in order_totals:
    grand_total = grand_total + total
    print("Added order:", total)

print("Grand total:", grand_total)

print()
print("Find high value orders")
print("----------------------")

for total in order_totals:
    if total >= 700:
        print(total, "is a high value order")
    else:
        print(total, "is a regular order")

print()
print("Your experiment")
print("---------------")
print("Change menu_items and order_totals, then run this file again.")
