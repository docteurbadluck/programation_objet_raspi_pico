from machine import Pin
from time import sleep
from moteur_DC_objet import Moteur_Led


    

#moteur = Moteur_Led(2,15,25) #relais 1, relais 2, led signal

#while True:  # Loop forever
 #   moteur.loop_test()
  
pin1 =  Pin(15, Pin.IN);
  
print(pin1.read())