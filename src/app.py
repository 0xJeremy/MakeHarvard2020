from flask import Flask, Response, render_template
import threading

lock = threading.lock()
outputFrame = None

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'


@app.route("/video_feed")
def video_feed():
	return Response(generate(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")

def generate():
	global outputFrame, lock
	while True:
		with lock:
			if outputFrame is None: continue
			(flag, encodedImage) = cv2.imencode(".jpg", outputFrame)
			if not flag: continue
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')
