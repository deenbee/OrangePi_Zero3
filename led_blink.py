import wiringpi
from wiringpi import GPIO
import time

# Initialize WiringPi
if wiringpi.wiringPiSetup() == -1:
    print("WiringPi setup failed!")
    exit(1)

# Set GPIO pin 2 as OUTPUT
pin = 11
wiringpi.pinMode(11, GPIO.OUTPUT)
wiringpi.pinMode(12, GPIO.OUTPUT)
wiringpi.pinMode(14, GPIO.OUTPUT)

print("Blinking LED on GPIO pin 2...")

def turn_all_off(delay_time):
    wiringpi.digitalWrite(11, GPIO.LOW)
    wiringpi.digitalWrite(12, GPIO.LOW)
    wiringpi.digitalWrite(14, GPIO.LOW)
    time.sleep(delay_time)

def sequencia1(dl_time):
    # Turn LED ON
    wiringpi.digitalWrite(11, GPIO.HIGH)
    wiringpi.digitalWrite(12, GPIO.HIGH)
    wiringpi.digitalWrite(14, GPIO.HIGH)
    time.sleep(dl_time)  # Wait for 0.5 seconds
    turn_all_off(0.2)     
        
def sequencia2():
    wiringpi.digitalWrite(11, GPIO.HIGH)
    time.sleep(0.1)
    wiringpi.digitalWrite(12, GPIO.HIGH)
    time.sleep(0.15)
    wiringpi.digitalWrite(14, GPIO.HIGH)
    time.sleep(0.2)
    turn_all_off(0.2)  
    
def sequencia3():
    wiringpi.digitalWrite(14, GPIO.HIGH)
    time.sleep(0.1)
    wiringpi.digitalWrite(12, GPIO.HIGH)
    time.sleep(0.15)
    wiringpi.digitalWrite(11, GPIO.HIGH)
    time.sleep(0.2)
    turn_all_off(0.2)
    
def sequencia4(dl_time, cicle):
    for i in range(cicle):
        wiringpi.digitalWrite(14, GPIO.HIGH)
        time.sleep(dl_time)
        wiringpi.digitalWrite(14, GPIO.LOW)
        
        wiringpi.digitalWrite(11, GPIO.HIGH)
        time.sleep(dl_time)
        wiringpi.digitalWrite(11, GPIO.LOW)
        
        wiringpi.digitalWrite(12, GPIO.HIGH)
        time.sleep(dl_time)
        wiringpi.digitalWrite(12, GPIO.LOW)
        
def sequencia5(dl_time, cicle):
    for i in range(cicle):
        wiringpi.digitalWrite(12, GPIO.HIGH)
        time.sleep(dl_time)
        wiringpi.digitalWrite(12, GPIO.LOW)
        
        wiringpi.digitalWrite(11, GPIO.HIGH)
        time.sleep(dl_time)
        wiringpi.digitalWrite(11, GPIO.LOW)
        
        wiringpi.digitalWrite(14, GPIO.HIGH)
        time.sleep(dl_time)
        wiringpi.digitalWrite(14, GPIO.LOW)     
        
try:
    while True:
        sequencia1(0.5)
        sequencia2()
        sequencia3()
        sequencia4(0.2, 4)
        sequencia5(0.2, 4)
except KeyboardInterrupt:
    # Graceful exit on Ctrl+C
    print("\nExiting program.")
    turn_all_off(0.1)  # Ensure LED is OFF before exiting
