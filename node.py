from link_parser import LinkParser

class Node:
	def __init__(self, url):
		self.url = url
		self.children = []
		self.link_parser = LinkParser()
		self.link_parser.start_collecting(self)
	def add_child(self, node):
		self.children.append(node)