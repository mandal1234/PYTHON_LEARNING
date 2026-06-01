# Day 2 - User Input and Decisions

Today your goal is to make Python react to the user.

Yesterday you learned that variables store values. Today you learn how values
can come from the keyboard, and how a program can make a decision.

## What You Learn Today

- `input()` gets text from the user.
- `int()` converts text into a whole number.
- `float()` converts text into a decimal number.
- `if`, `elif`, and `else` let Python choose a path.
- Comparison operators help Python ask questions.

## Important Idea

`input()` always gives you text.

So if the user types `30`, Python first sees it as text, not a number.
To do math, convert it:

```python
days = int(input("Days: "))
```

## Run The Day 2 Example

From the fresh learning folder, run:

```powershell
.\env\Scripts\python.exe .\learning\day_02_input_and_decisions.py
```

The program will ask you for customer name, meals per day, days, and price.
Type an answer and press Enter each time.

## Practice Task

After the example works, complete:

```powershell
.\env\Scripts\python.exe .\learning\day_02_practice.py
```

## Interview Questions And Answers

Use this section for interview speaking practice. Keep the answer simple,
clear, and connected to the small programs you wrote.

---

### 🟦 QUESTION

## **What does the input function do in Python?**

### 🟩 ANSWER

**Definition**

The input function takes a value from the **user through the keyboard**.

**Key Points**

- It pauses the program and waits for the user.
- The user types a value and presses Enter.
- The value comes into Python as text.

**Example**

```python
customer_name = input("Customer name: ")
```

**Interview Answer**

"The input function takes a value from the user through the keyboard. Whatever
the user types is received as text."

---

### 🟦 QUESTION

## **Why does input return text?**

### 🟩 ANSWER

**Definition**

The input function returns text because Python does not know what type of value
the user wants to enter.

**Key Points**

- The user may type a name.
- The user may type a number.
- The user may type an email or address.
- Python gives it as text first, then we convert it if needed.

**Interview Answer**

"Python cannot know whether the user wants text, a number, or something else,
so input gives the value as text first. Then we convert it if needed."

---

### 🟦 QUESTION

## **Why do we convert input into a number?**

### 🟩 ANSWER

**Definition**

We convert input when we want to do **math or comparison** with the user's
value.

**Key Points**

- Text cannot be used properly for numeric calculation.
- Whole numbers are converted using the integer function.
- Decimal numbers are converted using the float function.

**Example**

```python
days = int(input("Number of days: "))
price = float(input("Price: "))
```

**Interview Answer**

"The input function gives text. If I want to do calculation, I convert the text
into a number using integer conversion or float conversion."

---

### 🟦 QUESTION

## **What is type conversion?**

### 🟩 ANSWER

**Definition**

Type conversion means changing a value from **one data type to another**.

**Key Points**

- Text can be converted into a number.
- A number can be converted into text.
- Conversion is important when working with user input.

**Example**

```python
days = int("30")
price = float("80.50")
message = str(100)
```

**Interview Answer**

"Type conversion means changing a value from one data type to another. For
example, we can convert the text 30 into the number 30 before calculation."

---

### 🟦 QUESTION

## **When do you use integer conversion?**

### 🟩 ANSWER

**Definition**

Integer conversion is used when we need a **whole number**.

**Key Points**

- Use it for days.
- Use it for quantity.
- Use it for age.
- Use it for meals per day.

**Example**

```python
meals_per_day = int(input("Meals per day: "))
```

**Interview Answer**

"I use integer conversion when I need a whole number for calculation, like
days, quantity, age, or meals per day."

---

### 🟦 QUESTION

## **When do you use float conversion?**

### 🟩 ANSWER

**Definition**

Float conversion is used when we need a number with a **decimal point**.

**Key Points**

- Use it for ratings.
- Use it for weight.
- Use it for percentages.
- Use it for prices with decimals.

**Example**

```python
rating = float(input("Rating: "))
discount_percent = float(input("Discount percent: "))
```

**Interview Answer**

"I use float conversion when I need a number that can have decimals, like
rating, weight, percentage, or price with paise."

---

### 🟦 QUESTION

## **What is an if statement?**

### 🟩 ANSWER

**Definition**

An if statement lets a program **make a decision**.

**Key Points**

- If the condition is true, one block runs.
- If the condition is false, another block can run.
- It helps us write business rules.

**Example**

```python
if order_total >= 500:
    print("Free delivery")
else:
    print("Delivery fee added")
```

**Interview Answer**

"An if statement lets the program make a decision. If a condition is true, one
block of code runs. Otherwise another block can run."

---

### 🟦 QUESTION

## **What are comparison operators?**

### 🟩 ANSWER

**Definition**

Comparison operators compare values and return **true** or **false**.

**Key Points**

- Greater than checks if one value is bigger.
- Less than checks if one value is smaller.
- Double equals checks if two values are equal.
- Not equal checks if two values are different.

**Example**

```python
order_total >= 500
days == 30
status != "cancelled"
```

**Interview Answer**

"Comparison operators compare values and give True or False. They are used in
conditions, like checking whether an order total is greater than 500."

---

### 🟦 QUESTION

## **What is the difference between if, elif, and else?**

### 🟩 ANSWER

**Definition**

These keywords help Python choose between **multiple paths**.

**Key Points**

- **if** checks the first condition.
- **elif** checks another condition if the first one is false.
- **else** runs when none of the previous conditions are true.

**Example**

```python
if days >= 30:
    discount_percent = 10
elif days >= 7:
    discount_percent = 5
else:
    discount_percent = 0
```

**Interview Answer**

"If checks the first condition. Elif checks another condition if the first one
is false. Else runs when none of the previous conditions are true."

---

### 🟦 QUESTION

## **Can you give a real example of if and else?**

### 🟩 ANSWER

**Example**

In a tiffin app:

- If the order total is **500 or more**, delivery is free.
- Otherwise, the customer pays a delivery fee.

**Code**

```python
if order_total >= 500:
    delivery_fee = 0
else:
    delivery_fee = 40
```

**Interview Answer**

"In a tiffin app, if the order total is 500 or more, delivery can be free.
Otherwise, the customer pays a delivery fee. That rule can be written with if
and else."

---

### 🟦 QUESTION

## **What is indentation in Python?**

### 🟩 ANSWER

**Definition**

Indentation means **spaces at the start of a line**.

**Key Points**

- Python uses indentation to understand code blocks.
- Code inside an if statement must be indented.
- Wrong indentation can cause errors.

**Example**

```python
if final_total >= 5000:
    print("High value customer")
```

**Interview Answer**

"Indentation means spaces at the start of a line. Python uses indentation to
understand which lines belong inside an if statement, loop, function, or
class."

---

### 🟦 QUESTION

## **What error can happen with user input?**

### 🟩 ANSWER

**Definition**

An error can happen when Python cannot convert the user's input into the
expected type.

**Key Points**

- If the program expects a number and the user types text, conversion fails.
- This can create a ValueError.
- Later, we can handle this using exception handling.

**Example**

```python
days = int(input("Number of days: "))
```

If the user types this:

```text
abc
```

Python cannot convert it into a number.

**Interview Answer**

"If I convert input into a number and the user types normal text, Python cannot
convert it and gives a ValueError. Later, I can handle this using exception
handling."

---

### 🟦 QUESTION

## **How would you explain your Day 2 program?**

### 🟩 ANSWER

**Key Points**

- It takes customer order details from the user.
- It converts number inputs into numbers.
- It calculates subtotal.
- It applies discount rules using conditions.
- It prints the final bill.

**Interview Answer**

"My Day 2 program takes customer order details from the user, converts number
inputs into integers, calculates the subtotal, applies discount rules using if,
elif, and else, and prints the final total."

## Done Checklist

- [ ] I ran the Day 2 example.
- [ ] I entered my own values.
- [ ] I changed the discount rules once.
- [ ] I completed the practice file.
- [ ] I can explain `input()`, `int()`, and `if` in my own words.
