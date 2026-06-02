print("Day 14: Mini Command Line App")
print("-----------------------------")

orders = []


def add_order(customer_name, total):
    order = {"customer": customer_name, "total": total}
    orders.append(order)


def show_orders():
    if len(orders) == 0:
        print("No orders yet.")
        return

    for order in orders:
        print(order["customer"], "-", order["total"])


def calculate_revenue():
    revenue = 0

    for order in orders:
        revenue = revenue + order["total"]

    return revenue


add_order("Rahul", 500)
add_order("Priya", 850)
add_order("Amit", 300)

print("Orders:")
show_orders()

print()
print("Total revenue:", calculate_revenue())

print()
print("High value orders:")

for order in orders:
    if order["total"] >= 700:
        print(order["customer"], "-", order["total"])
