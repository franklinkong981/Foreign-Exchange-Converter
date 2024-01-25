"""This file contains functions for validating the form data submitted by the user."""
from forex_python.converter import CurrencyRates

rates = CurrencyRates();
VALID_CURRENCIES = ["USD"]
for currency_code in rates.get_rates('USD').keys():
    VALID_CURRENCIES.append(currency_code) # The submitted values of the first 2 inputs must match one of the valid currencies in VALID_CURRENCIES.

def get_form_error_messages(currency_from, currency_to, amount):
    """Validates form data by checking to see if the first 2 inputs match one of the currencies in VALID_CURRENCIES, and whether the third input
    is in the form of a negative number.
    Returns a list of error messages to be displayed, one for each invalid input. If all inputs are valid, the list returned will be empty."""
    error_messages = []

    if not is_currency_valid(currency_from):
        error_messages.append(f"Currency A: Must be a valid 3-letter currency code. Your input: {currency_from}")
    if not is_currency_valid(currency_to):
        error_messages.append(f"Currency B: Must be a valid 3-letter currency code. Your input: {currency_to}")
    if not is_amount_valid(amount):
        error_messages.append(f"Amount cannot be negative and thus cannot contain the negative sign. Your input: {amount}")
    return error_messages

def is_currency_valid(currency_input):
    """Checks to see if currency_input matches one of the 3-digit currency codes in VALID_CURRENCIES. If it does, return True, else return False.
    The check is not case-sensitive, so a lowercase version of the 3-letter code will also return True.

    >>> is_currency_valid("AAA")
    False

    >>> is_currency_valid("usd")
    True

    >>> is_currency_valid("USD")
    True

    """
    if len(currency_input) != 3 or not currency_input.isalpha():
        return False
    elif currency_input.upper() not in VALID_CURRENCIES:
        return False
    else:
        return True
    
def is_amount_valid(amount):
    """Checks to see if the string amount inputted by the user in the form data is negative/contains a negative sign.
    If it does, return False. Otherwise, return True.
    
    >>> is_amount_valid("-2.00")
    False

    >>> is_amount_valid("2.00")
    True

    """
    if amount.find("-") != -1:
        return False
    else:
        return True
    
def format_amount(amount):
    """Properly format the string amount that the user entered into the third text input in the form into a float to 2 decimal places
    that is returned as a string.

    >>> format_amount("0")
    '0.00'
    
    >>> format_amount("2.")
    '2.00'

    >>> format_amount("56.2")
    '56.20'

    >>> format_amount("45.24")
    '45.24'

    """
    formatted_amount = ""

    if amount[0] == ".": # If amount starts with a decimal point, add a 0 to the beginning.
        formatted_amount += "0"

    formatted_amount += amount

    if amount.find(".") == -1: # If the amount doesn't contain a decimal, add a decimal and 2 zeros at the end.
        formatted_amount += ".00"
    elif amount.endswith("."): # If the last character is a decimal, add 2 zeros.
        formatted_amount += "00"
    elif amount[-2] == ".": # If there is only one digit after the decimal, add 1 zero.
        formatted_amount += "0"
    
    return formatted_amount