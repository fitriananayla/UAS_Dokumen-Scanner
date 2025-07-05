import cv2

print("Versi OpenCV:", cv2.__version__)

# Coba buka kamera
cap = cv2.VideoCapture(0)
success, frame = cap.read()

if success:
    print("Berhasil membuka kamera")
    cv2.imshow("Test Kamera", frame)
    cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()
else:
    print("Gagal membuka kamera")
