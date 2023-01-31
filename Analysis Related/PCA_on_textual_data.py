import numpy as np
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer

# Load data
documents = ["This is the first document.",
             "This is the second document.",
             "And the third one.",
             "Is this the first document?"]

# Convert texts to numerical representation using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents).toarray()

# Perform PCA
pca = PCA(n_components=2)
X_transformed = pca.fit_transform(X)

# Print explained variance ratio
print(pca.explained_variance_ratio_)
