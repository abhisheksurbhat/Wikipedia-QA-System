'''
        Script to extract keywords from a question.
        Written By - Abhishek Surbhat
                                                                            '''

import re
import requests
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim import corpora, models

def getLinks(keyword):

    '''Used to fetch Wikipedia links. Not used currently.'''
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

def trylda(clean_words):

    '''Main LDA Algorithm. Have to fix output format.'''
    word_list = []
    keywords = []
    something = ""
    for i in clean_words:
        word_list.append(clean_words)
    dictionary = corpora.Dictionary(word_list)
    corpus = [dictionary.doc2bow(i) for i in word_list]
    ldamodel = models.ldamodel.LdaModel(
        corpus, num_topics=1, id2word=dictionary, passes=6)
    keys = ldamodel.print_topics(num_words=3)
    for i in keys:
        keystring = i[1]
    keystring = re.split("\W", keystring)
    pattern = re.compile("[a-zA-Z]+")
    for i in keystring:
        if pattern.match(i):
            keywords.append(i)
    return keywords

def initialize():

    '''Start of script.'''
    question = input("Enter question.(End question with ?)\n")
    clean_words = cleanup(question)
    keywords = trylda(clean_words)
    for i in keywords:
        getLinks(i)

if __name__ == '__main__':
    initialize()
