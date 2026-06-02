# Day 39 - Transactions And Data Integrity

Today your goal is to **understand safe database changes**.

This is part of the **SQL And Database** section of your Python/Django job-readiness
course.

## What You Learn Today

- What a transaction is
- Commit
- Rollback
- Why partial saves are dangerous

## Important Idea

```sql
SELECT customer, total
FROM orders
WHERE total >= 700
ORDER BY total DESC;
```

## Run The Day 39 Example

```powershell
.\env\Scripts\python.exe .\learning\day_39_transactions_and_data_integrity.py
```

## Practice Task

```powershell
.\env\Scripts\python.exe .\learning\day_39_practice.py
```

## Today Practice Checklist

- Explain commit
- Explain rollback
- Write one transaction example idea

## Interview Questions And Answers

Use this section for interview speaking practice. Keep the answer simple,
specific, and connected to your tiffin project.

---

### 🟦 QUESTION

## **What is Transactions And Data Integrity?**

### 🟩 ANSWER

**Definition**

Transactions And Data Integrity is today's topic. It helps you **understand safe database changes**.

**Key Points**

- What a transaction is
- Commit
- Rollback

**Interview Answer**

"Transactions And Data Integrity helps me understand safe database changes. I practiced it with small examples and connected it
to the tiffin project I am building."

---

### 🟦 QUESTION

## **Why is this important for a Python/Django developer?**

### 🟩 ANSWER

**Key Points**

- Real backend projects need clear thinking and organized code.
- This topic appears in daily development work.
- It helps me understand Django project code with less fear.

**Interview Answer**

"This is important because backend developers work with data, user input,
business rules, and project structure every day. Learning this topic helps me
write cleaner Django code."

---

### 🟦 QUESTION

## **How will you practice Day 39?**

### 🟩 ANSWER

**Practice Plan**

- Explain commit
- Explain rollback
- Write one transaction example idea

**Interview Answer**

"I will run the example, complete the practice file, explain the code out loud,
and connect the idea to my tiffin project."

## Done Checklist

- [ ] I read this lesson.
- [ ] I ran the Day 39 example file.
- [ ] I completed the Day 39 practice file.
- [ ] I answered the interview questions out loud.
- [ ] I wrote one short note about what I learned.
