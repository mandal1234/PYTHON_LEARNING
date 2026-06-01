print("Day 2 Practice: Delivery Fee Calculator")
print("---------------------------------------")

customer_name = input("Customer name: ")
order_total = int(input("Order total: "))
customer_distance_km = int(input("Customer distance in km: "))

# TODO 1:
# If order_total is 500 or more, delivery_fee should be 0.
# Otherwise delivery_fee should be 40.
delivery_fee = 0

# TODO 2:
# If customer_distance_km is more than 5, add 20 extra to delivery_fee.

final_amount = order_total + delivery_fee

print()
print("Final bill")
print("----------")
print("Customer:", customer_name)
print("Order total:", order_total)
print("Distance:", customer_distance_km)
print("Delivery fee:", delivery_fee)
print("Final amount:", final_amount)

# Expected thinking:
# order_total = 600 and distance = 3 means delivery fee is 0.
# order_total = 300 and distance = 3 means delivery fee is 40.
# order_total = 300 and distance = 8 means delivery fee is 60.
