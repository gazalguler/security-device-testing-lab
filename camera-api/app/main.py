from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI(title="Security Device Testing Lab")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/camera/status")
def get_camera_status():
    return {
        "camera_id": "CAM-001",
        "status": "online"
    }


from pydantic import BaseModel
from fastapi import HTTPException
from app.simulator import simulate_camera_event


class CameraEventRequest(BaseModel):
    event_type: str


@app.post("/camera/events")
def create_camera_event(request: CameraEventRequest):
    try:
        return simulate_camera_event(request.event_type)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid camera event"
        )
