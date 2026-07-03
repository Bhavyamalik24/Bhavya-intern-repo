# Understanding Clean Code Principles

## Core Principles of Clean Code

### 1. Simplicity
Keep code as simple as possible, solve the problem in the most
straightforward way without adding unnecessary complexity. Simple code
is easier to test, debug, and maintain. If you find yourself writing
something clever, ask whether a simpler solution exists.

> "Make everything as simple as possible, but not simpler." — Albert Einstein

### 2. Readability
Code is read far more often than it is written. Readable code uses
meaningful variable and function names, clear structure, and logical
flow so that any developer (including your future self) can understand
it without needing the original author to explain it.

### 3. Maintainability
Maintainable code is structured so that future changes are easy to make
without breaking other parts of the system. This means avoiding tightly
coupled code, writing modular functions, and not relying on "magic"
numbers or undocumented assumptions that only the original author understands.

### 4. Consistency
Following consistent style guides, naming conventions, and patterns across
a codebase makes it feel like it was written by one person rather than many.
Consistency reduces cognitive load — once you learn the patterns in a
codebase, you can navigate and understand new parts quickly without relearning
different styles in different files.

### 5. Efficiency
Write performant, optimized code — but avoid premature optimization. Focus
first on making the code correct and readable, then optimize only the parts
that actually need it based on real performance data. Over-engineered
"optimizations" often reduce readability without measurable benefit.

---

## Example of Messy Code

```python
def c(a, b, l):
    x = []
    for i in range(len(l)):
        if l[i] > a and l[i] < b:
            x.append(l[i])
    r = 0
    for i in range(len(x)):
        r = r + x[i]
    if len(x) == 0:
        return 0
    return r / len(x)
```

### Why this is difficult to read
- **Meaningless names:** `c`, `a`, `b`, `l`, `x`, `r`, and `i` give no
  indication of what they represent. You have to trace the entire function
  just to understand what it does.
- **Manual index loops:** Using `range(len(l))` and accessing `l[i]` is
  unnecessarily verbose in Python — there are cleaner ways to iterate.
- **No docstring or comments:** There is no explanation of what the function
  does, what its parameters mean, or what it returns.
- **Logic split unnecessarily:** Filtering and summing are done in two
  separate loops when they could be combined more cleanly.
- **Poor structure:** The edge case (`len(x) == 0`) is handled at the end
  instead of being a clear guard clause at the top.

---

## Rewritten Clean Version

```python
def average_within_range(min_value: float, max_value: float, numbers: list) -> float:
    """
    Calculate the average of all numbers in a list that fall within
    a given range (exclusive of min and max boundaries).

    Args:
        min_value: The lower boundary (exclusive).
        max_value: The upper boundary (exclusive).
        numbers: A list of numeric values to filter and average.

    Returns:
        The average of the filtered numbers, or 0 if none fall in range.
    """
    values_in_range = [n for n in numbers if min_value < n < max_value]

    if not values_in_range:
        return 0

    return sum(values_in_range) / len(values_in_range)
```

### Why this is cleaner
- **Meaningful names:** `average_within_range`, `min_value`, `max_value`,
  `numbers`, and `values_in_range` all clearly describe what they represent.
- **Docstring:** The function's purpose, parameters, and return value are
  all documented.
- **List comprehension:** Filtering is done in one clean, readable line
  instead of a verbose loop.
- **Guard clause first:** The edge case is handled early and clearly before
  the main logic runs.
- **Type hints:** `float`, `list`, and `-> float` make the expected input
  and output types explicit without needing comments.
- **Built-in functions:** Using `sum()` and `len()` directly is more
  Pythonic and readable than manual accumulation.

---

## Key Takeaways
- Clean code is not about writing less code — it is about writing code
  that communicates its intent clearly
- Naming is one of the most powerful tools for readability — a well-named
  variable or function can eliminate the need for a comment entirely
- Consistency and simplicity together make a codebase feel professional
  and approachable, even to developers who are new to the project
- Maintainability is really about empathy — writing code that your future
  self or a teammate can work with confidently

  ---

## Code Formatting & Style Guides

### Research: Why is code formatting important?
Consistent code formatting makes a codebase feel unified and professional,
regardless of how many developers have worked on it. When everyone follows
the same style guide, code reviews become faster because reviewers can
focus on logic and functionality rather than debating whether to use single
or double quotes. Formatting tools like ESLint and Prettier remove
subjective style decisions entirely by enforcing rules automatically —
meaning developers never have to think about spacing or semicolons again,
they just write code and let the tools handle the rest.

The Airbnb JavaScript Style Guide is one of the most widely adopted style
guides in the industry. Key rules include:
- Use `const` by default, `let` when reassignment is needed, never `var`
- Always use semicolons
- Use single quotes for strings
- Use arrow functions for callbacks
- Always use strict equality (`===` instead of `==`)
- Use meaningful, descriptive variable names

### Tools Installed
- **ESLint** (by Microsoft) — installed via VS Code Extensions
- **Prettier - Code formatter** (by Prettier) — installed via VS Code Extensions

### Test File: Before Formatting
```javascript
const x=1
var y =2
function add(a,b){
return a+b
}
console.log(add(x,y))
```
![Code before formatting showing ESLint warnings and style issues](Screenshot-before-formatting.png)

### Test File: After Prettier & ESLint
```javascript
const x = 1;
const y = 2;
function add(a, b) {
  return a + b;
}
console.log(add(x, y));
```
![Code after Prettier and ESLint formatting applied](Screenshot-after-formatting.png)

### What issues did the linter and formatter detect?
- **Missing spaces** around operators (`x=1` → `x = 1`)
- **Missing semicolons** at the end of every statement
- **Missing spaces** after commas in function parameters (`add(a,b)` →
  `add(a, b)`)
- **Missing indentation** inside the function body
- **Use of `var`** — ESLint flagged this as a violation of the Airbnb
  style guide, suggesting `const` instead since `y` is never reassigned
- **Missing space** before the opening brace of the function (`){` → `) {`)

### Did formatting the code make it easier to read?
Yes — significantly. The before version looked rushed and inconsistent,
making it harder to scan quickly. The after version has clear, consistent
spacing, proper indentation, and explicit semicolons that make the
structure of the code immediately obvious. Even for a simple 6-line
function, the difference in readability was noticeable. In a larger
codebase with hundreds of files, consistent formatting like this would
make navigating and understanding unfamiliar code much faster.

### Key takeaway
Prettier handles formatting (spacing, semicolons, indentation) while ESLint
handles code quality (catching `var` usage, undefined variables, missing
returns). Used together, they act as an automated first line of code review
— catching style and quality issues before a human reviewer ever sees the
code. Setting these up early in a project saves significant time and
prevents style inconsistencies from accumulating over time.

---

## Naming Variables & Functions

### Research: Best Practices for Naming

**Variables:**
- Use descriptive, intention-revealing names (`userAge` not `a`)
- Use nouns for variables (`totalPrice`, `userName`, `isLoggedIn`)
- Boolean variables should read as yes/no questions (`isActive`,
  `hasPermission`, `canEdit`)
- Avoid abbreviations unless they are universally understood (`url`, `id`)
- Use camelCase for JavaScript variables and functions

**Functions:**
- Use verbs for functions since they perform actions (`calculateTotal`,
  `getUserData`, `sendEmail`)
- Function names should describe exactly what the function does —
  if you can't name it clearly, the function probably does too much
- Avoid vague names like `handle`, `process`, `doStuff`, or `update`
  without context

---

### ❌ Example of Poorly Named Code

```python
def proc(d, f, t):
    r = []
    for i in d:
        if i[f] == t:
            r.append(i)
    return r

data = [
    {"n": "Bhavya", "s": "active"},
    {"n": "Jeremy", "s": "inactive"},
    {"n": "Focus", "s": "active"},
]

res = proc(data, "s", "active")
print(res)
```

### Why this is poorly named
- `proc`, `d`, `f`, `t`, `r`, `i`, `n`, `s`, `res` — none of these
  reveal any intent or meaning
- You have to trace through the entire function and test data just to
  understand that it filters a list of users by a given field value
- `n` and `s` as dictionary keys are meaningless — what do they represent?
- If this code broke in production, debugging it would be painful because
  nothing is self-explanatory

---

### ✅ Refactored Clean Version

```python
def filter_records_by_field(records: list, field: str, target_value: str) -> list:
    """
    Filter a list of records, returning only those where the given
    field matches the target value.

    Args:
        records: List of dictionaries to filter.
        field: The dictionary key to filter by.
        target_value: The value to match against.

    Returns:
        A list of matching records.
    """
    return [record for record in records if record[field] == target_value]


users = [
    {"name": "Bhavya", "status": "active"},
    {"name": "Jeremy", "status": "inactive"},
    {"name": "Focus", "status": "active"},
]

active_users = filter_records_by_field(users, "status", "active")
print(active_users)
```

### How refactoring improved readability
- `filter_records_by_field` immediately tells you what the function does
  without reading a single line of its body
- `records`, `field`, and `target_value` clearly describe what each
  parameter represents
- `users` and `active_users` make the data's purpose obvious
- Dictionary keys `name` and `status` are self-documenting — no need
  to guess what `n` or `s` meant
- The list comprehension replaces the loop cleanly, and with meaningful
  variable names it reads almost like plain English:
  "return each record where record's field equals target value"

---

### 📝 Reflection

### What makes a good variable or function name?
A good name is specific, intention-revealing, and readable in context.
It should answer "what is this?" for a variable or "what does this do?"
for a function without requiring the reader to look elsewhere. The best
names make comments unnecessary — the code explains itself.

### What issues can arise from poorly named variables?
- **Debugging is slower** — you can't tell what a variable holds without
  tracing its entire history through the code
- **Onboarding takes longer** — new team members spend time decoding
  names instead of understanding logic
- **Bugs are harder to spot** — when nothing is named clearly, incorrect
  logic blends in with the surrounding noise
- **Refactoring is risky** — renaming `x` across a large codebase when
  you're not sure what `x` represents in every context is dangerous
- **Code reviews are slower** — reviewers have to understand the names
  before they can evaluate the logic

### How did refactoring improve readability?
The refactored version reads almost like a plain English description of
what the code does. `filter_records_by_field(users, "status", "active")`
explains itself completely — you know what goes in, what comes out, and
why, without reading the function body at all. The original version
required reading every line just to understand the basic concept.

---

## Writing Small, Focused Functions

### Research: Best Practices
- Each function should do **one thing and do it well** (Single
  Responsibility Principle)
- If you need to use "and" to describe what a function does, it probably
  does too much — split it
- Functions should be short enough to fit on one screen
- Small functions are easier to test, debug, reuse, and understand
- A well-named small function eliminates the need for comments explaining
  what a block of code does

---

### ❌ Example of a Large, Unfocused Function

```python
def process_order(order):
    # Validate order
    if not order.get("items"):
        print("Error: No items in order")
        return None
    if not order.get("customer_email"):
        print("Error: No customer email")
        return None
    total = 0
    for item in order["items"]:
        if item["quantity"] <= 0:
            print(f"Error: Invalid quantity for {item['name']}")
            return None
        total += item["price"] * item["quantity"]
    if order.get("discount"):
        if order["discount"] > 50:
            print("Error: Discount cannot exceed 50%")
            return None
        total = total * (1 - order["discount"] / 100)
    tax = total * 0.1
    total_with_tax = total + tax
    email_body = f"Dear customer, your order total is ${total_with_tax:.2f}"
    print(f"Sending email to {order['customer_email']}: {email_body}")
    receipt = {
        "customer": order["customer_email"],
        "total": total_with_tax,
        "tax": tax,
        "items": order["items"]
    }
    print(f"Receipt generated: {receipt}")
    return receipt
```

### Why this is problematic
- The function does at least five different things: validates the order,
  calculates the total, applies a discount, calculates tax, sends an
  email, and generates a receipt
- It is over 30 lines long and hard to scan
- Testing any single part (e.g. discount logic) requires running the
  entire function
- If the email sending breaks, the whole function fails
- Adding new functionality (e.g. a loyalty points system) means editing
  an already complex function and risking breaking other parts

---

### ✅ Refactored into Small, Focused Functions

```python
def validate_order(order: dict) -> bool:
    """Check that the order has required fields and valid quantities."""
    if not order.get("items"):
        print("Error: No items in order")
        return False
    if not order.get("customer_email"):
        print("Error: No customer email")
        return False
    for item in order["items"]:
        if item["quantity"] <= 0:
            print(f"Error: Invalid quantity for {item['name']}")
            return False
    return True


def calculate_subtotal(items: list) -> float:
    """Calculate the total price of all items before discount and tax."""
    return sum(item["price"] * item["quantity"] for item in items)


def apply_discount(subtotal: float, discount_percent: float) -> float:
    """Apply a percentage discount to the subtotal."""
    if discount_percent > 50:
        print("Error: Discount cannot exceed 50%")
        return subtotal
    return subtotal * (1 - discount_percent / 100)


def calculate_total_with_tax(subtotal: float, tax_rate: float = 0.1) -> tuple:
    """Calculate tax and return the final total with tax included."""
    tax = subtotal * tax_rate
    return subtotal + tax, tax


def send_order_confirmation(email: str, total: float) -> None:
    """Send an order confirmation email to the customer."""
    email_body = f"Dear customer, your order total is ${total:.2f}"
    print(f"Sending email to {email}: {email_body}")


def generate_receipt(order: dict, total: float, tax: float) -> dict:
    """Generate and return a receipt dictionary for the order."""
    receipt = {
        "customer": order["customer_email"],
        "total": total,
        "tax": tax,
        "items": order["items"]
    }
    print(f"Receipt generated: {receipt}")
    return receipt


def process_order(order: dict) -> dict | None:
    """
    Process a customer order by validating, calculating totals,
    sending confirmation, and generating a receipt.
    """
    if not validate_order(order):
        return None

    subtotal = calculate_subtotal(order["items"])

    if order.get("discount"):
        subtotal = apply_discount(subtotal, order["discount"])

    total, tax = calculate_total_with_tax(subtotal)
    send_order_confirmation(order["customer_email"], total)
    return generate_receipt(order, total, tax)
```

---

### 📝 Reflection

### Why is breaking down functions beneficial?
- **Easier to test:** Each small function can be tested independently
  you can test `apply_discount` without needing a full order object
- **Easier to debug:** When something breaks, the error points to a
  specific, small function rather than a 30-line monster
- **Easier to reuse:** `calculate_subtotal` or `send_order_confirmation`
  can be called from other parts of the codebase without duplicating logic
- **Easier to read:** `process_order` now reads like a clear summary of
  steps rather than a wall of mixed concerns
- **Easier to extend:** Adding loyalty points just means adding one new
  function and calling it in `process_order` — no risk of breaking
  existing logic

### How did refactoring improve the structure of the code?
The refactored `process_order` function now reads like a plain English
checklist of steps: validate, calculate, apply discount, add tax, send
email, generate receipt. Each step is a clearly named function that can
be understood, tested, and modified independently. The overall structure
is immediately obvious, a new developer could read `process_order` and
understand the full workflow in seconds, then dive into any individual
function only when needed.

---

## Avoiding Code Duplication (DRY Principle)

### Research: The DRY Principle
"Don't Repeat Yourself" (DRY) means that every piece of knowledge or
logic in a system should have a single, unambiguous representation.
When the same logic appears in multiple places, any change or bug fix
has to be made in every copy — and it's easy to miss one, introducing
inconsistencies. DRY code centralises logic so that a change only needs
to be made in one place.

---

### ❌ Example of Duplicated Code

```python
def send_welcome_email(user_email, user_name):
    subject = "Welcome to Focus Bear!"
    greeting = f"Hi {user_name},"
    body = "Thanks for signing up. We're excited to have you on board."
    footer = "The Focus Bear Team"
    message = f"{greeting}\n\n{body}\n\n{footer}"
    print(f"Sending to {user_email}:")
    print(f"Subject: {subject}")
    print(message)


def send_password_reset_email(user_email, user_name):
    subject = "Reset Your Focus Bear Password"
    greeting = f"Hi {user_name},"
    body = "Click the link below to reset your password."
    footer = "The Focus Bear Team"
    message = f"{greeting}\n\n{body}\n\n{footer}"
    print(f"Sending to {user_email}:")
    print(f"Subject: {subject}")
    print(message)


def send_cancellation_email(user_email, user_name):
    subject = "Sorry to See You Go"
    greeting = f"Hi {user_name},"
    body = "Your account has been cancelled. We hope to see you again."
    footer = "The Focus Bear Team"
    message = f"{greeting}\n\n{body}\n\n{footer}"
    print(f"Sending to {user_email}:")
    print(f"Subject: {subject}")
    print(message)
```

### Why this is problematic
- The email formatting logic (`greeting`, `footer`, `message` structure,
  and the two `print` statements) is identical in all three functions
- If the footer changes from "The Focus Bear Team" to "Focus Bear Support",
  it needs to be updated in three places and it's easy to miss one
- If the email sending mechanism changes (e.g. from `print` to an actual
  API call), every function needs to be updated individually
- Adding a fourth email type means copying and pasting the same structure
  again, making the problem worse

---

### ✅ Refactored DRY Version

```python
def send_email(user_email: str, user_name: str, subject: str, body: str) -> None:
    """
    Send a formatted email to a user.

    Args:
        user_email: The recipient's email address.
        user_name: The recipient's name for the greeting.
        subject: The email subject line.
        body: The main content of the email.
    """
    greeting = f"Hi {user_name},"
    footer = "The Focus Bear Team"
    message = f"{greeting}\n\n{body}\n\n{footer}"
    print(f"Sending to {user_email}:")
    print(f"Subject: {subject}")
    print(message)


def send_welcome_email(user_email: str, user_name: str) -> None:
    send_email(
        user_email,
        user_name,
        subject="Welcome to Focus Bear!",
        body="Thanks for signing up. We're excited to have you on board."
    )


def send_password_reset_email(user_email: str, user_name: str) -> None:
    send_email(
        user_email,
        user_name,
        subject="Reset Your Focus Bear Password",
        body="Click the link below to reset your password."
    )


def send_cancellation_email(user_email: str, user_name: str) -> None:
    send_email(
        user_email,
        user_name,
        subject="Sorry to See You Go",
        body="Your account has been cancelled. We hope to see you again."
    )
```

---

### 📝 Reflection

### What were the issues with duplicated code?
The original version repeated the same email formatting and sending logic
in every function. This meant:
- A change to the footer, greeting format, or sending mechanism required
  updating three separate places
- Each copy was a potential source of inconsistency, one function could
  accidentally end up with a different footer or format
- Adding new email types would continue to spread the duplication further
- The functions were harder to read because the unique part (the subject
  and body) was buried inside repeated boilerplate

### How did refactoring improve maintainability?
The refactored version centralises all email formatting and sending logic
in a single `send_email` function. Now:
- Changing the footer means updating one line in one place
- Changing the sending mechanism (e.g. integrating a real email API) only
  requires editing `send_email`, all other functions automatically benefit
- Adding a new email type is as simple as writing a two-line function that
  calls `send_email` with a new subject and body
- Each function now clearly shows only what makes it unique, the subject
  and body, making the intent of each email type immediately obvious

### Key takeaway
DRY is not just about reducing lines of code — it is about reducing the
number of places where a piece of knowledge or logic lives. Every
duplication is a future maintenance burden and a potential source of
inconsistency. When logic is centralised, the codebase becomes more
reliable, easier to change, and easier to understand.

---

## Refactoring Code for Simplicity

### Research: Common Refactoring Techniques
- **Extract Method:** Pull repeated or complex logic into its own function
- **Replace Temp with Query:** Instead of storing intermediate results in
  variables, call a function directly
- **Simplify Conditionals:** Replace complex if/else chains with guard
  clauses, dictionaries, or built-in functions
- **Remove Dead Code:** Delete unused variables, functions, and comments
  that no longer apply
- **Replace Magic Numbers:** Replace unexplained numbers with named constants
- **Flatten Nested Logic:** Reduce deeply nested if/else blocks by
  returning early or restructuring conditions

---

### ❌ Overly Complicated Code

```python
def get_user_discount(user):
    discount = 0
    if user is not None:
        if user.get("is_active") == True:
            if user.get("membership") is not None:
                if user["membership"] == "gold":
                    if user.get("years") is not None:
                        if user["years"] >= 3:
                            discount = 30
                        else:
                            discount = 20
                elif user["membership"] == "silver":
                    if user.get("years") is not None:
                        if user["years"] >= 3:
                            discount = 15
                        else:
                            discount = 10
                elif user["membership"] == "bronze":
                    discount = 5
                else:
                    discount = 0
            else:
                discount = 0
        else:
            discount = 0
    else:
        discount = 0
    return discount
```

### What made the original code complex?
- **Deeply nested conditionals:** Six levels of nesting make it extremely
  hard to follow the logic — you have to track every opening `if` to
  understand what each branch covers
- **Repeated `discount = 0`:** The default value is set in four separate
  places, which is redundant and error-prone
- **Verbose boolean check:** `== True` is unnecessary in Python —
  `if user.get("is_active")` is cleaner and equivalent
- **Repeated `user.get("years") is not None`:** The same check appears
  twice for different membership levels
- **No clear structure:** It is hard to see at a glance what the possible
  outcomes are — you have to trace every branch to build a mental model

---

### ✅ Refactored Simple Version

```python
# Discount table: (membership_tier, min_years) -> discount_percent
DISCOUNT_TABLE = {
    ("gold", 3): 30,
    ("gold", 0): 20,
    ("silver", 3): 15,
    ("silver", 0): 10,
    ("bronze", 0): 5,
}


def get_user_discount(user: dict) -> int:
    """
    Return the discount percentage for a given user based on their
    membership tier and years as a member.

    Args:
        user: A dictionary containing user details.

    Returns:
        An integer discount percentage (0 if not eligible).
    """
    if not user or not user.get("is_active"):
        return 0

    membership = user.get("membership")
    years = user.get("years", 0)

    if not membership:
        return 0

    min_years = 3 if years >= 3 else 0
    return DISCOUNT_TABLE.get((membership, min_years), 0)
```

---

### Reflection

### What made the original code complex?
The original code used deeply nested conditionals that made it almost
impossible to follow without tracing every branch. The same default value
(`discount = 0`) was set in four separate places, and the same `years`
check was duplicated for each membership tier. There was no clear overview
of what the possible outcomes were — you had to read the entire function
to understand even the simplest case.

### How did refactoring improve it?
The refactored version reduced the function from 30 lines to 10 by making
three key changes:

1. **Guard clauses first:** Invalid or ineligible users are handled
   immediately at the top with early returns, eliminating the need for
   deeply nested checks and reducing the entire "invalid user" case to
   two lines.

2. **Lookup table instead of conditionals:** The discount logic is now
   expressed as a dictionary (`DISCOUNT_TABLE`) that maps membership tier
   and years to a discount percentage. This makes all possible outcomes
   visible at a glance and eliminates the need for nested if/else entirely.

3. **Single years check:** Instead of repeating the years check for each
   membership tier, it is calculated once (`min_years = 3 if years >= 3
   else 0`) and reused.

The result reads cleanly from top to bottom — validate the user, get their
membership and years, look up their discount. Adding a new membership tier
now only requires adding one line to `DISCOUNT_TABLE` rather than adding
another nested if/else block.

### Key takeaway
Complexity often comes from conditionals that grow over time without
being restructured. Guard clauses, lookup tables, and early returns are
powerful tools for flattening nested logic into something linear and
readable. The goal of refactoring for simplicity is not to reduce line
count, it is to reduce the mental effort required to understand the code.

---

## Handling Errors & Edge Cases

### Research: Error Handling Strategies

**Guard Clauses**
Guard clauses are early return statements at the top of a function that
handle invalid inputs or edge cases immediately, before the main logic
runs. They flatten deeply nested code and make the "happy path" clear.

**Try/Except Blocks**
Wrap code that might fail (file reading, API calls, type conversions) in
try/except blocks to catch and handle exceptions gracefully rather than
crashing the program.

**Input Validation**
Check that inputs are of the expected type, within valid ranges, and not
None/empty before processing them.

**Meaningful Error Messages**
Raise errors or return messages that actually explain what went wrong and
what the valid input should benot just "error" or "invalid input."

**Edge Cases to Always Consider**
- None/null values
- Empty strings or lists
- Zero or negative numbers where only positive values make sense
- Division by zero
- Unexpected data types

---

### ❌ Original Code Without Error Handling

```python
def calculate_average_score(scores, passing_threshold):
    total = sum(scores)
    average = total / len(scores)
    passing = [s for s in scores if s >= passing_threshold]
    pass_rate = len(passing) / len(scores) * 100
    return {
        "average": round(average, 2),
        "pass_rate": round(pass_rate, 2),
        "highest": max(scores),
        "lowest": min(scores)
    }
```

### What was wrong with the original code?
- **No check for empty list:** If `scores` is empty, `len(scores)` is 0,
  causing a `ZeroDivisionError` on the very first line
- **No type validation:** If `scores` contains strings or None values,
  `sum(scores)` will throw a `TypeError`
- **No range validation:** Scores below 0 or above 100 are accepted
  without question, producing meaningless results silently
- **No threshold validation:** A negative `passing_threshold` or one
  above 100 would produce nonsensical pass rates without any warning
- **Silent failures:** None of these issues produce helpful error messages
  — the program just crashes with a cryptic Python traceback

---

### ✅ Refactored With Proper Error Handling

```python
def calculate_average_score(scores: list, passing_threshold: float) -> dict:
    """
    Calculate statistics for a list of scores.

    Args:
        scores: A list of numeric scores between 0 and 100.
        passing_threshold: The minimum score required to pass (0-100).

    Returns:
        A dictionary containing average, pass rate, highest, and lowest scores.

    Raises:
        TypeError: If scores is not a list or contains non-numeric values.
        ValueError: If scores is empty, any score is out of range, or
                    passing_threshold is invalid.
    """
    # Guard clause: validate input types
    if not isinstance(scores, list):
        raise TypeError(f"Expected a list of scores, got {type(scores).__name__}")

    if not isinstance(passing_threshold, (int, float)):
        raise TypeError(
            f"passing_threshold must be a number, got {type(passing_threshold).__name__}"
        )

    # Guard clause: validate list is not empty
    if not scores:
        raise ValueError("scores list cannot be empty")

    # Guard clause: validate all scores are numeric and in range
    for i, score in enumerate(scores):
        if not isinstance(score, (int, float)):
            raise TypeError(
                f"Score at index {i} must be a number, got {type(score).__name__}"
            )
        if not 0 <= score <= 100:
            raise ValueError(
                f"Score at index {i} is {score} — scores must be between 0 and 100"
            )

    # Guard clause: validate passing threshold is in range
    if not 0 <= passing_threshold <= 100:
        raise ValueError(
            f"passing_threshold must be between 0 and 100, got {passing_threshold}"
        )

    # Main logic — only runs if all inputs are valid
    total = sum(scores)
    average = total / len(scores)
    passing = [s for s in scores if s >= passing_threshold]
    pass_rate = len(passing) / len(scores) * 100

    return {
        "average": round(average, 2),
        "pass_rate": round(pass_rate, 2),
        "highest": max(scores),
        "lowest": min(scores)
    }


# Example usage with error handling
if __name__ == "__main__":
    try:
        result = calculate_average_score([85, 92, 78, 45, 60], passing_threshold=70)
        print(result)
    except (TypeError, ValueError) as e:
        print(f"Could not calculate scores: {e}")
```

---

### 📝 Reflection

### What was the issue with the original code?
The original function assumed perfect inputs every time. In a real
application, data rarely arrives perfectly formatted — users submit
empty forms, APIs return unexpected types, and edge cases like empty
lists are common. The original code would crash silently with a
cryptic Python error rather than explaining what went wrong, making
debugging unnecessarily difficult.

### How does handling errors improve reliability?
Proper error handling makes code significantly more reliable in three ways:

1. **Fail fast and clearly:** Guard clauses catch invalid inputs at the
   entry point and immediately raise a descriptive error. This prevents
   bad data from silently propagating through the system and causing a
   confusing crash somewhere deeper in the code.

2. **Protect the happy path:** By handling all edge cases at the top of
   the function, the main logic at the bottom is clean and readable —
   you can trust that by the time you reach `total = sum(scores)`, the
   inputs are guaranteed to be valid.

3. **Better user and developer experience:** Meaningful error messages
   like "Score at index 2 is -5 — scores must be between 0 and 100"
   make it immediately obvious what went wrong and how to fix it,
   rather than leaving developers guessing from a generic traceback.

### Key takeaway
Robust code does not just handle the expected case — it anticipates what
could go wrong and fails gracefully with clear, actionable messages.
Guard clauses are the most effective tool for this: handle the invalid
cases first, then write the main logic with confidence that inputs are
safe to use.
