import serial
print "\n\n\nstarting Numato\n"
port = "/dev/tty.usbmodemFA131"
import datetime

start_time = datetime.datetime(2017,2,14,19,8)
last_reported_time=datetime.datetime.now()

ser = serial.Serial(port, timeout=1)
print ser.name


on = False
try:
	while True:
		if datetime.datetime.now().second != last_reported_time.second:
			last_reported_time = datetime.datetime.now()
			print "%s - %s" % (datetime.datetime.strftime(last_reported_time, "%a %b %-d %-I:%M:%S %p"), "ON" if on else "OFF")
		if datetime.datetime.now() > start_time and not on:
			ser.write("gpio set 0\r")


			on = True
except:
	print "somethings wrong"
finally:
	ser.write("gpio clear 0\r")	
	ser.close()
print "Ser closed\n\n\n"
