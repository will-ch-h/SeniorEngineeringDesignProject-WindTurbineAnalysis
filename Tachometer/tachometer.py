import RPi.GPIO as GPIO
import time
import datetime
GPIO.setmode(GPIO.BCM)
IRPin = 4
Intervals = 3
    #IR Sensor // The amount of Blades + 1
    #Hall Effect // Amount of magnets 
IntervalTime = 5
    #Calculates RPM every x Seconds, The higher the number the more acurate I guess

GPIO.setup(IRPin, GPIO.IN)

RPMCalcTime = 60/IntervalTime
    #1 Second 60/1 = 60
    #5 second 60/5 = 12
    
def main():
    starttime = time.time()
    detections = 0
    rotations=0
    for i in range(10000000):
        if time.time() - starttime <=IntervalTime: 
            if GPIO.input(IRPin) == 0:
                detections += 1
                #print(detections)
                if detections == Intervals:
                    #print("Rotation")
                    detections = 0
                    rotations += 1
                while GPIO.input(IRPin) == 0:
                    time.sleep(0.001)
                else:
                    pass
        else:
            return rotations

def rpm():
    rotations=main()
    rpm = rotations*RPMCalcTime
    time = datetime.time(15, 8, 24, 78915)
    print(rpm)
    with open("log.txt", "a") as f:
        f.write(str(time)+str(rpm)+"\n")
    
try:
    while True:
        main()
        rpm()
finally:
    GPIO.cleanup()