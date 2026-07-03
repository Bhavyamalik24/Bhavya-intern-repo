# 🔍 Identifying & Fixing Code Smells

## What are Code Smells?
Code smells are patterns in code that indicate deeper problems with
design, readability, or maintainability. They don't necessarily cause
bugs immediately, but they make code harder to understand, modify, and
debug over time.

---

## 1. Magic Numbers & Strings

### ❌ Before
```python
def calculate_final_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"

discount = price * 0.15
max_retries = 3
```

### ✅ After
```python
GRADE_A_THRESHOLD = 90
GRADE_B_THRESHOLD = 80
PASSING_THRESHOLD = 50
DISCOUNT_RATE = 0.15
MAX_RETRIES = 3

def calculate_final_grade(score):
    if score >= GRADE_A_THRESHOLD:
        return "A"
    elif score >= GRADE_B_THRESHOLD:
        return "B"
    elif score >= PASSING_THRESHOLD:
        return "Pass"
    else:
        return "Fail"

discount = price * DISCOUNT_RATE
```

**Why:** Named constants make the meaning of numbers obvious and allow
changes in one place rather than hunting through the entire codebase.

---

## 2. Long Functions

### ❌ Before
```python
def handle_user_registration(data):
    # Validate
    if not data.get("email") or "@" not in data["email"]:
        return "Invalid email"
    if not data.get("password") or len(data["password"]) < 8:
        return "Password too short"
    # Create user
    user = {"email": data["email"], "password": hash(data["password"])}
    # Save to database
    db.insert("users", user)
    # Send welcome email
    subject = "Welcome!"
    body = f"Hi, thanks for joining us."
    send_email(data["email"], subject, body)
    # Log activity
    log.info(f"New user registered: {data['email']}")
    return "Registration successful"
```

### ✅ After
```python
def validate_registration_data(data: dict) -> str | None:
    if not data.get("email") or "@" not in data["email"]:
        return "Invalid email"
    if not data.get("password") or len(data["password"]) < 8:
        return "Password too short"
    return None

def create_user(data: dict) -> dict:
    return {"email": data["email"], "password": hash(data["password"])}

def send_welcome_email(email: str) -> None:
    send_email(email, "Welcome!", "Hi, thanks for joining us.")

def handle_user_registration(data: dict) -> str:
    error = validate_registration_data(data)
    if error:
        return error
    user = create_user(data)
    db.insert("users", user)
    send_welcome_email(data["email"])
    log.info(f"New user registered: {data['email']}")
    return "Registration successful"
```

---

## 3. Duplicate Code

### ❌ Before
```python
def get_admin_report():
    conn = db.connect("production")
    data = conn.query("SELECT * FROM users WHERE role = 'admin'")
    conn.close()
    return data

def get_customer_report():
    conn = db.connect("production")
    data = conn.query("SELECT * FROM users WHERE role = 'customer'")
    conn.close()
    return data
```

### ✅ After
```python
def get_users_by_role(role: str) -> list:
    conn = db.connect("production")
    data = conn.query(f"SELECT * FROM users WHERE role = '{role}'")
    conn.close()
    return data

def get_admin_report():
    return get_users_by_role("admin")

def get_customer_report():
    return get_users_by_role("customer")
```

---

## 4. Large Classes (God Objects)

### ❌ Before
```python
class App:
    def register_user(self, data): ...
    def login_user(self, email, password): ...
    def send_email(self, to, subject, body): ...
    def generate_invoice(self, order): ...
    def process_payment(self, card, amount): ...
    def generate_report(self, date_range): ...
    def backup_database(self): ...
    def resize_image(self, image, size): ...
```

### ✅ After
```python
class AuthService:
    def register_user(self, data): ...
    def login_user(self, email, password): ...

class EmailService:
    def send_email(self, to, subject, body): ...

class BillingService:
    def generate_invoice(self, order): ...
    def process_payment(self, card, amount): ...

class ReportingService:
    def generate_report(self, date_range): ...

class DatabaseService:
    def backup_database(self): ...

class ImageService:
    def resize_image(self, image, size): ...
```

**Why:** Each class now has one clear responsibility. Changes to billing
logic don't risk breaking email or authentication code.

---

## 5. Deeply Nested Conditionals

### ❌ Before
```python
def process_payment(user, payment):
    if user:
        if user.is_active:
            if payment:
                if payment.amount > 0:
                    if payment.method in ["card", "paypal"]:
                        return charge(user, payment)
                    else:
                        return "Invalid payment method"
                else:
                    return "Invalid amount"
            else:
                return "No payment provided"
        else:
            return "User inactive"
    else:
        return "No user provided"
```

### ✅ After
```python
def process_payment(user, payment):
    if not user:
        return "No user provided"
    if not user.is_active:
        return "User inactive"
    if not payment:
        return "No payment provided"
    if payment.amount <= 0:
        return "Invalid amount"
    if payment.method not in ["card", "paypal"]:
        return "Invalid payment method"
    return charge(user, payment)
```

---

## 6. Commented-Out Code

### ❌ Before
```python
def calculate_total(items):
    total = 0
    for item in items:
        total += item.price
    # total = total * 1.1  # old tax calculation
    # if total > 1000:     # old bulk discount
    #     total *= 0.9
    return total
```

### ✅ After
```python
def calculate_total(items: list) -> float:
    """Calculate the total price of all items."""
    return sum(item.price for item in items)
```

**Why:** Commented-out code clutters the file and confuses readers.
Git history preserves old code — there is no need to keep it as comments.

---

## 7. Inconsistent Naming

### ❌ Before
```python
def get_usr_data(ID):
    uData = db.find(ID)
    usr_name = uData["name"]
    EmailAddress = uData["email"]
    return usr_name, EmailAddress
```

### ✅ After
```python
def get_user_data(user_id: int) -> tuple:
    user_data = db.find(user_id)
    user_name = user_data["name"]
    user_email = user_data["email"]
    return user_name, user_email
```

**Why:** Consistent snake_case naming, full words instead of
abbreviations, and descriptive names make the code immediately readable.

---

## 📝 Reflection

### What code smells did you find?
All seven code smells were present in the examples above — magic numbers,
long functions, duplicate code, god objects, deeply nested conditionals,
commented-out code, and inconsistent naming. In real projects these
rarely appear in isolation; a long function often also contains magic
numbers, duplicate logic, and deeply nested conditionals all at once,
compounding the readability problem.

### How did refactoring improve readability and maintainability?
Each refactor made the code's intent clearer and its structure more
predictable:
- Magic numbers became self-documenting constants
- Long functions became readable step-by-step workflows
- Duplicate code became a single reusable function
- The god object became focused, single-responsibility services
- Nested conditionals became a flat, scannable list of guard clauses
- Commented-out code was removed, leaving only working code
- Inconsistent naming became uniform and descriptive throughout

### How can avoiding code smells make future debugging easier?
Code smells make debugging harder because they obscure intent. When
a bug occurs in deeply nested conditionals, you have to trace multiple
levels of logic simultaneously. When magic numbers appear, you don't
know what `0.15` represents without context. When functions are long,
the bug could be anywhere in 50 lines of mixed concerns.

Clean, smell-free code narrows the search area immediately — a bug in
discount calculation goes straight to the `DISCOUNT_RATE` constant or
the `apply_discount` function, not somewhere in a 100-line monolith.
This makes debugging faster, less stressful, and less likely to
introduce new bugs while fixing existing ones.
