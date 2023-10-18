import unittest
from date_stuff import month_short_name


class TestMonthShortName(unittest.TestCase):
    def test_in_range(self):
        self.assertEqual(month_short_name(1),'янв')
        self.assertEqual(month_short_name(2),'фев')
        self.assertEqual(month_short_name(3),'мар')
        self.assertEqual(month_short_name(4),'апр')
        self.assertEqual(month_short_name(5),'май')
        self.assertEqual(month_short_name(6),'июн')
        self.assertEqual(month_short_name(7),'июл')
        self.assertEqual(month_short_name(8),'авг')
        self.assertEqual(month_short_name(9),'сен')
        self.assertEqual(month_short_name(10),'окт')
        self.assertEqual(month_short_name(11),'ноя')
        self.assertEqual(month_short_name(12),'дек')

    def test_out_range(self):
      self.assertTrue(month_short_name(900))

    def test_input(self):
       self.assertTrue(month_short_name('bruh'))