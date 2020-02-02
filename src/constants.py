import cv2

#############
### ROBOT ###
#############

ROBOT_ENABLE = True
CAMERA = 1

#############
### IMAGE ###
#############

IM_WIDTH = 800
IM_HEIGHT = 480 
FRAME_RATE = 10
FONT = cv2.FONT_HERSHEY_SIMPLEX
SHOW_FRAME = False

#############
### CARDS ###
#############

RANKS = ['Ace','Two','Three','Four','Five','Six','Seven',
		 'Eight','Nine','Ten','Jack','Queen','King']
SUITS = ['Spades','Diamonds','Clubs','Hearts']
COLOR = ['Red', 'Black']
REDS = ['Diamonds', 'Hearts']
BLACKS = ['Spades, Clubs']
NUM_PLAYERS = 4
NUM_DEAL_CARDS = 5

##############
### MOTORS ###
##############

# ARM CLASS

# Servo Driver Pins
ARM_CHANNEL_1 = 0
ARM_CHANNEL_2 = 1

# Arm Open Angles
ARM_OPEN_ANGLE_1 = 30
ARM_OPEN_ANGLE_2 = 90

# Arm Closed Angles
ARM_CLOSE_ANGLE_1 = 180
ARM_CLOSE_ANGLE_2 = 0

# Time to Lower Arms (in seconds)
ARM_LOWER_SLEEP_TIME = 1
# Time to Raise Arms (in seconds)
ARM_RAISE_SLEEP_TIME = 1

# Servo Motor Channels
SMOTOR_CHANNEL_1 = 2
SMOTOR_CHANNEL_2 = 3

# DC Motor Pin Number
MOTOR_PIN = 21

# Time to spin motors (in seconds)
MOTOR_SPIN_TIME = 1

######################

# BASE CLASS
# Servo Driver Pins for the Base
BASE_CHANNEL_1 = 4
BASE_CHANNEL_2 = 5

# Time (seconds) to perform one full rotation
FULL_ROTATION_TIME = 10
