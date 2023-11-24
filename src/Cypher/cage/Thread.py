import threading
import json
import os
import nmap
from django.http import HttpResponse

class Scanners(threading.Thread):
	def __init__(self, url, stack=[]):
		self.stack = stack
		self.url = url
		threading.Thread.__init__(self)

	def run(self):
		try:
			print("Thread execution started")
			sc = nmap.PortScanner()
			url= self.url
			print(url)
			container = {}
			k = sc.scan(url, '1-1024', '-v -sS -sV -sC -A -O')
			print(os.getcwd())
			with open('../Cypher/DATA/nscan.json', 'w') as f:
				json.dump(k['scan'], f, indent=4)
				f.close()
			with open('../Cypher/DATA/data.json', 'r') as fi:
				hotspots = json.load(fi)['Analytics and Tracking'][0][0]
				fi.close()

			units = ["hotjar"]
			os.system("scrapy crawl vulscan -a urls=" + "https://nvd.nist.gov/vuln/search/results?form_type=Basic'&'results_type=overview'&'query="+ units[0] + "'&'search_type=all&isCpeNameSearch=false")
			print("Done")
			print(hotspots)
		except Exception as e:
			print(e)
