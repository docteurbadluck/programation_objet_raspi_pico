from machine import Pin
import time
from led import Led
from button import Bouton

class Moteur:
    
    
    
    
    def __init__(self, relais_1, relais_2) :
        self.R1 = Pin(relais_1, Pin.OUT)
        self.R2 = Pin(relais_2,Pin.OUT)
        self.on_time = 2;
        self.break_time = 2;
        self.R1.value(0)
        self.R2.value(0)
    
    def clock_way (self):
        print("clock_way on")
        self.R1.value(1)
        self.R2.value(0)
        
        
    def anti_clock_way (self):
        print ("anti_clock_way on")
        self.R1.value(0)
        self.R2.value(1)
        
    def stop_motor(self):
        print("stop")
        self.R1.value(0)
        self.R2.value(0)
        
    def loop_test(self) :
        print("loop_test on ")
        Moteur.clock_way(self)
        time.sleep(self.on_time)
        Moteur.stop_motor(self)
        time.sleep(self.break_time)
        Moteur.anti_clock_way(self)
        time.sleep(self.on_time)
        Moteur.stop_motor(self)
        time.sleep(self.break_time)
        print("loop_test off")
        
        
class Moteur_Led(Moteur):
    
    def __init__(self, relais_1, relais_2, signal) :
        self.R1 = Pin(relais_1, Pin.OUT)
        self.R2 = Pin(relais_2,Pin.OUT)
        self.on_time = 2;
        self.break_time = 2;
        self.led_moteur = Led(signal)
        
    def loop_test(self) :
        print("loop_test on ")
        self.led_moteur.test_blink()
        
        Moteur.clock_way(self)
        time.sleep(self.on_time)
        Moteur.stop_motor(self)
        time.sleep(self.break_time)
        Moteur.anti_clock_way(self)
        time.sleep(self.on_time)
        Moteur.stop_motor(self)
        time.sleep(self.break_time)
        self.led_moteur.blink()
        print("loop_test off")        
    
    
class Moteur_Bouton(Moteur):
    
    def __init__(self, relais_1, relais_2, signal_bouton) :
        self.R1 = Pin(relais_1, Pin.OUT)
        self.R2 = Pin(relais_2,Pin.OUT)
        self.on_time = 2;
        self.break_time = 2;
        self.bouton_moteur = Bouton(signal_bouton)
        self.valeur_sens = 0
        
    def loop_test(self) :
        print("loop_test on ")
        self.clock_way()
        
        while True:
            
            if self.bouton_moteur.monBouton.value()==1 and (self.valeur_sens ==0) :
                self.stop_motor()
                self.anti_clock_way()
                self.valeur_sens =1
                time.sleep(self.break_time)

            
            if self.bouton_moteur.monBouton.value()==1 and (self.valeur_sens ==1) :
                self.stop_motor()
                self.clock_way()
                self.valeur_sens =0
                time.sleep(self.break_time)
                
class Moteur_Bouton_Led(Moteur_Bouton):
    
    def __init__(self, relais_1, relais_2, signal_bouton, signal_led) :
        self.R1 = Pin(relais_1, Pin.OUT)
        self.R2 = Pin(relais_2,Pin.OUT)
        self.on_time = 2;
        self.break_time = 2;
        self.bouton_moteur = Bouton(signal_bouton)
        self.valeur_sens = 0
        self.led_moteur = Led(signal_led)
    
    def loop_test(self) :
        print("loop_test on ")
        self.led_moteur.test_blink()
        self.clock_way()
        
        while True:
            
            if self.bouton_moteur.monBouton.value()==1 and (self.valeur_sens ==0) :
                self.stop_motor()
                self.anti_clock_way()
                self.valeur_sens =1
                time.sleep(self.break_time)

            
            if self.bouton_moteur.monBouton.value()==1 and (self.valeur_sens ==1) :
                self.stop_motor()
                self.clock_way()
                self.valeur_sens =0
                time.sleep(self.break_time)

            
        
        
