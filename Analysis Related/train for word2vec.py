import gensim
from gensim.models import Word2Vec

# Load texts from a list of sentences
texts = [["this", "is", "a", "sentence"],
         ["this", "is", "another", "sentence"],
         ["yet", "another", "sentence", "here"]]

# Train a Word2Vec model on the texts
model = Word2Vec(texts, min_count=1, size=100, workers=4)

# Save the model for later use
model.save("word2vec.model")

# Access the word vectors
vector = model["sentence"]

# Get the most similar words to a word
most_similar = model.wv.most_similar("sentence")
