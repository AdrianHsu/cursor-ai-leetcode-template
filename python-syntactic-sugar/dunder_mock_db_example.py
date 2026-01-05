import unittest

"""
By implementing __enter__ and __exit__
Now it supports `with` statement
"""
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.is_connected = False
        self.log = []

    def __enter__(self):
        self.is_connected = True
        msg = f"DEBUG: Connecting to {self.db_name}..."
        print(msg)
        self.log.append(msg)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.is_connected = False
        msg = "DEBUG: Connection closed."
        print(msg)
        self.log.append(msg)
        
        if exc_type:
            err_msg = f"DEBUG: Error caught: {exc_val}"
            print(err_msg)
            self.log.append(err_msg)
        
        return False

    def execute_query(self, query):
        print(f"DEBUG: Executing {query}")
        return f"Results for '{query}'"

class TestDatabaseConnection(unittest.TestCase):
    def test_successful_connection(self):
        print("\n--- Running Success Test ---")
        db_instance = DatabaseConnection("Production_DB")
        with db_instance as db:
            db.execute_query("SELECT * FROM users")
            
    def test_connection_closes_on_error(self):
        print("\n--- Running Error Test ---")
        db_instance = DatabaseConnection("Test_DB")
        try:
            with db_instance as db:
                raise ValueError("Query Timeout!")
        except ValueError:
            pass

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)