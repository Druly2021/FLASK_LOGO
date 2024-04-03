from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world!"


@app.route('/name/<s>')
def show_string(s):
    print(type(s))
    return f"Hello, {s}"


@app.route('/<x>/<y>/<opp>')
def calculate(x, y, opp):
    x, y = float(x), float(y)
    if opp == 'add':
        return f"{x} + {y} = {x + y}"
    elif opp == 'sub':
        return f"{x} - {y} = {x - y}"
    elif opp == 'mul':
        return f"{x} * {y} = {x * y}"
    elif opp == 'div':
        return f"{x} / {y} = {x / y}"
    else:
        "На ноль делить нельзя!"


if __name__ == '__main__':
    app.run()
