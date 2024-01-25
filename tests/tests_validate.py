"""Tests for the functions in validate.py"""
from unittest import TestCase
import validate
import random

class ValidateTestCase(TestCase):
    def test_get_form_error_messages(self):
        """Ensures that the function get_form_error_messages works as intended and 
        returns the number of error messages that match the number of invalid inputs."""
        self.assertEqual(len(validate.get_form_error_messages("", "", "-0")), 3)
        self.assertEqual(len(validate.get_form_error_messages("AAA", "BBB", "20.0")), 2)
        self.assertEqual(len(validate.get_form_error_messages("usd", "usd", "-0")), 1)
        self.assertEqual(len(validate.get_form_error_messages("USD", "USD", "-0")), 1)
        self.assertEqual(len(validate.get_form_error_messages("usd", "inr", "0")), 0)
        self.assertEqual(len(validate.get_form_error_messages("jpy", "sgd", "9745.")), 0)

    def test_is_currency_valid(self):
        """Ensures that the function is_currency_valid works as intended and that only inputs that match
        a 3-letter code in the VALID_CURRENCIES list result in True being returned."""
        self.assertFalse(validate.is_currency_valid(""))
        self.assertFalse(validate.is_currency_valid("ABCDEFG"))
        self.assertFalse(validate.is_currency_valid("AAA"))
        self.assertTrue(validate.is_currency_valid("USD"))
        self.assertTrue(validate.is_currency_valid("usd"))
        self.assertTrue(validate.is_currency_valid(random.choice(validate.VALID_CURRENCIES)))
    
    def test_is_amount_valid(self):
        """Ensures that the function is_amount_valid works as intended and that all amount strings
        with a negative sign result in False being returned."""
        self.assertFalse(validate.is_amount_valid("-0"))
        self.assertTrue(validate.is_amount_valid("0"))
        self.assertFalse(validate.is_amount_valid("0-0"))
        self.assertFalse(validate.is_amount_valid("-0.00"))
        self.assertTrue(validate.is_amount_valid("256.85"))
        self.assertFalse(validate.is_amount_valid("-256.85"))

    def test_format_amount(self):
        """Ensures that the format_amount function properly formats the string input into 
        a float to 2 decimal places."""
        self.assertEqual(validate.format_amount("0"), "0.00")
        self.assertEqual(validate.format_amount("2056"), "2056.00")
        self.assertEqual(validate.format_amount("."), "0.00")
        self.assertEqual(validate.format_amount("0."), "0.00")
        self.assertEqual(validate.format_amount("29.5"), "29.50")
        self.assertEqual(validate.format_amount("29.56"), "29.56")
    