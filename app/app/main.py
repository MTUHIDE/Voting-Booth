from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from HIDE's new solution"

@app.route("/menu/")
def menu():
    return render_template('menu.html')

@app.route("/max/")
def max():
    return "Hello world from Max"


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
