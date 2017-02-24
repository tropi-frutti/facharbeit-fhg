def auswahl():
	print("1. Stromstaerke")
	print("2. Spannung")
	print("3. Widerstand")
	print("4. Temperatur")
##	print("5. Entfernung")
##	print("6. pH-Wert")
	global Auswahl
	Auswahl = int(input("Waehlen sie aus, was sie messen moechten:"))
	return Auswahl
	
def anzahlwdh():
	global wdh
	wdh=int(input("geben sie die anzahl an gewuenschten wiederholungen ein:"))
	return wdh

def abstandwdh():
	global abstand
	abstand=int(input("geben sie den abstand zwischen den messungen in Sekunden ein:"))
	return abstand