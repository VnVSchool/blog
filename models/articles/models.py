from app import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

    @property
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "category": self.category.serialize
        }

    @property
    def serialize_without_category(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
        }



class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    articles = db.relationship("Article", backref="category")

    @property
    def serialize_with_article(self):
        articles = []
        for article in self.articles:
            articles.append(article.serialize_without_category)
        return {
            "id": self.id,
            "title": self.title,
            "articles": articles
        }

    @property
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title
        }
