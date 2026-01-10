import unittest
from coffee_menu import CoffeeMenu

class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        self.menu = CoffeeMenu()

    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.getprice("espresso"), 2.5)

    def test_get_price_non_existing_item(self):
        with self.assertRaises(KeyError):
            self.menu.getprice("Green Tea")

    def test_add_item(self):
        self.menu.additem("green tea", 2.75)
        self.assertEqual(self.menu.getprice("green tea"), 2.75)


if __name__ == "__main__":
    unittest.main()
