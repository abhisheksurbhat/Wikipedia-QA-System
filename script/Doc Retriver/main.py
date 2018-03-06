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

    question = input("Enter the question to be searched: ")	#take question input form user ? should be there

    tokens = QP.tokenize(question)				#converting sentence into words thats it

    keywords = QP.postag(tokens)				#eliminating some keywords based on parts of speech tagging

    if(len(keywords) == 0):     					# if pos tagging eliminates all the word
        keywords = tokens

    query_keys = QP.bigram(keywords)				# making search keys into two keys to search wikipedia

    if(len(query_keys) == 0):       					# if there is only one key element bigram cannot happen
        query_keys = keywords					

#---------------------------Question Processing  Done-------------------------#

    n = AE.getArticles(query_keys)				# gets the article soupifies and writes to a file under doc folder
    print("Fetched ",n, "articles",sep = ' ')				# just printing how many articles v fetched
    
    #-------------------------------TF-IDF-------------------------------------------#
    
    print('\n--------unigram rank---------')
    TF_IDF.unigrams(tokens)					# it is as it seems
    print('\n---------bigram rank---------')
    TF_IDF.bigrams(tokens)
    exit()		# lets try unigram bigram and also trigram hashing


if __name__ == '__main__' :
    main()
