Starting with sQuaD Dataset

1. Understand the dataset structure which is hierarchical.
2. Script to write paragraphs into seperate docs
3. The same script seperates question answer into a seperate folder with the same name as the paragraph with "Q" attatched.
4. Script for inverted index(ii) generator.
	1. Just considering paragraph docs for ii 
	2. Using NLTK library to tokinize 
	3. Using python function to convert word to lower case
	4. Using NLKT stopword list to eliminate stopwords
	to be done...
		1. Stemming
5. Writing inverted index to a txt file in a python dictionary format so that it can be easily loaded and hashed.
6. rusult consists of around 80k unique words.

Existing problems
1. stemming has t be done
2. chinese and other non english words must be eliminates.
3. better docs name to resuce ii file size
4. major problem - how to deal with wikipedia that is so large.

future thoughts
1. Question analysis/processing
2. how to indentify keywords in question. 