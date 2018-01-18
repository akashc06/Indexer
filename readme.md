# Search Engine Indexer

All the tasks are coded in Python, version 2.7

NOTE : Before running any of the .py files, kindly change the path to the input files

**********************************************************************************************************************	

Task 1,

  --- Files parsed and all HTML tags removed.
  --- Case folding for all files.
  --- File names with "-", "_", etc are renamed by removing such characters.
  --- All punctuations except hypens are removed from text.
  --- No punctions are removed from digits or alphanumeric.

Task 2,

  --- Input for the Indexer are text files obtained from Task 1.
  --- Seperate Indexes created for word unigrams, word bigrams and word trigrams.
  --- Indexes are of form WORD -> (DocID, tf), (DocID, tf), (DocID, tf).....
  --- Data Structure used for Index is Dictionary.
  --- Use of dictionary to keep all the terms as keys, and the corresponding inverted index as values.
  --- The inverted index is again a dictionary with the DocID as key and the tf as value.

Task 3,

  --- For each of the indexes created in Task 2, a table of the form term and tf is generated.
  --- For each of the indexes created in Task 2, a table of the form term, DocID, df is generated.
  --- Tables with term and tf are sorted on the term frequency from most to least.
  --- Tables with term, DocID and df are sorted lexicographically based on terms. 
  --- Generated a list of stop words from the current corpus, and brief explanation and comments on stoplist

**************************************************************************************************************************
To run the program 

-> Go to the folder where the file is located in command prompt
-> use the commad python <filename>.py

**************************************************************************************************************************
The link to download python 2.7 
https://www.python.org/  

**************************************************************************************************************************
Sources of Information:

1. https://www.tutorialspoint.com/python/
2. https://docs.python.org/2/library/functions.html
