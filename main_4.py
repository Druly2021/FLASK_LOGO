from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, world!"


# http://127.0.0.1:5000/info@app.route("/info")
@app.route("/info")
def information():
    return "Сегодня хорошая погода!"


# http://127.0.0.1:5000/name/Ivan
@app.route("/name/<s>")
def show_string(s):
    print(type(s))
    return f'Hello, {s}'


# http://127.0.0.1:5000/add/23/18
@app.route("/sum/<int:x>/<int:y>")
def add(x, y):
    return f'{x} + {y} = {x + y}'


# http://127.0.0.1:5000/sum/23.45/18.21
@app.route("/sum_float/<float:x>/<float:y>")
def sum_float(x, y):
    return f'{x} + {y} = {x + y}'


# http://127.0.0.1:5000/hello?name=Petr&surname=Ivanov
@app.route("/hello")
def hello():
    name = request.args.get("name", "HELLO")
    surname = request.args.get("surname", "WORLD")
    return f'Hello {name} {surname}'


def get_all_users_from_db():
    return [
        {
            "id": 1,
            "username": "alex223190",
            "email": "alex_sidorov@gmail.com"
        },
        {
            "id": 23,
            "username": "petr22111965",
            "email": "petr_voronin@mail.ru"
        }
    ]


@app.route("/users")
def get_users():
    users = []
    for user in get_all_users_from_db():
        users.append(user)
    return jsonify(users)


if __name__ == "__main__":
    app.run()
