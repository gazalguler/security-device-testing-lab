VALID_EVENTS = {
    "online",
    "offline",
    "motion_detected",
}


def simulate_camera_event(event_type):
    if event_type not in VALID_EVENTS:
        raise ValueError("Invalid camera event")

    return {
        "camera_id": "CAM-001",
        "event": event_type,
    }
