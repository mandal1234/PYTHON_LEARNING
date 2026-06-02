print("Day 5: Functions")
print("----------------")


def calculate_total(price_per_meal, meals):
    return price_per_meal * meals


def apply_discount(total, discount_percent):
    discount_amount = total * discount_percent / 100
    return total - discount_amount


def print_bill(customer_name, subtotal, final_total):
    print("Customer:", customer_name)
    print("Subtotal:", subtotal)
    print("Final total:", final_total)


customer_name = "Rahul"
price_per_meal = 80
meals = 30

subtotal = calculate_total(price_per_meal, meals)
final_total = apply_discount(subtotal, 10)

print_bill(customer_name, subtotal, final_total)

print()
print("Function with different data")
print("----------------------------")

another_subtotal = calculate_total(120, 15)
another_final_total = apply_discount(another_subtotal, 5)

print_bill("Priya", another_subtotal, another_final_total)
