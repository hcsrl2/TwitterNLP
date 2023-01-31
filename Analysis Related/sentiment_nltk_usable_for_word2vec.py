import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Load the SentimentIntensityAnalyzer from NLTK
nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

# Texts to be analyzed
texts = ["This is a positive sentence.",
         "This is a negative sentence.",
         "This is a neutral sentence."]

# Scores of words in a dictionary
word_scores = {}

# Analyze the sentiment of each text
for text in texts:
    sentiment = sia.polarity_scores(text)
    words = text.split()
    for word in words:
        if word not in word_scores:
            word_scores[word] = []
        word_scores[word].append(sentiment["compound"])

# Average the scores of words
for word, scores in word_scores.items():
    word_scores[word] = sum(scores) / len(scores)

# Save the word scores to a file
with open("word_scores.txt", "w") as f:
    for word, score in word_scores.items():
        f.write(f"{word}: {score}\n")
