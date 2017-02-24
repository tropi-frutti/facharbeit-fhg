import globvar
def read():
	import serial
	global measure0
	global measure1
	global measure2
	global measure3
	global measure4
	global measure5
	global measure6
	global measure7
	
	ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
	retry = True
	while retry:
		line = ser.readline()
		measures = line.split()
		if len(measures) ==8:
			print(measures[0])
			measure=float(measures[0])
			globvar.measure0 =int(measure)
			
	##		measure1 = measures[1]
	##		measure2 = measures[2]
	##		measure3 = measures[3]
	##		measure4 = measures[4]
	##		measure5 = measures[5]
	##		measure6 = measures[6]
	##		measure7 = measures[7]
##			print(measure0)
##			print(measure1)
##			print(measure2)
##			print(measure3)
##			print(measure4)
##			print(measure5)
##			print(measure6)
##			print(measure7)
			
			retry=False
		else:
			print("wrong number of results")

