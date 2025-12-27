import cv2
from verify_pass import verify

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera not detected")
    exit()

detector = cv2.QRCodeDetector()
print("📸 Show QR code to camera. Press ESC to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    data, bbox, _ = detector.detectAndDecode(frame)

    if data:
        pass_id = data.strip()
        print("🆔 Scanned Pass ID:", pass_id)
        print(verify(pass_id))
        break

    cv2.imshow("QR Scanner", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

