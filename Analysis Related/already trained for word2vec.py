import numpy as np
import gensim

# Load a pre-trained Word2Vec model
model = gensim.models.Word2Vec.load("word2vec.model")

# Get the word vector for a word
word = "dog"
vector = model[word]

# Find the most similar words to a word
most_similar = model.wv.most_similar(positive=[word])

# Perform arithmetic operations with word vectors
result = model["king"] - model["man"] + model["woman"]
closest_word = model.wv.similar_by_vector(result)[0][0]

# Get the vector for a sentence
sentence = "A dog ran in the park"
sentence_vector = np.mean([model[word] for word in sentence.split()], axis=0)

# Get the similarity between two sentences
sentence1 = "A cat is playing with a ball"
sentence2 = "A dog is chasing a frisbee"
sentence1_vector = np.mean([model[word] for word in sentence1.split()], axis=0)
sentence2_vector = np.mean([model[word] for word in sentence2.split()], axis=0)
similarity = np.dot(sentence1_vector, sentence2_vector) / (np.linalg.norm(sentence1_vector) * np.linalg.norm(sentence2_vector))
