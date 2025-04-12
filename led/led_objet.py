#import the modules we will be using
import machine
import utime

class Led :
    
    def __init__(self, pin) :
        self.myLed = machine.Pin(pin, machine.Pin.OUT)
        self.myLed.value(0)
        self.on_time = 0.3
        self.break_time = 0.3
        
    def test_blink(self):
        print("test_blink on")
        self.myLed.value(0)
        for n  in range(6) :
            self.myLed.toggle()
            utime.sleep(self.break_time)
            
    def turn_on(self):
        print("turn_on called")
        self.myLed.value(1)
        
    def turn_off(self):
        print("turn_off called")
        self.myLed.value(0)
    
    
