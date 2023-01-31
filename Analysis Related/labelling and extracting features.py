import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pymongo
#Load the data into a Pandas DataFrame:
#TODO retrieve from mongo convert to csv
df = pd.read_csv("data.csv")
#Extract the features using CountVectorizer:

vectorizer = CountVectorizer()
features = vectorizer.fit_transform(df["text"])
#Perform train-test split:

X_train, X_test, y_train, y_test = train_test_split(features, df["label"], test_size=0.2)
#Train a Naive Bayes classifier:

classifier = MultinomialNB()
classifier.fit(X_train, y_train)
#Predict the labels for the test data:

y_pred = classifier.predict(X_test)
#Connect to MongoDB and create a collection:

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["results"]
#Save the results to the collection:

results = {"actual": y_test.tolist(), "predicted": y_pred.tolist()}
collection.insert_one(results)