import read_arduino
import globvar
def stromstaerke():
	
	read_arduino.read()
	Measure0=float(globvar.measure0)
	stromstaerkeSpan= Measure0*0.004887585532746823  #umwandeln von 8 bit in spannungswert
	stromstaerke= stromstaerkeSpan/10 #ohm
		
	return stromstaerke
	
