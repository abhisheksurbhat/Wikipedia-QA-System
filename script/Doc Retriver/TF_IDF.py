from nltk.corpus import PlaintextCorpusReader as pr
import nltk
import math
root = "d:/data/part2/doc"
para_list = pr(root,'.*')
fileslist = para_list.fileids()
#exit()

	#-----------------------calculate TF-IDF-----------------------------#
def calculateScore(tf,df):
	for i in tf.keys():
		#print('\n',i)
		s = 0
		for j in df.keys():
			try:
				score = (1+math.log( tf[i][j] / sum(tf[i].values()) )) / ( math.log(1 / df[j]) )	
				s += score
				#print(j,score,sep='-')
			except:
				pass
		print(i,'--->',s,sep=' ')



def unigrams(keys):
	df = {}
	tf = {}
	for i in keys:
		df[i.lower()] = 0
		
	for i in fileslist:
		word = para_list.words(i)

		tf[i] = {}
	#----------calculate df of each word in the question----------------------#
		for j in set(word):
			j = j.lower()
			try:
				df[j] += 1
			except:
				pass

		for j in df.keys():
			tf[i][j] = 0
		for k in word:
			k = k.lower()
			try:
				tf[i][k] += 1
			except:
				pass

	calculateScore(tf,df)

# unigrams(['What','is','the','oldest','structure','at','Notre','Dame'])

def bigrams(keys):
	df = {}
	tf = {}
	keys = list(nltk.bigrams(keys))
	for i in keys:
		i = i[0]+' '+i[1]
		df[i.lower()] = 0
		
	for i in fileslist:
		word = para_list.words(i)
		word = list(nltk.bigrams(word))
		bigram =[]
		for j in word:
			bigram.append(j[0]+' '+j[1])
		tf[i] = {}
	#----------calculate df of each word in the question----------------------#
		for j in set(bigram):
			j = j.lower()
			try:
				df[j] += 1
			except:
				pass

		for j in df.keys():
			tf[i][j] = 0
		for k in bigram:
			k = k.lower()
			try:
				tf[i][k] += 1
			except:
				pass
	calculateScore(tf,df)



# bigrams(['What','is','the','oldest','structure','at','Notre','Dame'])