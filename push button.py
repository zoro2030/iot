import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
Btn = 3
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Btn, GPIO.IN)


while 1:
    value = GPIO.input(Btn)
    print(value)
