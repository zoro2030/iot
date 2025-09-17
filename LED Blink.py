# Raspberry Pi GPIO Test Script
# Tests BCM pins 0–23 by blinking each one for 1 second
# Run with: sudo python3 gpio_test.py

import RPi.GPIO as GPIO
import time

# Use BCM numbering
GPIO.setmode(GPIO.BCM)

# List of pins to test
pins = list(range(0, 24))  # 0–23

# Set up all pins as outputs
for pin in pins:
    try:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
    except Exception as e:
        print(f"Skipping GPIO {pin}: {e}")

print("Starting GPIO test (0–23)... Press Ctrl+C to stop.")

try:
    while True:
        for pin in pins:
            try:
                GPIO.output(pin, GPIO.HIGH)
                print(f"GPIO {pin} ON")
                time.sleep(1)
                GPIO.output(pin, GPIO.LOW)
                print(f"GPIO {pin} OFF")
            except Exception as e:
                print(f"Error with GPIO {pin}: {e}")

except KeyboardInterrupt:
    print("\nTest stopped by user.")

finally:
    GPIO.cleanup()
    print("GPIO cleanup done.")
