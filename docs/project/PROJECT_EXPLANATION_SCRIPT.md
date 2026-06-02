# Project Explanation Script

Use this before every interview.

## 60-Second Project Pitch

"My main project is a Tiffin Order Management System built with Python, Django,
and Django REST Framework. Customers can view menu items, place orders, and
track order status. Admin users can manage menu items, subscriptions, and
orders. I used Django models for the database structure, Django ORM for
queries, forms and templates for web pages, DRF serializers and viewsets for
APIs, and tests for important logic."

## 2-Minute Technical Explanation

"I started by designing the database models. The main models are MenuItem,
Order, OrderItem, SubscriptionPlan, and Payment. MenuItem stores food details
like name, price, category, and availability. Order stores customer, status,
total amount, and delivery address. OrderItem connects orders with menu items,
because one order can contain many items.

For the web side, I used Django views, templates, forms, authentication, and
permissions. For the API side, I used Django REST Framework serializers,
viewsets, routers, and permission classes. I also added filters for order
status and search for menu items.

I prepared the project for production by using environment variables,
PostgreSQL-ready configuration, static file handling, and deployment checklist
notes."

## Questions You Must Be Ready For

### Why did you choose Django?

"I chose Django because it is a strong backend framework with built-in ORM,
admin, authentication, forms, and security features. It lets me build real web
applications quickly and cleanly."

### Why did you use Django REST Framework?

"I used DRF to expose project data through APIs. It helps with serializers,
validation, permissions, authentication, and viewsets."

### What was the hardest part?

"The hardest part was thinking through relationships between orders and menu
items. I learned that one order can contain many items, so I used an OrderItem
model to connect them."

### How did you calculate order total?

"Each OrderItem has quantity and price. The order total is calculated by
summing quantity multiplied by price for all items in the order."

### How did you protect routes?

"For web pages, I used login-required protection. For APIs, I used DRF
permission classes so only authenticated users or admins can perform certain
actions."

### What would you improve next?

"I would add online payment integration, notification emails, better dashboard
analytics, and deployment monitoring."
