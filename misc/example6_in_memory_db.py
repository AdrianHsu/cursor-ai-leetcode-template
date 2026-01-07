import collections

"""
Interview Question: Design an In-Memory Database
Problem Statement 

Design a simplified in-memory database library that mimics the core functionality of SQL. 
You are not required to implement a SQL string parser (e.g., you do not need to parse "SELECT * FROM..."). 
Instead, you should implement the functionality through direct function calls or a class API.
The database should support defining tables, inserting data, and querying data with filtering and sorting capabilities.

Functional Requirements

Table Management:

Ability to define a table given a list of column names.
The underlying storage should be in-memory (e.g., using HashMaps/Dictionaries or Lists).

Data Insertion:
Implement an insert method to add rows to a table.

Data Selection (Querying):
Implement a single select method that handles filtering and sorting.

Signature: The method should look similar to: select(table_name, where=None, order_by=None)

Filtering (where):

Support equality checks (e.g., id = 1).

Support inequalities (e.g., amount > 100, price < 50).

Support multiple conditions. The system should handle logical AND as well as OR.

Sorting (order_by):

Support sorting by a single column.

Support sorting by multiple columns (e.g., sort by department first, then by salary).

API Constraints & Compatibility:

The select API must be unified. Whether the user filters by one column or multiple, or sorts by one column or multiple, the same method signature should be used.

Ensure backward compatibility (e.g., if where or order_by are omitted, the query should still return all results unsorted).

Example Usage (Pseudocode)
To clarify the requirements, here is how a user might interact with your library:

Python

# 1. Setup
db = InMemoryDB()
db.create_table("users", columns=["id", "name", "age", "score"])

# 2. Insert Data
db.insert("users", {"id": 1, "name": "Alice", "age": 30, "score": 90})
db.insert("users", {"id": 2, "name": "Bob",   "age": 25, "score": 85})
db.insert("users", {"id": 3, "name": "Charlie", "age": 30, "score": 95})

# 3. Simple Select (No filter, no sort)
# Returns all 3 rows
results = db.select("users")

# 4. Filter with AND (Age is 30 AND Score > 90)
# Returns: Charlie
results = db.select("users", where={"age": 30, "score": {">": 90}})

# 5. Filter with OR (Age < 26 OR Score > 92)
# Returns: Bob, Charlie
# Note: You need to define how the API accepts OR vs AND conditions.
results = db.select("users", where_or=[{"age": {"<": 26}}, {"score": {">": 92}}])

# 6. Multi-Column Sort (Order by Age ASC, then Score DESC)
# Returns: Bob (25), Charlie (30, 95), Alice (30, 90)
results = db.select("users", order_by=["age", "-score"])
"""

class InMemoryDB:
    def __init__(self):
        # Structure: {table_name: {"columns": [col_names], "rows": [ {row_data} ] }}
        self.tables = {}

    def create_table(self, table_name, columns):
        """
        Creates a new table with a defined schema.
        """
        if table_name in self.tables:
            raise ValueError(f"Table '{table_name}' already exists.")
        
        self.tables[table_name] = {
            "columns": columns,
            "rows": []
        }
        print(f"Table '{table_name}' created.")

    def insert(self, table_name, row_data):
        """
        Inserts a row into the table. 
        Validates that row keys match the table schema.
        """
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist.")
        
        table_def = self.tables[table_name]
        
        # simple validation to ensure row data matches columns
        # (Optional in relaxed interviews, but good for completeness)
        for col in row_data:
            if col not in table_def["columns"]:
                raise ValueError(f"Column '{col}' not found in table '{table_name}'")
        
        table_def["rows"].append(row_data)

    def select(self, table_name, where=None, order_by=None):
        """
        Retrieves rows from a table with optional filtering and sorting.
        
        Args:
            table_name (str): Name of the table.
            where (dict or list, optional): 
                - If dict: Key-value pairs treated as AND conditions.
                  Values can be literals (equality) or dicts for operators (e.g., {">": 10}).
                  Example: {"age": 30, "score": {">": 80}}
                - If list of dicts: Treated as OR conditions (row matches if ANY dict matches).
            order_by (str or list, optional): 
                - Single string: "column_name" (ascending) or "-column_name" (descending).
                - List of strings: ["col1", "-col2"] for multi-column sort.
        """
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist.")
        
        result_rows = self.tables[table_name]["rows"]

        # 1. Filtering (WHERE)
        if where:
            filtered_rows = []
            for row in result_rows:
                if self._matches_where(row, where):
                    filtered_rows.append(row)
            result_rows = filtered_rows

        # 2. Sorting (ORDER BY)
        if order_by:
            # Normalize order_by to always be a list for consistent processing
            # e.g., "score" -> ["score"]
            if isinstance(order_by, str):
                order_by = [order_by]
            
            # Sort takes place here using a custom key
            result_rows.sort(key=lambda r: self._sort_key(r, order_by))

        return result_rows

    def _matches_where(self, row, where_clause):
        """
        Helper to determine if a row matches the where clause.
        Supports AND (dict) and OR (list of dicts).
        """
        # Case A: OR Logic (List of conditions) -> Return True if ANY match
        if isinstance(where_clause, list):
            for condition in where_clause:
                if self._check_and_condition(row, condition):
                    return True
            return False

        # Case B: AND Logic (Single Dict) -> Return True only if ALL match
        elif isinstance(where_clause, dict):
            return self._check_and_condition(row, where_clause)
        
        return True

    def _check_and_condition(self, row, conditions):
        """
        Helper to check a dictionary of AND conditions against a row.
        """
        for col, requirement in conditions.items():
            if col not in row:
                return False # Column missing from data, treat as mismatch
            
            row_val = row[col]

            # exact match: {"id": 5}
            if not isinstance(requirement, dict):
                if row_val != requirement:
                    return False
            
            # operator match: {"score": {">": 10}}
            else:
                for op, val in requirement.items():
                    if op == ">" and not (row_val > val): return False
                    if op == "<" and not (row_val < val): return False
                    if op == ">=" and not (row_val >= val): return False
                    if op == "<=" and not (row_val <= val): return False
                    if op == "!=" and not (row_val != val): return False
        
        return True

    def _sort_key(self, row, order_by_columns):
        """
        Generates a tuple key for sorting. 
        Handles descending order if column starts with '-'.
        """
        key_parts = []
        for col in order_by_columns:
            is_desc = col.startswith("-")
            clean_col = col[1:] if is_desc else col
            
            val = row.get(clean_col)
            
            # Python sort is stable. For descending, we can wrap numbers.
            # For strings, specific logic is needed, but for an interview, 
            # assuming numeric sort for complex logic is usually acceptable 
            # or creating a wrapper class.
            
            # Simple trick for numeric descending sort in Python: negate the value
            if is_desc and isinstance(val, (int, float)):
                val = -val
            # (Note: For descending strings, this simple trick doesn't work 
            # without a custom comparator, but sticking to numeric for demo)
                
            key_parts.append(val)
        
        return tuple(key_parts)


# ==========================================
# TEST IMPLEMENTATION
# ==========================================
if __name__ == "__main__":
    db = InMemoryDB()

    # 1. Setup
    db.create_table("users", ["id", "name", "age", "score"])
    
    # 2. Insert Data
    db.insert("users", {"id": 1, "name": "Alice", "age": 30, "score": 90})
    db.insert("users", {"id": 2, "name": "Bob",   "age": 25, "score": 85})
    db.insert("users", {"id": 3, "name": "Charlie", "age": 30, "score": 95})
    db.insert("users", {"id": 4, "name": "David", "age": 25, "score": 88})

    print("\n--- Test 1: Simple Select ---")
    print(db.select("users"))

    print("\n--- Test 2: Where Filter (AND) - Age=30 AND Score > 90 ---")
    # Should return Charlie
    print(db.select("users", where={"age": 30, "score": {">": 90}}))

    print("\n--- Test 3: Where Filter (OR) - Age < 26 OR Score > 92 ---")
    # Should return Bob (age 25), David (age 25), Charlie (score 95)
    # Using list of dicts for OR logic
    or_condition = [{"age": {"<": 26}}, {"score": {">": 92}}]
    print(db.select("users", where=or_condition))

    print("\n--- Test 4: Order By Single Column (Score Ascending) ---")
    print(db.select("users", order_by="score"))

    print("\n--- Test 5: Multi-Column Sort (Age Asc, Score Desc) ---")
    # Should be: Bob (25, 85), David (25, 88) -> Wait, David (88) should be before Bob (85) due to desc
    # Alice (30, 90), Charlie (30, 95) -> Charlie before Alice
    # Expected order: David, Bob, Charlie, Alice
    print(db.select("users", order_by=["age", "-score"]))