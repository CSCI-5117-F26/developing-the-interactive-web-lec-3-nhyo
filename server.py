from flask import Flask, request, render_template, redirect

app = Flask(__name__)

guests = []


@app.route("/")
def home():
    return render_template("main.html", guests=guests)


@app.route("/guestbook", methods=["POST"])
def guestbook():
    guest_name = request.json.get("guestName")

    if guest_name:
        guests.append(guest_name)

    return {
        "guestName": guest_name
    }