#Ping raspberrypi.local
#ssh pi@[IP address of Pi]
#pytghon final-code.py
#scp


import picamera     # Importing the library for camera module
from time import sleep
import explorerhat
import time


def record():

    camera = picamera.PiCamera()    # Setting up the camera
    camera.rotation = 180       
    camera.start_preview()      # You will see a preview window while recording
    camera.start_recording('/home/pi/video.h264') # Video will be saved at desktop
    sleep(10)
    camera.capture('/home/pi/imag.jpg') # Capturing the image
    camera.stop_recording()
    camera.stop_preview()
    sleep(1)
    camera.capture('/home/pi/imag.jpg') # Capturing the image
    print('Done')
    return


def move():


    
    print("""
    This basic example tests the various functions of Explorer HAT,
    touching any of the buttons should output a message, lights should pulse
    and analog/digital values should be read every second.

    Press CTRL+C to exit.
    """)

    explorerhat.motor.forwards()####

    touched = [False] * 8


    def ohai(channel, event):
        touched[channel - 1] = True
        print("{}: {}".format(channel, event))


    explorerhat.touch.pressed(ohai)
    explorerhat.touch.released(ohai)

    explorerhat.light[0].on()
    explorerhat.light[2].on()

    explorerhat.output[0].on()
    explorerhat.output[2].on()

    input_status = False
    record()

    #while True:

    if explorerhat.is_explorer_pro():
        print(explorerhat.analog.read())
    print(explorerhat.input.read())
    if sum(explorerhat.input.read().values()) == 4:
        input_status = True
    print('Input Status:', input_status)
    print('Touch Status:', sum(touched) == 8)

    if input_status and sum(touched) == 8:
        explorerhat.light.off()
        explorerhat.light.green.on()
    else:
        explorerhat.light.toggle()
    explorerhat.output.toggle()

   # time.sleep(10)

    #explorerhat.pause()
    return

if __name__ == '__main__':
   # recordVideoAndImage()
    move()


