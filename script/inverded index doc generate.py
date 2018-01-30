import json
fp = open("..\\data\\squad\\train-v1.1.json","r")
data = json.load(fp)
fp.close()
datal = data['data']
#data = data[0] #change here for other doc
#data = data['paragraphs']
d = 0

for data in datal:
	count  = 1
	data = data['paragraphs']
	for i in data:
		fd = open("..\\data\\processed\\doc\\doc"+str(d)+"A" + str(count) + ".txt", "w", encoding = "utf8")
		p = i['context']
		fd.write(p)
		fd.close()
		fd = open("..\\data\\processed\\docQ\\docQ"+str(d)+"A" + str(count) + ".txt", "w", encoding = "utf8")
		q = i['qas']
		for j in q:
			fd.write(" " + j['question']+"\n"+"\t" + j['answers'][0]['text'] + "\n")
		count += 1
	d += 1
	fd.close()