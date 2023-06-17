import serial
import time
import smbus
import pygame
from RPLCD.i2c import CharLCD

# deschide portul serial la o rată de transfer de 9600 de biți pe secundă
bluetooth = serial.Serial("/dev/rfcomm7",
                          9600)  

# configurarea magistralei I2C cu indexul 1
bus = smbus.SMBus(1)
#crearea unui obiect de tip lcd
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2)

while True:
    data = bluetooth.readline().decode().rstrip()  # citirea datelor de la Arduino
    #print(data)                                   # afișarea datelor în terminal
    lcd.clear()                                    #stergere continut ecran LCD
    lcd.write_string(data)                         #afișarea datelor pe LCD
    
    if data=="1":               #verificare dacă data primită prin Bluetooth corespunde cu gestul "1"din setul de date
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/1.wav")              #încărcarea sunetului din fișierul audio "1.wav"
        sound.play()                                           #redare fișier audio "1.wav"
        
    if data=="2":               #verificare dacă data primită prin Bluetooth corespunde cu gestul "2"din setul de date  
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/2.wav")              #încărcarea sunetului din fișierul audio "2.wav"
        sound.play()                                           #redare fișier audio "2.wav"
    
    if data=="3":               #verificare dacă data primită prin Bluetooth corespunde cu gestul "3"din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/3.wav")              #încărcarea sunetului din fișierul audio "3.wav"
        sound.play()                                           #redare fișier audio "3.wav"        
                
    if data=="4":               #verificare dacă data primită prin Bluetooth corespunde cu gestul "4"din setul de date   
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/4.wav")              #încărcarea sunetului din fișierul audio "4.wav"
        sound.play()                                           #redare fișier audio "4.wav"
    
    if data=="5":               #verificare dacă data primită prin Bluetooth corespunde cu gestul "5"din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/5.wav")              #încărcarea sunetului din fișierul audio "5.wav"
        sound.play()                                           #redare fișier audio "5.wav" 

    if data=="acolo":           #verificare dacă data primită prin Bluetooth corespunde cu gestul "acolo" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/acolo.wav")          #încărcarea sunetului din fișierul audio "acolo.wav" 
        sound.play()                                           #redare fișier audio "acolo.wav"     
            
    if data=="aici":            #verificare dacă data primită prin Bluetooth corespunde cu gestul "aici" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/aici.wav")           #încărcarea sunetului din fișierul audio "aici.wav"
        sound.play()                                           #redare fișier audio "aici.wav"

    if data=="ajutor!":         #verificare dacă data primită prin Bluetooth corespunde cu gestul "ajutor!" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/ajutor.wav")         #încărcarea sunetului din fișierul audio "ajutor.wav" 
        sound.play()                                           #redare fișier audio "ajutor.wav"
 
    if data=="am ajuns!":       #verificare dacă data primită prin Bluetooth corespunde cu gestul "am ajuns!" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/am ajuns.wav")       #încărcarea sunetului din fișierul audio "am ajuns.wav"
        sound.play()                                           #redare fișier audio "am ajuns.wav"

    if data=="vreau apa!":      #verificare dacă data primită prin Bluetooth corespunde cu gestul "vreau apa!" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/apa.wav")            #încărcarea sunetului din fișierul audio "apa.wav"
        sound.play()                                           #redare fișier audio "apa.wav"

    if data=="aproape":         #verificare dacă data primită prin Bluetooth corespunde cu gestul "aproape" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/aproape.wav")        #încărcarea sunetului din fișierul audio "aproape.wav"
        sound.play()                                           #redare fișier audio "aproape.wav"
    
    if data=="ma simt bine":    #verificare dacă data primită prin Bluetooth corespunde cu gestul "ma simt bine" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/bine.wav")           #încărcarea sunetului din fișierul audio "bine.wav"
        sound.play()                                           #redare fișier audio "bine.wav"
    
    if data=="imi este cald!":  #verificare dacă data primită prin Bluetooth corespunde cu gestul "imi este cald!" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/cald.wav")           #încărcarea sunetului din fișierul audio "cald.wav"
        sound.play()                                           #redare fișier audio "cald.wav"

    if data=="cand?":           #verificare dacă data primită prin Bluetooth corespunde cu gestul "cand?" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/cand.wav")           #încărcarea sunetului din fișierul audio "cand.wav"
        sound.play()                                           #redare fișier audio "cand.wav"

    if data=="cât este ceasul?":#verificare dacă data primită prin Bluetooth corespunde cu gestul "cât este ceasul?" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/cat e ceasul.wav")   #încărcarea sunetului din fișierul audio "cat e ceasul.wav"
        sound.play()                                           #redare fișier audio "cat e ceasul.wav"
    
    if data=="cine?":           #verificare dacă data primită prin Bluetooth corespunde cu gestul "cine?" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/cine.wav")           #încărcarea sunetului din fișierul audio "cine.wav"
        sound.play()                                           #redare fișier audio "cine.wav"

    if data=="continua":        #verificare dacă data primită prin Bluetooth corespunde cu gestul "continua" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/continua.wav")       #încărcarea sunetului din fișierul audio "continua.wav"
        sound.play()                                           #redare fișier audio "continua.wav"

    if data=="corect":          #verificare dacă data primită prin Bluetooth corespunde cu gestul "corect" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer 
        sound = pygame.mixer.Sound("audio/corect.wav")         #încărcarea sunetului din fișierul audio "corect.wav"
        sound.play()                                           #redare fișier audio "corect.wav"

    if data=="cum?":            #verificare dacă data primită prin Bluetooth corespunde cu gestul "cum?" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/cum.wav")            #încărcarea sunetului din fișierul audio "cum.wav"
        sound.play()                                           #redare fișier audio "cum.wav"
        
    if data=="da":              #verificare dacă data primită prin Bluetooth corespunde cu gestul "da" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/da.wav")             #încărcarea sunetului din fișierul audio "da.wav" 
        sound.play()                                           #redare fișier audio "da.wav"

    if data=="departe":         #verificare dacă data primită prin Bluetooth corespunde cu gestul "departe" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/departe.wav")        #încărcarea sunetului din fișierul audio "departe.wav" 
        sound.play()                                           #redare fișier audio "departe.wav"

    if data=="deschis":         #verificare dacă data primită prin Bluetooth corespunde cu gestul "deschis" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/deschis.wav")        #încărcarea sunetului din fișierul audio "deschis.wav"
        sound.play()                                           #redare fișier audio "deschis.wav"

    if data=="dreapta":         #verificare dacă data primită prin Bluetooth corespunde cu gestul "dreapta" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/dreapta.wav")        #încărcarea sunetului din fișierul audio "dreapta.wav" 
        sound.play()                                           #redare fișier audio "dreapta.wav"

    if data=="imi este foame":  #verificare dacă data primită prin Bluetooth corespunde cu gestul "imi este foame" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/foame.wav")          #încărcarea sunetului din fișierul audio "foame.wav"
        sound.play()                                           #redare fișier audio "foame.wav"
    
    if data=="imi este frig!":  #verificare dacă data primită prin Bluetooth corespunde cu gestul "imi este frig!" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/frig.wav")           #încărcarea sunetului din fișierul audio "frig.wav"
        sound.play()                                           #redare fișier audio "frig.wav"

    if data=="gresit":          #verificare dacă data primită prin Bluetooth corespunde cu gestul "gresit" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/gresit.wav")         #încărcarea sunetului din fișierul audio "gresit.wav"
        sound.play()                                           #redare fișier audio "gresit.wav"
        
    if data=="inceput":         #verificare dacă data primită prin Bluetooth corespunde cu gestul "inceput" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/inceput.wav")        #încărcarea sunetului din fișierul audio "inceput.wav"
        sound.play()                                           #redare fișier audio "inceput.wav"

    if data=="incet":           #verificare dacă data primită prin Bluetooth corespunde cu gestul "incet" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/incet.wav")          #încărcarea sunetului din fișierul audio "incet.wav"
        sound.play()                                           #redare fișier audio "incet.wav"

    if data=="inchis":          #verificare dacă data primită prin Bluetooth corespunde cu gestul "inchis" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/inchis.wav")         #încărcarea sunetului din fișierul audio "inchis.wav"
        sound.play()                                           #redare fișier audio "inchis.wav"

    if data=="in curand":       #verificare dacă data primită prin Bluetooth corespunde cu gestul "in curand" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/in curand.wav")      #încărcarea sunetului din fișierul audio "in curand.wav"
        sound.play()                                           #redare fișier audio "in curand.wav"

    if data=="mult":            #verificare dacă data primită prin Bluetooth corespunde cu gestul "mult" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/mult.wav")           #încărcarea sunetului din fișierul audio "mult.wav"
        sound.play()                                           #redare fișier audio "mult.wav"

    if data=="multumesc":       #verificare dacă data primită prin Bluetooth corespunde cu gestul "multumesc" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/multu.wav")          #încărcarea sunetului din fișierul audio "multu.wav"
        sound.play()                                           #redare fișier audio "multu.wav"
    
    if data=="nu":              #verificare dacă data primită prin Bluetooth corespunde cu gestul "nu" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/nu.wav")             #încărcarea sunetului din fișierul audio "nu.wav"
        sound.play()                                           #redare fișier audio "nu.wav"

    if data=="sunt obosit":     #verificare dacă data primită prin Bluetooth corespunde cu gestul "sunt obosit" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/obosit.wav")         #încărcarea sunetului din fișierul audio "obosit.wav"
        sound.play()                                           #redare fișier audio "obosit.wav"
    
    if data=="pleaca":          #verificare dacă data primită prin Bluetooth corespunde cu gestul "pleaca" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/pleaca.wav")         #încărcarea sunetului din fișierul audio "pleaca.wav"
        sound.play()                                           #redare fișier audio "pleaca.wav"
    
    if data=="am plecat":       #verificare dacă data primită prin Bluetooth corespunde cu gestul "am plecat" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/plecat.wav")         #încărcarea sunetului din fișierul audio "plecat.wav"
        sound.play()                                           #redare fișier audio "plecat.wav"
        
    if data=="putin":           #verificare dacă data primită prin Bluetooth corespunde cu gestul "putin" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/putin.wav")          #încărcarea sunetului din fișierul audio "putin.wav"
        sound.play()                                           #redare fișier audio "putin.wav"                                     

    if data=="repede":          #verificare dacă data primită prin Bluetooth corespunde cu gestul "repede" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/repede.wav")         #încărcarea sunetului din fișierul audio "repede.wav"
        sound.play()                                           #redare fișier audio "repede.wav"

    if data=="salut!":          #verificare dacă data primită prin Bluetooth corespunde cu gestul "salut" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/salut.wav")          #încărcarea sunetului din fișierul audio "salut.wav"
        sound.play()                                           #redare fișier audio "salut.wav"

    if data=="sfarsit":         #verificare dacă data primită prin Bluetooth corespunde cu gestul "sfarsit" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/sfarsit.wav")        #încărcarea sunetului din fișierul audio "sfarsit.wav"
        sound.play()                                           #redare fișier audio "sfarsit.wav"
    
    if data=="ma simt rau":     #verificare dacă data primită prin Bluetooth corespunde cu gestul "ma simt rau" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/simt rau.wav")       #încărcarea sunetului din fișierul audio "simt rau.wav"
        sound.play()                                           #redare fișier audio "simt rau.wav"
        
    if data=="stanga":          #verificare dacă data primită prin Bluetooth corespunde cu gestul "stanga" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/stanga.wav")         #încărcarea sunetului din fișierul audio "stanga.wav"
        sound.play()                                           #redare fișier audio "stanga.wav"
    
    if data=="stiu":            #verificare dacă data primită prin Bluetooth corespunde cu gestul "stiu" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/stiu.wav")           #încărcarea sunetului din fișierul audio "stiu.wav"
        sound.play()                                           #redare fișier audio "stiu.wav"
    
    if data=="suna-ma!":        #verificare dacă data primită prin Bluetooth corespunde cu gestul "suna-ma!" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/suna.wav")           #încărcarea sunetului din fișierul audio "suna.wav"
        sound.play()                                           #redare fișier audio "suna.wav"

    if data=="sunt gata":       #verificare dacă data primită prin Bluetooth corespunde cu gestul "sunt gata" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/sunt gata.wav")       #încărcarea sunetului din fișierul audio "sunt gata.wav"
        sound.play()                                            #redare fișier audio "sunt gata.wav"
    
    if data=="sunt odihnit!":   #verificare dacă data primită prin Bluetooth corespunde cu gestul "sunt odihnit!" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/sunt odihnit.wav")    #încărcarea sunetului din fișierul audio "sunt odihnit.wav" 
        sound.play()                                            #redare fișier audio "sunt odihnit.wav"
    
    if data=="termina":         #verificare dacă data primită prin Bluetooth corespunde cu gestul "termina" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/termina.wav")         #încărcarea sunetului din fișierul audio "termina.wav"
        sound.play()                                            #redare fișier audio "termina.wav"

    if data=="te rog":          #verificare dacă data primită prin Bluetooth corespunde cu gestul "te rog" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/te rog.wav")          #încărcarea sunetului din fișierul audio "te rog.wav"
        sound.play()                                            #redare fișier audio "te rog.wav"
    
    if data=="unde?":           #verificare dacă data primită prin Bluetooth corespunde cu gestul "unde?" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/unde.wav")            #încărcarea sunetului din fișierul audio "unde.wav"
        sound.play()                                            #redare fișier audio "unde.wav" 

    if data=="vino":            #verificare dacă data primită prin Bluetooth corespunde cu gestul "vino" din setul de date 
        pygame.mixer.init()     # inițializare Pygame Mixer
        sound = pygame.mixer.Sound("audio/vino.wav")            #încărcarea sunetului din fișierul audio "vino.wav"
        sound.play()                                            #redare fișier audio "vino.wav"
        
    time.sleep(0.1) #pauza de 0.1 secunde în execuția codului
