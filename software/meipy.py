# メインのプログラム
import cv2
import os
import datetime
import RPi.GPIO as GPIO
import collection
import time
import servo
import signal 

GPIO.setmode(GPIO.BCM)

LED_PIN = 3
GPIO.setup(LED_PIN,GPIO.OUT)
SWITCH_PIN = 2
GPIO.setup(SWITCH_PIN,GPIO.IN)
SERVO_PIN = 4
servo.init(SERVO_PIN)

db_path = "/home/pi/workspace/software/db"

signal.signal(signal.SIGINT, servo.handler)

def save_frame_camera_key(device_num, dir_path, basename, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)
    pre_pin_input = False
    pin_input = False

    print("waiting...")
    while True:
        ret, frame = cap.read()
       # cv2.imshow(window_name, frame)
        key = cv2.waitKey(delay) & 0xFF
        pre_pin_input = pin_input
        pin_input = GPIO.input(SWITCH_PIN)

        if (pre_pin_input == GPIO.HIGH) and (pin_input == GPIO.LOW) :
            d = datetime.datetime.now()
            time_str = d.strftime('%Y-%m-%d-%H-%M-%S')
            filename = '{}_{}.{}'.format(base_path, time_str, ext)
            cv2.imwrite(filename, frame)
            print("saved:",filename)

            result = collection.authenticate(filename)
            if result[0] != "":
              print("welcome",result[0])
              GPIO.output(LED_PIN,GPIO.HIGH)
              servo.drive(SERVO_PIN)
              GPIO.output(LED_PIN,GPIO.LOW)
            else:
              print("誰だよ")
            print("waiting...")

        if key == ord('q'):
            break

    cv2.destroyWindow(window_name)

save_frame_camera_key(0, 'data/visitor', 'camera_capture')
GPIO.cleanup()
