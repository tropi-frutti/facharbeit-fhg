import read_arduino
import globvar
def widerstand():
	
	
	read_arduino.read()
	Measure0=float(globvar.measure0)
	if Measure0==0:
		widerstand="messfehler"
	else:
		widerstandREF=1100
		widerstandSPAN=Measure0*0.004887585532746823		 #umwandeln von 8 bit in spannungswert
	
		#anwenden von u/(r1+r2)= u2/r2 umgewandelt zu r1=((u*r2)/u2)-r2
		widerstandZS1=5*widerstandREF
		widerstandZS2=widerstandZS1/widerstandSPAN
		widerstand=widerstandZS2-widerstandREF
	
		
	return widerstand