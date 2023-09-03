# Put your app in here.
from flask import Flask
import operations

app = Flask(__name__)


@app.route('/operation/<int:a>/<int:b>/<operation>', methods=["GET"])
def results(a, b, operation):
    if operation == "add":
        result = operations.add(a, b)
    elif operation == "subtract":
        result = operations.sub(a, b)
    elif operation == "mult":
        result = operations.mult(a, b)
    elif operation == "div":
        try:
            result = operations.div(a, b)
        except ValueError as e:
            return str(e), 400
    else:
        return "Invalid operation", 400

    return str(result)


if __name__ == '__main__':
    app.run(debug=True)
