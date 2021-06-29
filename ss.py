import RPi.GPIO as GPIO

import time

import Adafruit_DHT

sensor=Adafruit_DHT.DHT11

MOTER_A_A1=5

MOTER_A_B1=6

GPIO.setmode(GPIO.BCM)

GPIO.setup(MOTER_A_A1,GPIO.OUT)

GPIO.setup(MOTER_A_B1,GPIO.OUT)


MOTER_A_A1_PWM=GPIO.PWM(MOTER_A_A1,20)


MOTER_A_A1_PWM.start(0)

GPIO.output(MOTER_A_B1,GPIO.LOW)


try :

    while True :


        MOTER_A_A1_PWM.ChangeDutyCycle(duty)

       
        time.sleep(0.5)

finally :

        MOTER_A_A1_PWM.stop()

        GPIO.cleanup()      
