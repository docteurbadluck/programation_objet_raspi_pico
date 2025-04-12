
#create an object for our potentiometer on Pin(26)(only 3 pin on raspberry pico)
from machine import ADC, Pin, PWM
from utime import sleep

class capteur():
    
    def __init__(self, pin):
        self.mySensor = ADC(pin)
        self.valeur_sensor = 0
        
    def lire_valeur(self):
        total = 0
        num_samples = 10
        for _ in range(num_samples):
            total += self.mySensor.read_u16()
            sleep(0.001)
        self.valeur_sensor = total // num_samples
        print(self.valeur_sensor)
        sleep(0.01)

class capteur_pwm(capteur):
    
    def __init__(self, pin_capteur, pin_PWM, frequence=1000, break_time_def=0.0001):
        super().__init__(pin_capteur)
        self.myPWM = PWM(Pin(pin_PWM))
        self.myPWM.freq(frequence)
        self.break_time = break_time_def
        
    def lire_valeur(self):
        total = 0
        num_samples = 10
        for _ in range(num_samples):
            total += self.mySensor.read_u16()
            sleep(0.001)
        self.valeur_sensor = total // num_samples
        self.myPWM.duty_u16(self.valeur_sensor)
        print(self.valeur_sensor)
        sleep(0.01)

#mon_capteur = capteur_pwm(26, 15)

#while True:
 #   mon_capteur.lire_valeur()