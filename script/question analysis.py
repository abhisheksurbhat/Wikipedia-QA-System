import json
from nltk.corpus import PlaintextCorpusReader as pr
from nltk.tokenize import word_tokenize
import nltk
import matplotlib.pyplot as plt
fp = open("D:\\data\\SQuaD\\train-v1.1.json","r",encoding='utf8')

file = json.load(fp)

fw = open("question.txt","a",encoding='utf8')

#print(type(data[0]['paragraphs']),len(data[0]),data[0]['paragraphs'][0]['qas'][0].keys(),data[0]['paragraphs'][0]['qas'][0]['question'])
for i in file['data']:
	for j in i['paragraphs']:
		for k in j['qas']:
			fw.write(k['question']+"\n")

fw.close()
fp.close()

wordlists =open("question.txt","r",encoding='utf8').read()
words = word_tokenize(wordlists)
w = nltk.pos_tag(words)
D= {}

for i in w:
	try:
		D[i[1]]+=1
	except:
		D[i[1]]=1

print(D['WP'])
plt.bar(range(len(D)), list(D.values()), align='center')
plt.xticks(range(len(D)), list(D.keys()),rotation='90')
plt.show()