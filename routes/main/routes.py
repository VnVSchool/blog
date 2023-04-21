from app import app, db
from models import Article, Category
from flask import render_template, request, redirect


@app.route("/all")
def all():
    articles = Article.query.all()
    categories = Category.query.all()
    return render_template("main/all.html", articles=articles, categories=categories)




@app.route("/")
def index():
    return render_template("main/index.html")
