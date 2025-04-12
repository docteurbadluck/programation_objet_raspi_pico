from machine import Pin
import time
import moteur_DC_objet


    

moteur = Moteur(2,15,5) #relais 1, relais 2, led signal

while True:  # Loop forever
    moteur.loop_test()
       


