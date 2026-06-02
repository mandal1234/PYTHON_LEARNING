# Day 7 - Strings And F-Strings

Today your goal is to work better with text.

Backend developers handle names, emails, addresses, statuses, messages, and
API responses. Text skills matter.

## What You Learn Today

- Common string methods.
- How to clean spaces.
- How to change text case.
- How to check text.
- How to format output using **f-strings**.

## Important Idea

```python
customer_name = "rahul"
message = f"Welcome, {customer_name.title()}"
```

## Run The Day 7 Example

```powershell
.\env\Scripts\python.exe .\learning\day_07_strings.py
```

## Practice Task

```powershell
.\env\Scripts\python.exe .\learning\day_07_practice.py
```

## Interview Questions And Answers

---

### 🟦 QUESTION

## **What is a string method?**

### 🟩 ANSWER

**Definition**

A string method is an action we can perform on text.

**Example**

```python
name = " rahul "
clean_name = name.strip().title()
```

**Interview Answer**

"A string method is a built-in action for text, like removing spaces, changing
case, or checking whether text contains something."

---

### 🟦 QUESTION

## **What is an f-string?**

### 🟩 ANSWER

**Definition**

An f-string is a clean way to put variables inside text.

**Example**

```python
name = "Rahul"
total = 4800
print(f"{name}, your total is {total}")
```

**Interview Answer**

"An f-string is used to format text by placing variable values inside a string.
It makes output easier to read."

---

### 🟦 QUESTION

## **Why do we clean user text?**

### 🟩 ANSWER

**Key Points**

- Users may type extra spaces.
- Users may use different letter cases.
- Clean text makes searching and saving data easier.

**Interview Answer**

"We clean user text to remove extra spaces and make the data consistent before
we save or compare it."

## Done Checklist

- [ ] I ran the Day 7 example.
- [ ] I used strip, lower, upper, and title.
- [ ] I created one f-string.
- [ ] I completed the practice file.
