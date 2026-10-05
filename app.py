from flask import Flask, render_template, redirect, url_for, session, request, flash
from database import Database

app = Flask(__name__)

app.secret_key = "change-this-secret-key"

db = Database()


@app.route("/")
def index():
    if "user_id" not in session:
        return redirect(url_for("login"))

    return redirect(url_for("dashboard"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = db.authenticate(username, password)

        if user:
            session["user_id"] = user["id"]
            session["full_name"] = user["full_name"]
            return redirect(url_for("dashboard"))

        flash("Invalid username or password.")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    stats = db.get_dashboard_stats(session["user_id"])

    return render_template(
        "dashboard.html",
        stats=stats,
        full_name=session["full_name"]
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        full_name = request.form["full_name"]
        username = request.form["username"]
        password = request.form["password"]
        confirm = request.form["confirm"]

        if password != confirm:
            flash("Passwords do not match.")
            return redirect(url_for("register"))

        # continue your registration code here
        


    if request.method == "POST":

        full_name = request.form["full_name"]
        username = request.form["username"]
        password = request.form["password"]
        confirm = request.form["confirm"]

        if password != confirm:
            flash("Passwords do not match.")
            return redirect(url_for("register"))

        success, message = db.register_user(
            full_name,
            username,
            password
        )

        if success:
            flash("Account created successfully.")
            return redirect(url_for("login"))

        flash(message)

    return render_template("register.html")
@app.route("/subjects")
def subjects():

    if "user_id" not in session:
        return redirect(url_for("login"))

    records = db.get_subjects(session["user_id"])

    return render_template(
        "subjects.html",
        subjects=records
    )
def get_tasks(user_id):
    return 
@app.route("/tasks")
def tasks():
    if "user_id" not in session:
        return redirect(url_for("login"))

    records = get_tasks(session["user_id"])

    return render_template(
        "tasks.html",
        tasks=records
    )
@app.route("/study-sessions")
def study_sessions():
    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("study_sessions.html")
@app.route("/reports")
def reports():
    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("reports.html")
if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)