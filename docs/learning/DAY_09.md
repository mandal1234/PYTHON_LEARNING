# Day 9 - File Handling

Today your goal is to save and read simple data from files.

Apps usually save data in databases, but file handling teaches an important
idea: programs can create, read, and update stored information.

## What You Learn Today

- How to write text to a file.
- How to read text from a file.
- Why file paths matter.
- How to use **with open** safely.
- How stored data relates to databases later.

## Important Idea

```python
with open("orders.txt", "w", encoding="utf-8") as file:
    file.write("Order total: 500")
```

## Run The Day 9 Example

```powershell
.\env\Scripts\python.exe .\learning\day_09_file_handling.py
```

## Practice Task

```powershell
.\env\Scripts\python.exe .\learning\day_09_practice.py
```

## Interview Questions And Answers

---

### 🟦 QUESTION

## **What is file handling?**

### 🟩 ANSWER

**Definition**

File handling means reading from files and writing data into files.

**Key Points**

- We can save output into a file.
- We can read stored text later.
- The with statement closes the file automatically.

**Interview Answer**

"File handling means reading and writing files using Python. It is useful for
logs, reports, configuration, and simple stored data."

---

### 🟦 QUESTION

## **Why do we use with open?**

### 🟩 ANSWER

**Definition**

With open safely opens a file and closes it automatically.

**Example**

```python
with open("report.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

**Interview Answer**

"We use with open because it handles closing the file automatically, even if
something goes wrong."

---

### 🟦 QUESTION

## **What is the difference between write and append mode?**

### 🟩 ANSWER

**Key Points**

- **w** writes a new file or replaces old content.
- **a** adds new content at the end.
- **r** reads existing content.

**Interview Answer**

"Write mode creates or replaces file content, append mode adds content at the
end, and read mode reads existing content."

## Done Checklist

- [ ] I ran the Day 9 example.
- [ ] I saw the created report file.
- [ ] I read data from a file.
- [ ] I completed the practice file.
