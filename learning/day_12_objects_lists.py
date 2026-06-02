print("Day 12: Classes With Lists Of Objects")
print("-------------------------------------")


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)

    def calculate_total(self):
        total = 0

        for item in self.items:
            total = total + item.price

        return total

    def print_summary(self):
        print("Customer:", self.customer_name)
        print("Items:")

        for item in self.items:
            print("-", item.name, item.price)

        print("Total:", self.calculate_total())


dal_rice = MenuItem("Dal Rice", 80)
veg_thali = MenuItem("Veg Thali", 120)
curd_rice = MenuItem("Curd Rice", 70)

order = Order("Priya")
order.add_item(dal_rice)
order.add_item(veg_thali)
order.add_item(curd_rice)

order.print_summary()
