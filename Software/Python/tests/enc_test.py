from gopigo import *

fwd()
enc_tgt(1, 1, 18)
time.sleep(.01)
while True:
	print read_enc_status(),
