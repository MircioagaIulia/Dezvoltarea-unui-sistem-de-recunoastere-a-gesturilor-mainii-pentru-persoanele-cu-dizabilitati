# Dezvoltarea unui sistem de recunoaștere a gesturilor mâinii pentru persoanele cu dizabilități de vorbire

# Descriere
Lucrarea mea de licență constă în dezvoltarea unui sistem de recunoaștere a gesturilor pentru persoanele cu dizabilități de vorbire.
Proiectul conține 4 fișiere și un folder: un fișier Arduino, 3 fișiere Python și un folder ce conține 50 de fișiere audio. 
Fișierul Arduino este responsabil cu citirea datelor de la senzorii de flexie, cu recunoașterea gesturilor și cu trimiterea datelor prin Bluetooth către Raspberry Pi.
Fisierul Python transmitere_arduino_raspberry.py preia datele de la Arduino, afiseaza pe un LCD gesturile și le redă cu ajutorul unui Speaker. Celelalte două fișiere Python, thingspeak_variatia_rezistentelor.py și thingspeak_variatia_senzorilor_de_flexie.py sunt responsabile cu preluarea datelor de la senzori și trimiterea acestora către ThingSpeak. Mai jos sunt prezentați pașii care trebuie urmați pentru a putea rula sistemul de recunoaștere a gesturilor mâinii.

# Cerințe hardware
- Raspberry Pi 3 Model B: A fost utilizat un Raspberry Pi 3B pentru a rula sistemul de recunoaștere a gesturilor.
- Arduino Uno R3: Am conectat Arduino Uno la Raspberry Pi prin intermediul modulului Bluetooth HC-05.
- Senzori de flexie: Am utilizat 5 senzori de flexie conectați la Arduino Uno R3 pentru a detecta gesturile mâinii.
- LCD și speaker: Un LCD și un speaker au fost conectate la Raspberry Pi pentru a afișa informații și a reda sunete.

# Cerințe software
- Raspbian OS: Este necesară instalarea Raspbian OS pe Raspberry Pi pentru a rula sistemul de recunoaștere a gesturilor.
- Arduino IDE 1.8.12: Este necesară instalarea Arduino IDE pentru a încărca codul pe placa Arduino Uno.
- Python 3.9.2: A fost utilizată versiunea 3.9.2 a limbajului Python în dezvoltarea proiectului.
- Thonny IDE: Am folosit Thonny IDE pe Raspberry Pi pentru a deschide și a executa fișierele Python.

# Instalare și configurare
1. Descarcă Raspbian OS de pe site-ul oficial: https://www.raspberrypi.com/software/.
2. Achiziționează un card SD cu o capacitate suficientă pentru a găzdui sistemul de operare și alte fișiere necesare proiectului. Este recomandat să utilizezi un card SD de cel puțin 8 GB pentru a avea suficient spațiu de stocare.
3.Conectează cardul SD la computer prin intermediul unui cititor de carduri SD.
4. Deschide programul de creare a cardului SD bootabil (de exemplu, Raspberry Pi Imager).
5. Selectează fișierul  Raspbian OS descărcat (.img sau .zip).
6. Alege unitatea corespunzătoare cardului SD în program.
7. Apasă pe butonul "Flash" sau echivalent pentru a începe procesul de scriere a  Raspbian OS pe cardul SD. Acest proces poate dura câteva minute. Încărcarea sistemului de operare pe Raspberry Pi: După ce ai creat cu succes cardul SD bootabil, poți începe încărcarea sistemului de operare pe Raspberry Pi:
8. Inserează cardul SD bootabil în slotul corespunzător de pe Raspberry Pi.
9. Conectează alimentarea la Raspberry Pi pentru a-l porni.
10.Raspberry Pi va încărca sistemul de operare Raspbian OS de pe cardul SD și vei fi întâmpinat cu interfața de configurare inițială a Raspbian OS. 
11. Urmează ghidul de configurare inițială pentru a finaliza aceste setări și a obține un sistem de operare funcțional. Configurarea Display-ului, a conexiunii de internet, a interfețelor se realizează sin interfața de configurare, care se deschide cu ajutorul comenzii:
sudo raspi-config
12. Deschide terminalul pe Raspberry Pi și instalează Arduino IDE folosind următoarele comenzi:
sudo apt update
sudo apt install arduino
13. Conectează Arduino Uno la Raspberry Pi utilizând un cablu USB.
14. Configurează Arduino IDE pentru a utiliza placa Arduino Uno și portul corespunzător.
   Rularea fișierului se face cu ajutorul butonului Verify, iar încărcarea codului pe placa Arduino se face cu ajutorul butonului Upload.
16. Configureaza Raspbian OS cu ajutorul comenzii (display, sistem, interfete,  internet)
sudo raspi-config
17. Instalează Python 3.9.2 pe Raspberry Pi folosind următoarele comenzi:
sudo apt update
sudo apt install python3.9
18. Descarcă și instalează Thonny IDE pe Raspberry Pi folosind următoarele comenzi:
sudo apt update
sudo apt install thonny
11. Pentru rularea scripturilor de Python este necesară instalarea următoarelor biblioteci:
-serial:
pip install pyserial
- pygame
pip install pygame
- smbus
sudo apt install python3-smbus
- RPLCD
pip install RPLCD 
- requests
pip install requests
- numpy
pip install numpy
12. Instalează VLC pentru redarea sunetelor
sudo apt update
sudo apt install vlc
13. Configurarea Bluetooth
sudo bluetoothctl
scan on – pentru scanarea dispozitivelor bluetooth active
pair 98:D3:51:F6:00:3F -imperecherea cu dispozitivul bluetooth HC-05 a carei adresa MAC este 98:D3:51:F6:00:3F
exit
sudo rfcomm bind  7 98:D3:51:F6:00:3F- crează legatura intre canalul Bluetooth serial si adresa MAC a dispozitivului HC-05 cu care dorim sa stabilim conexiunea. 
După efectuarea pașilor de mai sus, sistemul de recunoaștere a gesturilor poate fi rulat apelând scriptul Python  transmitere_arduino_raspberry.py. Pentru funcționarea corectă este nevoie ca acest fișier să fie în acelasi folder cu folderul "audio" în interiorul căruia se află sunetele corespunzătoare fiecărui gest.
