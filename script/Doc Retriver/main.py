'''
        Main script to run Document Retriever.
                                                            '''
import os
import scripts.extract as extract
import scripts.getArticle as getArticle
import questionProcessor as QP
import articleExtractor as AE
import TF_IDF
def main():
    
    '''Main function.'''
    print("----------------------------------------------Document Retriever--------------------------------------------------")

    question = input("Enter the question to be searched: ")

    tokens = QP.tokenize(question)

    keywords = QP.postag(tokens)

    query_keys = QP.bigram(keywords)

#---------------------------Question Processing  Done-------------------------#

    n = AE.getArticles(query_keys)
    print("Fetched ",n, "articles",sep = ' ')
    
    #-------------------------------TF-IDF-------------------------------------------#
    
    TF_IDF.unigrams(tokens)
    TF_IDF.bigrams(tokens)
    exit()		# lets try unigram bigram and also trigram hashing


if __name__ == '__main__' :
    main()
