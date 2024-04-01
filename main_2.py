from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world!"


# http://127.0.1:5000/info


@app.route("/info")
def information():
    return "Сегодня хорошая погода!"


@app.route("/world")
def nature():
    return """
    На Псковщину пришла долгожданная весна!<br> В моем родном городе Великие Луки сейчас<br>идет дождик,
    но он не портит настроения т.к.<br>на улице тепло. Прилетели грачи, набухают<br>почки на деревьях
    и вся природа просыпается<br>после долгого зимнего сна! """


if __name__ == '__main__':
    app.run()
