from flask import Flask, request, render_template, redirect, flash, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension
from validate import get_form_error_messages, format_amount
from convert import get_conversion_string

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/')
def show_homepage_form():
    """Show the home page, which consists of the forex converter form."""
    return render_template("homepage.html")


@app.route('/convert', methods=['POST'])
def validate_and_convert():
    """Check to see whether the currencies the user entered is valid, as well as properly format the amount entered to 2 decimal places.
    If the currencies are valid, perform the conversion and display the result.
    If they aren't, redirect to the home page and display error messages above the form."""
    currency_from = request.form["currency-from"].strip()
    currency_to = request.form["currency-to"].strip()
    amount = request.form["amount"]
    
    # check for any invalid inputs
    error_messages = get_form_error_messages(currency_from, currency_to, amount)
    if len(error_messages) > 0:
        for error_message in error_messages:
            flash(error_message)
        return redirect("/")
    
    result_string = get_conversion_string(currency_from.upper(), currency_to.upper(), format_amount(amount))

    return render_template("result.html", result=result_string)