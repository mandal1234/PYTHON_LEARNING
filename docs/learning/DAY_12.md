# Day 12 - Classes With Lists Of Objects

Today your goal is to use objects together.

Real apps have many objects: many customers, many orders, many menu items.

## What You Learn Today

- How to store objects in lists.
- How one object can contain many other objects.
- How to calculate totals using object methods.
- How OOP can model real app logic.

## Important Idea

```python
items = [MenuItem("Dal Rice", 80), MenuItem("Veg Thali", 120)]
```

## Run The Day 12 Example

```powershell
.\env\Scripts\python.exe .\learning\day_12_objects_lists.py
```

## Practice Task

```powershell
.\env\Scripts\python.exe .\learning\day_12_practice.py
```

## Interview Questions And Answers

---

### 🟦 QUESTION

## **Can we store objects in a list?**

### 🟩 ANSWER

**Definition**

Yes, Python lists can store objects.

**Key Points**

- A list can store strings, numbers, dictionaries, or objects.
- Lists of objects are useful in real applications.
- We can loop through objects and use their attributes.

**Interview Answer**

"Yes, we can store objects in a list. This is useful when we have many records,
like many menu items or many orders."

---

### 🟦 QUESTION

## **Why combine classes and lists?**

### 🟩 ANSWER

**Key Points**

- A class represents one item.
- A list stores many items.
- Together, they help us model real business data.

**Interview Answer**

"Classes help represent one object, and lists help store many objects. Together
they are useful for modeling real application data."

---

### 🟦 QUESTION

## **How does this connect to Django?**

### 🟩 ANSWER

**Key Points**

- Django models are classes.
- Database records become model objects.
- Querysets are collections of model objects.

**Interview Answer**

"This connects to Django because Django models are classes, and database
records are represented as objects that we can work with in Python."

## Done Checklist

- [ ] I ran the Day 12 example.
- [ ] I stored objects in a list.
- [ ] I looped through objects.
- [ ] I calculated a total using object data.
- [ ] I completed the practice file.
