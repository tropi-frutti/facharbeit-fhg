'''
Created on 05.03.2017

@author: emillokal
'''
import read_arduino

def leistung():
    
    read_arduino.read()
    
    Measure0=globvar.measure0
    
    spannung=Measure0*0.004887585532746823  #umwandeln von 8 bit in spannungswert

    stromstaerke= stromstaerkeSpan/10 #ohm
    
    leistung=spannung*stromstaerke
    
    return leistung