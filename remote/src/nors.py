import time
#import grovepi


from norsutils.logmsgs.logger import Logger

logger = Logger()
logger.log("SIS application started.")



# Connect the Grove Tilt Switch to digital port D3
# SIG,NC,VCC,GND
# mag_switch = 3
# 
# grovepi.pinMode(mag_switch,"INPUT")
# 
# while True:
#     try:
#         print grovepi.digitalRead(mag_switch)
#         time.sleep(.5)
# 
#     except IOError:
#         print "Error"