'''
Created on 05.03.2017

@author: emillokal
'''
import read_arduino
import globvar
def leistung():
    
    read_arduino.read()    #Empfangen der Daten
    Measure0=globvar.measure0    #importieren der Daten
    spannung=Measure0*4.86/1023  #8 bit in spannungswert

    Measure1=globvar.measure1    #für die Leistung  2 werte messen
    stromstaerkeSpan=Measure1*4.86/1023  #8 bit in spannung
    stromstaerke= stromstaerkeSpan/10 #I=U/R
    
    leistung=spannung*stromstaerke
    
    return leistung    #Ausgabe der Leistung