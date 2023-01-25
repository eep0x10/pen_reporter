import os 
from flask import Flask, redirect, render_template, request, session 

app = Flask(__name__)
app.secret_key = os.urandom(24) 

@app.route("/")
def index():   
    if "username" in session:
        return render_template("index.html", username=session["username"])

    else:
        return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")


app.run()