import cv2
import numpy as numpy
import time
import os
import Cards
import VideoStream
from threading import Thread

IM_WIDTH = 800
IM_HEIGHT = 480 
FRAME_RATE = 10
FONT = cv2.FONT_HERSHEY_SIMPLEX

class sensor:
	def __init__(self, camera=1):
		self.frame_rate_calc = 1
		self.freq = cv2.getTickFrequency()
		self.videostream = VideoStream.VideoStream((IM_WIDTH,IM_HEIGHT),FRAME_RATE,camera,2).start()
		time.sleep(1)
		path = os.path.dirname(os.path.abspath(__file__))
		self.train_ranks = Cards.load_ranks( path + '/Card_Imgs/')
		self.train_suits = Cards.load_suits( path + '/Card_Imgs/')
		self.cards = []
		self.stopped = False

	def start(self):
		Thread(target=self.update, args=()).start()
		return self

	def update(self):
		while True:
			# Stop conditions
			if self.stopped:
				cv2.destroyAllWindows()
				self.videostream.stop()
				break
			key = cv2.waitKey(1) & 0xFF
			if key == ord("q"):
				self.stopped = True

			# Image acquisition
			image = self.videostream.read()
			t1 = cv2.getTickCount()

			# Card processing
			pre_proc = Cards.preprocess_image(image)
			cnts_sort, cnt_is_card = Cards.find_cards(pre_proc)
			cards = []
			if len(cnts_sort) != 0:
				k = 0
				for i in range(len(cnts_sort)):
					if(cnt_is_card[i] == 1):
						cards.append(Cards.preprocess_card(cnts_sort[i],image))
						cards[k].best_rank_match,cards[k].best_suit_match,cards[k].rank_diff,cards[k].suit_diff = Cards.match_card(cards[k],self.train_ranks,self.train_suits)
						image = Cards.draw_results(image, cards[k])
						k = k + 1

				# Card outlie drawing
				if len(cards) != 0:
					tmp_cnts = [i.contour for i in cards]
					cv2.drawContours(image, tmp_cnts, -1, (255,0,0), 2)

			self.cards = cards

			# Display functions
			cv2.putText(image,"FPS: "+str(int(self.frame_rate_calc)),(10,26),FONT,0.7,(255,0,255),2,cv2.LINE_AA)
			cv2.imshow("Card Detector",image)
			self.frame_rate_calc = 1/((cv2.getTickCount()-t1)/self.freq)

	def read(self):
		return self.frame

	def stop(self):
		self.stopped = True

	def get_cards(self):
		return self.cards, len(self.cards)
