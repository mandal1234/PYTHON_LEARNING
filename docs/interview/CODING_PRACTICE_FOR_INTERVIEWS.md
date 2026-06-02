# Coding Practice For Interviews

Use this file from Day 16 onward. Do not only read solutions. Try first.

## How To Practice

1. Read the problem.
2. Write the input and expected output.
3. Solve slowly.
4. Run the code.
5. Explain the logic out loud.

## Beginner Python Problems

### Problem 1 - Total Price

Given `price_per_meal` and `quantity`, return total price.

```python
def calculate_total(price_per_meal, quantity):
    return price_per_meal * quantity
```

### Problem 2 - Free Delivery

If order total is 500 or more, delivery is free. Otherwise delivery is 40.

```python
def delivery_fee(order_total):
    if order_total >= 500:
        return 0
    return 40
```

### Problem 3 - Count High Value Orders

Count how many orders are 700 or more.

```python
def count_high_value_orders(order_totals):
    count = 0

    for total in order_totals:
        if total >= 700:
            count = count + 1

    return count
```

### Problem 4 - Find Maximum Order

Find the highest order total from a list.

```python
def find_max_order(order_totals):
    highest = order_totals[0]

    for total in order_totals:
        if total > highest:
            highest = total

    return highest
```

### Problem 5 - Filter Active Customers

Return only active customers from a list of dictionaries.

```python
def active_customers(customers):
    result = []

    for customer in customers:
        if customer["is_active"]:
            result.append(customer)

    return result
```

## Must-Solve List

- Reverse a string.
- Count vowels in a string.
- Find duplicate values in a list.
- Remove duplicates from a list.
- Find second highest number.
- Count words in a sentence.
- Check if a number is even or odd.
- Sum all numbers in a list.
- Find all orders above 500.
- Group orders by status.

## Interview Habit

When solving, speak like this:

"First I understand the input. Then I decide the output. Then I use a loop or
condition based on the requirement. Finally I test with small examples."
