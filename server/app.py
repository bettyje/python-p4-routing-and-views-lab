#!/usr/bin/env python3

import sys
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter, file=sys.stdout)
    return parameter


@app.route("/count/<int:parameter>")
def count(parameter):
    numbers = '\n'.join(str(i) for i in range(parameter))
    return '\n'.join(str(i) for i in range(parameter)) + '\n'


@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero is not allowed.'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation. Please use +, -, *, div, or %.'

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
