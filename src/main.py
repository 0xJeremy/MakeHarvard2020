#!/usr/bin/python3

from sensor import sensor
import time

##################
### PARAMETERS ###
##################
CAMERA_NUM = 2 # 1 for PiCamera, 2 for USB Camera

###############
### GLOBALS ###
###############
cam = sensor(CAMERA_NUM)

def main():
	cam.start()
	while True:
		if cam.stopped:
			break
		cards, num = cam.get_cards()
		if num != 0:
			print(num)
			print("Card: {} {}".format(cards[0].best_rank_match, cards[0].best_suit_match))
		time.sleep(0.2)


if __name__ == '__main__':
	main()