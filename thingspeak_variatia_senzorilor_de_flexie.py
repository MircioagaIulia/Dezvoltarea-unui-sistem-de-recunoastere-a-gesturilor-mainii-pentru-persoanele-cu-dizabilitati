import time
import smbus
import requests
import serial
import numpy as np

# deschide portul serial la o rată de transfer de 9600 de biți pe secundă
bluetooth = serial.Serial("/dev/rfcomm7", 9600)  

THINGSPEAK_URL = 'https://api.thingspeak.com/update'
THINGSPEAK_CHANNEL_ID = '2163036'
THINGSPEAK_API_KEY = '6L0P2487RU6WTGQK'

# Listele pentru datele primite pentru fiecare deget
senzor1 = []
senzor2 = []
senzor3 = []
senzor4 = []
senzor5 = []

# Funcția pentru trimiterea datelor la Thingspeak
def send_to_thingspeak(data):
    payload = {                        #definire dicționar
        'api_key': THINGSPEAK_API_KEY,
        'field1': senzor1,  
        'field2': senzor2,
        'field3': senzor3,
        'field4': senzor4,
        'field5': senzor5
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
            valoare_senzor1=float(data)
            senzor1.append(valoare_senzor1) # Adăugarea valorilor în vectorul senzor1[]
            
            
            data = bluetooth.readline().decode().rstrip()  # Citirea și decodarea următoarei valori         
            valoare_senzor2=float(data)
            senzor2.append(valoare_senzor2) # Adăugarea valorilor în vectorul senzor2[]
            
            
            data = bluetooth.readline().decode().rstrip()  # Citirea și decodarea următoarei valori           
            valoare_senzor3=float(data)
            senzor3.append(valoare_senzor3) # Adăugarea valorilor în vectorul senzor3[]
            
            
            data = bluetooth.readline().decode().rstrip()  # Citirea și decodarea următoarei valori           
            valoare_senzor4=float(data)
            senzor4.append(valoare_senzor4) # Adăugarea valorilor în vectorul senzor4[]
            
            
            data = bluetooth.readline().decode().rstrip()  # Citirea și decodarea următoarei valori
            valoare_senzor5=float(data)
            senzor5.append(valoare_senzor5) # Adăugarea valorilor în vectorul senzor5[]

            send_to_thingspeak(valoare_senzor1)
            send_to_thingspeak(valoare_senzor2)
            send_to_thingspeak(valoare_senzor3)
            send_to_thingspeak(valoare_senzor4)
            send_to_thingspeak(valoare_senzor5)
       
except KeyboardInterrupt:
    bluetooth.close()
    print('Aplicația a fost întreruptă.')
    

