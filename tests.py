from os import environ
from unittest import TestCase


class MyTests(TestCase):
    def test_simple(self):
        self.assertEqual(1, 1)
