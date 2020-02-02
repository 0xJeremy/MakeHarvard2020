from sensor import sensor
# from motors import Actuation
from mapping import Mapping
from threading import Thread
import time

class Robot():
	def __init__(self, camera_num):
		self.cam = sensor(camera_num)
		# self.ctrl = Actuation()
		self.mapping = Mapping()
		self.last_card = None

	def start(self):
		Thread(target=self.update, args=()).start()
		return self

	def update(self):
		self.cam.start()
		while True:
			if self.cam.stopped:
				self.stopped = True
				break
			if self.stopped:
				self.cam.stop()
				break
			cards, num = self.cam.get_cards()
			if num == 1:
				card = cards[0]
				if card.best_rank_match is 'Unknown' or card.best_suit_match is 'Unknown':
					continue
				pos = self.mapping.get_pos(card)
				# self.ctrl.goto(pos)
				# self.ctrl.next_card()
				self.last_card = card
				print("Card: {} {}".format(card.best_rank_match, card.best_suit_match))

	def stop(self):
		self.stopped = True

	def get_img(self):
		return self.cam.read()

	def get_card_data(self):
		if self.last_card is None:
			return None
		return self.last_card.best_rank_match, self.last_card.best_suit_match
