from machine import PWM, Pin
from utime import sleep
import time


minDuty = 1900
maxDuty = 7200

class Servo_motor :
    position = minDuty
    
    def __init__(self, signal_sm, increment=1, breakTime=0.001):
        self.mon_servo = PWM(Pin(signal_sm))
        self.mon_servo.freq(50)
        self.inc = increment
        self.break_time =breakTime
        
    def aller_retour(self):
        print("aller_retour called")

        while True:
            self.aller_max()
            self.aller_min()
        
    def aller_max(self):
        print("aller_max called")

        while self.position < maxDuty :
            self.position += self.inc
            sleep(self.break_time)
            self.mon_servo.duty_u16(self.position)
            if self.position > maxDuty :
                self.position = maxDuty
                
    def aller_min(self):
        print("aller_min called")
        while self.position > minDuty :
            self.position -= self.inc
            sleep(self.break_time)
            self.mon_servo.duty_u16(self.position)
            if self.position < minDuty :
                self.position = minDuty
    
    def change_increment(self, new_inc):
        setattr(self, 'inc',new_inc)
    def change_break_time(self, new_break_time):
        setattr(self, 'break_time',new_break_time)



sm = Servo_motor(15,7)
sm.aller_max()
sm.change_increment(2)
sm.aller_min()
sm.change_break_time(0.002)
sm.aller_retour()
    
        
  