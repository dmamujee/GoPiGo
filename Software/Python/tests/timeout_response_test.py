from gopigo import *

fwd()
enable_com_timeout(1000)
time.sleep(.01)
while True:
	print read_timeout_status(),
