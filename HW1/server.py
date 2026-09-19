from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/survey", methods=["GET", "POST"])
def survey():
    return render_template("survey.html")


@app.route("/decline")
def decline():
    return render_template("decline.html")


@app.route("/thanks")
def thanks():
    return render_template("thanks.html")

@app.route("/summary")
def summary():
    return render_template("summary.html")