import read_arduino
import globvar
def spannung():

	read_arduino.read()
	
	Measure0=globvar.measure0
	
	spannung=Measure0*4.86/1023  #umwandeln von 8 bit in spannungswert

	return spannung
