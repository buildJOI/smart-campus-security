import cv2
import datetime
import os
import time

from security.detector import detect
from security.alerts import trigger_alert
from security.zones import inside_zone, ZONE_X1, ZONE_Y1, ZONE_X2, ZONE_Y2

from database.db import init_db
from database.db import log_event

init_db()

# Create evidence folder
os.makedirs("evidence", exist_ok=True)

CAMERA_ID = "0"
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError(
        "Could not open camera index 0. Run camera_index_test.py to find "
        "a working camera index, then update the cv2.VideoCapture(...) "
        "call in app.py accordingly."
    )

restricted_mode = False

last_alert_time = 0
ALERT_COOLDOWN = 10

while True:

    success, frame = cap.read()

    if not success:
        break

    intrusion_detected = False

    if restricted_mode:
        cv2.rectangle(
            frame,
            (ZONE_X1, ZONE_Y1),
            (ZONE_X2, ZONE_Y2),
            (0, 0, 255),
            1
        )

    results = detect(frame)

    for result in results:

        boxes = result.boxes

        for box in boxes:

            cls = int(box.cls[0])

            name = result.names[cls]

            if name != "person":
                continue

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            in_zone = inside_zone(cx, cy)

            box_color = (0, 0, 255) if (restricted_mode and in_zone) else (0, 255, 0)

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                box_color,
                2
            )

            cv2.putText(
                frame,
                name,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                box_color,
                2
            )

            # Restricted Room Logic
            if restricted_mode and in_zone:

                intrusion_detected = True

                current_time = time.time()

                if current_time - last_alert_time > ALERT_COOLDOWN:

                    trigger_alert("PERSON")

                    timestamp = datetime.datetime.now().strftime(
                        "%Y%m%d_%H%M%S"
                    )

                    image_path = f"evidence/{timestamp}.jpg"

                    cv2.imwrite(
                        image_path,
                        frame
                    )

                    log_event(
                        str(datetime.datetime.now()),
                        "person",
                        "RESTRICTED_ROOM_INTRUSION",
                        CAMERA_ID
                    )

                    print(
                        f"🚨 Intrusion detected! Evidence saved: {image_path}"
                    )

                    last_alert_time = current_time

    # Mode Banner
    mode_text = (
        "RESTRICTED MODE"
        if restricted_mode
        else
        "SURVEILLANCE MODE"
    )

    mode_color = (
        (0, 0, 255)
        if restricted_mode
        else
        (0, 255, 0)
    )

    cv2.putText(
        frame,
        mode_text,
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        mode_color,
        2
    )

    # Intrusion Banner
    if intrusion_detected:

        cv2.putText(
            frame,
            "INTRUSION DETECTED",
            (10, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )

    cv2.imshow(
        "Smart Campus Security System",
        frame
    )

    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):

        restricted_mode = not restricted_mode

        if restricted_mode:
            print("🔒 Restricted Mode Enabled")
        else:
            print("👁 Surveillance Mode Enabled")

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()