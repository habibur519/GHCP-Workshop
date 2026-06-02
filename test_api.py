from app import app
from main import OPTIONS


def test_post_choice_endpoint_returns_result_for_rock():
    client = app.test_client()
    response = client.post("/rock")

    assert response.status_code == 200
    body = response.get_json()
    assert body["user_choice"] == "rock"
    assert body["computer_choice"] in OPTIONS
    assert body["result"] in {"tie", "user", "computer"}


def test_post_play_payload_returns_result_for_spock():
    client = app.test_client()
    response = client.post("/play", json={"choice": "spock"})

    assert response.status_code == 200
    body = response.get_json()
    assert body["user_choice"] == "spock"
    assert body["computer_choice"] in OPTIONS
    assert body["result"] in {"tie", "user", "computer"}


def test_post_invalid_choice_returns_400():
    client = app.test_client()
    response = client.post("/fire")

    assert response.status_code == 400
    body = response.get_json()
    assert body["error"] == "Invalid choice"


def test_post_play_payload_missing_choice_returns_400():
    client = app.test_client()
    response = client.post("/play", json={})

    assert response.status_code == 400
    body = response.get_json()
    assert body["error"] == "Missing choice"
