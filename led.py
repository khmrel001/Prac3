import time
import RPi.GPIO as GPIO

def main():
    GPIO.setmode(GPIO.OUT)
    GPIO.setup(7,GPIO.OUT)
    while True:
        GPIO.output(7,True)
        time.sleep(2)
        GPIO.output(7,False)
        time.sleep(2)
    
if name==__name__=="main":
    main()
    
    
    
    