from app import app


def test_articles_list():
    with app.test_client() as client:
        response = client.get("/api/v1/articles")
        assert response.status_code == 200
        assert len(response.json) > 0


def test_articles_create():
    with app.test_client() as client:
        response = client.post("/api/v1/articles", json={
            "title": "hello",
            "body": "hello hello",
            "category_id": 1
        })
        assert response.status_code == 201
        assert response.json.get("category").get("id") == 1
        res_delete = client.delete("/api/v1/articles/" + str(response.json.get("id")))
        assert res_delete.status_code == 204