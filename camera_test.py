import cv2

for i in range(10):
    cap = cv2.VideoCapture(i)

    if cap.isOpened():
        ret, frame = cap.read()
        print(f"Camera {i}: Opened = {ret}")
    else:
        print(f"Camera {i}: Not found")

    cap.release()

cv2.destroyAllWindows()