'''
        Script to extract keywords from a question.
        Written By - Abhishek Surbhat
                                                                            '''

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim import corpora, models

def cleanup(string):
    
    words = word_tokenize(string)
    stopWords = stopwords.words('english')
    words = [ i for i in words if i not in stopWords ]
    words.pop()
    return words

def tryLDA(cleanWords):

    wordList = []
    something = ""
    for i in cleanWords:
        wordList.append(cleanWords)
    dictionary = corpora.Dictionary(wordList)
    corpus = [ dictionary.doc2bow(i) for i in wordList ]
    ldamodel = models.ldamodel.LdaModel(
                                                corpus, num_topics=1,
                                                id2word=dictionary, passes=4
                                               )
    keys = ldamodel.print_topics(num_words=3)
    for i in keys:
        something = i[1]
    whatever = something.split()
    print(whatever)

def initialize():

    question = input("Enter question.(End question with ?)\n")
    cleanWords = cleanup(question)
    
    tryLDA(cleanWords)

if __name__ == '__main__':
    initialize()
