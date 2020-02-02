from constants import RANKS, SUITS, COLOR, REDS, BLACKS

class Mapping():
	def __init__(self, mode="ranks"):
		self.mode = mode
		if self.mode == 'ranks':
			self.top_level = RANKS
			self.f = self.get_ranks
		elif self.mode == 'suits':
			self.top_level = SUITS
			self.f = self.get_suits
		else:
			self.top_level = COLOR
			self.f = self.get_color

		self.pos_size = 360 / len(self.top_level)
		self.curr_piles = 0
		self.map = {}

	def get_pos(self, card):
		return self.f(card)

	def get_ranks(self, card):
		if card.best_rank_match in self.map.keys():
			return self.map[card.best_rank_match]
		return self.new_pos(card.best_rank_match)

	def get_suits(self, card):
		if card.best_suit_match in self.map.keys():
			return self.map[card.best_suit_match]
		return self.new_pos(card.best_suit_match)

	def get_color(self, card):
		color = 'Red' if card.best_suit_match in REDS else 'Black'
		if color in self.map.keys():
			return self.map[color]
		return self.new_pos(color)

	def new_pos(self, card):
		self.map[card] = self.curr_piles
		self.curr_piles += self.pos_size
		return self.map[card]
