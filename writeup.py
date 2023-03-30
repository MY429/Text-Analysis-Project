"""
Project Overview: In doing this project, I read the instructions and follow the steps. 
First, I went on Project Gutenberg website and found a text that I am interested, (was gonna find Game of Throne but could not find it),
so I used another text/novel <<The Return of Sherlock Holmes>>. I started by fiquring out the frequencies of some key charaters in the novel.
Then I went ahead and tested the sentiment of a sentence related to a murder scene in the novel.

Impelmentation: For the text frequency part, the file is converted into a list, and the words in the file are each converted to a single variable. 
As for the second part, I used the natural language proccesing toolkit to do a sentiment analysis by sentiment analyzer and import functions to help analyze the sentiment of a sentence I selected.

Result: One interesting thing I find from the text analysis is that the name of the main character, detective Sherlock Holmes appeared in the novel for a total of 349 times.
Whereas the name of the biggest villain Charles Augustus Milverton in this novel also appeared 349 times in total. In which it can be said that whenever Sherlock Holmes is called or showed up in the book, the villain Charles Augustus Milverton will also show up.
Regarding the NLTK sentiment analysis, I found that the crime scene sentence I picked from the novel "His head had been horribly mutilated by an expanding revolver bullet, but no weapon of any sort was to be found in the room." has a generally a more negatively neutural(compound:-0.7783) sentiment with absolutely 0 positive sentiment.

Reflection: If there are someting to be improved, I would like to pick an review of a book or movie, in that way, the sentiment analysis could better detect the emotions of the author.
"""