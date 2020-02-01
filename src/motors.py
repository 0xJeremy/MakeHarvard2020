from adafruit_servokit import ServoKit
from gpiozero import LED

class arms():
	def __init__(self, kit, pin1, pin2):
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
		return

	def close(self):
		if self.openState:
			return
		self.kit.servo[0] = 90
		self.kit.servo[1] = 90
		self.openState = True
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



