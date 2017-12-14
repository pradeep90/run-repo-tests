#!/usr/bin/python
import unittest


class SumTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_foo(self):
        self.assertEqual(2 + 2, 5)

if __name__ == '__main__':
    unittest.main()
