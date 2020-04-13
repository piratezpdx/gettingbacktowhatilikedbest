"""
unit testing for the first 15 Project Euler problems. Generally testing will
be limited to getting the right answer in most cases. Note that the hierarchy
of where tests are located doesn't match in github to where things are located
in the code ... unimportant reasons do exist.
"""

import unittest
import euler_1_15


class EulerTestCase(unittest.TestCase):

    def test_euler1(self):
        self.assertEqual(euler_1_15.euler1(), 233168)

    def test_euler2(self):
        self.assertEqual(euler_1_15.euler2(4000000), 4613732)

    def test_euler3(self):
        self.assertEqual(euler_1_15.euler3(), 6857)


if __name__ == '__main__':
    unittest.main()
