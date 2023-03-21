from flask import Flask
from flask import Request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1> hello March  </h1>"

@app.route("/one")
def hello_A():
    return "</h1> Hello, AAA"

@app.route("/two")
def hello_B():
    return "<h1> hello BBBB </h1>"

@app.route("/add")
def add():
    a = 5+6
    return "this is my result {}".format(a)

@app.route("/in")
def test2():
    data = Request.args.get("x")
    return "this is input from my url {}".format(data)

if __name__ == "__main__":
    app.run(host = "0.0.0.0")