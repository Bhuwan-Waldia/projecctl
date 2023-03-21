from flask import Flask

pp = Flask(__name__)

@pp.route("/")
def march():
    return "<h1> Hello march, be good ! </h1>"

if __name__ == "__main__":
    pp.run(host = "0.0.0.0")