import read_arduino
import math
import globvar

def temperatur():

	
	read_arduino.read()
		#Berechnung des Widerstandswert vom NTC
	tempOhmREF =1100
	Measure0=float(globvar.measure0)
	tempSPAN =Measure0*0.0048875855327468 #umwandeln von 8 bit in spannungswert
		#anwenden von u/(r1+r2)= u2/r2 umgewandelt zu r1=((u*r2)/u2)-r2
	tempZS1 =5*tempOhmREF
	tempZS2 =tempZS1/tempSPAN 
	tempNTCohm =tempZS2-tempOhmREF
		
		#Berechnung der Temperatur anhand von widerstand + ntc Eigenschaften
	tempZS1= tempNTCohm/1008154053
	tempZS2 =math.log10(tempZS1)	
	TempKelvin =3435/tempZS2
		
	Temperatur= TempKelvin-273.15 #umwandeln in Celsius
		
	return Temperatur
	
