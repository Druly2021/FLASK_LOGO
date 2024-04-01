from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Arithmetic operations"


@app.route("/summ/<float:x>/<float:y>")
def summ(x, y):
    return f'{x} + {y} = {x + y}'


@app.route("/sub/<float:x>/<float:y>")
def sub(x, y):
    return f'{x} - {y} = {x - y}'


@app.route("/mul/<float:x>/<float:y>")
def mul(x, y):
    return f'{x} * {y} = {x * y}'


@app.route("/div/<float:x>/<float:y>")
def div(x, y):
    if y:
        return f'{x} / {y} = {x / y}'
    else:
        return "Нельзя делить на ноль"


if __name__ == "__main__":
    app.run()
