import os
import time

while True:
	temp = os.popen("vcgencmd measure_temp").readline()
	mhz = os.popen("vcgencmd measure_clock arm").readline()
	mhz =mhz[14:]
	mhz =mhz[::-1]
	mhz =mhz[7:]
	mhz =mhz[::-1]
	print (temp)
	print mhz
	print ("")
	time.sleep(1)
