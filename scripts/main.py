'''
        Main script to run Document Retriever.
                                                            '''
import os
import extract
import getArticle

def main():
    
    '''Main function.'''
    print("\t\t\tDocument Retriever.\nEnter the question to be searched.\n")
    baseDir = "/home/abhishek/Projects/Wikipedia-QA-System/"
    resultDir = baseDir+"results"
    scriptDir = baseDir+"scripts"
    linkList = []
    titleList = []
    fileList = []
    question = input();
    cleanWords = extract.cleanup(question)
    nouns, keywords = extract.posTag(cleanWords)
    bigrams = extract.bigram(keywords)
    print("Fetching links...\n")
    for i in bigrams:
        searchString = i[0]+" "+i[1]
        title, link = extract.getLinks(searchString)
        linkList.append(link)
        titleList.append(title)
    for i in nouns:
        title, link = extract.getLinks(i)
        linkList.append(link)
        titleList.append(title)
    for i in titleList:
         fileString = i.replace(" ", "")
         fileList.append(fileString)
    print("Fetching Articles...\n")
    os.chdir(resultDir)
    for i in range(len(linkList)):
        getArticle.Data(titleList[i], linkList[i])
    os.remove('newfile.txt')

if __name__ == '__main__' :
    main()
