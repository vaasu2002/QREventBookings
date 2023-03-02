import cv2
from QRBooking.Entry.verifyEntry import verifyEntry
vid = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
import time

def qr_code_reader():
    vid = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    while True:
        ret, frame = vid.read()
        data, bbox, straight_qrcode = detector.detectAndDecode(frame)
        if len(data) > 0:
            yield data
            time.sleep(3)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()

my_generator = qr_code_reader()

for data in my_generator:
    print(type(data))
    verifyEntry(data)


    # QRBooking\Entry\readQR.py