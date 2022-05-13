import RPi.GPIO as GPIO
import time
#from socket import *

#####################USE SOCKET########################
#port = 9000
#clientSock = socket(AF_INET,SOCK_STREAM)
#clientSock.connect(('10.0.1.128',port))
#######################################################

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

trig_open = 2
echo_open = 3

GPIO.setup(trig_open, GPIO.OUT)
GPIO.setup(echo_open, GPIO.IN)

def umpa_forOpen() :
    GPIO.output(trig_open, GPIO.LOW)
    time.sleep(0.0001)
    GPIO.output(trig_open, GPIO.HIGH)

    while GPIO.input(echo_open) == 0 :
        pulse_start = time.time()

    while GPIO.input(echo_open) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    open_distance = pulse_duration * 17000
    open_distance = round(open_distance, 2)

    return open_distance

trig_trash = 23
echo_trash = 24

GPIO.setup(trig_trash, GPIO.OUT)
GPIO.setup(echo_trash, GPIO.IN)

def umpa_forTrash() :
    GPIO.output(trig_trash, GPIO.LOW)
    time.sleep(0.0001)
    GPIO.output(trig_trash, GPIO.HIGH)

    while GPIO.input(echo_trash) == 0 :
        pulse_start = time.time()

    while GPIO.input(echo_trash) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    trash_distance = pulse_duration * 17000
    trash_distance = round(trash_distance, 2)

    return trash_distance

DT =21
SCK=20

GPIO.setup(SCK, GPIO.OUT)

def readCount():
    i=0
    Count=0
    GPIO.setup(DT, GPIO.OUT)
    GPIO.output(DT,1)
    GPIO.output(SCK,0)
    GPIO.setup(DT, GPIO.IN)

    while GPIO.input(DT) == 1:
        i=0
    for i in range(24):
        GPIO.output(SCK,1)
        Count=Count<<1

        GPIO.output(SCK,0)
        #time.sleep(0.001)
        if GPIO.input(DT) == 0: 
            Count=Count+1
            #print Count
    GPIO.output(SCK,1)
    Count=Count^0x800000
    #time.sleep(0.001)
    GPIO.output(SCK,0)
    
    return Count

def checkweight(sample, count) :
    weight = (count - sample) / 406
        
    return weight

def changeflag(weight, distance):
    change_flag = False

    if distance <= 3.5 and weight >= 500 :
        change_flag = True

    return change_flag

def checkVolume(distance) :
    standard = 19

    if distance == 19 or distance == 20 :
        percentage = 0
    else :
        percentage = 100 - (distance / standard * 100)
    
    if percentage < 0 :
        percentage = 0

    return percentage
        
SERVO = 15
GPIO.setup(SERVO,GPIO.OUT)

SERVO_PWM = GPIO.PWM(SERVO,50)
SERVO_PWM.start(0)

def move_head() :
    SERVO_PWM.ChangeDutyCycle(7.5)
    time.sleep(2)

def return_head() :
    SERVO_PWM.ChangeDutyCycle(0.1)

"""---------MAIN---------"""

print("Ready to Check weight and distance")
for i in range (3,0, -1):
    print(i)
    time.sleep(1)
print("Start Check Data")
sample = readCount()

while True:
    count = readCount()
    weight = 0
    weight = checkweight(sample, count)
    open_distance = umpa_forOpen()
    trash_distance = umpa_forTrash()
    trash_volume = checkVolume(trash_distance)

    if open_distance <= 7 :
        move_head()
    else :
        return_head()

    flag = changeflag(weight, trash_distance)

    if flag == True :
        print("Change Trash Can Please")

    ################SEND DRONE############################
    #strdistance = str(distance)
    #strweight = str(weight)
    #sendDistanceData = strdistance
    #sendWeightData= strweight
    #clientSock.send(sendDistanceData.encode('utf-8'))

    #print("distance = ",sendDistanceData.encode('utf-8'))
    #time.sleep(1)
    #clientSock.send(sendWeightData.encode('utf-8'))
    #print("weight = ",weight)
    #time.sleep(1)
    ######################################################

    print("open distance : %d cm" %(open_distance))
    print("trash distance : %d cm" %(trash_distance))
    print("%d g" %(weight))
    print("trash_volume : %d %" %(trash_volume))

    time.sleep(1)

