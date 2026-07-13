# Using .env to Keep Database Credentials Secret

## What I Did

- Installed `python-dotenv` to load environment variables from a `.env` file
- Created a `.env` file storing PostgreSQL database credentials securely
- Wrote `env_credentials_demo.py` to load credentials using `python-dotenv`
  and demonstrate a secure database connection
- Added `.env` to `.gitignore` to ensure credentials are never committed
  to version control
- Verified that `.env` does not appear in `git status` after fixing the
  `.gitignore` line endings issue

### How it works

```python
import os
from dotenv import load_dotenv

# Load all variables from .env into the environment
load_dotenv()

# Access credentials safely
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_port = os.getenv("DB_PORT")
```

### .env file structure (never committed to GitHub)
```
DB_HOST=localhost
DB_NAME=focusbear
DB_USER=analyst
DB_PASSWORD=your_password_here
DB_PORT=5432
```

### .gitignore entries added
```
focusbear-env/
.env
```

---

## Reflection

### Why is it more secure to use a .env file for database credentials?
Hardcoding credentials directly in a Python script is dangerous for
several reasons:

- **Version control exposure:** If the script is committed to GitHub,
  the credentials become permanently visible in the commit history —
  even if you delete them later, they remain in past commits
- **Accidental sharing:** Sharing a script file, screenshot, or code
  review inadvertently exposes the credentials to anyone who sees it
- **Team access control:** Hardcoded credentials give everyone with
  repo access the same credentials, making it impossible to revoke
  access for one person without changing the password for everyone

Using a `.env` file solves all of these:
- The `.env` file is listed in `.gitignore` so it is never committed
- Each developer has their own local `.env` with their own credentials
- The script itself contains no sensitive information and can be safely
  shared, reviewed, and committed
- In production, environment variables are injected by the server or
  deployment platform rather than stored in any file at all

For Focus Bear specifically, this means that database credentials for
the production PostgreSQL instance are never at risk of being exposed
through the intern repo, even if the repo is public.

### How can python-dotenv simplify managing environment variables?
Without `python-dotenv`, you would have to manually set environment
variables in your terminal before running a script:

```bash
# Without python-dotenv - tedious and easy to forget
export DB_HOST=localhost
export DB_PASSWORD=your_password
python my_script.py
```

With `python-dotenv`, you just call `load_dotenv()` at the top of your
script and it automatically reads all variables from the `.env` file —
no manual setup required each time. This makes the development workflow
much smoother:

- New team members just create their own `.env` file from a
  `.env.example` template and are immediately set up
- Switching between development and production environments is as simple
  as having different `.env` files
- All credential management is centralised in one file rather than
  scattered across terminal sessions and shell configuration files

In a Jupyter Notebook context specifically, `load_dotenv()` can be
called in the first cell, making all credentials available to every
subsequent cell without ever writing a password in the notebook itself.
