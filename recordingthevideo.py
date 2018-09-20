from picamera import PiCamera
from time import sleep

camera=PiCamera()

camera.start_preview()#'turns on' camera
camera.start_recording('/home/pi/testingit3.h264') # saves file to directory 
sleep(60) # records for 60 seconds
camera.stop_recording()# stops recording
camera.stop_preview()#'turns off' camera
