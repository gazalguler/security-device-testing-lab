type CameraStatus = "online" | "offline";

interface CameraResponse {
    camera_id: string;
    status: CameraStatus;
}

async function loadCameraStatus(): Promise<void> {
    const statusElement = document.getElementById("camera-status");

    if (statusElement === null) {
        throw new Error("Camera status element not found");
    }

    statusElement.textContent = "Loading...";

    try {
        const response = await fetch("http://127.0.0.1:8000/camera/status");

        if (!response.ok) {
            throw new Error("Camera API request failed");
        }

        const camera: CameraResponse = await response.json();
        statusElement.textContent =
            camera.status === "online" ? "Online" : "Offline";
    } catch (error) {
        statusElement.textContent = "Error";
        console.error("Failed to load camera status:", error);
    }
}

loadCameraStatus();
