from flask import Flask, render_template, request
from sympy import symbols, solve_univariate_inequality
from sympy.parsing.sympy_parser import parse_expr
import os

app = Flask(__name__)

x = symbols('x')

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    expression = ""

    if request.method == "POST":
        expression = request.form.get("expression")

        try:
            expr = parse_expr(expression)
            solution = solve_univariate_inequality(expr, x)
            result = str(solution)
        except Exception as e:
            result = "Invalid inequality"

    return render_template("index.html", result=result, expression=expression)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
