# Final Portfolio Project - Tiffin Order Management System

This is the project you should build for interviews.

## Project Goal

Build a Django + DRF application where customers can view menu items and place
tiffin orders, while admins can manage menu, orders, subscriptions, and status.

## Core Features

- User registration and login.
- Public menu list.
- Customer order creation.
- Customer order history.
- Admin menu management.
- Admin order status management.
- Subscription plan management.
- REST API for menu and orders.
- PostgreSQL-ready settings.
- Basic tests.
- README with setup, screenshots, and API examples.

## Suggested Apps

- `accounts`
- `menu`
- `orders`
- `subscriptions`
- `payments`
- `api`

## Suggested Models

### CustomerProfile

- user
- phone
- address
- city

### MenuItem

- name
- description
- price
- category
- is_available
- created_at

### Order

- customer
- status
- total_amount
- delivery_address
- created_at

### OrderItem

- order
- menu_item
- quantity
- price

### SubscriptionPlan

- name
- meals_per_day
- duration_days
- price
- is_active

### Payment

- order
- amount
- status
- payment_method
- created_at

## API Endpoints

```text
GET    /api/menu/
POST   /api/orders/
GET    /api/orders/
GET    /api/orders/{id}/
PATCH  /api/orders/{id}/
GET    /api/subscriptions/
```

## Tests You Should Add

- Menu item creation test.
- Order total calculation test.
- Login required page test.
- API menu list test.
- API order creation test.
- Permission test for admin-only action.

## README Must Include

- Project name.
- Short summary.
- Tech stack.
- Features.
- Screenshots.
- Local setup steps.
- API endpoints.
- Test command.
- Demo login details if safe.
- What you learned.

## Interview Explanation

"I built a Tiffin Order Management System using Django and Django REST
Framework. It has user authentication, menu management, order creation, order
status tracking, REST APIs, PostgreSQL-ready settings, and tests. I designed
the models around real business entities like customers, menu items, orders,
subscriptions, and payments."
