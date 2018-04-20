import unittest

from fizzbuzz import robot

class FizzbuzzTest(unittest.TestCase):
    def test_say_1_when_1(self):
        self.assertEqual(robot(1), '1')

    def test_say_fizz_when_3(self):
        self.assertEqual(robot(3), 'fizz')

    def test_say_buzz_when_5(self):
        self.assertEqual(robot(5), 'buzz')

    def test_say_fizzbuzz_when_15(self):
        self.assertEqual(robot(15), 'fizzbuzz')