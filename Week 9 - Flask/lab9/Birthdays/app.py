import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
db = SQL("sqlite:///birthdays.db")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        # Insert the data into the database
        db.execute("INSERT INTO birthdays (name, month, day) VALUES (:name, :month, :day)", name=name, month=month, day=day)

        # Redirect to the homepage to display the updated data
        return redirect("/")
    else:
        # Display the entries in the database on index.html
        birthdays = db.execute("SELECT name, month, day FROM birthdays")
        return render_template("index.html", birthdays=birthdays)

if __name__ == "__main__":
    app.run()
