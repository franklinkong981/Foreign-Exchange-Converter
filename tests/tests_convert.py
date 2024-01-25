"""Tests for the functions in convert.py"""
from unittest import TestCase
import convert

class ConvertTestCase(TestCase):
    def test_get_conversion_string(self):
        """Ensures that the function getConversionString works as intended and returns the proper conversion string."""
        self.assertEqual(convert.get_conversion_string("USD", "USD", "1.00"), "Your input of $1.00 (USD) is equivalent to $1.00 (USD)")
    
    def test_calculate_conversion(self):
        """Tests the function calculate_conversion to make sure the function calculates a conversion properly."""
        self.assertEqual(convert.calculate_conversion("USD", "USD", 1.00), 1.00)
        self.assertEqual(convert.calculate_conversion("USD", "USD", 1.56), 1.56)
        self.assertEqual(convert.calculate_conversion("GBP", "GBP", 3.65), 3.65)