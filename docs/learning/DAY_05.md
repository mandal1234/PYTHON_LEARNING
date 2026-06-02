# Day 5 - Functions

Today your goal is to stop repeating code.

A function is a named block of code that does one job.

## What You Learn Today

- What a **function** is.
- Why functions help us organize code.
- How to pass values using **parameters**.
- How to send back results using **return**.
- How functions help in Django views, models, and services.

## Important Idea

```python
def calculate_total(price, quantity):
    return price * quantity
```

## Run The Day 5 Example

```powershell
.\env\Scripts\python.exe .\learning\day_05_functions.py
```

## Practice Task

```powershell
.\env\Scripts\python.exe .\learning\day_05_practice.py
```

## Interview Questions And Answers

---

### 🟦 QUESTION

## **What is a function in Python?**

### 🟩 ANSWER

**Definition**

A function is a **reusable block of code** that performs a specific task.

**Key Points**

- It helps avoid repeated code.
- It makes code easier to read.
- It can receive input and return output.

**Example**

```python
def greet_customer(name):
    print("Welcome", name)
```

**Interview Answer**

"A function is a reusable block of code that performs one task. It helps keep
code organized and avoids repeating the same logic."

---

### 🟦 QUESTION

## **What is a parameter?**

### 🟩 ANSWER

**Definition**

A parameter is a variable inside a function that receives a value.

**Example**

```python
def calculate_total(price, quantity):
    return price * quantity
```

Here, **price** and **quantity** are parameters.

**Interview Answer**

"A parameter is a value that a function receives so it can work with different
inputs."

---

### 🟦 QUESTION

## **What does return do?**

### 🟩 ANSWER

**Definition**

Return sends a value back from a function.

**Example**

```python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(80, 5)
```

**Interview Answer**

"Return gives a result back from a function, so I can store it in a variable or
use it in another calculation."

## Done Checklist

- [ ] I ran the Day 5 example.
- [ ] I created one new function.
- [ ] I used parameters.
- [ ] I used return.
- [ ] I completed the practice file.
