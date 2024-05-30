# import sentence segmentation class 
from idsentsegmenter.sentence_segmentation import SentenceSegmentation

news_content = ""
# open sample news content 
with open("news_example.txt", "r") as fio:
    news_content = fio.read()

print("news content: ")
print(news_content)

print("-" * 82)

# create sentence segmenter instance from SentenceSegmentation class
sentence_segmenter = SentenceSegmentation()

# parse text to sentences 
sentences, end_of = sentence_segmenter.get_sentences(news_content)

print("news sentences: ")
# print sentences from previous sentence segmentation process
for i, sent in enumerate(sentences):
    print(i, sent)

print("=======================")
for i,end in enumerate(end_of):
    if i==0:
        print(i,news_content[:end])
    else:
        print(i,news_content[end_of[i-1]:end])