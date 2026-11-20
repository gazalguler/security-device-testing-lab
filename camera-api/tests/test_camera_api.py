from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_camera_status():
    response = client.get("/camera/status")

    assert response.status_code == 200
    assert response.json() == {
        "camera_id": "CAM-001",
        "status": "online"
    }


def test_unknown_camera_endpoint():
    response = client.get("/camera/unknown")

    assert response.status_code == 404


def test_motion_detected_event():
    response = client.post(
        "/camera/events",
        json={"event_type": "motion_detected"}
    )

    assert response.status_code == 200
    assert response.json() == {
        "camera_id": "CAM-001",
        "event": "motion_detected"
    }


def test_invalid_camera_event():
    response = client.post(
        "/camera/events",
        json={"event_type": "camera_exploded"}
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid camera event"
    }


import pytest


@pytest.mark.parametrize("event_type", ["online", "offline"])
def test_camera_connection_events(event_type):
    response = client.post(
        "/camera/events",
        json={"event_type": event_type}
    )

    assert response.status_code == 200
    assert response.json() == {
        "camera_id": "CAM-001",
        "event": event_type
    }
