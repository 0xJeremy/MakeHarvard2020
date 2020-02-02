from mapping import Mapping

class card():
	def __init__(self, a, b):
		self.best_rank_match = a
		self.best_suit_match = b

# Testing ranks
# mapping = Mapping("ranks")
# print(mapping.get_pos(card("Ace", "Diamonds")))
# print(mapping.get_pos(card("Two", "Diamonds")))
# print(mapping.get_pos(card("Three", "Diamonds")))
# print(mapping.get_pos(card("Four", "Diamonds")))
# print(mapping.get_pos(card("Five", "Diamonds")))
# print(mapping.get_pos(card("Six", "Diamonds")))
# print(mapping.get_pos(card("Seven", "Diamonds")))
# print(mapping.get_pos(card("Eight", "Diamonds")))
# print(mapping.get_pos(card("Nine", "Diamonds")))

# print(mapping.get_pos(card("Ace", "Spades")))
# print(mapping.get_pos(card("Two", "Spades")))
# print(mapping.get_pos(card("Three", "Spades")))
# print(mapping.get_pos(card("Four", "Spades")))
# print(mapping.get_pos(card("Five", "Spades")))
# print(mapping.get_pos(card("Six", "Spades")))
# print(mapping.get_pos(card("Seven", "Spades")))
# print(mapping.get_pos(card("Eight", "Spades")))
# print(mapping.get_pos(card("Nine", "Spades")))

# print(mapping.get_pos(card("Eight", "Hearts")))
# print(mapping.get_pos(card("Nine", "Clubs")))

# Testing suits
# mapping = Mapping("suits")
# print(mapping.get_pos(card("Ace", "Diamonds")))
# print(mapping.get_pos(card("Two", "Diamonds")))
# print(mapping.get_pos(card("Three", "Diamonds")))
# print(mapping.get_pos(card("Four", "Diamonds")))
# print(mapping.get_pos(card("Five", "Diamonds")))
# print(mapping.get_pos(card("Six", "Diamonds")))
# print(mapping.get_pos(card("Seven", "Diamonds")))
# print(mapping.get_pos(card("Eight", "Diamonds")))
# print(mapping.get_pos(card("Nine", "Diamonds")))

# print(mapping.get_pos(card("Ace", "Spades")))
# print(mapping.get_pos(card("Two", "Spades")))
# print(mapping.get_pos(card("Three", "Spades")))
# print(mapping.get_pos(card("Four", "Spades")))
# print(mapping.get_pos(card("Five", "Spades")))
# print(mapping.get_pos(card("Six", "Spades")))
# print(mapping.get_pos(card("Seven", "Spades")))
# print(mapping.get_pos(card("Eight", "Spades")))
# print(mapping.get_pos(card("Nine", "Spades")))

# print(mapping.get_pos(card("Eight", "Hearts")))
# print(mapping.get_pos(card("Nine", "Clubs")))

# Testing deal
mapping = Mapping("deal")
print(mapping.get_pos(card("Ace", "Diamonds")))
print(mapping.get_pos(card("Two", "Diamonds")))
print(mapping.get_pos(card("Three", "Diamonds")))
print(mapping.get_pos(card("Four", "Diamonds")))
print(mapping.get_pos(card("Five", "Diamonds")))
print(mapping.get_pos(card("Six", "Diamonds")))
print(mapping.get_pos(card("Seven", "Diamonds")))
print(mapping.get_pos(card("Eight", "Diamonds")))
print(mapping.get_pos(card("Nine", "Diamonds")))
print(mapping.get_pos(card("Ace", "Spades")))
print(mapping.get_pos(card("Two", "Spades")))
print(mapping.get_pos(card("Three", "Spades")))
print(mapping.get_pos(card("Four", "Spades")))
print(mapping.get_pos(card("Five", "Spades")))
print(mapping.get_pos(card("Six", "Spades")))
print(mapping.get_pos(card("Seven", "Spades")))
print(mapping.get_pos(card("Eight", "Spades")))
print(mapping.get_pos(card("Nine", "Spades")))
print(mapping.get_pos(card("Eight", "Hearts")))
print(mapping.get_pos(card("Nine", "Clubs")))
