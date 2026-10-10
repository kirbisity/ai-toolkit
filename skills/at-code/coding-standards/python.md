---
name: pragmatic-python-conventions
description: Pragmatic Python coding conventions emphasizing clarity, minimal abstractions, and observed project patterns
---

# Pragmatic Python Coding Conventions

This guide captures pragmatic coding conventions observed in exploratory and production Python projects. The focus is on clarity, consistency, and matching existing patterns—not on strict adherence to arbitrary rules.

## Core Principles

1. **Code clarity over cleverness**: Self-documenting code beats verbose comments; use simple syntax over advanced features
2. **Minimal comments**: Only explain non-obvious intent or workarounds; omit comments for self-explanatory code
3. **Descriptive naming**: Method and variable names should explain intent; make comments unnecessary
4. **Reusability first**: Write functions that can be used in multiple contexts; prefer general-purpose solutions
5. **Simple syntax**: Avoid advanced Python features (comprehensions over 1 line, decorators, metaclasses); prioritize readability
6. **Practical error handling**: Return sensible defaults; don't swallow errors silently
7. **Keep it focused**: Functions should do one thing well

## Python File Structure

### Preamble
```python
#!/usr/bin/python

import os
import json
# ... standard library imports

import requests
# ... third-party imports

from local_module import LocalClass
# ... local imports
```

- Shebang at top: `#!/usr/bin/python`
- Standard library imports first, then third-party, then local
- Blank line between import groups

### Organization
- Module-level constants and configuration at the top
- Classes and functions grouped by logical purpose
- Mark sections with comments: `# API Functions`, `# Data Processing`, `# Utilities`
- Script-level code at bottom, wrapped in `if __name__ == "__main__":`

## Naming Conventions

| Element | Style | Example |
|---------|-------|---------|
| Functions | `snake_case` | `process_data()`, `is_valid()` |
| Variables | `snake_case` | `api_key`, `response_data` |
| Classes | `PascalCase` | `ChatGPTCaller`, `DataProcessor` |
| Constants | `UPPER_SNAKE_CASE` or `snake_case` | `API_ENDPOINT` or `default_timeout` |
| Privates | `_leading_underscore` | `_internal_method()` |

**Guidelines:**
- **Prioritize descriptive naming**: Names should explain intent; avoid abbreviations (use `user_count` not `uc`, `response_data` not `resp`)
- **Use verb-noun for functions**: `get_data()`, `process_query()`, `is_valid()`, `has_permission()`, `validate_input()`
- **Use noun for variables**: `response`, `config`, `max_retries`, `user_list`, `processed_data`
- **Make names self-documenting**: A clear name eliminates the need for a comment
  - `process_user_data()` → no comment needed
  - `calculate_avg()` → needs comment "calculate rolling average"; better: `calculate_rolling_average()`
  - `filter_items()` → needs comment; better: `filter_items_by_date()` or `filter_expired_items()`

## Type Hints

Include type hints on function signatures where possible:

```python
def search(self, query: str, limit: int = 10) -> dict:
    pass

def validate(self) -> bool:
    pass

def process_items(items: list[dict]) -> None:
    pass
```

**When to use:**
- Public methods and API interfaces (required)
- External service integrations (strongly recommended)
- Complex functions with multiple parameters (recommended)
- Simple internal utilities (optional)

## Docstrings

### Classes
One-line description of purpose:
```python
class APIClient:
    """Makes HTTP requests to an external API with retry logic."""
```

### Functions/Methods
Include summary, Args, and Returns:
```python
def process_data(input_file: str, output_dir: str, limit: int = 0) -> str:
    """Process input file and write results to output directory.
    
    Args:
        input_file (str): Path to input CSV file.
        output_dir (str): Directory to write processed files.
        limit (int): Max items to process; 0 means all.
    
    Returns:
        str: Path to output file, or empty string on error.
    """
```

**Docstring style:**
- Use triple quotes (""")
- One-line summary, then blank line, then details
- Args section with parameter name, type, and description
- Returns section with type and description
- Only document public methods; skip obvious internal helpers

## Comments

### Minimal Comments Philosophy
**Goal: Code should be self-documenting through clear naming and structure.** Only add comments for:
- Non-obvious intent or business logic
- Important constraints or workarounds
- Why something is done a certain way (not how)

**Default: Write no comment.** Add one only if the reader wouldn't understand without it.

### When to Comment
Comments explain **WHY**, not WHAT. Prefer descriptive naming to avoid needing comments:

```python
# ✗ Bad: Comment needed because name is unclear
# Retry with exponential backoff
for attempt in range(max_retries):
    time.sleep(2 ** attempt)

# ✓ Better: Descriptive naming, minimal comment
# Handle temporary API rate limits with backoff
for attempt in range(max_retries):
    time.sleep(2 ** attempt)

# ✓ Best: Self-documenting through naming (prefer this)
retry_attempts = 0
while retry_attempts < max_retries:
    try:
        return make_request()
    except RateLimitError:
        retry_attempts += 1
        time.sleep(2 ** retry_attempts)  # Exponential backoff
```

**Good comment examples:**
```python
# Cache results to avoid repeated API calls (why)
# Only process first 100 items due to memory constraints (constraint)
# Use string comparison, not numeric (important for correctness)
```

**Bad comment examples (avoid):**
```python
# Loop 5 times (what - obvious from code)
# Get the user data (what - obvious from function name)
# Check if valid (what - obvious from is_valid() name)
```

### Section Comments
Mark logical sections with comments:
```python
# API Communication
def make_request(self, url: str):
    pass

# Data Parsing
def parse_response(self, data: dict):
    pass

# Validation
def is_valid(self):
    pass
```

### Procedural Steps
Number steps in procedures:
```python
def run_pipeline(self):
    # Step 1: Fetch data from source
    data = self.fetch()
    
    # Step 2: Clean and transform
    data = self.clean(data)
    
    # Step 3: Save results
    self.save(data)
```

### Guidelines
- Omit comments if code is self-explanatory
- Use inline comments sparingly
- Keep comments up-to-date when code changes
- Remove commented-out code before commit

## Simple Syntax & Readability

### Avoid Advanced Python Features
Prefer clarity and readability over cleverness. Use simple syntax that any Python developer can understand instantly.

**❌ Avoid (too clever):**
```python
# List comprehension harder to read than loop
result = [x * 2 for x in items if x > 10 and isinstance(x, int)]

# Walrus operator confuses some readers
if (data := fetch_data()) and len(data) > 0:
    process(data)

# Decorators and metaclasses add complexity
@cached_property
@retry(max_attempts=3)
def expensive_operation(self):
    pass

# f-string with complex expressions
msg = f"Status: {status.upper() if status else 'unknown'}"
```

**✓ Prefer (simple and clear):**
```python
# Loop is immediately understandable
result = []
for x in items:
    if x > 10 and isinstance(x, int):
        result.append(x * 2)

# Clear assignment and condition
data = fetch_data()
if data and len(data) > 0:
    process(data)

# Simple methods instead of decorators
def get_expensive_operation(self):
    if self._cached_result is None:
        self._cached_result = self._compute()
    return self._cached_result

# Simple string formatting
status_text = status.upper() if status else 'unknown'
msg = f"Status: {status_text}"
```

**Simple syntax guidelines:**
- Use loops instead of multi-line comprehensions
- Use `if x:` instead of walrus operators
- Avoid decorators; use methods instead
- Use simple variable names in f-strings
- Avoid lambda unless for `.map()` or `.filter()`
- Use explicit if/else over ternary for complex conditions
- Use plain functions over `functools` utilities for simple cases
- Avoid type annotations beyond function signatures unless they add clarity

### Why Simple Over Advanced

1. **Other developers understand it**: No need to look up syntax
2. **Easier to debug**: Plain loops show what's happening
3. **Less magical**: No hidden side effects
4. **Maintains consistency**: Complex code varies more
5. **Future-proofs code**: Simple code withstands refactoring

## Error Handling

### API & External Calls
Catch broad exceptions, return sensible defaults:
```python
def make_request(self, query: str) -> dict:
    try:
        response = requests.get(self.endpoint, params={"q": query})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Request failed: {e}")
        return None

def search(self, query: str) -> list:
    try:
        return self.api.search(query)
    except Exception:
        return []
```

### Validation
Return False for validation checks:
```python
def is_api_key_valid(self) -> bool:
    try:
        # Test request
        self.api.validate()
        return True
    except Exception:
        return False
```

### Initialization
Raise exceptions for required configuration:
```python
def __init__(self, api_key: str = None):
    if api_key is None:
        if "API_KEY" not in os.environ:
            raise Exception("API_KEY environment variable required")
        api_key = os.environ["API_KEY"]
    self.api_key = api_key
```

### Guidelines
- Don't swallow exceptions silently
- Log or print errors for debugging
- Return None or empty collections, not raising in production calls
- Validate configuration early, in __init__
- Use specific exception types where possible, broad catches for external APIs

## Classes & Methods

### Class Structure
```python
class DataProcessor:
    """Processes and transforms data files."""
    
    # Class constants
    DIR_INPUT = 'data/input'
    DIR_OUTPUT = 'data/output'
    DEFAULT_ENCODING = 'utf-8'
    
    def __init__(self, config: dict = None):
        """Initialize processor with optional configuration."""
        self.config = config or {}
    
    # Utility methods
    @staticmethod
    def read_file(path: str) -> str:
        with open(path, 'r') as f:
            return f.read()
    
    # Instance methods
    def process(self, data: dict) -> dict:
        pass
```

### Patterns
- Class constants at the top (configuration, paths, defaults)
- Use static methods for utilities that don't need instance state
- Empty `__init__` is acceptable: `def __init__(self): pass`
- Keep methods focused; break large methods into smaller ones
- Suffix validation methods: `is_valid()`, `has_key()`, `can_process()`

## Functions

### Keep Them Focused
```python
# ✓ Good: Single responsibility
def fetch_data(url: str) -> dict:
    return requests.get(url).json()

def validate_response(data: dict) -> bool:
    return "id" in data and "name" in data

def save_to_file(data: dict, path: str) -> None:
    with open(path, 'w') as f:
        json.dump(data, f)
```

### Parameters & Defaults
```python
def process(input_file: str, output_dir: str = "output", 
            limit: int = 0, retry: int = 3) -> str:
    """Process file with optional parameters."""
    pass
```

**Guidelines:**
- 3-4 parameters is comfortable; refactor if more than 5
- Use defaults for optional behavior
- Accept collections for flexibility: `items: list` instead of `item1, item2`
- Return single values or None, use tuples for multiple returns

### Conditional Returns
Simple logic can use inline returns:
```python
def validate(self, data):
    if not data:
        return False
    if "error" in data:
        return False
    return True
```

## Reusability

### Design for Multiple Contexts
Write functions that can be reused in different situations, not just the current task.

**❌ Single-purpose (not reusable):**
```python
def generate_user_report(user_id: int) -> str:
    """Generate a report specifically for users."""
    user = get_user(user_id)
    return f"User: {user['name']}, Email: {user['email']}"
```

**✓ Reusable (works for different data):**
```python
def format_person_details(person: dict) -> str:
    """Format a person's details as a string."""
    name = person.get('name', 'Unknown')
    email = person.get('email', 'No email')
    return f"Person: {name}, Email: {email}"

# Can be used for users, contacts, employees, etc.
```

**❌ Tightly coupled (not reusable):**
```python
def fetch_and_save_user_data():
    """Fetch user data and save to 'output/users.json'."""
    data = requests.get('http://api.example.com/users').json()
    with open('output/users.json', 'w') as f:
        json.dump(data, f)
```

**✓ Reusable (configurable):**
```python
def fetch_data(url: str) -> dict:
    """Fetch JSON data from URL."""
    return requests.get(url).json()

def save_to_file(data: dict, path: str) -> None:
    """Save data to JSON file."""
    with open(path, 'w') as f:
        json.dump(data, f)

# Can be used for any data and any path
data = fetch_data('http://api.example.com/users')
save_to_file(data, 'output/users.json')
```

**Reusability guidelines:**
- Accept data/paths as parameters instead of hardcoding
- Don't mix I/O with logic (separate concerns)
- Use general names: `filter_data()` instead of `filter_users()`
- Return simple types (dict, list) not custom objects when possible
- Make helper functions work independently, not just within a class
- Avoid assuming data structure (use `.get()` instead of direct access)

### Benefits of Reusable Code

1. **Less duplication**: One function serves multiple purposes
2. **Easier testing**: Can test in isolation
3. **Easier maintenance**: Changes in one place
4. **Flexible**: Works in contexts you didn't anticipate
5. **Cleaner code**: Less special-case logic

## Data Processing Patterns

### Reading & Processing Data
```python
@staticmethod
def read_data(directory: str, columns: list) -> pd.DataFrame:
    """Read CSV files from directory into single DataFrame."""
    dfs = []
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            df = pd.read_csv(os.path.join(directory, filename), usecols=columns)
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

@staticmethod
def filter_by_date(df: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
    """Filter DataFrame by date range."""
    start_date = pd.to_datetime(start)
    end_date = pd.to_datetime(end)
    return df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
```

## Script-Level Code

### Module as Script & Import
```python
def main():
    """Main execution function."""
    config = load_config()
    processor = DataProcessor(config)
    processor.run()

if __name__ == "__main__":
    main()
```

### Configuration & Constants
```python
# File paths
INPUT_FILE = "input/data.csv"
OUTPUT_DIR = "output"
TEMP_DIR = "temp"

# Configuration
DEFAULT_TIMEOUT = 10
MAX_RETRIES = 5
BATCH_SIZE = 100

# Initialize and run
if __name__ == "__main__":
    with open(INPUT_FILE, 'r') as f:
        data = json.load(f)
```

## Shell Scripts

```bash
#!/bin/bash

# Set configuration
export API_KEY="your-key-here"
export LOG_LEVEL="INFO"

# Run Python script
python3 process_data.py --input data.csv --output output/
```

**Guidelines:**
- Comment environment variable setup
- Export variables before calling Python
- Use python3 explicitly
- Keep scripts simple; complex logic in Python

## What to Avoid

| Avoid | Reason |
|-------|--------|
| Helper utilities for single-use code | Creates unnecessary indirection |
| Premature abstraction | Wait until you see the pattern 3+ times |
| Over-commenting | Self-documenting code is clearer; use descriptive names instead |
| Comments explaining WHAT code does | Code should be self-explanatory; only comment WHY |
| Advanced syntax (walrus, comprehensions > 1 line) | Reduces readability; prioritize clarity |
| Decorators, metaclasses for simple cases | Use plain methods/functions instead |
| List comprehensions > 1 line | Use loops; they're more readable |
| Nested if/else > 3 levels | Use early returns to flatten |
| Bare `except:` blocks | Specifically catch expected exceptions |
| Star imports `from x import *` | Pollutes namespace; hide dependencies |
| Magic numbers in code | Use named constants instead |
| Unused imports | Clean them up; be explicit about dependencies |
| Generic exception catching at module level | Let errors propagate from scripts |
| Inconsistent naming within file | Stick to conventions; maintain symmetry |
| Tightly coupled code (hardcoded paths, IDs) | Design for reuse; accept as parameters |
| Single-purpose functions (only work for one task) | Write general-purpose functions |

## Review Checklist

Before submitting code:

**Naming & Clarity:**
- [ ] **Naming**: Descriptive and self-documenting; avoid abbreviations
- [ ] **Method names**: Clear and explain intent (e.g., `filter_expired_items()` not `filter_items()`)
- [ ] **Type hints**: Included on public/API methods

**Documentation:**
- [ ] **Docstrings**: Present for classes/functions; includes Args/Returns
- [ ] **Comments**: Minimal; only explain non-obvious intent or constraints
- [ ] **No redundant comments**: Code is self-explanatory; comments add value beyond the name

**Code Quality:**
- [ ] **Syntax**: Simple and readable; no advanced Python features
- [ ] **Loops over comprehensions**: Multi-line comprehensions replaced with explicit loops
- [ ] **Reusability**: Functions work in multiple contexts, not just current task
- [ ] **Error handling**: Returns None/empty, prints errors, doesn't swallow silently
- [ ] **Functions**: Focused on single responsibility; under 50-100 lines
- [ ] **No hardcoding**: Paths, IDs, values passed as parameters

**Organization:**
- [ ] **Imports**: Removed unused; organized (stdlib, third-party, local)
- [ ] **Consistency**: Matches similar code in repo and same module
- [ ] **Style**: No accidental whitespace; focused changes only

## Git Commit Messages

Keep commit messages brief and focused:
```
Fixed API timeout handling in retry loop
Added market data filtering utilities
Updated configuration loading
```

**Guidelines:**
- One-line summary (50 chars or less)
- Capitalize first word
- Use imperative mood when possible: "Add" not "Added"
- Detailed explanation in body if needed (separate by blank line)
- Reference issues if applicable: "Fixes #123"

## When in Doubt

1. **Look at similar code**: Find comparable patterns in the same project
2. **Match the module style**: If it's in a file, follow that file's conventions
3. **Keep it minimal**: Simpler is better; don't over-engineer
4. **Prefer readability**: Make intent clear to someone reading the code cold
5. **Test it works**: Verify changes work in context before committing
