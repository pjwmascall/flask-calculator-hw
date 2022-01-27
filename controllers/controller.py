from flask import render_template
from flask import request, redirect
from app import app
from modules.calculator import Calculator

calculator = Calculator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<operation>', methods=["POST"])
def get_form(operation):
    if request.method == "POST":
        num1 = request.form.get("firstnum")
        num2 = request.form.get("secondnum")
        if num1 == "":
            num1 = None
        if num2 == "":
            num2 = None
        return redirect(f"/{operation}/{num1}/{num2}")


@app.route('/<operation>/<num1>/<num2>')
def calculate(operation, num1="", num2=""):
    if operation == "add":
        result = calculator.add(num1, num2)
        if isinstance(result, float):
            result = f"The answer is {result}"
    if operation == "subtract":
        result = calculator.subtract(num1, num2)
        if isinstance(result, float):
            result = f"The answer is {result}"
    if operation == "multiply":
        result = calculator.multiply(num1, num2)
        if isinstance(result, float):
            result = f"The answer is {result}"
    if operation == "divide":
        result = calculator.divide(num1, num2)
        if isinstance(result, float):
            result = f"The answer is {result}"
    return render_template('result.html', result_message=result)