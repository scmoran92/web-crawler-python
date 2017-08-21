#import random
import time
from url_thread import UrlThread
import urllib

class LinkParserSingle:
	def __init__(self, url):
		self.links = []
		self.url = url
		self.page = None

		try:
			print(self.url)
			self.page = urllib.urlopen(self.url).read()
		except:
			self.content = "ERROR"

		if (self.page != None):
			splits = self.page.split("href=\"")

			for i in range(0, len(splits)-1):
				if splits[i][0:2] == "//":
					self.links.append("https://" + splits[i][2:].split("\"")[0])
				elif splits[i][0:4] == "http":
					self.links.append(splits[i].split("\"")[0])
				elif splits[i][0:4] == "www.":
					self.links.append(splits[i].split("\"")[0])
				elif splits[i][0] == "/":
					self.links.append(self.url + splits[i].split("\"")[0])