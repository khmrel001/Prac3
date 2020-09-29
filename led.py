import time
import RPi.GPIO as GPIO

def main():
    
    #set pin modes
    GPIO.setmode(GPIO.BCM)
    
    #assign pin values names
    ledPin=22
    pushButton=5
    
    #set up pins
    GPIO.setup(LedPin,GPIO.OUT)
    GPIO.setup(LedPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    
    #toggle led on and off as switch is pressed
    while True:
        #button press
        buttonPress= GPIO.input(PushButton)      
        
        #turn on led if button was pressed and the led was off
        if buttonPress == False and ledPin==False:
            GPIO.output(ledPin,True)
        #turn off led if the button was pressed and the led was on
        elif buttonPress== False and ledPin==True:
            GPIO.output(ledPin,False)
        time.sleep(0.1)
    
        
if name==__name__=="main":
    main()
    
    
    
    