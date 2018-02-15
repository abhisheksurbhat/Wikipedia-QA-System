'''
        Script to extract keywords from a question.
        Written By - Abhishek Surbhat
                                                                            '''

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim import corpora, models

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
    something = ""
    for i in clean_words:
        word_list.append(clean_words)
    dictionary = corpora.Dictionary(word_list)
    corpus = [dictionary.doc2bow(i) for i in word_list]
    ldamodel = models.ldamodel.LdaModel(
        corpus, num_topics=1, id2word=dictionary, passes=4)
    keys = ldamodel.print_topics(num_words=3)
    for i in keys:
        something = i[1]
    whatever = something.split()
    print(whatever)

def initialize():

    '''Start of script.'''
    question = input("Enter question.(End question with ?)\n")
    clean_words = cleanup(question)
    trylda(clean_words)

if __name__ == '__main__':
    initialize()
