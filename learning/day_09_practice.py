from pathlib import Path

print("Day 9 Practice: Save Customer Report")
print("------------------------------------")

report_path = Path(__file__).with_name("day_09_customer_report.txt")

customers = [
    {"name": "Rahul", "city": "Pune"},
    {"name": "Priya", "city": "Mumbai"},
]

# TODO 1:
# Open report_path in write mode.
# Write a report title.
# Loop through customers and write name and city into the file.

# TODO 2:
# Open the file in read mode and print its content.

print("Report path:", report_path)
