def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_list_items(client):
    create_response = client.post("/items", json={"name": "apple"})
    assert create_response.status_code == 201
    assert create_response.json() == {"id": 1, "name": "apple"}

    list_response = client.get("/items")
    assert list_response.status_code == 200
    assert list_response.json() == [{"id": 1, "name": "apple"}]


def test_get_item(client):
    client.post("/items", json={"name": "banana"})

    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "banana"}


def test_get_missing_item_returns_404(client):
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "not found"}


def test_create_item_requires_name(client):
    response = client.post("/items", json={})
    assert response.status_code == 422
