from django.shortcuts import render
import json
import os
import nmap
import time, asyncio
from asgiref.sync import sync_to_async
from .Thread import Scanners
from django.http import HttpResponse
from .models import *
from urllib.parse import urlparse
import subprocess
import shlex
import tempfile

target = "No target selected"


def Landing(request):
	os.system("rm -rf DATA")
	os.system("mkdir DATA")
	print("delete")
	return render(request, "index.html", {})


def Scanpad(request):
	print(target)
	if request.GET:
		if "spidey" in os.getcwd():
			os.chdir("../Cypher/")
		module = request.GET['query']
		query =shlex.split(f"python Nettacker/nettacker.py -i {target} -m {module} " )
		out, err = subprocess.Popen(query, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
		print(err)
		with open("DATA/output.txt", 'w') as f:
			f.write(out.decode())
			f.close()
		with open("DATA/output.txt", "r") as f:
			out = f.readlines()
			f.close()
		result = []
		for i in out:
			result.append(i.replace("\n", " "))
		print(result)
		os.system("cp -a Nettacker/.data/results/. ./DATA/")
		return render(request, "vul.html", {"target" : target, "output": result } )
	else:
		os.system("rm -rf Nettacker/.data/")
		return render(request, "vul.html", {"target" : target,  "greetings":"jatin@linux:Cypher/home> Hello My name is Spectorn! What kind of scan you would like to perform on target?" })
		


def result(request):
	try:
		start = time.time()
		url = request.GET['text']
		damn = urlparse(url)
		global target
		target = damn.netloc		
		print(damn)
		url = url[8:]
		os.chdir(os.getcwd()+ "/../spidey/")
		os.system("scrapy crawl stack -a " + "urls=https://builtwith.com/?https%3a%2f%2f" + url)
		with open( os.getcwd() + "/../Cypher/DATA/data.json", "r") as f:
			data = json.load(f)
			f.close()
		Scanners(damn.netloc, list(data.keys()).pop()).start()
		return render(request, "result.html", { "data": data, "url": url })
	except Exception as e:
		print(e)
		return HttpResponse("<h2> Something went wrong please check the URL... </h2>")


def result2(request):
	sub = {}
	print(os.getcwd())
	with open("../Cypher/DATA/nscan.json", 'r') as f:
		nres = json.load(f)
		f.close()
	# os.remove("nscan.json")
	nres = nres[list(nres.keys()).pop()]
	lists = [ k for k, v in nres.items() if (type(v) == list and v != [])]
	dicts = [ k for k, v in nres.items() if (type(v) == dict and v != {})]
	return render(request, "result2.html", {'nres': nres, 'lis':lists })


def vulnrecord(request):
	print(os.getcwd())
	with open( os.getcwd() + '/../Cypher/DATA/vul.json', 'r') as fi:
		data = json.load(fi)
		fi.close()
	return render(request, "va.html", data)





def signal(request):
	try:
		print(os.getcwd())
		with open("../Cypher/DATA/nscan.json", 'r') as f:
			f.close()
		return HttpResponse()
	except:
		return HttpResponse( status=404)

