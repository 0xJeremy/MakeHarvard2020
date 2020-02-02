from adafruit_servokit import ServoKit
from motors import Base
import time

kit = ServoKit(channels=16)

channel1 = 0
channel2 = 1

base = Base(kit, channel1, channel2)
base.go(1)
time.sleep(2)
base.go(0)
