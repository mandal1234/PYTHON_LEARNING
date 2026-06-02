# Master Interview Question Bank

Use this file after Day 60 and again after Day 90.

Do not memorize word-for-word. Read the answer, close the file, and explain it
in your own words.

## Python Questions

### 🟦 QUESTION

## **What are Python's main data types?**

### 🟩 ANSWER

**Key Points**

- **str** stores text.
- **int** stores whole numbers.
- **float** stores decimal numbers.
- **bool** stores True or False.
- **list** stores many values by position.
- **dict** stores key-value pairs.
- **tuple** stores fixed ordered values.
- **set** stores unique values.

**Interview Answer**

"Python has data types like string, integer, float, boolean, list, dictionary,
tuple, and set. I choose the type based on the data I need to store."

---

### 🟦 QUESTION

## **What is the difference between list, tuple, set, and dictionary?**

### 🟩 ANSWER

**Key Points**

- **list**: ordered, changeable, allows duplicates.
- **tuple**: ordered, not changeable, allows duplicates.
- **set**: unordered, changeable, unique values only.
- **dictionary**: key-value pairs.

**Example**

```python
items = ["Dal Rice", "Veg Thali"]
roles = ("admin", "customer")
cities = {"Pune", "Mumbai"}
customer = {"name": "Rahul", "city": "Pune"}
```

**Interview Answer**

"A list is good for ordered changeable data. A tuple is fixed data. A set is
for unique values. A dictionary stores named data as key-value pairs."

---

### 🟦 QUESTION

## **What is a function and why do we use it?**

### 🟩 ANSWER

**Key Points**

- A function is a reusable block of code.
- It helps avoid repeated logic.
- It makes code easier to test.
- It can accept parameters and return results.

**Example**

```python
def calculate_total(price, quantity):
    return price * quantity
```

**Interview Answer**

"A function is a reusable block of code that does one task. I use functions to
organize logic, avoid repetition, and make code easier to test."

---

### 🟦 QUESTION

## **What is exception handling?**

### 🟩 ANSWER

**Key Points**

- Exception handling lets us handle errors safely.
- Risky code goes inside **try**.
- Error handling code goes inside **except**.
- It prevents the program from crashing suddenly.

**Example**

```python
try:
    total = int(input("Total: "))
except ValueError:
    print("Please enter a valid number")
```

**Interview Answer**

"Exception handling lets me handle errors safely. I put risky code inside try
and handle the error inside except."

---

### 🟦 QUESTION

## **What is object-oriented programming?**

### 🟩 ANSWER

**Key Points**

- OOP organizes code using **classes** and **objects**.
- A class is a blueprint.
- An object is an instance of a class.
- Attributes store data.
- Methods define behavior.

**Example**

```python
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
```

**Interview Answer**

"Object-oriented programming organizes code around classes and objects. A
class is a blueprint, and an object is the actual item created from it."

## Django Questions

### 🟦 QUESTION

## **What is Django?**

### 🟩 ANSWER

**Key Points**

- Django is a Python web framework.
- It helps build secure web applications quickly.
- It includes ORM, admin, authentication, forms, templates, and routing.

**Interview Answer**

"Django is a Python web framework used to build web applications. It provides
many built-in features like ORM, admin, authentication, forms, and templates."

---

### 🟦 QUESTION

## **What is the difference between a Django project and app?**

### 🟩 ANSWER

**Key Points**

- A **project** contains the main settings and configuration.
- An **app** is a smaller feature module.
- One project can contain many apps.

**Interview Answer**

"A Django project is the full website configuration. An app is one feature
module inside the project, like menu, orders, or users."

---

### 🟦 QUESTION

## **Explain Django request-response flow.**

### 🟩 ANSWER

**Flow**

1. User sends a request.
2. Django checks URL patterns.
3. Matching view function or class runs.
4. View talks to models or forms if needed.
5. View returns a response, often HTML or JSON.

**Interview Answer**

"A request comes to Django, Django matches the URL, the view runs, the view may
use models or forms, and then it returns a response to the user."

---

### 🟦 QUESTION

## **What is a Django model?**

### 🟩 ANSWER

**Key Points**

- A model is a Python class.
- It represents a database table.
- Fields become database columns.
- Objects become database rows.

**Example**

```python
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
```

**Interview Answer**

"A Django model is a Python class that represents a database table. Its fields
become columns, and each object represents a row."

---

### 🟦 QUESTION

## **What are migrations?**

### 🟩 ANSWER

**Key Points**

- Migrations are Django's way to update the database schema.
- `makemigrations` creates migration files.
- `migrate` applies them to the database.

**Interview Answer**

"Migrations are files that describe database changes. I run makemigrations to
create them and migrate to apply them."

---

### 🟦 QUESTION

## **What is Django ORM?**

### 🟩 ANSWER

**Key Points**

- ORM means Object Relational Mapper.
- It lets us work with database records using Python code.
- It reduces the need to write raw SQL for common operations.

**Example**

```python
available_items = MenuItem.objects.filter(is_available=True)
```

**Interview Answer**

"Django ORM lets me interact with the database using Python classes and
methods instead of writing raw SQL for every query."

## Django REST Framework Questions

### 🟦 QUESTION

## **What is Django REST Framework?**

### 🟩 ANSWER

**Key Points**

- DRF is used to build APIs with Django.
- It provides serializers, API views, viewsets, routers, permissions, and
  authentication tools.

**Interview Answer**

"Django REST Framework is a toolkit for building APIs in Django. It helps with
serializers, views, permissions, authentication, and API routing."

---

### 🟦 QUESTION

## **What is a serializer?**

### 🟩 ANSWER

**Key Points**

- A serializer converts model objects to JSON-friendly data.
- It also validates incoming API data.
- A ModelSerializer is commonly used with Django models.

**Interview Answer**

"A serializer converts complex data like Django model objects into JSON data,
and it also validates incoming request data."

---

### 🟦 QUESTION

## **What is a ViewSet?**

### 🟩 ANSWER

**Key Points**

- A ViewSet groups related API actions in one class.
- It can handle list, create, retrieve, update, and delete.
- Routers can generate URLs automatically for ViewSets.

**Interview Answer**

"A ViewSet groups related API logic in one class. With routers, DRF can
automatically create standard CRUD API URLs."

---

### 🟦 QUESTION

## **What is the difference between authentication and permission?**

### 🟩 ANSWER

**Key Points**

- **Authentication** checks who the user is.
- **Permission** checks what the user is allowed to do.

**Interview Answer**

"Authentication identifies the user. Permission decides whether that user can
perform a particular action."

## SQL Questions

### 🟦 QUESTION

## **What is SQL?**

### 🟩 ANSWER

**Key Points**

- SQL is used to work with relational databases.
- It can create, read, update, and delete data.
- Common commands are SELECT, INSERT, UPDATE, and DELETE.

**Interview Answer**

"SQL is a language used to interact with relational databases. It is used to
query, insert, update, and delete data."

---

### 🟦 QUESTION

## **What is a primary key and foreign key?**

### 🟩 ANSWER

**Key Points**

- A **primary key** uniquely identifies a row.
- A **foreign key** connects one table to another table.

**Example**

An order has a `customer_id` foreign key that points to a customer.

**Interview Answer**

"A primary key uniquely identifies a record. A foreign key creates a
relationship between two tables."

---

### 🟦 QUESTION

## **What is a JOIN?**

### 🟩 ANSWER

**Key Points**

- A JOIN combines rows from related tables.
- It is commonly used when data is split into multiple tables.

**Example**

```sql
SELECT customers.name, orders.total
FROM customers
JOIN orders ON orders.customer_id = customers.id;
```

**Interview Answer**

"A JOIN is used to combine data from related tables, like customers and their
orders."
