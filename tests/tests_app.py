"""This file tests the Flask portion of the Forex converter, namely the routes in app.py"""
from unittest import TestCase
from app import app

app.config["TESTING"] = True
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]          

class FlaskTests(TestCase):
    def test_homepage_form(self):
        """Make sure the home page form at the route '/' is displayed."""
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<label for="currency-from-input">', html)
            self.assertIn('<label for="currency-to-input">', html)
            self.assertIn('<label for="amount-input">', html)
    
    def test_invalid_input(self):
        """Make sure submitting invalid form input results in a redirect to the home page."""
        with app.test_client() as client:
            resp = client.post('/convert', data={'currency-from': 'AAA', 'currency-to': 'BBB', 'amount': '-0'})

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "/") 

    def test_invalid_input_redirection(self):
        """Make sure submitting invalid form input results in the appropriate flash messages being displayed."""
        with app.test_client() as client:
            resp = client.post('/convert', data={'currency-from': 'AAA', 'currency-to': 'BBB', 'amount': '-0'}, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<label for="currency-from-input">', html)
            self.assertIn('<label for="currency-to-input">', html)
            self.assertIn('<label for="amount-input">', html)
            self.assertIn('Currency A: Must be a valid 3-letter currency code.', html)
            self.assertIn('Currency B: Must be a valid 3-letter currency code.', html)
            self.assertIn("Amount cannot be negative and thus cannot contain the negative sign.", html) 
    
    def test_valid_input(self):
        """Make sure submitting valid form input results in result.html being displayed with the appropriate result string."""
        with app.test_client() as client:
            resp = client.post('/convert', data={'currency-from': 'USD', 'currency-to': 'USD', 'amount': '1.00'}, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<a class="home-link" href="/">Back to Home</a>', html)
            self.assertIn('Your input of $1.00 (USD) is equivalent to $1.00 (USD)', html)