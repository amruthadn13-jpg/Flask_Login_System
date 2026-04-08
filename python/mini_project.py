from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "1234":
        message = "Login Successful"
    else:
        message = "Invalid Credentials"

    return f"<h2>{message}</h2>"

app.run(debug=True)
