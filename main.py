from node import Node
from link_parser import LinkParser
from link_parser_single import LinkParserSingle
import time
import threading
from url_thread import UrlThread
from guppy import hpy
import urllib
import random


max_depth = 1000
#link_parser = LinkParser()
#root = Node("https://google.com/")
ks = 0
file = open("links", "w")

'''def build_tree(node, k):	
	global ks
	global text
	
	if k >= max_depth:
		return
	
	#start = time.time()
	links = link_parser.start_collecting(node)
	#end = time.time()
	#print(end-start)
	
	for i in range(len(links)):
		text += links[i] + "\n"
		node.add_child(Node(links[i]))
		build_tree(node.children[i], k + 1)'''

def build_list(mode, root_url):
	depth = 0
	links = []

	if (mode == "swarm"):
		link_parsers = [LinkParser(root_url, mode)]
		time.sleep(1) #make sure its loaded
		links += link_parsers[0].grab()
		
		pos = 0
		c = 0
		while depth < max_depth and len(links) > 0:
			for link in links[pos:]:
				link_parsers.append(LinkParser(link))
			links_num = len(links)

			time.sleep(5)

			for link_parser in link_parsers[pos:]:
				start = time.time()
				while not link_parser.is_done():
					if time.time() - start > 0.1:
						print("timed out")
						break
					continue
				c+=1
				if (c%100 == 0):
					print("links: " + str(len(links)))
				links += link_parser.grab()
			pos += links_num
			depth += 1
			h = hpy()

		#print(links)
		print h.heap()
		print("\n" + str(len(links)))
		#print(links)

		return links
	elif (mode == "single"):
		link_stack = [root_url]
		visited = [root_url] # False: seen but not traversed.  True: seen and traversed

		while (depth < max_depth):
			#get links of current url
			parser = LinkParserSingle(link_stack[-1])
			#print(link_stack[-1])
			links = parser.links
			links = [x for x in links if x not in visited]

			#pick random link, if they exist, otherwise pop off stack
			if (len(links) == 0):
				print("\nDead end - backing up\n")
				link_stack = link_stack[:-1]
				depth -= 1
			else:
				n = random.randrange(len(links))
				link_stack.append(links[n])
				visited.append(links[n])
				depth += 1
			print("progress: " + str(depth) + "/" + str(max_depth) + ",   unique links: " + str(len(visited)))

		print("went through: " + str(depth+1) + " links and ended at " + str(link_stack[-1]))

		return visited

def main():
	start = time.time()
	#build_tree(root, 0)
	text = ""
	links = build_list("single" ,"https://www.cnn.com/")
	
	for link in links:
		text += link + "\n"

	args = []
	urls = []
	'''for i in range(20):
		args.append("https://www.google.com")
	try:

		for i in range(100):
			#urllib.urlopen("https://www.google.com")
			urls.append(UrlThread("https://www.google.com"))
			t = urls[i].start()
		#t.start()
		#while t.content == "":
		#	continue
	except:
		print("failed to start thread")'''

	file.write(text)
	file.close()
	print(time.time() - start)

if __name__ == "__main__":
	main()