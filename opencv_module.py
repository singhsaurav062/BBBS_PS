import numpy as np
import cv2
import serial
import time

def measureLightIntensity():
    # Simulated function to measure light intensity
    # Replace this function with actual code to measure light intensity
    # Return a value representing the light intensity, e.g., lux
    return 500  # Example value

def detectCars():
    rectangles = []
    casc = cv2.CascadeClassifier(r"C:\Users\saura\OneDrive\Desktop\BBBS_Problem\cars.xml")

    while True:
        light_intensity = measureLightIntensity()

        if light_intensity < 100 or light_intensity > 1000:
            print("Light intensity outside acceptable range. Waiting for adjustment...")
            time.sleep(1)  # Wait for 1 second and check again
            continue

        vc = cv2.VideoCapture(0)  # 0 represents the default camera, you can change it to another camera index if needed

        if not vc.isOpened():
            print("Error: Failed to open camera.")
            return

        while True:
            val, frame = vc.read()
            if not val:
                print("Error: Couldn't retrieve frame from the camera.")
                break

            frameHeight, frameWidth, _ = frame.shape
            frame = cv2.resize(frame, (1000, 1000))
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Haar cascade detection for cars
            cars = casc.detectMultiScale(gray, 1.3, 3)

            for (x, y, w, h) in cars:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

            cv2.imshow("Result", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
                break

        vc.release()
        cv2.destroyAllWindows()

detectCars()
