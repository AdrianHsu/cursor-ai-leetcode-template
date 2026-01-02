# String Operation Template

## Basic Operations
```python
# Common string methods
s = "hello"
s[i]                    # Access character
s[i:j]                  # Slice
s[::-1]                 # Reverse
s.split()               # Split by whitespace
s.split(',')            # Split by delimiter
','.join(list)          # Join list to string
s.replace(old, new)     # Replace substring
s.strip()               # Remove whitespace
s.lower(), s.upper()    # Case conversion
```

## Common Patterns

### 1. Character Frequency
```python
from collections import Counter

def char_frequency(s):
    return Counter(s)
```

### 2. String Reversal
```python
def reverse_string(s):
    return s[::-1]

def reverse_words(s):
    return ' '.join(s.split()[::-1])
```

### 3. Palindrome Check
```python
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
```

isalnum() meaning is the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).

### 4. String Matching
```python
def find_substring(s, pattern):
    for i in range(len(s) - len(pattern) + 1):
        if s[i:i+len(pattern)] == pattern:
            return i
    return -1
```

### 5. String Parsing
```python
def parse_string(s):
    result = []
    current = ""
    for char in s:
        if char == delimiter:
            if current:
                result.append(current)
                current = ""
        else:
            current += char
    if current:
        result.append(current)
    return result
```

### 6. Character Manipulation
```python
def manipulate_chars(s):
    # Convert to list for mutable operations
    chars = list(s)
    # Modify chars
    chars[i] = new_char
    return ''.join(chars)
```

## Key Techniques
- Use list for mutable string operations
- String slicing for substrings
- Regular expressions for complex patterns
- Two pointers for palindrome/anagram checks

