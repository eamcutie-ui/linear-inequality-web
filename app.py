from flask import Flask, render_template, request
from sympy import symbols, solve_univariate_inequality, parse_expr

app = Flask(__name__)
x = symbols('x')

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        expr = request.form.get("expression")
        try:
            solution = solve_univariate_inequality(parse_expr(expr), x)
            result = str(solution)
        except:
            result = "Invalid inequality"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
