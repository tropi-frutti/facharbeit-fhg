import read_arduino
import math
import globvar

def temperatur():
	
	
	read_arduino.read()
		#Berechnung des Widerstandswert vom NTC
	tempOhmREF =1100
	Measure0=float(globvar.measure0)
	tempSPAN =Measure0*0.004887585532746823 #umwandeln von 8 bit in spannungswert
		#anwenden von u/(r1+r2)= u2/r2 umgewandelt zu r1=((u*r2)/u2)-r2
	tempZS1 =5*tempOhmREF
	tempZS2 =tempZS1/tempSPAN 
	tempNTCohm =tempZS2-tempOhmREF
	
	##tempNTCohm=10000	
		#Berechnung der Temperatur anhand von widerstand + ntc Eigenschaften
	ntczs1=tempNTCohm/10000
	ntczs2=math.log10(ntczs1)
	ntczs3=ntczs2*0.0002911208151382824	
	ntczs4=ntczs3+0.0033540164346805303
	TempKelvin=1/ntczs4
	
	
	Temperatur= TempKelvin-273.15 #umwandeln in Celsius
		
	return Temperatur
	
