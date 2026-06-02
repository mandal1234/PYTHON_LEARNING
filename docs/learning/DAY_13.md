# Day 13 - Filtering And List Comprehensions

Today your goal is to select the data you need.

Backend developers often filter data: active users, paid orders, pending
deliveries, high-value customers.

## What You Learn Today

- How to filter lists using loops.
- How to use list comprehensions.
- How to create new lists from old lists.
- How filtering connects to Django queries.

## Important Idea

```python
high_orders = [total for total in order_totals if total >= 700]
```

## Run The Day 13 Example

```powershell
.\env\Scripts\python.exe .\learning\day_13_filtering.py
```

## Practice Task

```powershell
.\env\Scripts\python.exe .\learning\day_13_practice.py
```

## Interview Questions And Answers

---

### 🟦 QUESTION

## **What is filtering?**

### 🟩 ANSWER

**Definition**

Filtering means selecting only the values that match a condition.

**Example**

```python
high_orders = []

for total in order_totals:
    if total >= 700:
        high_orders.append(total)
```

**Interview Answer**

"Filtering means selecting only the values that match a condition, like active
customers or high-value orders."

---

### 🟦 QUESTION

## **What is a list comprehension?**

### 🟩 ANSWER

**Definition**

A list comprehension is a shorter way to create a new list.

**Example**

```python
high_orders = [total for total in order_totals if total >= 700]
```

**Interview Answer**

"A list comprehension is a compact way to create a new list from an existing
list, usually with a condition or transformation."

---

### 🟦 QUESTION

## **How does filtering connect to Django?**

### 🟩 ANSWER

**Key Points**

- Django often filters database records.
- Example: active users or pending orders.
- Python filtering helps understand Django query filtering.

**Interview Answer**

"Filtering connects to Django because we often filter database records, like
getting only active users or pending orders."

## Done Checklist

- [ ] I ran the Day 13 example.
- [ ] I filtered a list using a loop.
- [ ] I used one list comprehension.
- [ ] I completed the practice file.
