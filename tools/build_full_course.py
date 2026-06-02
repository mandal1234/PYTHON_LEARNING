from pathlib import Path
import re
import textwrap


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs" / "learning"
LEARNING_DIR = ROOT / "learning"


CURRICULUM = [
    (16, "Terminal And VS Code Workflow", "Developer Tools", "use the terminal and VS Code like a developer", ["Open the correct folder in VS Code", "Run Python files from the terminal", "Understand folders, paths, and commands", "Use one clean workspace for learning"], ["Open VS Code in the learning folder", "Run any Day 1 to Day 15 file", "Write down three commands you used"]),
    (17, "Virtual Environments And Pip", "Developer Tools", "understand isolated Python environments and package installation", ["What a virtual environment is", "Why projects need separate environments", "How pip installs packages", "How requirements files work"], ["Activate the environment", "Check Python version", "Read requirements_course.txt"]),
    (18, "Git Basics", "Developer Tools", "track code changes using Git", ["What Git is", "What a repository is", "How status, add, commit, and log work", "Why commits matter"], ["Create a Git practice note", "Learn git status", "Write your first commit message example"]),
    (19, "GitHub And Portfolio Repositories", "Developer Tools", "prepare code for public portfolio sharing", ["What GitHub is", "What a remote repository is", "What README files do", "How interviewers look at repositories"], ["Draft a README introduction", "List project features", "Write setup steps"]),
    (20, "Python Coding Style And Debugging", "Developer Tools", "write readable code and inspect problems", ["Readable variable names", "Small functions", "Using print for debugging", "Reading errors calmly"], ["Rename unclear variables", "Add one debug print", "Explain one error message"]),
    (21, "Tuples And Sets", "Advanced Python", "learn more Python collection types", ["What tuples are", "What sets are", "When to use each collection", "How sets remove duplicates"], ["Create a tuple of weekdays", "Create a set of delivery cities", "Remove duplicate cities"]),
    (22, "Advanced Dictionaries", "Advanced Python", "work confidently with dictionary data", ["get method", "keys and values", "looping through dictionaries", "updating nested values"], ["Create a customer dictionary", "Use get for optional phone", "Loop through keys and values"]),
    (23, "Nested Data Structures", "Advanced Python", "store real app-like data using lists and dictionaries together", ["Lists inside dictionaries", "Dictionaries inside lists", "Nested loops", "Real order data structure"], ["Create three orders", "Each order should include items", "Print customer and item names"]),
    (24, "JSON Data", "Advanced Python", "understand JSON used by APIs", ["What JSON is", "Python dict to JSON", "JSON to Python dict", "Why APIs use JSON"], ["Convert an order dict to JSON", "Read JSON back into Python", "Explain JSON in interview words"]),
    (25, "CSV Files", "Advanced Python", "handle simple tabular data", ["What CSV is", "Reading CSV rows", "Writing CSV reports", "CSV vs JSON"], ["Write orders to CSV", "Read orders from CSV", "Print total order count"]),
    (26, "Dates And Times", "Advanced Python", "work with order dates and delivery times", ["date and datetime", "Formatting dates", "Comparing dates", "Using dates in orders"], ["Print today's date", "Create a delivery date", "Format it for users"]),
    (27, "Pathlib And Project Paths", "Advanced Python", "manage files and folders cleanly", ["What pathlib is", "Absolute vs relative paths", "Creating paths safely", "Using __file__"], ["Build a report path", "Create a folder path", "Explain why paths matter"]),
    (28, "Logging Basics", "Advanced Python", "record useful application events", ["What logging is", "logging vs print", "Log levels", "Why backend apps need logs"], ["Log one order created message", "Log one warning", "Explain logging simply"]),
    (29, "Unit Testing With Unittest", "Advanced Python", "test small pieces of code", ["What a test is", "Why tests matter", "unittest basics", "Arrange, act, assert"], ["Write a test idea for total calculation", "Run the example", "Explain why testing helps confidence"]),
    (30, "Type Hints And Clean Code", "Advanced Python", "make code easier to understand", ["What type hints are", "Function signatures", "Readable return values", "Clean code habits"], ["Add type hints to one function", "Write one clean function", "Explain type hints"]),
    (31, "SQL Introduction And SQLite", "SQL And Database", "understand databases before Django models", ["What a database is", "What SQL is", "What SQLite is", "Why Django uses databases"], ["Create a simple table idea", "Explain database vs file", "Run the example"]),
    (32, "Tables And CRUD", "SQL And Database", "create, read, update, and delete records", ["CREATE TABLE", "INSERT", "SELECT", "UPDATE", "DELETE"], ["Create menu item rows", "Update one price", "Delete one sample row"]),
    (33, "Where And Order By", "SQL And Database", "filter and sort database records", ["WHERE conditions", "ORDER BY", "Filtering active data", "Sorting reports"], ["Find high value orders", "Sort orders by amount", "Explain WHERE"]),
    (34, "Aggregations", "SQL And Database", "calculate totals from database data", ["COUNT", "SUM", "AVG", "MIN and MAX", "GROUP BY idea"], ["Count orders", "Sum revenue", "Find average order total"]),
    (35, "Joins", "SQL And Database", "connect related tables", ["Why joins exist", "Primary key idea", "Foreign key idea", "Joining customers and orders"], ["Draw customers and orders", "Explain foreign key", "Run join example idea"]),
    (36, "Constraints And Relationships", "SQL And Database", "protect database data quality", ["NOT NULL", "UNIQUE", "Foreign keys", "Valid relationships"], ["List constraints for users", "List constraints for orders", "Explain data integrity"]),
    (37, "Database Design For Tiffin App", "SQL And Database", "design tables for your interview project", ["Customer table", "Menu item table", "Order table", "Subscription table", "Payment table"], ["Sketch tables", "Write fields for each table", "Explain one relationship"]),
    (38, "Python With SQLite", "SQL And Database", "connect Python code to a database", ["sqlite3 module", "Connection", "Cursor", "Executing SQL from Python"], ["Create a Python database script", "Insert sample rows", "Read rows back"]),
    (39, "Transactions And Data Integrity", "SQL And Database", "understand safe database changes", ["What a transaction is", "Commit", "Rollback", "Why partial saves are dangerous"], ["Explain commit", "Explain rollback", "Write one transaction example idea"]),
    (40, "SQL Interview Review", "SQL And Database", "review important database interview answers", ["SQL definitions", "CRUD", "Joins", "Aggregations", "Database design"], ["Answer five SQL questions", "Explain joins out loud", "Review table design"]),
    (41, "HTTP Basics", "Web Basics", "understand request and response flow", ["What HTTP is", "Request and response", "GET and POST", "Status codes"], ["Explain GET vs POST", "List common status codes", "Connect HTTP to Django views"]),
    (42, "HTML Basics For Backend Developers", "Web Basics", "read and write simple templates", ["HTML tags", "Forms", "Tables", "Links", "Template structure"], ["Create a simple menu page idea", "Write form fields", "Explain HTML role"]),
    (43, "Forms And Request Data", "Web Basics", "understand how browser input reaches backend code", ["Form method", "Form action", "Input names", "Request data"], ["Design an order form", "List input names", "Explain request data"]),
    (44, "JSON And APIs", "Web Basics", "understand API data exchange", ["What an API is", "JSON request", "JSON response", "Frontend/backend communication"], ["Write a sample order JSON", "Explain API response", "Compare HTML page and API"]),
    (45, "Authentication Concepts", "Web Basics", "understand login and user identity", ["Authentication", "Authorization", "Sessions", "Tokens", "Password safety"], ["Explain login flow", "Explain permission", "Write role examples"]),
    (46, "Install Django And Create Project", "Django", "start the Django part of the course", ["Install Django", "Check Django version", "Create project", "Run development server"], ["Install requirements when ready", "Create tiffin_project", "Run the server"]),
    (47, "Django Project Vs App", "Django", "understand Django structure", ["Project folder", "App folder", "settings.py", "manage.py", "INSTALLED_APPS"], ["Create core app", "Add app to settings", "Explain project vs app"]),
    (48, "URLs And Views", "Django", "connect browser URLs to Python functions", ["URLconf", "path function", "function based views", "HttpResponse", "include"], ["Create home view", "Create menu view", "Connect app URLs"]),
    (49, "Templates", "Django", "return HTML using Django templates", ["Template folders", "render function", "Template variables", "For loops in templates"], ["Create home.html", "Pass menu items", "Loop in template"]),
    (50, "Static Files And Base Layout", "Django", "add CSS and shared page layout", ["static folder", "CSS files", "base.html", "Template inheritance"], ["Create base template", "Add CSS", "Extend base page"]),
    (51, "Models And Migrations", "Django", "create database tables using Django models", ["Model classes", "Fields", "makemigrations", "migrate", "Database tables"], ["Create MenuItem model", "Run migrations", "Explain model to table"]),
    (52, "Django Admin", "Django", "manage data through Django admin", ["Admin site", "Superuser", "Register model", "list_display", "Search in admin"], ["Create superuser", "Register models", "Add menu data"]),
    (53, "QuerySet Basics", "Django", "read database data with Django ORM", ["QuerySet", "all", "filter", "get", "order_by"], ["Filter available menu items", "Order by price", "Explain QuerySet"]),
    (54, "Django Forms", "Django", "validate user input using forms", ["Form class", "ModelForm", "cleaned_data", "Validation errors"], ["Create order form", "Validate phone", "Show form errors"]),
    (55, "CRUD Menu Items", "Django", "build create, read, update, delete pages", ["List view", "Create view", "Update view", "Delete view", "Redirect"], ["Build menu CRUD", "Test each action", "Explain CRUD"]),
    (56, "CRUD Orders", "Django", "build order management pages", ["Order model", "Order item idea", "Create order", "Update status", "Order list"], ["Build order CRUD", "Add status choices", "Filter pending orders"]),
    (57, "User Authentication", "Django", "add login and logout", ["Django auth", "LoginView", "LogoutView", "User model", "Login templates"], ["Create login page", "Add logout link", "Protect one page"]),
    (58, "Permissions And Login Required", "Django", "control who can do what", ["login_required", "User roles", "Staff users", "Access control"], ["Protect admin-like pages", "Allow customers to see own orders", "Explain permission"]),
    (59, "Search Filter Pagination", "Django", "make list pages useful", ["Search query", "Filtering by status", "Pagination", "GET parameters"], ["Search menu by name", "Filter orders by status", "Paginate orders"]),
    (60, "Django Messages And Validation", "Django", "give users helpful feedback", ["messages framework", "Success messages", "Validation messages", "User experience"], ["Show order success message", "Show invalid form message", "Explain feedback"]),
    (61, "Class Based Views", "Django", "understand Django reusable view classes", ["ListView", "DetailView", "CreateView", "UpdateView", "DeleteView"], ["Convert one list view", "Create one DetailView", "Explain CBV"]),
    (62, "File Uploads And Media", "Django", "handle images and uploaded files", ["MEDIA_ROOT", "MEDIA_URL", "ImageField idea", "Upload safety"], ["Add menu item image field", "Configure media", "Display image"]),
    (63, "Django Testing", "Django", "test views and models", ["TestCase", "Client", "Model tests", "View tests", "Test database"], ["Test MenuItem string", "Test home page status", "Test order total"]),
    (64, "Environment Variables And Settings", "Django", "separate development and production secrets", ["SECRET_KEY", "DEBUG", ".env", "python-dotenv", "Production settings"], ["Create .env.example", "Read DEBUG from env", "Explain secret safety"]),
    (65, "Django Review Mini Project", "Django", "review web project skills", ["Models", "Templates", "Forms", "CRUD", "Auth", "Tests"], ["Review your tiffin web app", "Fix one weak area", "Explain app flow"]),
    (66, "DRF Setup", "Django REST Framework", "start building APIs", ["Install DRF", "Add rest_framework", "API route", "Browsable API"], ["Add DRF to settings", "Create first API URL", "Open browsable API"]),
    (67, "Serializers", "Django REST Framework", "convert model objects to JSON", ["Serializer", "ModelSerializer", "Validation", "JSON output"], ["Create MenuItemSerializer", "Serialize list data", "Explain serializer"]),
    (68, "APIView", "Django REST Framework", "write API views manually", ["APIView class", "get method", "post method", "Response", "status codes"], ["Create menu list API", "Create menu create API", "Return JSON response"]),
    (69, "Generic Views", "Django REST Framework", "reduce API boilerplate", ["ListCreateAPIView", "RetrieveUpdateDestroyAPIView", "queryset", "serializer_class"], ["Build menu generic API", "Build order detail API", "Explain generic views"]),
    (70, "ViewSets And Routers", "Django REST Framework", "build REST endpoints cleanly", ["ModelViewSet", "DefaultRouter", "register", "CRUD endpoints"], ["Create MenuItemViewSet", "Register router", "Test generated endpoints"]),
    (71, "API Permissions", "Django REST Framework", "control API access", ["AllowAny", "IsAuthenticated", "IsAdminUser", "Custom permission idea"], ["Protect order API", "Allow public menu API", "Explain permission classes"]),
    (72, "Token And JWT Authentication", "Django REST Framework", "understand API login tokens", ["Token idea", "JWT idea", "Access token", "Refresh token", "Authorization header"], ["Install simplejwt", "Get token", "Call protected API"]),
    (73, "Filtering Ordering Pagination API", "Django REST Framework", "make APIs usable for real clients", ["Filtering", "Search", "Ordering", "Pagination", "Query parameters"], ["Filter orders by status", "Search menu", "Paginate API response"]),
    (74, "API Tests", "Django REST Framework", "test API behavior", ["APITestCase", "APIClient", "Status codes", "Authentication in tests"], ["Test menu API", "Test protected order API", "Test invalid input"]),
    (75, "API Documentation And Postman", "Django REST Framework", "document and test APIs professionally", ["Endpoint list", "Request body", "Response body", "Postman collection", "README API section"], ["Write API docs", "Capture sample requests", "Explain one endpoint"]),
    (76, "PostgreSQL Basics For Django", "Deployment And Production", "prepare for production database work", ["Why PostgreSQL", "Connection settings", "psycopg", "Local vs production database"], ["Read DATABASE settings", "Write env variables", "Explain PostgreSQL"]),
    (77, "Docker Basics", "Deployment And Production", "understand containerized development", ["What Docker is", "Image", "Container", "Dockerfile", "Why teams use Docker"], ["Read sample Dockerfile", "Explain image vs container", "List app dependencies"]),
    (78, "Docker Compose For Django", "Deployment And Production", "run app and database together", ["docker-compose.yml", "Services", "Environment variables", "Volumes", "Ports"], ["Design web and db services", "Explain ports", "Explain volumes"]),
    (79, "Static Files And WhiteNoise", "Deployment And Production", "serve static files safely", ["collectstatic", "STATIC_ROOT", "WhiteNoise", "Production static files"], ["Configure static settings", "Run collectstatic later", "Explain static handling"]),
    (80, "Deployment Checklist", "Deployment And Production", "prepare app for live hosting", ["DEBUG false", "SECRET_KEY", "ALLOWED_HOSTS", "HTTPS", "check --deploy"], ["Run through checklist", "Write production env notes", "Explain DEBUG risk"]),
    (81, "CI Basics With GitHub Actions", "Deployment And Production", "automate checks before deployment", ["What CI is", "GitHub Actions", "Test workflow", "Lint workflow"], ["Draft CI workflow", "List checks", "Explain why CI matters"]),
    (82, "Portfolio README", "Portfolio Project", "present your project professionally", ["Project summary", "Features", "Tech stack", "Screenshots", "Setup", "API docs"], ["Write README sections", "Add feature list", "Add interview explanation"]),
    (83, "Final Project Phase 1 Models", "Portfolio Project", "design final tiffin project database", ["Customer profile", "Menu item", "Order", "Subscription", "Payment"], ["Create final model plan", "Write relationships", "Explain each model"]),
    (84, "Final Project Phase 2 Web CRUD", "Portfolio Project", "build web pages for final project", ["Menu pages", "Order pages", "Admin workflow", "Customer workflow"], ["Build web CRUD checklist", "Test flows manually", "Write screenshots list"]),
    (85, "Final Project Phase 3 REST API", "Portfolio Project", "add API layer to final project", ["Serializers", "ViewSets", "Routers", "Permissions", "API docs"], ["Create API checklist", "Test endpoints", "Write API examples"]),
    (86, "Final Project Phase 4 Tests And Deployment", "Portfolio Project", "finish project for interviews", ["Model tests", "View tests", "API tests", "Deployment", "README polish"], ["Run tests", "Deploy app", "Record project demo notes"]),
    (87, "Python Interview Revision", "Interview And Job Prep", "revise Python interview answers", ["Variables", "Data types", "Functions", "OOP", "Errors", "Files"], ["Answer 20 Python questions", "Explain one project code file", "Practice out loud"]),
    (88, "Django Interview Revision", "Interview And Job Prep", "revise Django interview answers", ["Project vs app", "Models", "Migrations", "ORM", "Admin", "Auth", "Middleware"], ["Answer 20 Django questions", "Explain request flow", "Explain your models"]),
    (89, "SQL And DRF Interview Revision", "Interview And Job Prep", "revise database and API answers", ["SQL CRUD", "Joins", "Serializers", "ViewSets", "Permissions", "JWT"], ["Answer SQL questions", "Answer API questions", "Explain one endpoint"]),
    (90, "Resume Mock Interview And Job Application Plan", "Interview And Job Prep", "prepare to apply for jobs", ["Resume points", "Project explanation", "Mock interview", "Daily application plan", "Follow-up routine"], ["Write resume bullets", "Practice project pitch", "Create job application tracker"]),
]


PHASE_REFERENCES = {
    "Django": [
        ("Django 6.0 tutorial", "https://docs.djangoproject.com/en/6.0/intro/tutorial01/"),
        ("Django installation FAQ", "https://docs.djangoproject.com/en/6.0/faq/install/"),
    ],
    "Django REST Framework": [
        ("DRF serializers", "https://www.django-rest-framework.org/api-guide/serializers/"),
        ("DRF viewsets", "https://www.django-rest-framework.org/api-guide/viewsets/"),
        ("DRF routers", "https://www.django-rest-framework.org/api-guide/routers/"),
    ],
    "Deployment And Production": [
        ("Django deployment guide", "https://docs.djangoproject.com/en/6.0/howto/deployment/"),
        ("Django deployment checklist", "https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/"),
    ],
}


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", title.lower()).strip("_")
    return slug


def wrap_lines(items):
    return "\n".join(f"- {item}" for item in items)


def command_for(day: int, title: str, kind: str) -> str:
    slug = slugify(title)
    if kind == "example":
        return f".\\env\\Scripts\\python.exe .\\learning\\day_{day:02d}_{slug}.py"
    return f".\\env\\Scripts\\python.exe .\\learning\\day_{day:02d}_practice.py"


def django_command_block(day: int, phase: str) -> str:
    if phase == "Django":
        return textwrap.dedent(
            """
            ```powershell
            # When you reach Django days, install course packages first.
            .\\env\\Scripts\\python.exe -m pip install -r requirements_course.txt
            .\\env\\Scripts\\python.exe -m django --version
            ```
            """
        ).strip()
    if phase == "Django REST Framework":
        return textwrap.dedent(
            """
            ```python
            # Typical DRF shape:
            # model object -> serializer -> JSON response -> API client
            ```
            """
        ).strip()
    if phase == "SQL And Database":
        return textwrap.dedent(
            """
            ```sql
            SELECT customer, total
            FROM orders
            WHERE total >= 700
            ORDER BY total DESC;
            ```
            """
        ).strip()
    if phase == "Deployment And Production":
        return textwrap.dedent(
            """
            ```powershell
            # Production thinking starts with checks.
            .\\env\\Scripts\\python.exe manage.py check --deploy
            ```
            """
        ).strip()
    return textwrap.dedent(
        """
        ```python
        # Small change, run, observe, repeat.
        print("Build one small skill today")
        ```
        """
    ).strip()


def build_doc(day: int, title: str, phase: str, focus: str, learn: list[str], practice: list[str]) -> str:
    refs = PHASE_REFERENCES.get(phase, [])
    ref_block = ""
    if refs:
        ref_lines = "\n".join(f"- [{name}]({url})" for name, url in refs)
        ref_block = f"\n## Useful Official References\n\n{ref_lines}\n"

    return f"""# Day {day} - {title}

Today your goal is to **{focus}**.

This is part of the **{phase}** section of your Python/Django job-readiness
course.

## What You Learn Today

{wrap_lines(learn)}

## Important Idea

{django_command_block(day, phase)}

## Run The Day {day} Example

```powershell
{command_for(day, title, "example")}
```

## Practice Task

```powershell
{command_for(day, title, "practice")}
```

## Today Practice Checklist

{wrap_lines(practice)}
{ref_block}
## Interview Questions And Answers

Use this section for interview speaking practice. Keep the answer simple,
specific, and connected to your tiffin project.

---

### 🟦 QUESTION

## **What is {title}?**

### 🟩 ANSWER

**Definition**

{title} is today's topic. It helps you **{focus}**.

**Key Points**

{wrap_lines(learn[:3])}

**Interview Answer**

"{title} helps me {focus}. I practiced it with small examples and connected it
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

## **How will you practice Day {day}?**

### 🟩 ANSWER

**Practice Plan**

{wrap_lines(practice)}

**Interview Answer**

"I will run the example, complete the practice file, explain the code out loud,
and connect the idea to my tiffin project."

## Done Checklist

- [ ] I read this lesson.
- [ ] I ran the Day {day} example file.
- [ ] I completed the Day {day} practice file.
- [ ] I answered the interview questions out loud.
- [ ] I wrote one short note about what I learned.
"""


def build_example(day: int, title: str, phase: str, focus: str, learn: list[str]) -> str:
    return f'''print("Day {day}: {title}")
print("{'-' * (len(str(day)) + len(title) + 6)}")

lesson = {{
    "phase": "{phase}",
    "goal": "{focus}",
    "learn": {learn!r},
}}

print("Phase:", lesson["phase"])
print("Goal:", lesson["goal"])

print()
print("Today you learn")
print("---------------")

for item in lesson["learn"]:
    print("-", item)

print()
print("Small tiffin data example")
print("-------------------------")

orders = [
    {{"customer": "Rahul", "total": 250, "status": "paid"}},
    {{"customer": "Priya", "total": 900, "status": "paid"}},
    {{"customer": "Amit", "total": 400, "status": "pending"}},
]

paid_orders = [order for order in orders if order["status"] == "paid"]
high_value_orders = [order for order in orders if order["total"] >= 700]

revenue = 0

for order in paid_orders:
    revenue = revenue + order["total"]

print("Paid order count:", len(paid_orders))
print("High value order count:", len(high_value_orders))
print("Paid revenue:", revenue)

print()
print("Developer habit")
print("---------------")
print("Change one value, run again, and explain what changed.")
'''


def build_practice(day: int, title: str, phase: str, practice: list[str]) -> str:
    return f'''print("Day {day} Practice: {title}")
print("{'-' * (len(str(day)) + len(title) + 16)}")

practice_tasks = {practice!r}

print("Complete these tasks:")

for task in practice_tasks:
    print("-", task)

print()
print("Your work area")
print("--------------")

# TODO 1:
# Write notes, variables, functions, SQL, Django commands, or project changes
# for today's topic below this line.


# TODO 2:
# After completing the work, explain the topic out loud in 3 simple sentences.

print("When you finish, send your output or question to Codex for checking.")
'''


def build_course_index() -> str:
    phase_days: dict[str, list[tuple[int, str]]] = {}
    for day, title, phase, _focus, _learn, _practice in CURRICULUM:
        phase_days.setdefault(phase, []).append((day, title))

    lines = [
        "# Complete Python And Django Developer Course",
        "",
        "This course is built for your goal: **Python/Django developer job readiness**.",
        "",
        "Start at Day 1 and move one day at a time. Do not rush. The goal is to",
        "be able to explain and build, not just finish files.",
        "",
        "## How To Study Each Day",
        "",
        "1. Read the day file in `docs/learning`.",
        "2. Run the example file in `learning`.",
        "3. Complete the practice file.",
        "4. Read the interview questions out loud.",
        "5. Write one short note: what did I learn today?",
        "",
        "## Course Sections",
        "",
    ]

    for phase, days in phase_days.items():
        lines.append(f"### {phase}")
        lines.append("")
        for day, title in days:
            lines.append(f"- Day {day}: {title}")
        lines.append("")

    lines.extend(
        [
            "## Later Django Setup",
            "",
            "When you reach Day 46, install the course packages:",
            "",
            "```powershell",
            ".\\env\\Scripts\\python.exe -m pip install -r requirements_course.txt",
            ".\\env\\Scripts\\python.exe -m django --version",
            "```",
            "",
            "## Official References Used",
            "",
            "- [Django 6.0 tutorial](https://docs.djangoproject.com/en/6.0/intro/tutorial01/)",
            "- [Django installation FAQ](https://docs.djangoproject.com/en/6.0/faq/install/)",
            "- [Django deployment guide](https://docs.djangoproject.com/en/6.0/howto/deployment/)",
            "- [Django REST Framework serializers](https://www.django-rest-framework.org/api-guide/serializers/)",
            "- [Django REST Framework viewsets](https://www.django-rest-framework.org/api-guide/viewsets/)",
            "- [Django REST Framework routers](https://www.django-rest-framework.org/api-guide/routers/)",
        ]
    )
    return "\n".join(lines) + "\n"


def build_requirements() -> str:
    return """Django>=6.0,<6.1
djangorestframework
django-filter
djangorestframework-simplejwt
python-dotenv
psycopg[binary]
whitenoise
gunicorn
pytest
pytest-django
ruff
"""


def main() -> None:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    LEARNING_DIR.mkdir(parents=True, exist_ok=True)

    for day, title, phase, focus, learn, practice in CURRICULUM:
        doc_path = DOCS_DIR / f"DAY_{day:02d}.md"
        slug = slugify(title)
        example_path = LEARNING_DIR / f"day_{day:02d}_{slug}.py"
        practice_path = LEARNING_DIR / f"day_{day:02d}_practice.py"

        doc_path.write_text(
            build_doc(day, title, phase, focus, learn, practice),
            encoding="utf-8",
        )
        example_path.write_text(
            build_example(day, title, phase, focus, learn),
            encoding="utf-8",
        )
        practice_path.write_text(
            build_practice(day, title, phase, practice),
            encoding="utf-8",
        )

    (ROOT / "COURSE_INDEX.md").write_text(build_course_index(), encoding="utf-8")
    (ROOT / "requirements_course.txt").write_text(build_requirements(), encoding="utf-8")

    print("Generated Day 16 to Day 90 course files.")
    print("Created COURSE_INDEX.md and requirements_course.txt.")


if __name__ == "__main__":
    main()
