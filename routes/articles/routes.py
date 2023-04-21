from app import app, db
from models import Article, Category
from flask import render_template, request, redirect


@app.route("/article/<int:id>")
def article_details(id):
    categories = Category.query.all()
    article = Article.query.get(id)
    return render_template("main/article_detail.html", article=article, categories=categories)


@app.route("/article/create")
def article_create():
    categories = Category.query.all()
    return render_template("main/article_form.html", categories=categories)


@app.route("/article", methods=["POST"])
def article_save():
    data = request.form
    article = Article(title=data.get("title"), body=data.get("body"), category_id=int(data.get("category")))
    db.session.add(article)
    db.session.commit()
    return redirect("/")


@app.route("/article/<int:id>/edit")
def article_edit(id):
    article = Article.query.get(id)
    categories = Category.query.all()

    return render_template("main/article_form.html", article=article, categories=categories)


@app.route("/article/<int:id>/update", methods=["POST"])
def article_update(id):
    article = Article.query.get(id)
    article.title = request.form.get("title")
    article.body = request.form.get("body")
    article.category_id = request.form.get("category")
    db.session.add(article)
    db.session.commit()
    return redirect("/")


@app.route("/article/<int:id>/delete")
def article_delete(id):
    article = Article.query.get(id)
    db.session.delete(article)
    db.session.commit()
    return redirect("/")


@app.route("/category/<int:id>")
def category_detail(id):
    category = Category.query.get(id)
    categories = Category.query.all()
    return render_template("main/index.html", articles=category.articles, categories=categories)


@app.route("/category/create")
def category_create():
    categories = Category.query.all()
    return render_template("main/category_form.html", categories=categories)


@app.route("/category/save", methods=["POST"])
def category_save():
    data = request.form
    category = Category(title=data.get("title"))
    db.session.add(category)
    db.session.commit()
    return redirect("/")


@app.route("/search")
def search():
    categories = Category.query.all()
    q = request.args.get("q", "")
    articles = Article.query.filter(Article.title.like("%" + q + "%") | Article.body.like("%" + q + "%")).all()
    return render_template("main/index.html", articles=articles, categories=categories)
