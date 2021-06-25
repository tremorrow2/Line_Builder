# line-builder
from flask import Flask
from flask import request, escape
import LB2


app = Flask(__name__)

@app.route("/")
def index():
    input = request.args.get("input", "")
    output = request.args.get("output", "")
    if output:

        LB2.Main(input,output)
        status = "Built"
    else:
        status = "Component Missing"
    return (
        """<form action="" method="get">
                Input File: <input type="text" name="input">
                 Output File: <input type="text" name="output">
                <input type="submit" value="Build">
              </form>"""
        + "Status: "
        + status
    )
"""
def fahrenheit_from(celsius):
    Convert Celsius to Fahrenheit degrees.
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"
"""
@app.errorhandler(502)
def internal_error(error):
    return "502 error"

@app.errorhandler(404)
def not_found(error):
    return "404 error",404

if __name__ == "__main__":
    app.run()
