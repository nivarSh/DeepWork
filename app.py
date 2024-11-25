import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///deepwork.db")

confirmSession = False

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Sets the timer"""
    return render_template("index.html")

@app.route("/start_timer", methods=["POST"])
@login_required
def start_timer():
    """Shows Timer and Tasks"""
    minutes = int(request.form.get("minutes"))
    session["minutes"] = minutes
    return render_template("start_timer.html", minutes=minutes)

@app.route("/log_session", methods=["GET"])
@login_required
def log_session():
    """Handle session confirmation"""
    global confirmSession  # Use `global` to modify the global variable
    confirmSession = True
    # Perform any additional logging or actions here
    return redirect("/history")  # Redirect to the history page after logging

@app.route("/history")
@login_required
def history():
    """Shows all DW sessions: timestamp, time, tasks"""
    # Create if to differentiate between clicking in the navbar (insert) vs announcement (don't insert)
    if session.get("minutes") and confirmSession == True:
        db.execute("INSERT INTO history (user_id, session_minutes) VALUES (? , ?)", session["user_id"], session["minutes"])
        session.pop("minutes")
    total_user_sessions = db.execute("SELECT * FROM history WHERE user_id = ?", session["user_id"])
    return render_template("history.html", total_user_sessions=total_user_sessions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()
    tasks=[]

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Username Creation
    if request.method == "POST":
        username = request.form.get("username")
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if not username or len(rows) != 0:
            return apology("Username has been taken or you haven't entered a username")
        
        # Password Creation
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not password or not confirmation or password != confirmation:
            return apology("Enter Password or Passwords does not match")
        
        # Update database for new user
        hash = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES (? , ?)", username, hash)
        rows = db.execute("SELECT * FROM users WHERE username=?", username)
        session["user_id"] = rows[0]["id"]
        return redirect("/")

    # GET
    else:
        return render_template("register.html")

