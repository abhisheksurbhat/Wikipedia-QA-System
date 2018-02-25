import nltk
import re
import os
from urllib import request
from bs4 import BeautifulSoup

def Data(title, url):

    print("Fetching ",title)
    sentence_words = []
    waste = []
    more_waste = []
    html = request.urlopen(url)
    raw = BeautifulSoup(html, 'html.parser')

    waste = raw.find_all("p", class_ = re.compile('.*'))
    more_waste = raw.find_all("p", id = re.compile('.*') )
    so_much_waste = raw.find_all("p > script language" )
    excessive_waste = raw.find_all("p", {"data-reactid" : re.compile('.*')})
    allstuff = raw.find_all("p")
    para_part = [val for val in allstuff if val not in waste]
    para_part1 = [val for val in para_part if val not in excessive_waste]
    para_part2 = [val for val in para_part1 if val not in so_much_waste]
    para = [val for val in para_part1 if val not in more_waste]

    file2 = open('newfile.txt','w')

    for line in para:
        sentence_words.append(line)

    for i in sentence_words:
        file2.write(str(i))
        file2.write("\n")

    file2.close()
    file1 = open("newfile.txt",'r')
    filename = title+".txt"
    op = open(filename,'w')
    new = BeautifulSoup(file1,"html5lib")
    for line in new:
        random = line.get_text()
        op.write(str(random))
    file1.close()
    op.close()
