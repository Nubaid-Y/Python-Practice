import unittest

from string_utils import reverse_string, capitalize_string, is_capitalized

class MyTestCase(unittest.TestCase):
    def testreverse(self):
        self.assertEqual(reverse_string("Rock"),"kcoR")
    def testcap(self):
        self.assertEqual(capitalize_string("hello"),"Hello")
    def testiscap(self):
        self.assertTrue(is_capitalized("Hello"))
        self.assertFalse(is_capitalized("hello"))


if __name__ == "__main__":
    unittest.main()
