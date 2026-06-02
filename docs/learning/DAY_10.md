# Day 10 - Modules And Imports

Today your goal is to organize code across files.

Real projects do not keep everything in one file. We split useful code into
modules and import it where needed.

## What You Learn Today

- What a **module** is.
- How to use **import**.
- How to create your own helper module.
- Why project structure matters.
- How this connects to Django apps.

## Important Idea

```python
from tiffin_utils import calculate_total

total = calculate_total(80, 30)
```

## Run The Day 10 Example

```powershell
.\env\Scripts\python.exe .\learning\day_10_modules_imports.py
```

## Practice Task

```powershell
.\env\Scripts\python.exe .\learning\day_10_practice.py
```

## Interview Questions And Answers

---

### 🟦 QUESTION

## **What is a module in Python?**

### 🟩 ANSWER

**Definition**

A module is a Python file that contains reusable code.

**Key Points**

- A module can contain functions, classes, and variables.
- We use import to use code from another file.
- Modules help keep projects organized.

**Interview Answer**

"A module is a Python file that contains reusable code. We can import it into
another file to keep our project organized."

---

### 🟦 QUESTION

## **What does import do?**

### 🟩 ANSWER

**Definition**

Import allows one Python file to use code from another Python file or library.

**Example**

```python
import math
```

**Interview Answer**

"Import lets me use code from another module or library instead of writing
everything again."

---

### 🟦 QUESTION

## **Why is code organization important?**

### 🟩 ANSWER

**Key Points**

- It makes code easier to read.
- It makes code easier to test.
- It helps teams work on bigger projects.

**Interview Answer**

"Code organization is important because real projects grow. Splitting code into
modules makes it easier to read, reuse, and maintain."

## Done Checklist

- [ ] I ran the Day 10 example.
- [ ] I understood import.
- [ ] I imported one helper function.
- [ ] I completed the practice file.
