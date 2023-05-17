from app import api, db
from flask_restful import Resource
from flask import request
from models import Article, Category


class ArticleResource(Resource):
    def get(self):
        article_query = Article.query
        if request.args.get("id"):
            article_query = article_query.filter(Article.id == request.args.get("id"))
        if request.args.get("title"):
            article_query = article_query.filter(Article.title == request.args.get("title"))
        if request.args.get("body"):
            article_query = article_query.filter(Article.body.like("%" + request.args.get("body") + "%"))

        articles = article_query.all()
        articles_list = []
        for article in articles:
            articles_list.append(article.serialize)
        return articles_list

    def post(self):
        data = request.json
        article = Article(
            title=data.get("title"),
            body=data.get("body"),
            category_id = data.get("category_id")
        )
        db.session.add(article)
        db.session.commit()
        return article.serialize, 201


class ArticleSingleResource(Resource):
    def get(self, id):
        article = Article.query.get(id)
        data = article.serialize
        return data

    def put(self, id):
        article = Article.query.get(id)
        article.title = request.json.get("title")
        article.body = request.json.get("body")
        article.category_id = request.json.get("category_id")
        db.session.add(article)
        db.session.commit()
        return article.serialize

    def delete(self, id):
        article = Article.query.get(id)
        db.session.delete(article)
        db.session.commit()
        return {}, 204


class CategoryResource(Resource):
    def get(self):
        category_query = Category.query
        if request.args.get("id"):
            category_query = category_query.filter(Category.id == request.args.get("id"))
        if request.args.get("title"):
            category_query = category_query.filter(Category.title == request.args.get("title"))

        categories = category_query.all()
        categories_list = []
        for category in categories:
            categories_list.append(category.serialize_with_article)
        return categories_list


api.add_resource(ArticleResource, "/api/v1/articles")
api.add_resource(ArticleSingleResource, "/api/v1/articles/<int:id>")
api.add_resource(CategoryResource, "/api/v1/categories")
