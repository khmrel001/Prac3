import time
import RPi.GPIO as GPIO

def main():
    
    #set pin modes
    GPIO.setmode(GPIO.BCM)
    
    #assign pin values names
    LedPin=22
    
    #set up pins
    GPIO.setup(LedPin,GPIO.OUT)
    
    #toggle led on and off after 2seconds
    while True:
        GPIO.output(7,True)
        time.sleep(2)
        GPIO.output(7,False)
        time.sleep(2)
if name==__name__=="main":
    main()
    
    
    
    