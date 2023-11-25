
# # PROJECT - TRAFFIC LIGHT SIMULATION

# ## Raspberry Pi


import RPi.GPIO as GPIO
import time


# Define GPIO pin numbers for LEDs
RED = 17
YELLOW = 27
GREEN = 22



# Setup GPIO mode and define pin configurations
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)



def traffic_light_sequence():
    # Green Phase
    GPIO.output(GREEN, GPIO.HIGH)
    time.sleep(3)

    GPIO.output(GREEN, GPIO.LOW)
    # Yellow Phase
    GPIO.output(YELLOW, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(YELLOW, GPIO.LOW)
    # Red Phase
    GPIO.output(RED, GPIO.HIGH)
    time.sleep(2)

    # Yellow Overlap
    GPIO.output(YELLOW, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(RED, GPIO.LOW)

try:
    while True:
        traffic_light_sequence()

except KeyboardInterrupt:
    # Cleanup GPIO settings on keyboard interrupt
    GPIO.cleanup()