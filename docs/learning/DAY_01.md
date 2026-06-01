# Day 1 - Python Basics

Today your goal is not to become fast. Your goal is to become comfortable
reading small Python programs and changing them without fear.

## What You Learn Today

- What a Python file is.
- How to run a Python file.
- How to use `print()`.
- How to store values in variables.
- Basic data types: text, numbers, and true/false values.
- How software engineers check their own thinking by predicting output.

## Run The Day 1 Example

From the project folder, run:

```powershell
.\env\Scripts\python.exe .\learning\day_01_python_basics.py
```

If you first activate the environment, you can run:

```powershell
.\env\Scripts\activate
python .\learning\day_01_python_basics.py
```

## How To Study This File

1. Open `learning/day_01_python_basics.py`.
2. Read one section at a time.
3. Before running it, guess what it will print.
4. Run the file.
5. Change one value and run it again.

This is how developers learn: small change, run, observe, repeat.

## Your Practice Task

Open `learning/day_01_practice.py` and complete the TODOs.

Try to make the output look like this, but use your own values:

```text
Customer: Rahul
Plan: Monthly Veg Plan
Meals per day: 2
Days: 30
Price per meal: 80
Total price: 4800
```

## Interview Questions And Answers

Use this section for interview speaking practice. Read the question, cover the
answer, and try to explain it in your own words.

---

### 🟦 QUESTION

## **What is Python?**

### 🟩 ANSWER

**Definition**

Python is a **high-level programming language**.

**Key Points**

- It is easy to **read** and **write**.
- It is used for **backend development**, **automation**, **data work**, and
  **web development**.
- For web development, Python is often used with **Django**.

**Interview Answer**

"Python is a high-level programming language. It is readable, practical, and
commonly used for backend development, automation, data work, and web
applications with frameworks like Django."

---

### 🟦 QUESTION

## **Why are you learning Python?**

### 🟩 ANSWER

**Key Points**

- I want to become a **Python/Django backend developer**.
- Python is good for building **real web applications** and **APIs**.
- It is beginner-friendly but also used in professional companies.

**Interview Answer**

"I am learning Python because I want to become a backend/Django developer.
Python is readable, practical, and useful for building real web applications
and APIs."

---

### 🟦 QUESTION

## **What is a Python file?**

### 🟩 ANSWER

**Definition**

A Python file is a **text file** that contains Python code.

**Key Points**

- A Python file usually ends with the **.py** extension.
- We run it using the **Python interpreter**.
- It can contain variables, conditions, functions, classes, and more.

**Example**

```powershell
.\env\Scripts\python.exe .\learning\day_01_python_basics.py
```

**Interview Answer**

"A Python file is a text file that contains Python code. It usually ends with
.py, and we run it using the Python interpreter."

---

### 🟦 QUESTION

## **What is a variable?**

### 🟩 ANSWER

**Definition**

A variable is a **name that stores a value**.

**Key Points**

- Variables help us **reuse values**.
- Variable names should be clear and meaningful.
- A variable can store text, numbers, true/false values, and more.

**Example**

```python
customer_name = "Rahul"
price_per_meal = 80
```

**Interview Answer**

"A variable is a name that stores a value so we can reuse it later in the
program. For example, customer_name can store a customer's name."

---

### 🟦 QUESTION

## **What is the print function used for?**

### 🟩 ANSWER

**Definition**

The print function is used to **show output in the terminal**.

**Key Points**

- It helps us display results.
- It is useful while learning.
- It also helps during basic debugging.

**Example**

```python
print("Welcome to Python")
print("Total price:", 4800)
```

**Interview Answer**

"The print function is used to show output in the terminal. It helps display
results and check what is happening while learning or debugging."

---

### 🟦 QUESTION

## **What is a data type?**

### 🟩 ANSWER

**Definition**

A data type tells Python **what kind of value** we are working with.

**Key Points**

- Text is called **string**.
- Whole numbers are called **integer**.
- Decimal numbers are called **float**.
- True/false values are called **boolean**.

**Example**

```python
customer_name = "Rahul"
days = 30
price = 80.50
is_active = True
```

**Interview Answer**

"A data type tells Python what kind of value is stored. Common examples are
string for text, integer for whole numbers, float for decimal numbers, and
boolean for true or false values."

---

### 🟦 QUESTION

## **What is a string?**

### 🟩 ANSWER

**Definition**

A string is **text** in Python.

**Key Points**

- Strings are written inside quotes.
- Names, cities, emails, and messages are usually strings.

**Example**

```python
customer_name = "Rahul"
city = "Pune"
```

**Interview Answer**

"A string is text in Python. We write strings inside quotes, like a customer
name or city name."

---

### 🟦 QUESTION

## **What is an integer?**

### 🟩 ANSWER

**Definition**

An integer is a **whole number** without a decimal point.

**Key Points**

- Integers can be positive, negative, or zero.
- Integers are useful for quantity, days, age, and count.

**Example**

```python
days = 30
meals_per_day = 2
```

**Interview Answer**

"An integer is a whole number without a decimal point. Examples are 30, 100,
and minus 5."

---

### 🟦 QUESTION

## **What is a boolean?**

### 🟩 ANSWER

**Definition**

A boolean stores only **true** or **false**.

**Key Points**

- Booleans help programs make decisions.
- They are commonly used in conditions.
- In Python, true and false are written with capital first letters.

**Example**

```python
is_active_subscription = True
has_discount = False
```

**Interview Answer**

"A boolean stores only two possible values: True or False. It is commonly used
for conditions, like checking whether a subscription is active."

---

### 🟦 QUESTION

## **What is the difference between assignment and comparison?**

### 🟩 ANSWER

**Definition**

Assignment stores a value. Comparison checks a value.

**Key Points**

- Single equals means **assign a value**.
- Double equals means **compare two values**.

**Example**

```python
price = 80
price == 80
```

**Interview Answer**

"Single equals is used to assign a value to a variable. Double equals is used
to compare two values."

---

### 🟦 QUESTION

## **How do you think like a developer while learning?**

### 🟩 ANSWER

**Key Points**

- First, I try to **predict the output**.
- Then I **run the code**.
- If the output is different, I make **one small change** and run again.

**Interview Answer**

"I try to predict what the code will do, then I run it and compare the output.
If something is wrong, I change one small thing, run again, and learn from the
result."

## Done Checklist

- [ ] I ran `day_01_python_basics.py`.
- [ ] I changed at least three values.
- [ ] I completed `day_01_practice.py`.
- [ ] I can explain what a variable is in my own words.
