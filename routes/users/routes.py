import bcrypt
from app import app, db
from models import User
from flask import render_template, request, redirect, session


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        user = User(
            first_name=request.form.get("first_name"),
            last_name=request.form.get("last_name"),
            email=request.form.get("email"),
            password=bcrypt.hashpw(request.form.get("password").encode("utf-8"), bcrypt.gensalt())
        )
        db.session.add(user)
        db.session.commit()
        session["user"] = user.serialize
        return redirect("/")
    else:
        return render_template("main/sign-up.html")


@app.route("/sign-in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        user = User.query.filter(User.email == request.form.get("email")).first()
        if user:
            if bcrypt.checkpw(request.form.get("password").encode("utf-8"), user.password.encode("utf-8")):
                session["user"] = user.serialize
        return redirect("/")
    else:
        return render_template("main/sign-in.html")


@app.route("/logout")
def logout():
    del session["user"]
    return redirect("/")