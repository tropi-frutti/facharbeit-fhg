run=True
import sys
import stromstaerke
import time
import waehlen
import spannung
import widerstand
import leistung
import temperatur
import entfernung
##import phwert


if run==True:
	while run:
		auswahl=waehlen.auswahl()
		wdh=waehlen.anzahlwdh()
		abstand=waehlen.abstandwdh()
		Durchgaenge=0
		zeit=time.strftime("%d.%m.%Y %H:%M:%S")
		titel2="Wiederholungen:"+str(wdh)
		titel3="Abstand:"+str(abstand)
		titel="Messung mit Dem Pi Multimeter "+zeit
		messungen=[titel]
		messungen.append(titel2)
		messungen.append(titel3)
		if (auswahl == 1):
			messungen.append("Stromstaerke in Ampere")
		elif (auswahl == 2):
			messungen.append("Spannung in Volt")
		elif (auswahl == 3):
			messungen.append("Widerstand in Ohm")
		elif (auswahl == 4):
			messungen.append("Temperatur in Celsius")
		elif (auswahl == 5):
			messungen.append("Entfernung in Zentimetern")
		elif (auswahl == 6):
			messungen.append("leistung in Watt")
				
		##	elif (waehlen.Auswahl == 7):
		##		messungen.append("pH-Wert"))
				
		else:
			print("Fehlerhafte Eingabe")
			continue
		
		while Durchgaenge<wdh:
			if (auswahl == 1):
				messung=stromstaerke.stromstaerke()
			elif (auswahl == 2):
				messung=spannung.spannung()
				
			elif (auswahl == 3):
				messung=widerstand.widerstand()
				
			elif (auswahl == 4):
				messung=temperatur.temperatur()
			
			elif (auswahl == 5):
				messung=entfernung.distanz()
			elif (auswahl == 6):
				messung=leistung.leistung()
				
##	elif (waehlen.Auswahl == 7):
#			messung=phwert.phwert()
				
			else:
				print("Dies solllte eigentlich niemals erscheinen")
			print(messung)
			messungen.append(messung)
			Durchgaenge=Durchgaenge+1
			time.sleep(abstand)
		print (messungen)
		try:
				d = open("ergebnisse.csv","w")
		except:
			print("Dateizugriff nicht erfolgreich")
			sys.exit(0)
		
		csv=messungen
		csvS=0
		while len(messungen)>csvS:
			d.write(str(csv[csvS])+ "\n")
			csvS=csvS+1
			if csvS==len(messungen):
				print("Die messungen wurden gespeichert")
		d.close()

