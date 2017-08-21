import threading
#import urllib2
import urllib

class UrlThread(threading.Thread):
	def __init__(self, url):
		threading.Thread.__init__(self)
		self.url = url
		self.request = None
		self.content = ""
		self.ran = False
		#self.start = time.time()
	def run(self):
		if not self.ran:
			try:
				self.content = urllib.urlopen(self.url).read()
			except:
				print(str(self.url))
				self.content = "error"
			self.ran = True
			#self.request = urllib2.Request(self.url, headers={ 'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36" })
			#self.content = urllib2.urlopen(self.request)
		#except urllib2.HTTPError as error:
		#    print(str(error) + " : " + self.url)
		#except urllib2.URLError as error:
		#    print(error)
		#except timeout as error:
		#    print(error)
	def get(self):
		return self.content