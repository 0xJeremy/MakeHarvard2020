#!/usr/bin/python3

from sensor import sensor
from motors import Actuation
from mapping import Mapping
import time

##################
### PARAMETERS ###
##################
CAMERA_NUM = 1 # 1 for PiCamera, 2 for USB Camera

###############
### GLOBALS ###
###############
cam = sensor(CAMERA_NUM)
ctrl = Actuation()
mapping = Mapping()

def main():
	cam.start()
	while True:
		if cam.stopped:
			break
		cards, num = cam.get_cards()
		if num == 1:
			card = cards[0]
			if card.best_rank_match is 'Unknown' or card.best_suit_match is 'Unknown':
				continue
			pos = mapping.get_pos(card)
			ctrl.goto(pos)
			ctrl.next_card()
			print("Card: {} {}".format(card.best_rank_match, card.best_suit_match))
		time.sleep(0.2)


if __name__ == '__main__':
	main()