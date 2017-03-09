import serial
import globvar
"""import logging

logging.basicConfig(filename="log/multimeter.log",
				level=logging.DEBUG,
				)
logger = logging.getLogger("read_arduino")"""


def read():
	"""
	reads analog measured data via usb from a connected arduino
	"""
	global measure0
	global measure1
	global measure2
	global measure3
	global measure4
	global measure5
	global measure6
	global measure7
		
	ser = serial.Serial('COM6', 115200, timeout=1)
	retry = True
	retries = 0

	while retries < 5 :
		line = ser.readline()
		measures = line.split()
		if len(measures) ==8:
			try:
				
				globvar.measure0 =int(measures[0])
				
				globvar.measure1 =int(measures[1])
				break
			except ValueError:
				# garbaged input will be ignored and retried
				pass
			
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
			
		else:
			##retryy!

			retries = retries + 1
	
	if retries == 5:
		msg = "no correct result after 5 tries"
		##logger.fatal(msg)
		raise ValueError(msg)