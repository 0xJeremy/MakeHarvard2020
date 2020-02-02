import time
from adafruit_servokit import ServoKit
from gpiozero import LED
from constants import ARM_CHANNEL_1, ARM_CHANNEL_2, MOTOR_PIN, ARM_OPEN_ANGLE, ARM_CLOSE_ANGLE, ARM_LOWER_SLEEP_TIME, ARM_RAISE_SLEEP_TIME, BASE_CHANNEL_1, BASE_CHANNEL_2, FULL_ROTATION_TIME

class Arms():
	def __init__(self, kit, channel1, channel2, motor):
		self.kit = kit
		self.openState = True
		self.channel1 = channel1
		self.channel2 = channel2
		self.motor = LED(motor)

	def open(self):
		if not self.openState:
			return
		self.kit.servo[self.channel1].angle = ARM_OPEN_ANGLE
		self.kit.servo[self.channel2].angle = ARM_OPEN_ANGLE
		self.openState = False
		time.sleep(ARM_RAISE_SLEEP_TIME)
		return

	def close(self):
		if self.openState:
			return
		self.kit.servo[self.channel1].angle = ARM_CLOSE_ANGLE
		self.kit.servo[self.channel2].angle = ARM_CLOSE_ANGLE
		self.openState = True
		time.sleep(ARM_LOWER_SLEEP_TIME)
		return

	def motors(self, state):
		if state:
			self.motor.on()
		else:
			self.motor.off()
		return

	def close_and_on(self):
		self.close()
		self.motors(True)

	def open_and_off(self):
		self.motors(False)
		self.open()

class Base():
	def __init__(self, kit, channel1, channel2):
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

class Actuation():
	def __init__(self):
		self.kit = ServoKit(channels=16)
		self.arms = Arms(self.kit, ARM_CHANNEL_1, ARM_CHANNEL_2, MOTOR_PIN)
		self.base = Base(self.kit, BASE_CHANNEL_1, BASE_CHANNEL_2)

	def next_card(self):
		self.arms.close_and_on()
		self.arms.open_and_off()

	def goto(self, pos):
		self.base.rotate(pos)
