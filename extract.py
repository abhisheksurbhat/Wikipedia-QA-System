'''
        Script to extract keywords from a question.
        Written By - Abhishek Surbhat
                                                                            '''

import re
import nltk
import requests
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim import corpora, models

def getLinks(keyword):

    '''Used to fetch Wikipedia links. Needs modification.'''
    baseurl = 'http://en.wikipedia.org/w/api.php'
    my_atts = {}
    my_atts['action'] = 'query'
    my_atts['format'] = 'json'
    my_atts['srsearch'] = keyword
    my_atts['list'] = 'search'
    my_atts['srlimit'] = 2

    resp = requests.get(baseurl, params=my_atts)
    #print(resp.url)
    data = resp.json()
    for i in data['query']['search']:
        link = "https://en.wikipedia.org/?curid="+str(i['pageid'])
        print(i['title'], "\t", link)
    

def cleanup(string):

    '''Used to clean up the sentence(i.e. to remove stop words and formatters)'''
    words = word_tokenize(string)
    stop_words = stopwords.words('english')
    words = [i for i in words if i not in stop_words]
    words.pop()
    return words

def tryLda(cleanWords):

    '''Main LDA Algorithm. Not usable for now.'''
    word_list = []
    keywords = []
    something = ""
    qWords = ["What", "Where", "Who", "How", "When", "Why" ]
    for i in cleanWords:
        word_list.append(cleanWords)
    dictionary = corpora.Dictionary(word_list)
    corpus = [dictionary.doc2bow(i) for i in word_list]
    ldamodel = models.ldamodel.LdaModel(
        corpus, num_topics=1, id2word=dictionary, passes=1)
    keys = ldamodel.print_topics(num_words=3)
    for i in keys:
        keystring = i[1]
    keystring = re.split("\W", keystring)
    pattern = re.compile("[a-zA-Z]+")
    for i in keystring:
        if pattern.match(i):
            keywords.append(i)
    keywords = [i for i in keywords if i not in qWords]
    return keywords

def posTag(cleanWords):

    '''Parts of Speech tagging. Useful for pulling keywords.'''
    keywords = []
    tags = nltk.pos_tag(cleanWords)
    for i in tags:
        if i[1] == "NNP" or i[1]=="NNS" or i[1]=="NN":
            keywords.append(i[0])
    print(keywords)

def initialize():

    '''Start of script.'''
    question = input("Enter question.(End question with ?)\n")
    cleanWords = cleanup(question)
    #keywords = tryLda(cleanWords)
    keywords = posTag(cleanWords)
    for i in keywords:
        print("Keyword->",i)
        getLinks(i)

if __name__ == '__main__':
    initialize()
