import time
from url_thread import UrlThread
import urllib

class LinkParser:
	def __init__(self, url, mode):
		self.links = []
		self.url = url
		self.mode = mode
		
		self.url_thread = UrlThread(url)
		self.url_thread.start()
	def grab(self):
		splits = self.url_thread.get().split("href=\"")

		for i in range(0, len(splits)-1):
			if splits[i][0] == "/":
				self.links.append(self.url + splits[i].split("\"")[0])
			elif splits[i][0] == "h":
				self.links.append(splits[i].split("\"")[0])

		return self.links
	def is_done(self):
		return self.url_thread.get() != "" or self.url_thread.ran