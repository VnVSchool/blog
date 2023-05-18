from app import app, db
from models import Article, Category
# TODO add mock


def test_article_create():
    with app.test_client() as client:
        data = {"title": "New Article", "body": "New Article Body", "category": 1}
        response = client.post('/article', data=data)
        assert response.status_code == 302
        article = Article.query.filter_by(title="New Article").first()
        assert article is not None


def test_article_details():
    with app.test_client() as client:
        response = client.get('/article/11')
        assert response.status_code == 200


def test_article_get():
    with app.test_client() as client:
        response = client.get('/article/create')
        assert response.status_code == 200


def test_article_edit():
    with app.test_client() as client:
        response = client.get('/article/11/edit')
        assert response.status_code == 200


def test_article_update():
    with app.test_client() as client:
        data = {"title": "Updated Article", "body": "Updated Article Body", "category": 2}
        response = client.post('/article/11/update', data=data)
        assert response.status_code == 302
        article = Article.query.filter_by(title="Updated Article").first()
        assert article is not None


def test_article_delete():
    with app.test_client() as client:
        response = client.get('/article/11/delete')
        assert response.status_code == 302
        article = Article.query.filter_by(id=11).first()
        assert article is None


def test_category_detail():
    with app.test_client() as client:
        response = client.get('/category/1')
        assert response.status_code == 200


def test_category_create():
    with app.test_client() as client:
        response = client.get('/category/create')
        assert response.status_code == 200


def test_category_save():
    with app.test_client() as client:
        data = {"title": "New Category"}
        response = client.post('/category/save', data=data)
        assert response.status_code == 302
        category = Category.query.filter_by(title="New Category").first()
        assert category is not None


def test_search():
    with app.test_client() as client:
        response = client.get('/search?q=article')
        assert response.status_code == 200
