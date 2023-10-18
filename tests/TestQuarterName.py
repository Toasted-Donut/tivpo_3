import unittest
from date_stuff import quarter_name


class TestQuarterName(unittest.TestCase):
    def test_in_range(self):
        self.assertEqual(quarter_name(1),"Зима")
        self.assertEqual(quarter_name(2), "Зима")
        self.assertEqual(quarter_name(12), "Зима")
        self.assertEqual(quarter_name(3), "Весна")
        self.assertEqual(quarter_name(4), "Весна")
        self.assertEqual(quarter_name(5), "Весна")
        self.assertEqual(quarter_name(6), "Лето")
        self.assertEqual(quarter_name(7), "Лето")
        self.assertEqual(quarter_name(8), "Лето")
        self.assertEqual(quarter_name(9), "Осень")
        self.assertEqual(quarter_name(10), "Осень")
        self.assertEqual(quarter_name(11), "Осень")

    def test_out_range(self):
        self.assertTrue(quarter_name(900))

    def test_input(self):
        self.assertTrue(quarter_name('bruh'))
