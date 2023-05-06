from app import app


def test_home_page():
    with app.test_client() as client:
        resp = client.get("/")
        assert resp.status_code == 200
        assert b'Home' in resp.data
        assert b'Bootstrap' in resp.data


def test_category_create():
    with app.test_client() as client:
        resp = client.get("/category/create")
        assert resp.status_code == 200
        assert b'Tite category' in resp.data