const int flexPin1=A1;   //declarăm pinul analogic pentru primul senzor
const int flexPin2=A2;   //declarăm pinul analogic pentru al doilea senzor
const int flexPin3=A3;   //declarăm pinul analogic pentru al treilea senzor
const int flexPin4=A4;   //declarăm pinul analogic pentru al patrulea senzor
const int flexPin5=A5;   //declarăm piul analogic pentru al cincilea senzor

int recunoasteri_corectex=0; 
int recunoasteri_corecte=0;  //variabila ce stocheaza numarul de recunoasteri corecte
int recunoasteri_totale=0;   //variabila ce stocheaza numarul de recunoasteri totale

unsigned long timp_raspuns=0;  //variabila ce stocheaza timpul mediu de raspuns
unsigned long timp_start=0;    //variabila ce stocheaza timpul de inceput
unsigned long timp_final=0;    //variabila ce stocheaza timpul de sfarsit 

const float VCC=5;         //tensiunea de alimentare
const float RDIV=47000.0;  //rezistenta de referinta a senzorului de flexie=47KOhm

void setup() {
  Serial.begin(9600);  //initializarea comunicarii seriale

  pinMode(flexPin1, INPUT); //setarea flexPin1 ca INPUT
  pinMode(flexPin2, INPUT); //setarea flexPin2 ca INPUT
  pinMode(flexPin3, INPUT); //setarea flexPin3 ca INPUT
  pinMode(flexPin4, INPUT); //setarea flexPin4 ca INPUT
  pinMode(flexPin5, INPUT); //setarea flexPin5 ca INPUT
  
}

void loop() {
  
  timp_start=millis();  //timpul curent
  
  //variabile ce stocheaza citirile analogice
  int val_senzor_flexie1, val_senzor_flexie2, val_senzor_flexie3, val_senzor_flexie4, val_senzor_flexie5; 
  
  val_senzor_flexie1=analogRead(flexPin1);     //citeste valoarea de la flexPin1
  val_senzor_flexie2=analogRead(flexPin2);     //citeste valoarea de la flexPin2
  val_senzor_flexie3=analogRead(flexPin3);     //citeste valoarea de la flexPin3 
  val_senzor_flexie4=analogRead(flexPin4);     //citeste valoarea de la flexPin4
  val_senzor_flexie5=analogRead(flexPin5);     //citeste valoarea de la flexPin5

  //variabile ce stocheaza tensiunile calculate
  float tensiune1, tensiune2, tensiune3, tensiune4, tensiune5; 
  //variabile ce stocheaza rezistentele calculate
  float rezistenta1, rezistenta2, rezistenta3, rezistenta4, rezistenta5;  

  tensiune1=val_senzor_flexie1*VCC/1023.0;     //calculeaza tensiunea pentru primul senzor
  rezistenta1=RDIV*(VCC/tensiune1-1);          //calculeaza rezistenta pentru primul senzor

  tensiune2=val_senzor_flexie2*VCC/1023.0;    //calculeaza tensiunea pentru al doilea senzor
  rezistenta2=RDIV*(VCC/tensiune2-1);         //calculeaza rezistenta pentru al doilea senzor
 
  tensiune3=val_senzor_flexie3*VCC/1023.0;    //calculeaza tensiunea pentru al treilea senzor
  rezistenta3=RDIV*(VCC/tensiune3-1);         //calculeaza rezistenta pentru al treilea senzor
 
  tensiune4=val_senzor_flexie4*VCC/1023.0;    //calculeaza tensiunea pentru al patrulea senzor
  rezistenta4=RDIV*(VCC/tensiune4-1);         //calculeaza rezistenta pentu al patrulea senzor
 
  tensiune5=val_senzor_flexie5*VCC/1023.0;    //calculeaza tensiunea pentru al cinecilea senzor 
  rezistenta5=RDIV*(VCC/tensiune5-1);         //calculeaza rezistenta pentru al cincilea senzor
  
  String semn; //variabila ce stocheaza semnul recunoscut
    
                if(rezistenta1>=20000&&rezistenta1<45000){ //degetul mare este întins
                  if(rezistenta2>=20000&&rezistenta2<45000){ //degetul arătător este întins
                    if(rezistenta3>=20000&&rezistenta3<45000){ //degetul mijlociu este întins
                      if(rezistenta4>=20000&&rezistenta4<45000){ //degetul inelar este întins
                        if(rezistenta5>=20000&&rezistenta5<45000){ //degetul mic este întins
                        semn="5"; 
                        recunoasteri_corecte++;
                        }else{
                          if(rezistenta5>=60000&&rezistenta5<=120000){ //degetul mic este îndoit
                            semn="4";
                            recunoasteri_corecte++;
                          }  
                        }
                      }else{
                        if(rezistenta4>=60000&&rezistenta4<=120000){ //degetul inelar este îndoit
                          if(rezistenta5>=20000&&rezistenta5<45000){ //degetul mic este întins
                            semn="ajutor!";
                            recunoasteri_corecte++;
                          }else{
                          if(rezistenta5>=60000&&rezistenta4<=120000){ //degetul mic este îndoit
                            semn="3";
                            recunoasteri_corecte++;
                          }
                         }
                        }
                      }
                    }else{
                      
                      if(rezistenta3>=60000&&rezistenta3<=120000){ //degetul mijlociu este îndoit
                        if(rezistenta4>=20000&&rezistenta4<45000){ //degetul inelar este întins
                          if(rezistenta5>=20000&&rezistenta5<45000){ //degetul mic este întins
                            semn="salut!";
                            recunoasteri_corecte++;
                          }else{
                            if(rezistenta5>=60000&&rezistenta5<=120000){ //degetul mic este îndoit
                              semn="am ajuns!";
                              recunoasteri_corecte++;
                            }
                          }
                        }else{
                          if(rezistenta4>=60000&&rezistenta4<=120000){ //degetul inelar este îndoit
                            if(rezistenta5>=20000&&rezistenta5<45000){ //degetul mic este întins 
                              semn="imi este frig!"; 
                              recunoasteri_corecte++;
                            }else{
                              if(rezistenta5>=60000&&rezistenta5<=120000){ //degetul mic este îndoit
                                semn="2";
                                recunoasteri_corecte++;
                              }
                            }
                           
                            
                          }
                        }
                      }
                    }
                  }else{
                     if(rezistenta2>=60000&&rezistenta4<=120000){  //degetul arătător este îndoit
                       if(rezistenta3>=60000&&rezistenta3<=120000){ //degetul mijlociu este îndoit
                         if(rezistenta4>=60000&&rezistenta4<=120000){ //degetul inelar este îndoit
                           if(rezistenta5>=20000&&rezistenta5<45000){  //degetul mic este întins
                             semn="suna-ma!";
                             recunoasteri_corecte++;
                           }else{
                           if(rezistenta5>=60000&&rezistenta5<=120000){ //degetul mic este îndoit
                           semn="1";
                           recunoasteri_corecte++;
                           }
                          }
                        }else{
                          if(rezistenta4>=20000&&rezistenta4<45000){ //degetul inelar este întins
                            if(rezistenta5>=20000&&rezistenta5<45000){ //degetul mic este întins
                              semn="am plecat";
                              recunoasteri_corecte++;
                            }else{
                              if(rezistenta5>=60000&&rezistenta5<=120000){ //degetul mic este îndoit
                                semn="sunt obosit";
                                recunoasteri_corecte++;
                              }
                            }
                          }
                        }
                     }else{
                      if(rezistenta3>=20000&&rezistenta3<45000){  //degetul mijlociu este întins
                        if(rezistenta4>=20000&&rezistenta4<45000){  //degetul inelar este întins
                          if(rezistenta5>=20000&&rezistenta5<45000){  //degetul mic este întins
                            semn="in curand";
                            recunoasteri_corecte++;
                          }else{
                            if(rezistenta5>=60000&&rezistenta5<=120000){  //degetul mic este îndoit
                              semn="sunt gata";
                              recunoasteri_corecte++;
                            }
                          }
                        }else{
                          if(rezistenta4>=60000&&rezistenta4<=120000){  //degetul inelar este îndoit
                            if(rezistenta5>=20000&&rezistenta5<45000){  //degetul mic este întins
                              semn="repede";
                              recunoasteri_corecte++;
                            }else{
                              if(rezistenta5>=60000&&rezistenta5<=120000){  //degetul mic este îndoit
                                semn="incet";
                                recunoasteri_corecte++;
                              }
                            }
                          }
                        }
                      }
                     }
                    }
               
                  }
                }else{
                  
                  if(rezistenta1>=45000&&rezistenta1<60000){   //degetul mare este parțial îndoit
                    if(rezistenta2>=45000&&rezistenta2<60000){  //degetul arătător este parțial îndoit
                      if(rezistenta3>=45000&&rezistenta3<60000){ //degetul mijlociu este parțial îndoit
                        if(rezistenta4>=45000&&rezistenta4<60000){ //degetul inelar este parțial îndoit
                          if(rezistenta5>=45000&&rezistenta5<60000){ //degetul mic este parțial îndoit
                            semn="vreau apa!";
                            recunoasteri_corecte++;
                          }
                        }else{
                          if(rezistenta4>=20000&&rezistenta4<45000){  //degetul inelar este întins
                            if(rezistenta5>=20000&&rezistenta5<45000){ //degetul mic este întins
                              semn="continua";
                              recunoasteri_corecte++;
                            }
                          }else{
                            if(rezistenta4>=60000&&rezistenta4<=120000){ //degetul inelar este îndoit
                              if(rezistenta5>=60000&&rezistenta5<=120000){ //degetul mic este îndoit
                                semn="termina";
                                recunoasteri_corecte++;
                              }
                            }
                          }
                        }
                      }else{
                        if(rezistenta3>=60000&&rezistenta3<=120000){  //degetul mijlociu este îndoit
                          if(rezistenta4>=60000&&rezistenta4<120000){  //degetul inelar este îndoit
                            if(rezistenta5>=45000&&rezistenta5<60000){ //degetul mic este parțial îndoit
                              semn="imi este cald!";
                              recunoasteri_corecte++;
                            }else{
                              if(rezistenta5>=60000&&rezistenta5<=120000){ //degetul mic este îndoit
                                semn="putin";
                                recunoasteri_corecte++;
                              }
                            }
                          }
                        }else{
                          if(rezistenta3>=20000&&rezistenta3<45000){ //degetul mijlociu este întins
                            if(rezistenta4>=20000&&rezistenta4<45000){ //degetul inelar este întins
                              if(rezistenta5>=20000&&rezistenta5<45000){ //degetul inelar este întins
                                semn="mult";
                                recunoasteri_corecte++;
                              }
                            }
                          }
                        }
                      }
                    }else{
                      if(rezistenta2>=60000&&rezistenta2<=120000){ //degetul arătător este îndoit
                        if(rezistenta3>=60000&&rezistenta3<=120000){ //degetul mijlociu este îndoit
                          if(rezistenta4>=20000&&rezistenta4<45000){  //degetul inelar este întins
                            if(rezistenta5>=20000&&rezistenta5<45000){ //degetul mic este întins
                              semn="cand?";
                              recunoasteri_corecte++;
                            }
                          }else{
                            if(rezistenta4>=45000&&rezistenta4<60000){ //degetul inelar este parțial îndoit
                              if(rezistenta5>=45000&&rezistenta5<60000){ //degetul mic este parțial îndoit
                                semn="cum?";
                                recunoasteri_corecte++;
                              }else{
                                if(rezistenta5>=60000&rezistenta5<=120000){ //degetul mic este îndoit
                                  semn="sunt odihnit";
                                  recunoasteri_corecte++;
                                }
                              }
                            }
                            
                          }
                        }
                      }
                    }
                  }
                 else{
                  
                  if(rezistenta1>=60000&&rezistenta1<=120000){   //degetul mare este îndoit
                    if(rezistenta2>=20000&&rezistenta2<45000){    //degetul arătător este întins
                      if(rezistenta3>=20000&&rezistenta3<45000){   //degetul mijlociu este întins
                        if(rezistenta4>=20000&&rezistenta4<45000){  //degetul inelar este întins
                          if(rezistenta5>=20000&&rezistenta5<45000){ //degetul mic este întins
                            semn="da";
                            recunoasteri_corecte++;
                          }
                        }else{
                          if(rezistenta4>=60000&&rezistenta4<=120000){ //degetul inelar este îndoit 
                            if(rezistenta5>=60000&&rezistenta5<=120000){ //degetul mic este îndoit
                              semn="ma simt bine";
                              recunoasteri_corecte++;
                            }else{
                              if(rezistenta5>=20000&&rezistenta5<45000){ //degetul mic este întins 
                                semn="deschis";
                                recunoasteri_corecte++;
                              }
                            }
                          }
                        }
                      }else{
                        
                        if(rezistenta3>=60000&&rezistenta3<=120000){  //degetul mijlociu este îndoit
                          if(rezistenta4>=60000&&rezistenta4<=120000){ //degetul inelar este îndoit
                            if(rezistenta5>=20000&&rezistenta5<45000){  //degetul mic este întins
                              semn="dreapta";
                              recunoasteri_corecte++;
                            }else{
                              if(rezistenta5>=60000&&rezistenta5<=120000){ //degetul mic este îndoit
                                semn="stiu";
                                recunoasteri_corecte++;
                              }
                            }
                          }else{
                            if(rezistenta4>=20000&&rezistenta4<45000){ //degetul inelar este întins
                              if(rezistenta5>=20000&&rezistenta5<45000){ //degetul mic este întins
                                semn="inceput";
                                recunoasteri_corecte++;
                              }else{
                                if(rezistenta5>=60000&&rezistenta5<=120000){ //degetul mic este îndoit
                                  semn="aproape";
                                  recunoasteri_corecte++;
                                }
                              }
                            }
                          }
                        }
                      }
                    }else{
                      
                      if(rezistenta2>=45000&&rezistenta2<60000){  //degetul arătător este parțial îndoit
                        if(rezistenta3>=45000&&rezistenta3<60000){ //degetul mijlociu este parțial îndoit
                          if(rezistenta4>=45000&&rezistenta4<60000){ //degetul inelar este parțial îndoit
                            if(rezistenta5>=45000&&rezistenta5<60000){ //degetul mic este parțial îndoit
                              semn="nu";
                              recunoasteri_corecte++;
                            }else{
                              if(rezistenta5>=60000&&rezistenta5<=120000){ //degetul mic este îndoit
                                semn="cât este ceasul?";
                                recunoasteri_corecte++;
                                
                              }
                            }
                          }else{
                            if(rezistenta4>=60000&&rezistenta4<=120000){ //degetul inelar este îndoit
                              if(rezistenta5>=60000&&rezistenta5<=120000){ //degetul mic este îndoit
                                semn="ma simt rau";
                                recunoasteri_corecte++;
                              }else{
                                if(rezistenta5>=45000&&rezistenta5<60000){ //degetul mic este parțial îndoit
                                  semn="inchis";
                                  recunoasteri_corecte++;
                                }
                              }
                            }
                          }
                        }else{
                          if(rezistenta3>=60000&&rezistenta3<=120000){ //degetul mijlociu este îndoit
                            if(rezistenta4>=60000&&rezistenta4<=120000){ //degetul inelar este îndoit
                              if(rezistenta5>=45000&&rezistenta5<60000){ //degetul mic este parțial îndoit
                                semn="stanga";
                                recunoasteri_corecte++;
                              }
                            }else{
                              if(rezistenta4>=45000&&rezistenta4<60000){ //degetul inelar este parțial îndoit
                                if(rezistenta5>=45000&&rezistenta5<60000){ //degetul mic este parțial îndoit
                                  semn="sfarsit";
                                  recunoasteri_corecte++;
                                }else{
                                  if(rezistenta5>=60000&&rezistenta5<=120000){ //degetul mic este îndoit
                                    semn="departe";
                                    recunoasteri_corecte++;
                                  }
                                }
                              }
                            }
                          }
                        }
                      }else{
                      
                      if(rezistenta2>=60000&&rezistenta2<=120000){  //degtul arătător este îndoit
                        if(rezistenta3>=60000&&rezistenta3<=120000){ //degetul mijlociu este îndoit
                          if(rezistenta4>=60000&&rezistenta4<=120000){ //degetul inelar este îndoit
                            if(rezistenta5>=20000&&rezistenta5<45000){  //degetul mic este întins
                              semn="te rog";
                              recunoasteri_corecte++;
                            }else{
                              if(rezistenta5>=45000&&rezistenta5<60000){  //degetul mic este parțial îndoit
                                semn="multumesc";
                                recunoasteri_corecte++;
                              }else{
                                if(rezistenta5>=60000&&rezistenta5<=120000){ //degetul mic este îndoit
                                  semn="imi este foame";
                                  recunoasteri_corecte++;
                                }
                              }
                            }
                          }else{
                            if(rezistenta4>=20000&&rezistenta4<45000){  //degetul inelar este întins
                              if(rezistenta5>=20000&&rezistenta5<45000){ //degetul mic este întins
                                semn="cine?";
                                recunoasteri_corecte++;
                              }else{
                                if(rezistenta5>=60000&&rezistenta5<=120000){ //degetul mic este îndoit
                                  semn="acolo";
                                  recunoasteri_corecte++;
                                }
                              }
                            }else{
                              if(rezistenta4>=45000&&rezistenta4<60000){ //degetul inelar este parțial îndoit
                                if(rezistenta5>=60000&&rezistenta5<=120000){ //degetul mic este îndoit
                                  semn="aici";
                                  recunoasteri_corecte++;
                                  }
                                }
                            }
                         }
                        }else{
                          if(rezistenta3>=20000&&rezistenta3<45000){  //degetul mijlociu este întins
                            if(rezistenta4>=20000&&rezistenta4<45000){ //degetul inelar este întins
                              if(rezistenta5>=20000&&rezistenta5<45000){ //degetul mic este întins
                                semn="corect";
                                recunoasteri_corecte++;
                              }else{
                                if(rezistenta5>=60000&&rezistenta5<=120000){ //degetul mic este îndoit
                                  semn="vino";
                                  recunoasteri_corectex++;
                                }
                              }
                            }else{
                              if(rezistenta4>=60000&&rezistenta4<120000){ //degetul inelar este îndoit
                                if(rezistenta5>=20000&&rezistenta5<45000){ //degetul mic este întins
                                  semn="unde?";
                                  recunoasteri_corecte++;
                                }
                                }
                              }
                            }
                            else{
                            if(rezistenta3>=45000&&rezistenta3<60000){ //degetul mijlociu este parțial îndoit
                              if(rezistenta4>=45000&&rezistenta4<60000){ //degetul inelar este parțial îndoit
                                if(rezistenta5>=45000&&rezistenta5<60000){ //degetul mic este parțial îndoit
                                  semn="gresit";
                                  recunoasteri_corecte++;
                                }else{
                                  if(rezistenta5>=60000&&rezistenta5<=120000){ //degetul mic este îndoit
                                    semn="pleaca";
                                    recunoasteri_corecte++;
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
                  
                 
              }
              
        }
    
    
    Serial.println(semn); //afisarea gestului recunoscut
    
    recunoasteri_totale++; //se incrementeaza numarul recunoasterilor totale
    
    timp_final=millis();  //timpul de final

    //calculul ratei de recunoastere
    float calcul_rata_recunoastere=(float)recunoasteri_corectex/recunoasteri_totale*100; 

    //calculul timpului de răspuns
    timp_raspuns=timp_final-timp_start;

    //calculul timpului mediu de răspuns
    float timp_mediu_raspuns=(float) timp_raspuns/recunoasteri_totale;

    //afisarea valorilor senzorilor de flexie     
               // Serial.print("val_senzor_flexie1: ");
               // Serial.println(val_senzor_flexie1);
               // Serial.print("val_senzor_flexie2: ");
               // Serial.println(val_senzor_flexie2);
               // Serial.print("val_senzor_flexie3: ");
               // Serial.println(val_senzor_flexie3);
               // Serial.print("val_senzor_flexie4: ");
               // Serial.println(val_senzor_flexie4);
               // Serial.print("val_senzor_flexie5: ");
               // Serial.println(val_senzor_flexie5);

   //afisarea valorilor rezistentelor senzorilor de flexie         
              // Serial.print("Rezistenta1: ");
              // Serial.println(rezistenta1);
              // Serial.print("Rezistenta2: ");
              // Serial.println(rezistenta2);
              // Serial.print("Rezistenta3: ");
              // Serial.println(rezistenta3);
              // Serial.print("Rezistenta4: ");
              // Serial.println(rezistenta4);
              // Serial.print("Rezistenta5: ");
              // Serial.println(rezistenta5);
               
   //afisarea ratei de recunoastere a sistemului   
              //Serial.print("Rata de recunoastere=");
              //Serial.print(calcul_rata_recunoastere);
              //Serial.println("%");
   //afisarea timpului de raspuns al sistemului
              //Serial.print("Timp raspuns=");
              //Serial.println(timp_mediu_raspuns);
          
  delay(5000);  // așteaptă un moment pentru a evita supraîncărcarea portului serial
}
