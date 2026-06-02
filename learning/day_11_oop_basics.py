print("Day 11: OOP Basics")
print("------------------")


class Customer:
    def __init__(self, name, city, is_active):
        self.name = name
        self.city = city
        self.is_active = is_active

    def display_profile(self):
        print("Customer:", self.name)
        print("City:", self.city)
        print("Active:", self.is_active)


class Order:
    def __init__(self, customer_name, total):
        self.customer_name = customer_name
        self.total = total

    def is_high_value(self):
        return self.total >= 700


customer = Customer("Rahul", "Pune", True)
customer.display_profile()

print()
order = Order("Rahul", 850)

print("Order customer:", order.customer_name)
print("Order total:", order.total)
print("High value order:", order.is_high_value())
