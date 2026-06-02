# SQL Practice For Interviews

Use this after Day 31.

## Tables

Assume these tables:

```sql
customers(id, name, city, is_active)
orders(id, customer_id, total, status, created_at)
menu_items(id, name, price, is_available)
```

## Practice Queries

### Get All Customers

```sql
SELECT *
FROM customers;
```

### Get Active Customers

```sql
SELECT *
FROM customers
WHERE is_active = true;
```

### Get High Value Orders

```sql
SELECT *
FROM orders
WHERE total >= 700;
```

### Sort Orders By Total

```sql
SELECT *
FROM orders
ORDER BY total DESC;
```

### Count Orders

```sql
SELECT COUNT(*) AS order_count
FROM orders;
```

### Total Revenue

```sql
SELECT SUM(total) AS revenue
FROM orders
WHERE status = 'paid';
```

### Orders With Customer Names

```sql
SELECT customers.name, orders.total, orders.status
FROM orders
JOIN customers ON orders.customer_id = customers.id;
```

### Revenue By Customer

```sql
SELECT customers.name, SUM(orders.total) AS revenue
FROM orders
JOIN customers ON orders.customer_id = customers.id
GROUP BY customers.name;
```

## Interview Questions

### 🟦 QUESTION

## **What is the difference between WHERE and HAVING?**

### 🟩 ANSWER

**Key Points**

- **WHERE** filters rows before grouping.
- **HAVING** filters grouped results after `GROUP BY`.

**Interview Answer**

"WHERE filters individual rows before grouping. HAVING filters grouped results
after aggregation."

---

### 🟦 QUESTION

## **What is normalization?**

### 🟩 ANSWER

**Key Points**

- Normalization means organizing tables to reduce duplicate data.
- It separates related data into different tables.
- Relationships are handled using keys.

**Interview Answer**

"Normalization organizes database tables to reduce duplicate data and keep
relationships clean."
