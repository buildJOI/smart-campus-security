from ultralytics import YOLO

# Load the model once at import time so every call to detect() reuses it
# instead of reloading the weights from disk on every frame.
_model = YOLO("yolov8n.pt")


def detect(frame, conf=0.5):
    """
    Run YOLO object detection on a single BGR frame (as returned by
    cv2.VideoCapture.read()).

    Returns the list of ultralytics Results objects, matching the format
    app.py expects (result.boxes, result.names, box.cls, box.xyxy).
    """
    results = _model.predict(source=frame, conf=conf, verbose=False)
    return results
