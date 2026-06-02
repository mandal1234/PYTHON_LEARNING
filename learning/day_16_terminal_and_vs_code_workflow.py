print("Day 16: Terminal And VS Code Workflow")
print("-------------------------------------")

lesson = {
    "phase": "Developer Tools",
    "goal": "use the terminal and VS Code like a developer",
    "learn": ['Open the correct folder in VS Code', 'Run Python files from the terminal', 'Understand folders, paths, and commands', 'Use one clean workspace for learning'],
}

print("Phase:", lesson["phase"])
print("Goal:", lesson["goal"])

print()
print("Today you learn")
print("---------------")

for item in lesson["learn"]:
    print("-", item)

print()
print("Small tiffin data example")
print("-------------------------")

orders = [
    {"customer": "Rahul", "total": 250, "status": "paid"},
    {"customer": "Priya", "total": 900, "status": "paid"},
    {"customer": "Amit", "total": 400, "status": "pending"},
]

paid_orders = [order for order in orders if order["status"] == "paid"]
high_value_orders = [order for order in orders if order["total"] >= 700]

revenue = 0

for order in paid_orders:
    revenue = revenue + order["total"]

print("Paid order count:", len(paid_orders))
print("High value order count:", len(high_value_orders))
print("Paid revenue:", revenue)

print()
print("Developer habit")
print("---------------")
print("Change one value, run again, and explain what changed.")
