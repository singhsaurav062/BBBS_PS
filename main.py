import numpy as np
import cv2
import serial
import time


 
def detectCars(filename):
  rectangles = []
  casc = cv2.CascadeClassifier(r"cars.xml")

  vc = cv2.VideoCapture(r"sample.mp4")

  if vc.isOpened():
      val , frame = vc.read()
  else:
      val = False


  while val:
    val, frame = vc.read()
    frameHeight, frameWidth, depth = frame.shape
    frame = cv2.resize(frame, ( 800,  600 ))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # haar detection.
    cars = casc.detectMultiScale(gray, 1.3, 3)


    for (x, y, w, h) in cars:
      #send_signal('1')
      cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow("Result",frame)

    if cv2.waitKey(33) == ord('q'):
      break

  vc.release()


detectCars(cv2.VideoCapture)


'''arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

def send_signal(signal):
  arduino.write(bytes(signal, 'utf-8'))
  time.sleep(0.05)
  data = arduino.readline()
  return data'''
