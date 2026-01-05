import unittest

"""
The Dunder methods (Magic Methods) used here allow your custom DataBox class to 
"pretend" to be a built-in Python type. Without these dunders, you couldn't use len(), [], 
or call the object like a function.

Dunder Method	What it does in your code	Syntax it enables
__init__	Initializes the object with a list of data.	box = DataBox([1, 2])
__len__	Tells Python how to calculate the size of your object.	len(box)
__getitem__	Allows you to access data inside the object using an index.	box[1]
__call__	Makes the object "Callable" (like a function).	box(4)
__repr__	Defines how the object looks when you print it or debug it.	print(box)
"""

class DataBox:
        def __init__(self, data):
            self._data = list(data)

        def __len__(self):
            return len(self._data)

        def __getitem__(self, index):
            return self._data[index]

        def __call__(self, new_item):
            """Calling the object adds an item."""
            self._data.append(new_item)

        def __repr__(self):
            return f"DataBox({self._data})"


class TestMagicMethods(unittest.TestCase):
    def setUp(self):
        self.box = DataBox([1, 2, 3])

    def test_indexing_and_len(self):
        self.assertEqual(len(self.box), 3)
        self.assertEqual(self.box[1], 2)

    def test_callable(self):
        self.box(4)  # Call call(), which basically adds an item
        self.assertEqual(len(self.box), 4)
        self.assertEqual(self.box[3], 4)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)