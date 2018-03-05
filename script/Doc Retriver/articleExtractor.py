from urllib import request
from bs4 import BeautifulSoup
import requests
import re
def  getArticles(keywords):
	baseurl = 'http://en.wikipedia.org/w/api.php'
	my_atts = {
		'action' : 'query',
		'format' : 'json',
		'list' : 'search',
		'srlimit' : 4	# change to get more number of articles
	}

	print("Fetching Articles.............")
	link = []
	for i in keywords:
		print(i)
		my_atts['srsearch'] = i
		resp = requests.get(baseurl, params=my_atts)
		data = resp.json()
		for i in data['query']['search']:
			link.append("https://en.wikipedia.org/?curid="+str(i['pageid']))
			# print(i['title'], "\t", link)
	count = 0
	for url in link:
		print(url)
		html = request.urlopen(url)
		raw = BeautifulSoup(html, 'html.parser')
		# fp = open("doc/"+str(count)+".txt","a",encoding='utf8')
		para = raw.find_all("p")
		count1 = 0
		for i in para:
			fp = open("doc/"+str(count)+".txt","a",encoding='utf8')		#+str(count1)
			fp.write(i.get_text())
		#count1 += 1
		fp.close()
		count+=1
	
	return len(link)