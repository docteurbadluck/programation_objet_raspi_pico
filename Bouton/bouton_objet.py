

from machine import Pin
from utime import sleep
from led import Led


class Bouton:
    def __init__(self,pin_signal) :
        
        self.monBouton = Pin(pin_signal, Pin.IN)
        self.message_test = "button pressed"
        self.click = False
        
        
    def send (self):
        
        print("send called")
        print (self.click)
        return self.click
        
    def listening(self):
        print("listening called")
        while True:
            self.click = False     
            if self.monBouton.value() == 1:
                print(self.message_test)
                self.click = True
                self.send()
                sleep(.5)
                
                
                
class Bouton_Led(Bouton):
    
    def __init__(self,pin_signal,pin_led) :
        self.monBouton = Pin(pin_signal, Pin.IN)
        self.message_test = "button pressed"
        self.click = False
        self.led = Led(pin_led)
        
        
    def listening(self):
        print("listening called")
        self.led.test_blink()
        while True:
            self.click = False     
            if self.monBouton.value() == 1:
                print(self.message_test)
                self.click = True
                self.send()
                self.led.blink()
                
            
        
        

#mybutton = Bouton_Led(11,15)

#mybutton.listening()


#include Pin.PULL_DOWN to activate internal pull-down resistor, as follows:
#button = Pin(11, Pin.IN, Pin.PULL_DOWN)
