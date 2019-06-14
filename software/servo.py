# サーボモータ制御用モジュール

import RPi.GPIO as GPIO
import time
import signal
import sys

def handler(signal, frame):
  GPIO.cleanup()
  sys.exit(0)

def init(pin):
  GPIO.setup(pin, GPIO.OUT)

def drive(pin):
  servo = GPIO.PWM(pin, 50)

  servo.start(0)

  servo.ChangeDutyCycle(2.5)
  time.sleep(7.0)

  servo.ChangeDutyCycle(12)
  time.sleep(3.0)

  servo.stop()
