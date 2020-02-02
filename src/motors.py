import time
from adafruit_servokit import ServoKit
from gpiozero import LED
from constants import ARM_CHANNEL_1, ARM_CHANNEL_2, MOTOR_PIN
from constants import SMOTOR_CHANNEL_1, SMOTOR_CHANNEL_2
from constants import ARM_OPEN_ANGLE_1, ARM_OPEN_ANGLE_2, ARM_CLOSE_ANGLE_1, ARM_CLOSE_ANGLE_2
from constants import ARM_LOWER_SLEEP_TIME, ARM_RAISE_SLEEP_TIME
from constants import BASE_CHANNEL_1, BASE_CHANNEL_2, FULL_ROTATION_TIME

##################
### ARMS CLASS ###
##################

class Arms():
	def __init__(self, kit, channel1=ARM_CHANNEL_1, channel2=ARM_CHANNEL_2, DCmotor=MOTOR_PIN, \
				 smotor1=SMOTOR_CHANNEL_1, smotor2=SMOTOR_CHANNEL_2):
		self.kit = kit
		self.openState = True
		self.channel1 = channel1
		self.channel2 = channel2
		self.DCmotor = LED(DCmotor)
		self.smotor1 = smotor1
		self.smotor2 = smotor2

	def open(self):
		if not self.openState:
			return
		self.kit.servo[self.channel1].angle = ARM_OPEN_ANGLE_1
		self.kit.servo[self.channel2].angle = ARM_OPEN_ANGLE_2
		self.openState = False
		return

	def close(self):
		if self.openState:
			return
		self.kit.servo[self.channel1].angle = ARM_CLOSE_ANGLE_1
		self.kit.servo[self.channel2].angle = ARM_CLOSE_ANGLE_2
		self.openState = True
		return

	def motors(self, state):
		if state:
			self.DCmotor.on()
			self.kit.continuous_servo[self.smotor1] = 1
			self.kit.continuous_servo[self.smotor1] = -1
		else:
			self.DCmotor.off()
			self.kit.continuous_servo[self.smotor1] = 0
			self.kit.continuous_servo[self.smotor1] = 0
		return

	def close_and_on(self):
		self.close()
		time.sleep(ARM_LOWER_SLEEP_TIME)
		self.motors(True)
		time.sleep(MOTOR_SPIN_TIME)

	def open_and_off(self):
		self.motors(False)
		self.open()
		time.sleep(ARM_RAISE_SLEEP_TIME)

##################
### BASE CLASS ###
##################

class Base():
	def __init__(self, kit, channel1=BASE_CHANNEL_1, channel2=BASE_CHANNEL_2):
		self.kit = kit
		self.channel1 = channel1
		self.channel2 = channel2
		self.pos = 0
		self.go(0)

	def go(self, direction):
		self.kit.continuous_servo[self.channel1].throttle = direction
		self.kit.continuous_servo[self.channel2].throttle = direction

	def rotate(self, pos):
		diff = pos - self.pos
		direction = 1 if diff > 0 else -1
		duration = (FULL_ROTATION_TIME * abs(diff)) / 360
		start = time.time()
		while (time.time() - start) < duration:
			self.go(direction)
		self.go(0)
		self.pos = pos

###########################
### ACTUATION INTERFACE ###
###########################

class Actuation():
	def __init__(self):
		self.kit = ServoKit(channels=16)
		self.arms = Arms(self.kit)
		self.base = Base(self.kit)

	def next_card(self):
		print("Activating next Card")
		self.arms.close_and_on()
		self.arms.open_and_off()

	def goto(self, pos):
		print("Going to pos: {}".format(pos))
		self.base.rotate(pos)
