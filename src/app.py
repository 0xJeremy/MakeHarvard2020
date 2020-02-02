from flask import Flask, Response, render_template, request
import threading
from constants import CAMERA, ROBOT_ENABLE

robot = None
if ROBOT_ENABLE:
	from robot import Robot
	robot = Robot(CAMERA).start()

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

@app.route('/start', methods=['POST'])
def start():
	global robot
	if ROBOT_ENABLE:
		robot.sort(request.form['type'])
	print("Starting sorting with {}".format(request.form['type']))
	return "Success!"
