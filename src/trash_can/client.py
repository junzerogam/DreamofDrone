import RPi.GPIO as GPIO
import time
from socket import *

#####################USE SOCKET########################
port = 9000
clientSock = socket(AF_INET,SOCK_STREAM)
clientSock.connect(('10.0.1.128',port))
#######################################################

# remove warning info
GPIO.setwarnings(False)
# mapping gpio pin num to bcm num
GPIO.setmode(GPIO.BCM)

# outside ultrasonic wave sensor i/o set bcm num
trig_open = 27   # input
echo_open = 22   # output

GPIO.setup(trig_open, GPIO.OUT)
GPIO.setup(echo_open, GPIO.IN)

# open trashcan func
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

# inside ultrasonic wave sensor i/o set bcm num
trig_trash = 23
echo_trash = 24

GPIO.setup(trig_trash, GPIO.OUT)
GPIO.setup(echo_trash, GPIO.IN)

# measure the height of garbage func
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

# weight sensor i/o set bcm num
DT =21  # data
SCK=20  # clock

GPIO.setup(SCK, GPIO.OUT)

######################will modify#####################
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
##################################################

# calculate trash_can to be changed or not
def changeflag(weight, volume):
    change_flag = False

    if volume >= 75 or weight >= 500 :
        change_flag = True

    return change_flag

# servo motor sensor i/o set bcm num
SERVO = 15
GPIO.setup(SERVO,GPIO.OUT)

# make servo can move
SERVO_PWM = GPIO.PWM(SERVO,50)
SERVO_PWM.start(0)

# open trash_can
def move_head() :
    SERVO_PWM.ChangeDutyCycle(7.5)  # servo degree(90)
    time.sleep(2)

# close trash_can
def return_head() :
    SERVO_PWM.ChangeDutyCycle(0.1)  # servo degree(origin)

# calculate distance to percent
def checkVolume(distance) :
    standard = 19

    if distance == 19 or distance == 20 :
        percentage = 0
    else :
        percentage = 100 - (distance / standard * 100)
    
    if percentage < 0 :
        percentage = 0

    return percentage

#########################--MAIN--##################################

print("Ready to Check weight and distance")
for i in range (3,0,-1):
    print(i)
    time.sleep(1)
print("Start Check Data")
sample = readCount()    # read weight sensor initial data

while True:
    count = readCount()
    trash_weight = 0
    trash_weight = checkweight(sample, count)
    open_distance = umpa_forOpen()
    trash_distance = umpa_forTrash()
    trash_volume = checkVolume(trash_distance)

    # under 7cm then open
    if open_distance <= 7 :
        move_head()
        print("[Notice] : Open Head!")
    else :
        return_head()

    flag = changeflag(trash_weight, trash_volume)

    ##########################SEND DRONE###########################
    intTrashDistance = int(trash_distance)
    intTrashWeight = int(trash_weight)
    intTrashVolume = int(trash_volume)
    sendTrashDistance = str(intTrashDistance)
    sendTrashWeight = str(intTrashWeight)
    sendTrashVolume = str(intTrashVolume)
    
    clientSock.send(sendTrashWeight.encode('utf-8'))
    nothing = clientSock.recv(1024)
    clientSock.send(sendTrashDistance.encode('utf-8'))
    nothing = clientSock.recv(1024)
    clientSock.send(sendTrashVolume.encode('utf-8'))
    nothing = clientSock.recv(1024)
    ################################################################

    # print terminal
    print("---------------------")
    print("[Open Distance] : %d cm\n" %(open_distance))
    print("[Trash Weight]  : %d g" %(trash_weight))
    print("[Trash Distance]: %d cm" %(trash_distance))
    print("[Trash Volume]  : %d %%\n" %(trash_volume))
    
    if flag == True :
        print("[Status]        : Need Changed\n")
    else :
        print("[Status]        : Normal\n")

    time.sleep(3)
