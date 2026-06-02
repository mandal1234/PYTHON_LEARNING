# Day 11 - Object-Oriented Programming Basics

Today your goal is to understand **classes** and **objects**.

Django uses classes often, so this is an important step.

## What You Learn Today

- What a **class** is.
- What an **object** is.
- What attributes are.
- What methods are.
- How one class can represent real-world data.

## Important Idea

```python
class Customer:
    def __init__(self, name, city):
        self.name = name
        self.city = city
```

## Run The Day 11 Example

```powershell
.\env\Scripts\python.exe .\learning\day_11_oop_basics.py
```

## Practice Task

```powershell
.\env\Scripts\python.exe .\learning\day_11_practice.py
```

## Interview Questions And Answers

---

### 🟦 QUESTION

## **What is a class?**

### 🟩 ANSWER

**Definition**

A class is a blueprint for creating objects.

**Key Points**

- A class defines what data and behavior an object has.
- It helps model real-world things.
- In Django, models are written as classes.

**Interview Answer**

"A class is a blueprint for creating objects. It defines what data and methods
the object should have."

---

### 🟦 QUESTION

## **What is an object?**

### 🟩 ANSWER

**Definition**

An object is a real value created from a class.

**Example**

```python
customer = Customer("Rahul", "Pune")
```

**Interview Answer**

"An object is an instance created from a class. If the class is a blueprint,
the object is the actual thing created from it."

---

### 🟦 QUESTION

## **What is self in Python classes?**

### 🟩 ANSWER

**Definition**

Self refers to the current object.

**Key Points**

- It lets the object access its own data.
- It is used inside class methods.
- Python passes it automatically when a method is called.

**Interview Answer**

"Self refers to the current object. It is used inside class methods to access
the object's own attributes and methods."

## Done Checklist

- [ ] I ran the Day 11 example.
- [ ] I created one class.
- [ ] I created one object.
- [ ] I used attributes and methods.
- [ ] I completed the practice file.
