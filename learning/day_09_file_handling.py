from pathlib import Path

print("Day 9: File Handling")
print("--------------------")

report_path = Path(__file__).with_name("day_09_orders_report.txt")

orders = [
    {"customer": "Rahul", "total": 480},
    {"customer": "Priya", "total": 850},
    {"customer": "Amit", "total": 300},
]

with open(report_path, "w", encoding="utf-8") as file:
    file.write("Tiffin Orders Report\n")
    file.write("--------------------\n")

    for order in orders:
        line = f"{order['customer']} - Rs {order['total']}\n"
        file.write(line)

print("Report saved:", report_path)

print()
print("Read report")
print("-----------")

with open(report_path, "r", encoding="utf-8") as file:
    content = file.read()

print(content)
