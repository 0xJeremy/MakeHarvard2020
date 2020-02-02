from adafruit_servokit import ServoKit
from motors import Base
from gpiozero import LED
import time

kit = ServoKit(channels=16)

# channel1 = 0
# channel2 = 1

# base = Base(kit, channel1, channel2)
# base.go(1)
# time.sleep(2)
# base.go(0)
# time.sleep(0.5)
# base.go(-1)
# time.sleep(2)
# base.go(0)


motor = LED(40)

motor.on()
time.sleep(1)
motor.off()

