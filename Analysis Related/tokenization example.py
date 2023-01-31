import nltk
with open("file.txt", "r") as file:
    text = file.read()

#Tokenize the text into a list of words:

nltk.download('punkt')
from nltk.tokenize import word_tokenize

words = word_tokenize(text)
#Create a dictionary to store the weight score of each word, take data from sentimentresults
word_weights = {}

# Assume that you have a list of tuples where each tuple contains a word and its weight score
for word, weight in word_weights_list:
    word_weights[word] = weight
#Analyze the text by summing up the weight scores of each word:
total_weight = 0
for word in words:
    if word in word_weights:
        total_weight += word_weights[word]
print("Total weight:", total_weight)