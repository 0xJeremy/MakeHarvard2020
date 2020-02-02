from adafruit_servokit import ServoKit
from gpiozero import LED
from constants import ARM_CHANNEL_1, ARM_CHANNEL_2, ARM_PIN_1,
					  ARM_PIN_2, ARM_LOWER_SLEEP_TIME, ARM_RAISE_SLEEP_TIME
					  BASE_CHANNEL_1, BASE_CHANNEL_2, FULL_ROTATION_TIME

class Arms():
	def __init__(self, kit, channel1, channel2, pin1, pin2):
		self.kit = kit
		self.openState = True
		self.motor1 = LED(pin1)
		self.motor2 = LED(pin2)

	def open(self):
		if not self.openState:
			return
		self.kit.servo[0] = 0
		self.kit.servo[1] = 0
		self.openState = False
		time.sleep(ARM_RAISE_SLEEP_TIME)
		return

	def close(self):
		if self.openState:
			return
		self.kit.servo[0] = 90
		self.kit.servo[1] = 90
		self.openState = True
		time.sleep(ARM_LOWER_SLEEP_TIME)
		return

	def l_motor(self, state):
		self.motor1.on() if state else self.motor1.off()
		return

	def r_motor(self, state):
		self.motor1.on() if state else self.motor1.off()
		return

	def motors_on(self):
		self.l_motor(True)
		self.r_motor(True)
		return

	def motors_off(self):
		self.l_motor(False)
		self.r_motor(False)
		return

	def close_and_on(self):
		self.close()
		self.motors_on()

	def open_and_off(self):
		self.motors_off()
		self.open()

class Base():
	def __init__(self, kit, channel1, channel2):
		self.kit = kit
		self.channel1 = channel1
		self.channel2 = channel2
		self.go(0)

	def go(self, direction):
		self.kit.continuous_servo[self.channel1].throttle = direction
		self.kit.continuous_servo[self.channel2].throttle = direction

	def rotate(self, pos):
		direction = 1 if self.pos < pos else -1
		diff = pos - self.pos
		duration = 10 / (diff / 360)
		start = time.time()
		while (time.time() - start) < duration:
			self.go(direction)
		self.go(0)
		self.pos = pos

class Actuation():
	def __init__(self):
		self.kit = ServoKit(channels=16)
		self.arms = Arms(kit, ARM_CHANNEL_1, ARM_CHANNEL_2, ARM_PIN_1, ARM_PIN_2)
		self.base = Base(kit, BASE_CHANNEL_1, BASE_CHANNEL_2)

	def next_card(self):
		self.arms.close_and_on()
		self.arms.open_and_off()

	def goto(self, pos):
		self.base.go(pos)
