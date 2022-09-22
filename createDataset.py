import cv2
import os
import time

class_name = input("Enter Class Name : ")
path = r"C:\Users\parul.chutani\opencv3hrs\Resources\Dataset/%s/" %class_name
webcam = cv2.VideoCapture(0)
counter = 0

while True:
    success, frame = webcam.read()
    cv2.imshow("Video", frame)

    if os.path.exists(path):
        # while (counter<=100):
        os.chdir(path)
        # filename = class_name + '_' + str(counter) + '.jpg'
        cv2.imwrite(str(counter) + '.jpg', frame )
        time.sleep(0.5)
        counter+=1
    else:
        os.mkdir(path)
        filename = class_name + '_' + str(counter) + '.jpg'
        cv2.imwrite(filename, frame)
        counter += 11

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


webcam.release()
cv2.destroyAllWindows()