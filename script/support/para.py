import json
fp = open("D:\\data\\SQuaD\\train-v1.1.json","r")
data = json.load(fp)
fp.close()
datal = data['data']
#data = data[0] #change here for other doc
#data = data['paragraphs']
d = 0
fd = open("text.txt", "a", encoding = "utf8")
for data in datal:
	count  = 1
	data = data['paragraphs']
	for i in data:	
		p = i['context']
		fd.write(p)
	fd.close()