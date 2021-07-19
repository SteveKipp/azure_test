from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> <b>H</b>ello <b>W</b>orld! </p>"


if __name__ == "__main__":
    app.debug = True
    app.run()
