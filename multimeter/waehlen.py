def auswahl():
	print("1. Stromstaerke")
	print("2. Spannung")
	print("3. Widerstand")
	print("4. Temperatur")
	print("5. Entfernung")
	print("6. Leistung")
##	print("7. pH-Wert")
	Auswahl = int(input("Waehlen sie aus, was sie messen moechten:"))
	return Auswahl
	
def anzahlwdh():
	wdh=int(input("geben sie die anzahl an gewuenschten wiederholungen ein:"))
	return wdh

def abstandwdh():
	abstand=float(input("geben sie den abstand zwischen den messungen in Sekunden ein:"))
	return abstand