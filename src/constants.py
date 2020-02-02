import cv2

#############
### ROBOT ###
#############

ROBOT_ENABLE = False
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

ARM_CHANNEL_1 = 0
ARM_CHANNEL_2 = 1
ARM_PIN_1 = 1
ARM_PIN_2 = 2

ARM_LOWER_SLEEP_TIME = 1
ARM_RAISE_SLEEP_TIME = 1

BASE_CHANNEL_1 = 2
BASE_CHANNEL_2 = 3

FULL_ROTATION_TIME = 10
