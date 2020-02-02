from flask import Flask, Response, render_template
import threading
from robot import Robot
import cv2

CAMERA = 2

lock = threading.Lock()
img = None
robot = Robot(CAMERA).start()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
	return Response(generate(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")

def generate():
	global robot, img, lock
	while True:
		with lock:
			img = robot.get_img()
			if img is None:
				print("Image is none :(")
				continue
			(flag, encodedImage) = cv2.imencode(".jpg", img)
			if not flag: continue
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')
