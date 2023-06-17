import time
import smbus
import requests
import serial
import numpy as np

 # deschide portul serial la o rată de transfer de 9600 de biți pe secundă
bluetooth = serial.Serial("/dev/rfcomm7", 9600) 

THINGSPEAK_URL = 'https://api.thingspeak.com/update'
THINGSPEAK_CHANNEL_ID = '2165910'
THINGSPEAK_API_KEY = 'ENKZVWDDPOBAWY9J'

# Listele pentru datele primite pentru fiecare deget
rezistenta1 = []
rezistenta2 = []
rezistenta3 = []
rezistenta4 = []
rezistenta5 = []

# Funcția pentru trimiterea datelor la Thingspeak
def send_to_thingspeak(data):
    payload = {                        #definire dicționar
        'api_key': THINGSPEAK_API_KEY,
        'field1': rezistenta1,  
        'field2': rezistenta2,
        'field3': rezistenta3,
        'field4': rezistenta4,
        'field5': rezistenta5
    }

    try:
        response = requests.get(THINGSPEAK_URL, params=payload)
        if response.status_code == 200:
            print('Datele au fost trimise cu succes la Thingspeak.')
        else:
            print('Eroare la trimiterea datelor la Thingspeak. Cod de eroare:', response.status_code)
    except requests.exceptions.RequestException as e:
        print('Eroare la trimiterea datelor la Thingspeak:', str(e))

# Bucla principală pentru a citi datele de la Arduino și a le trimite la Thingspeak
try:
                  
    while True:
            data = bluetooth.readline().decode().rstrip()  # Citirea și decodarea datelor
            valoare_rezistenta1=float(data)
            rezistenta1.append(valoare_rezistenta1) # Adăugarea valorii în vectorul rezistenta1[]
            
            
            data = bluetooth.readline().decode().rstrip()  # Citirea și decodarea următoarei valori         
            valoare_rezistenta2=float(data)
            rezistenta2.append(valoare_rezistenta2) # Adăugarea valorii în vectorul rezistenta2[]
            
            
            data = bluetooth.readline().decode().rstrip()  # Citirea și decodarea următoarei valori           
            valoare_rezistenta3=float(data)
            rezistenta3.append(valoare_rezistenta3) # Adăugarea valorii în vectorul rezistenta3[]
            
            
            data = bluetooth.readline().decode().rstrip()  # Citirea și decodarea următoarei valori           
            valoare_rezistenta4=float(data)
            rezistenta4.append(valoare_rezistenta4) # Adăugarea valorii în vectorul rezistenta4[]
            
            
            data = bluetooth.readline().decode().rstrip()  # Citirea și decodarea următoarei valori
            valoare_rezistenta5=float(data)
            rezistenta5.append(valoare_rezistenta5) # Adăugarea valorii în vectorul rezistenta5[]

            send_to_thingspeak(valoare_rezistenta1)
            send_to_thingspeak(valoare_rezistenta2)
            send_to_thingspeak(valoare_rezistenta3)
            send_to_thingspeak(valoare_rezistenta4)
            send_to_thingspeak(valoare_rezistenta5)
       
except KeyboardInterrupt:
    bluetooth.close()
    print('Aplicația a fost întreruptă.')
    


