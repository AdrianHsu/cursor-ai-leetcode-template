import time
from functools import wraps
import unittest
"""
Decorator example with Timer.

*args and **kwargs
By default, a function must be called with the correct number of arguments.
However, sometimes you may not know how many arguments that will be passed into your function.
*args and **kwargs allow functions to accept a unknown number of arguments.
"""

# --- CORE LOGIC ---
# `func` basically is a anonymous function for the `slow_function`
def my_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # start = time.perf_counter()
        result = func(*args, **kwargs)
        # end = time.perf_counter()
        # wrapper.duration = end - start  # Store for testing
        # print(f"Executed {func.__name__} in {wrapper.duration:.4f}s")        
        return result
    return wrapper

@my_timer
def slow_function(input_sec):
    time.sleep(input_sec)
    return "Done"

# --- TESTS ---
class TestDecorator(unittest.TestCase):
    def test_timer_execution(self):
        res = slow_function(2)
        self.assertEqual(res, "Done")
        # self.assertGreaterEqual(slow_function.duration, 2)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)