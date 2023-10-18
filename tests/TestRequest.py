import unittest
from currency_stuff import request


class TestRequest(unittest.TestCase):
    def test_on_success(self):
        self.assertEqual(request().code,200)
