from pathlib import Path

print("Day 15: Python Review Project")
print("-----------------------------")


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total(self):
        amount = 0

        for item in self.items:
            amount = amount + item.price

        return amount

    def is_high_value(self):
        return self.total() >= 700


def print_order(order):
    print("Customer:", order.customer_name)

    for item in order.items:
        print("-", item.name, item.price)

    print("Total:", order.total())
    print("High value:", order.is_high_value())


def save_report(orders):
    report_path = Path(__file__).with_name("day_15_orders_report.txt")

    with open(report_path, "w", encoding="utf-8") as file:
        file.write("Day 15 Tiffin Orders Report\n")
        file.write("---------------------------\n")

        for order in orders:
            file.write(f"{order.customer_name} - Rs {order.total()}\n")

    return report_path


dal_rice = MenuItem("Dal Rice", 80)
veg_thali = MenuItem("Veg Thali", 120)
paneer_thali = MenuItem("Paneer Thali", 180)

rahul_order = Order("Rahul")
rahul_order.add_item(dal_rice)
rahul_order.add_item(veg_thali)

priya_order = Order("Priya")
priya_order.add_item(paneer_thali)
priya_order.add_item(paneer_thali)
priya_order.add_item(paneer_thali)
priya_order.add_item(veg_thali)
priya_order.add_item(veg_thali)

orders = [rahul_order, priya_order]

for order in orders:
    print_order(order)
    print()

high_value_orders = [order for order in orders if order.is_high_value()]

print("High value order count:", len(high_value_orders))

report_path = save_report(orders)
print("Report saved:", report_path)
