"""This file contains the functions for performing the forex conversion and getting the appropriate currency symbols once all form fields are validated."""
from forex_python.converter import CurrencyRates, CurrencyCodes
from validate import format_amount

rates = CurrencyRates();
codes = CurrencyCodes();


def get_conversion_string(currency_from, currency_to, amount):
    """Generates a string that includes the conversion of the string "amount" of currency_from to the equivalent amount of currency_to.
    The string also includes appropriate currency symbols for currency_from and currency_to."""
    currency_from_symbol = codes.get_symbol(currency_from)
    currency_to_symbol = codes.get_symbol(currency_to)
    converted_amount = str(calculate_conversion(currency_from, currency_to, float(amount)))
    converted_amount = format_amount(converted_amount)

    return f"Your input of {currency_from_symbol}{amount} ({currency_from}) is equivalent to {currency_to_symbol}{converted_amount} ({currency_to})"

def calculate_conversion(currency_from, currency_to, amount):
    """Converts the float "amount" of currency_from to the equivalent amount in currency_to 
    and returns the converted number to at most 2 decimal places.
    
    >>> calculate_conversion("USD", "USD", 2.00)
    2.0

    """
    converted_amount = rates.convert(currency_from, currency_to, amount)
    converted_amount = round(converted_amount, 2)
    return converted_amount