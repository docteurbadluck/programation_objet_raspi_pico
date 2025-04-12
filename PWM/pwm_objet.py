# Example using PWM to fade an LED
from machine import Pin, PWM
from time import sleep

#Create PWM object, with LED on Pin(15)
class pwm :
    
    
    def __init__(self, pin , frequence = 1000, break_time_def = 0.0001) :
        self.myPWM = PWM(Pin(pin))
        self.myPWM.freq(frequence)
        self.break_time = break_time_def
        self.duty = 0
        
    def test_fade(self):
        while True:
            for duty in range(65025):
                self.myPWM.duty_u16(duty)
                sleep(self.break_time)
                
            for duty in range(65025, 0, -1):
                self.myPWM.duty_u16(duty)
                sleep(self.break_time)
            
            
mon_pwm =pwm(15)

mon_pwm.test_fade()
