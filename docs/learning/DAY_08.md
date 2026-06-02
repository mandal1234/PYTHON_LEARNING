# Day 8 - Error Handling

Today your goal is to stop being afraid of errors.

Errors are normal. Professional developers learn how to read them, prevent
them, and handle them.

## What You Learn Today

- What an error is.
- What an exception is.
- How to use **try** and **except**.
- How to handle invalid numbers.
- How error handling protects real apps.

## Important Idea

```python
try:
    quantity = int("abc")
except ValueError:
    print("Please enter a valid number")
```

## Run The Day 8 Example

```powershell
.\env\Scripts\python.exe .\learning\day_08_error_handling.py
```

## Practice Task

```powershell
.\env\Scripts\python.exe .\learning\day_08_practice.py
```

## Interview Questions And Answers

---

### 🟦 QUESTION

## **What is exception handling?**

### 🟩 ANSWER

**Definition**

Exception handling is a way to handle errors without crashing the program.

**Key Points**

- Code that may fail goes inside **try**.
- Error handling code goes inside **except**.
- It helps make programs safer.

**Interview Answer**

"Exception handling lets us handle errors safely. We put risky code inside try
and handle the error inside except."

---

### 🟦 QUESTION

## **What is ValueError?**

### 🟩 ANSWER

**Definition**

A ValueError happens when a value has the correct type idea but an invalid
content.

**Example**

```python
int("abc")
```

**Interview Answer**

"A ValueError can happen when Python cannot convert a value, like trying to
convert the text abc into an integer."

---

### 🟦 QUESTION

## **Why is error handling important in backend development?**

### 🟩 ANSWER

**Key Points**

- Users can send wrong input.
- APIs can receive missing or invalid data.
- Good error handling gives clear responses.

**Interview Answer**

"Error handling is important in backend development because users and APIs may
send invalid data. We handle errors to keep the application stable."

## Done Checklist

- [ ] I ran the Day 8 example.
- [ ] I understood try and except.
- [ ] I tested invalid input.
- [ ] I completed the practice file.
