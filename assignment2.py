import urllib.request

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

for word_count in range (len(collection)):
    if collection[word_count] == "Sherlocl" or collection[word_count] == "Holmes":
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
print (f'The main Main Villain of the detective sequel: Sherlock Holmes mentioned in the book for {sherlock_holmes_count} times in total')

#老师，我miss了好多节课，好多东西都没弄懂，可不可延一下assignment，下周等我回babson补课完再把这个余下的补上， 感谢。