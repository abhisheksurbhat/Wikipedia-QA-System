# https://en.wikipedia.org/w/api.php?action=query&format=xml&srsearch=notre+dame&list=search&srlimit=100
import requests
import json
keyword = input("Enter the keyword : ")
baseurl = 'http://en.wikipedia.org/w/api.php'
my_atts = {}
my_atts['action'] = 'query'  # action=query
my_atts['format'] = 'json'   # format=json
my_atts['srsearch'] = keyword
my_atts['list']='search'
my_atts['srlimit'] = 500

resp = requests.get(baseurl, params = my_atts)
print(resp.url)
data = resp.json()
for i in data['query']['search']:
	print(i['title'],"\thttps://en.wikipedia.org/?curid =",i['pageid'])


# https://en.wikipedia.org/?curid = ""