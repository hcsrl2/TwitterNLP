#Sentiment Analysis with Azure Text Analytics#

##Project Overview##

This project investigates how public opinions and discussions around environmental leadership and consciousness have evolved on Twitter over the past decade (2012-2022). Azure Text Analytics is the core tool used to analyze sentiment within tweets.

##Data##

* A large dataset of tweets collected from the Twitter API. Search queries will focus on keywords and hashtags related to environmental issues, climate change, sustainability, and similar topics.

##Methodology##

* ##Data Collection:##
* Use the Twitter API to collect a substantial volume of tweets relevant to environmental topics.
* **Data Pre-processing:**
* Clean tweets by removing irrelevant elements like links, special characters, and stop words.
* Normalize text using techniques like stemming and lemmatization.
* Break down tweets into individual words or phrases (tokenization).
* **Azure Text Analytics for Sentiment Analysis:**
* Employ Azure Text Analytics to assign sentiment scores (positive, negative, neutral) to each tweet.
* Track variations in average sentiment scores over time to identify significant shifts or trends.
* **Exploratory Analysis**
* Generate word clouds to visualize the most frequently used terms within environmental conversations on Twitter.

##nsights (To be Determined)##

* How has overall sentiment towards environmental issues changed over the past decade?
* Are there specific events or periods that correlate with significant spikes in positive or negative sentiment?
* What key terms and phrases consistently drive environmental discussions on the platform?

##Technologies##

* **Azure Text Analytics**
* **Python** (with libraries like Pandas, NumPy, NLTK, matplotlib)
* **Twitter API**
