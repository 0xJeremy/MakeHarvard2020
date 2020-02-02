from flask import Flask, Response, render_template
import threading
from robot import Robot
from constants import CAMERA

# robot = Robot(CAMERA).start()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_card')
def get_card():
	global robot
	card = robot.get_card_data()
	if card is None:
		return "No card visible"
	return "{} of suit {}".format(card[0], card[1])
