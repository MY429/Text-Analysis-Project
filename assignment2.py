import urllib.request 
from nltk.sentiment.vader import SentimentIntensityAnalyzer # for nltk sentiment
import nltk
nltk.download('vader_lexicon') 

#url = 'https://www.gutenberg.org/ebooks/221'
url = 'https://www.gutenberg.org/files/221/221-0.txt'
with urllib.request.urlopen(url) as f:
    response = urllib.request.urlopen(url)
    data = response.read()  # a `bytes` object
    text = data.decode('utf-8')
    print(text) # for testing

collection = list(text.split())
sherlock_holmes_count = 0
dr_waston = 0
charles_milverton = 0
word_count = 0

#find the name frequency appeared in text
for word_count in range (len(collection)):
    if collection[word_count] == "Sherlock" or collection[word_count] == "Holmes":
        sherlock_holmes_count += 1
        word_count +=1
    elif collection[word_count] == "Watson" or collection[word_count] == "John":
        dr_waston += 1
        word_count += 1
    elif collection[word_count] == "Charles" or collection[word_count] == "Augustus" or collection[word_count] == "Milverton":
        charles_milverton += 1
        word_count += 1
    else:
        word_count += 1


print (f'The main character of the detective sequel: Sherlock Holmes mentioned in the book for {sherlock_holmes_count} times in total')
print (f'The main close partner (of Sherlock Holmes) Dr. John Watson mentioned in the book for {dr_waston} times in total')
print (f'The main Main Villain of the detective sequel: Charles Augustus Milverton mentioned in the book for {sherlock_holmes_count} times in total')


#sentiment analysis using NLTK
sentence = 'His head had been horribly mutilated by an expanding revolver bullet, but no weapon of any sort was to be found in the room.'
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)


