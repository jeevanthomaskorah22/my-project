import unittest
from hello import greet  # Assuming greet() is a function in hello.py

class TestHello(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet(), "hello world")

if __name__ == "__main__":
    unittest.main()
