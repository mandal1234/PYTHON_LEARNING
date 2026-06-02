# Day 4 - Dictionaries

Today your goal is to store **related information** together.

Lists store many values. Dictionaries store values with **names**.

## What You Learn Today

- What a **dictionary** is.
- What **keys** and **values** are.
- How to read dictionary values.
- How to update dictionary values.
- How to store many dictionaries inside a list.

## Important Idea

A dictionary stores data in **key-value pairs**.

```python
customer = {
    "name": "Rahul",
    "city": "Pune",
    "is_active": True
}
```

## Run The Day 4 Example

```powershell
.\env\Scripts\python.exe .\learning\day_04_dictionaries.py
```

## Practice Task

```powershell
.\env\Scripts\python.exe .\learning\day_04_practice.py
```

## Interview Questions And Answers

---

### 🟦 QUESTION

## **What is a dictionary in Python?**

### 🟩 ANSWER

**Definition**

A dictionary stores data in **key-value pairs**.

**Key Points**

- A **key** is the name of the data.
- A **value** is the actual data.
- Dictionaries are useful for storing real-world objects.

**Example**

```python
customer = {"name": "Rahul", "city": "Pune"}
```

**Interview Answer**

"A dictionary is a collection that stores data as key-value pairs. It is useful
when I want to store related information, like customer name, city, and status."

---

### 🟦 QUESTION

## **What is the difference between a list and a dictionary?**

### 🟩 ANSWER

**Key Points**

- A **list** stores values by position.
- A **dictionary** stores values by name.
- Lists use indexes. Dictionaries use keys.

**Example**

```python
menu_items = ["Dal Rice", "Veg Thali"]
customer = {"name": "Rahul", "city": "Pune"}
```

**Interview Answer**

"A list stores values by position, but a dictionary stores values by key names.
Dictionaries are better when each value has a clear meaning."

---

### 🟦 QUESTION

## **Why are dictionaries useful in backend development?**

### 🟩 ANSWER

**Key Points**

- Backend apps work with structured data.
- Users, orders, menus, and payments have many fields.
- Dictionaries help represent one record clearly.

**Interview Answer**

"Dictionaries are useful in backend development because they can represent
structured data, like one user, one order, or one menu item."

## Done Checklist

- [ ] I ran the Day 4 example.
- [ ] I changed customer values.
- [ ] I added one new key.
- [ ] I completed the practice file.
- [ ] I can explain key-value pairs.
