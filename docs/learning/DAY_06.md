# Day 6 - While Loops And Input Validation

Today your goal is to repeat work **until a condition changes**.

For loops are good when we already have a list. While loops are good when we
continue until something becomes true or false.

## What You Learn Today

- What a **while loop** is.
- How to stop a loop.
- How to use a counter.
- How to validate user input.
- Why validation matters in real apps.

## Important Idea

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

## Run The Day 6 Example

```powershell
.\env\Scripts\python.exe .\learning\day_06_while_loops.py
```

## Practice Task

```powershell
.\env\Scripts\python.exe .\learning\day_06_practice.py
```

## Interview Questions And Answers

---

### 🟦 QUESTION

## **What is a while loop?**

### 🟩 ANSWER

**Definition**

A while loop repeats code while a condition is **true**.

**Key Points**

- It can run zero times, one time, or many times.
- The condition must eventually become false.
- If it never becomes false, the loop becomes infinite.

**Interview Answer**

"A while loop repeats a block of code while a condition is true. It is useful
when we do not know exactly how many times the loop should run."

---

### 🟦 QUESTION

## **What is an infinite loop?**

### 🟩 ANSWER

**Definition**

An infinite loop is a loop that never stops.

**Key Points**

- It happens when the condition always stays true.
- It can freeze or keep running the program.
- We avoid it by updating the condition inside the loop.

**Interview Answer**

"An infinite loop happens when a loop condition never becomes false. To avoid
it, we must update the value that controls the loop."

---

### 🟦 QUESTION

## **What is input validation?**

### 🟩 ANSWER

**Definition**

Input validation means checking that user input is correct before using it.

**Example**

```python
quantity = int(input("Quantity: "))

if quantity > 0:
    print("Valid quantity")
```

**Interview Answer**

"Input validation means checking user input before using it. It helps prevent
wrong data and errors in the program."

## Done Checklist

- [ ] I ran the Day 6 example.
- [ ] I understood how a while loop stops.
- [ ] I changed the counter value.
- [ ] I completed the practice file.
- [ ] I can explain infinite loop.
