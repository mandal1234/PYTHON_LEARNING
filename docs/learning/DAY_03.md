# Day 3 - Lists And Loops

Today your goal is to work with **many values**, not just one value.

In real apps, we rarely handle only one customer, one order, or one menu item.
We usually handle **lists of data**.

## What You Learn Today

- What a **list** is.
- How to read values from a list.
- Why list indexes start from **0**.
- How to add items to a list.
- How to count items in a list.
- How to repeat work using a **for loop**.
- How to calculate totals using a loop.

## Important Idea

A list stores **multiple values** in one variable.

```python
menu_items = ["Dal Rice", "Paneer Rice", "Veg Thali"]
```

A loop lets Python repeat work for each value.

```python
for item in menu_items:
    print(item)
```

## Run The Day 3 Example

From the fresh learning folder, run:

```powershell
.\env\Scripts\python.exe .\learning\day_03_lists_and_loops.py
```

## Practice Task

After the example works, complete:

```powershell
.\env\Scripts\python.exe .\learning\day_03_practice.py
```

## Interview Questions And Answers

Use this section for interview speaking practice. Speak slowly and use examples.

---

### 🟦 QUESTION

## **What is a list in Python?**

### 🟩 ANSWER

**Definition**

A list is a collection that stores **multiple values** in one variable.

**Key Points**

- A list can store many values.
- Lists are written using square brackets.
- A list can store strings, numbers, booleans, or mixed values.

**Example**

```python
menu_items = ["Dal Rice", "Paneer Rice", "Veg Thali"]
```

**Interview Answer**

"A list is a collection that stores multiple values in one variable. For
example, a menu list can store many food item names."

---

### 🟦 QUESTION

## **Why do we use lists?**

### 🟩 ANSWER

**Key Points**

- We use lists when we have many related values.
- Lists avoid creating too many separate variables.
- Lists make it easy to loop through data.

**Example**

```python
order_totals = [250, 500, 800, 1200]
```

**Interview Answer**

"We use lists to store many related values together. This makes the program
cleaner and allows us to process each value using loops."

---

### 🟦 QUESTION

## **What is an index in a list?**

### 🟩 ANSWER

**Definition**

An index is the **position number** of an item in a list.

**Key Points**

- Python list indexes start from 0.
- The first item is at index 0.
- The second item is at index 1.

**Example**

```python
menu_items = ["Dal Rice", "Paneer Rice", "Veg Thali"]

print(menu_items[0])
print(menu_items[1])
```

**Interview Answer**

"An index is the position of an item in a list. In Python, indexes start from
0, so the first item is at index 0."

---

### 🟦 QUESTION

## **How do you add an item to a list?**

### 🟩 ANSWER

**Definition**

We can add a new item to the end of a list using the append method.

**Example**

```python
menu_items = ["Dal Rice", "Paneer Rice"]
menu_items.append("Veg Thali")
```

**Interview Answer**

"We can add a new item to the end of a list using append. It changes the list
by adding the new value at the end."

---

### 🟦 QUESTION

## **What does the len function do?**

### 🟩 ANSWER

**Definition**

The len function counts how many items are inside a list.

**Example**

```python
menu_items = ["Dal Rice", "Paneer Rice", "Veg Thali"]
total_items = len(menu_items)
```

**Interview Answer**

"The len function returns the number of items in a list. It is useful when we
need to count records or values."

---

### 🟦 QUESTION

## **What is a loop?**

### 🟩 ANSWER

**Definition**

A loop repeats a block of code.

**Key Points**

- Loops help us avoid writing the same code again and again.
- A for loop is commonly used with lists.
- The loop runs once for each item.

**Example**

```python
menu_items = ["Dal Rice", "Paneer Rice", "Veg Thali"]

for item in menu_items:
    print(item)
```

**Interview Answer**

"A loop repeats a block of code. In Python, a for loop can go through each item
in a list and run code for every item."

---

### 🟦 QUESTION

## **Why are loops useful in backend development?**

### 🟩 ANSWER

**Key Points**

- Backend apps often handle many records.
- We may need to process many orders, users, payments, or menu items.
- Loops help us repeat the same logic for each record.

**Example**

```python
order_totals = [250, 500, 800]

for total in order_totals:
    print("Order total:", total)
```

**Interview Answer**

"Loops are useful in backend development because we often work with many
records, like orders or users. A loop lets us process each record one by one."

---

### 🟦 QUESTION

## **How do you calculate a total using a loop?**

### 🟩 ANSWER

**Key Points**

- Start with total as 0.
- Go through each number.
- Add each number to the total.

**Example**

```python
order_totals = [250, 500, 800]
grand_total = 0

for total in order_totals:
    grand_total = grand_total + total

print(grand_total)
```

**Interview Answer**

"To calculate a total using a loop, I start with a total value of 0, then add
each item value to the total inside the loop."

---

### 🟦 QUESTION

## **How would you explain your Day 3 program?**

### 🟩 ANSWER

**Key Points**

- It stores menu items in a list.
- It prints each menu item using a loop.
- It stores order totals in another list.
- It calculates the grand total using a loop.

**Interview Answer**

"My Day 3 program uses lists to store menu items and order totals. Then it uses
for loops to print each item and calculate the grand total."

## Done Checklist

- [ ] I ran the Day 3 example.
- [ ] I changed at least three menu items.
- [ ] I added one new item using append.
- [ ] I completed the practice file.
- [ ] I can explain list, index, len, and loop in my own words.
