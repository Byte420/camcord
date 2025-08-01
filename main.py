import os
import subprocess
import uuid
from datetime import datetime
import yaml

def load_camera_config(name):
    with open("cameras.yaml", "r") as f:
        config = yaml.safe_load(f)
        for cam in config["cameras"]:
            if cam["name"].lower() == name.lower():
                return cam
    raise ValueError(f"Camera '{name}' not found in cameras.yaml")

def take_snapshot(camera):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{camera['name']}_{timestamp}_{uuid.uuid4().hex[:6]}.jpg"
    output_path = os.path.join("snapshots", filename)

    # Build RTSP URL from camera fields
    url = f"rtsp://{camera['username']}:{camera['password']}@{camera['ip']}:{camera['port']}{camera['path']}"

    cmd = [
        "ffmpeg",
        "-rtsp_transport", "tcp",
        "-i", url,
        "-frames:v", "1",
        "-q:v", "2",
        output_path,
        "-y",
    ]

    try:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=10)
    except subprocess.TimeoutExpired:
        raise RuntimeError("Snapshot timed out")

    if not os.path.exists(output_path):
        raise RuntimeError("Snapshot failed to generate output file")

    return output_path

