from app import app, db
from models import Article, Category
from flask import render_template, request, redirect


@app.route("/")
def main():
    articles = Article.query.all()
    categories = Category.query.all()
    return render_template("main/index.html", articles=articles, categories=categories)

