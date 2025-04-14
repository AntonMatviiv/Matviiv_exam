import unittest
from main import *

class TestFunctions(unittest.TestCase):

    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(15))

    def test_classify_age(self):
        self.assertEqual(classify_age(-1), "Invalid")
        self.assertEqual(classify_age(5), "Child")
        self.assertEqual(classify_age(16), "Teen")
        self.assertEqual(classify_age(30), "Adult")
        self.assertEqual(classify_age(70), "Senior")

    def test_grade_to_letter(self):
        self.assertEqual(grade_to_letter(95), "A")
        self.assertEqual(grade_to_letter(85), "B")
        self.assertEqual(grade_to_letter(75), "C")
        self.assertEqual(grade_to_letter(65), "D")
        self.assertEqual(grade_to_letter(50), "F")
        self.assertEqual(grade_to_letter(-5), "Invalid")

    def test_calculate_discount(self):
        self.assertEqual(calculate_discount(10, 10), 0)
        self.assertEqual(calculate_discount(50, 10), 50)
        self.assertEqual(calculate_discount(100, 10), 200)
        self.assertEqual(calculate_discount(-1, 10), 0)

    def test_min_positive(self):
        self.assertEqual(min_positive([-1, 0, 5, 3]), 3)
        self.assertIsNone(min_positive([-5, -3, 0]))

    def test_shipping_cost(self):
        self.assertEqual(shipping_cost(0), 0)
        self.assertEqual(shipping_cost(0.5), 5)
        self.assertEqual(shipping_cost(3), 10)
        self.assertEqual(shipping_cost(10), 20)
        self.assertEqual(shipping_cost(30), 50)

    def test_triangle_type(self):
        self.assertEqual(triangle_type(3, 3, 3), "Equilateral")
        self.assertEqual(triangle_type(3, 3, 4), "Isosceles")
        self.assertEqual(triangle_type(3, 4, 5), "Scalene")
        self.assertEqual(triangle_type(1, 2, 3), "Not a triangle")

    def test_bmi_category(self):
        self.assertEqual(bmi_category(50, 1.8), "Underweight")
        self.assertEqual(bmi_category(65, 1.7), "Normal")
        self.assertEqual(bmi_category(85, 1.7), "Overweight")
        self.assertEqual(bmi_category(120, 1.7), "Obese")
        self.assertEqual(bmi_category(70, 0), "Invalid height")

    def test_time_to_minutes(self):
        self.assertEqual(time_to_minutes("01:30"), 90)
        self.assertEqual(time_to_minutes("00:00"), 0)
        self.assertEqual(time_to_minutes("invalid"), -1)

    def test_is_strong_password(self):
        self.assertTrue(is_strong_password("Strong123"))
        self.assertFalse(is_strong_password("weak"))
        self.assertFalse(is_strong_password("nocapital123"))
        self.assertFalse(is_strong_password("NOLOWERCASE123"))

    def test_next_day(self):
        self.assertEqual(next_day("Monday"), "Tuesday")
        self.assertEqual(next_day("Sunday"), "Monday")
        self.assertEqual(next_day("Invalid"), "Invalid day")

    def test_calculate_tax(self):
        self.assertEqual(calculate_tax(5000), 500)
        self.assertEqual(calculate_tax(20000), 1000 + 10000 * 0.2)
        self.assertEqual(calculate_tax(60000), 9000 + 10000 * 0.3)
        self.assertEqual(calculate_tax(-100), 0)

    def test_first_odd(self):
        self.assertEqual(first_odd([2, 4, 7, 8]), 7)
        self.assertIsNone(first_odd([2, 4, 6]))

    def test_is_alpha_only(self):
        self.assertTrue(is_alpha_only("abcDEF"))
        self.assertFalse(is_alpha_only("abc123"))
        self.assertFalse(is_alpha_only(""))

    def test_is_valid_date(self):
        self.assertTrue(is_valid_date("2024-04-01"))
        self.assertFalse(is_valid_date("2024-13-01"))
        self.assertFalse(is_valid_date("bad-date"))

    def test_atm_withdraw(self):
        self.assertEqual(atm_withdraw(1000, 200), 800)
        self.assertEqual(atm_withdraw(500, 600), "Insufficient funds")
        self.assertEqual(atm_withdraw(500, -10), "Invalid amount")

if __name__ == '__main__':
    unittest.main()
