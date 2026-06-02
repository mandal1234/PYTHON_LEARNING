print("Day 7: Strings And F-Strings")
print("----------------------------")

raw_name = "  rahul sharma  "
raw_city = "  pune "
email = "RAHUL@EXAMPLE.COM"

clean_name = raw_name.strip().title()
clean_city = raw_city.strip().title()
clean_email = email.strip().lower()

print("Clean name:", clean_name)
print("Clean city:", clean_city)
print("Clean email:", clean_email)

print()
print("Check text")
print("----------")

if clean_email.endswith("@example.com"):
    print("This is an example email address")

print()
print("F-string bill")
print("-------------")

customer_name = "Priya"
plan_name = "Monthly Veg Plan"
total = 4800

message = f"{customer_name}, your {plan_name} total is Rs {total}."
print(message)

print()
print("Split text")
print("----------")

items_text = "Dal Rice,Paneer Rice,Veg Thali"
items = items_text.split(",")

for item in items:
    print(item)
