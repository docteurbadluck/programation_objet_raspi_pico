from machine import PWM, Pin
from utime import sleep
import time

button_mode = Pin(4, Pin.IN, Pin.PULL_DOWN)
button_change_light = Pin(10, Pin.IN, Pin.PULL_DOWN)

counter =0

myDelay = 1 # myDelay is quarter of a second


minDuty = 1900
maxDuty = 7200

class Module :
    position = minDuty
    
    def __init__(self, pin_led):
        self.led = Pin(pin_led, Pin.OUT)
        self.led.value(0)
        
    def on(self) :
        print("on")
        self.led.value(1)
    def off(self) :
        print("off")
        self.led.value(0)
#////////////////////////////////////////////////////////////////////////////////////////

list_module = []
list_module.append(Module( 22)) 
list_module.append(Module( 17)) 
list_module.append(Module( 19)) #all check 



#/////////////////////////////////////////////////////////////////////////////////////////
    
def ensemble():
    for m in list_module:
        m.on()
        
    sleep(2)
    
    return True


def testLampe():
    print("allumé")
    for m in list_module:
        m.on()
    sleep(0.2)
    
    for m in list_module:
        m.off()
    sleep(0.2)
    print("éteint")
    for m in list_module:
        m.on()
    sleep(0.2)
    for m in list_module:
        m.off()
    sleep(0.2)
    print("éteint")
    for m in list_module:
        m.on()
    sleep(0.2)
        
    return True
            
    

while True:
  
  sleep(2)
  ensemble()
  if button_mode.value() == 1:
        print("Mode manuel")
        testLampe()
        sleep(myDelay)
        while (button_mode.value() == 0) :
            if button_change_light.value() == 1:
                counter +=1
                i = counter%3
                print ("next light : ")
                for m in list_module:
                    m.off()
        
                list_module[i].on()
                sleep(myDelay)
        print("Mode automatique")
                
                

    
    
        
  