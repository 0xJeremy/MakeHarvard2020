from flask import Flask, Response, render_template
import threading
from robot import Robot
from constants import CAMERA

robot = Robot(CAMERA)

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/get_card')
def get_card():
	global robot
	data = robot.get_card_data()
	if data is None:
		return "No current card visible"
	return "{} of suit {}".format(data[0], data[1])
