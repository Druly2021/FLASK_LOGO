from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, world!"


@app.route('/name/<s>')
def show_string(s):
    print(type(s))
    return f'Hello, {s}'


@app.route('/<x>/<y>/add')
def add(x, y):
    x, y = float(x), float(y)
    return f'{x} + {y} = {x + y}'


@app.route('/<x>/<y>/sub')
def sub(x, y):
    x, y = float(x), float(y)
    return f'{x} - {y} = {x - y}'


@app.route('/<x>/<y>/mul')
def mul(x, y):
    x, y = float(x), float(y)
    return f'{x} * {y} = {x * y}'


@app.route('/<x>/<y>/div')
def div(x, y):
    x, y = float(x), float(y)
    if y:
        return f'{x} / {y} = {x / y}'
    else:
        "На ноль делить нельзя"


if __name__ == "__main__":
    app.run()
