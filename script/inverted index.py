from nltk.corpus import PlaintextCorpusReader as pr
from nltk.corpus import stopwords
from nltk import FreqDist
import time
root = "..\\data\\processed\\doc"
wordlist = pr(root,".*")
#print(wordlist.fileids())

l = wordlist.fileids()
dictionary = {}


for i in l:
	words = wordlist.words(i)
	h = dict(FreqDist(words))
	for j,k in h.items():
		j = j.lower()
		if(j not in dictionary):
			dictionary[j] = [[i,k]]
		else:
			dictionary[j].append([i,k])
key = list(dictionary.keys())
key.sort()
fd = open("..\\index\\iindex.txt","w",encoding='utf8')
fd.write("{")
#for i,j in dictionary.items():
#	fd.write("\""+i+"\""+":"+str(j)+"\n")
stopwords = stopwords.words('english')
symbols = ['!','@','#','$','%','^','&','*','(',')','-','+','=','?',':',':',',','.','/','\\','\"','\'','`','~']
stopwords.extend(symbols)
for i in key:
	if(i not in stopwords):
		fd.write("\""+i+"\":"+str(dictionary[i])+"\n")
fd.write("}")
fd.close()