import json
from nltk.tokenize import word_tokenize
fp = open("..\\..\\data\\squad\\train-v1.1.json","r")
data = json.load(fp)
fp.close()
datal = data['data']
#data = data[0] #change here for other doc
#data = data['paragraphs']
d = 0
q = open('question.json',"w",encoding='utf8')
c = open('context.json',"w",encoding='utf8')
qd = {'data':[]}
cd = {'data':[]}

count = 0
dictionary = {'data':[]}
for data in datal:
	data = data['paragraphs']
	
	for i in data:
		p = i['context'].lower()
		cd['data'].append({count:word_tokenize(p)})
		qa = i['qas']
		for j in qa:
			a = j['answers'][0]['text'].lower()
			start = p.find(a)
			end = start+len(a)
			qd['data'].append({'id' : j['id'],'Q':word_tokenize(j['question'].lower()),'A':word_tokenize(a),'start':start,'end':end,'qid2cid':count})
		count += 1
q.write(json.dumps(qd))
c.write(json.dumps(cd))
q.close()
c.close()
	
