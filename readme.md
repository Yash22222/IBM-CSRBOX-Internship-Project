# **Web Scraping for Company Insights & Predicting Customer Buying Behaviours**


## Table of Contents
* [Web Scraping](#web-scraping)
* [Data Preprocessing](#data-preprocessing)
* [Sentiment Analysis](#sentiment-analysis)
* [Data Visualization](#data-visualization)
* [Libraries Utilized](#libraries-utilized)


## **Web Scraping**
Web scraping was employed to gather customer reviews and insights about Air India from the website [Airline Quality](https://www.airlinequality.com/airline-reviews/air-india/). Using web scraping techniques, data was extracted from the website, including customer comments, ratings, and other relevant information, which was then compiled into the "Reviews Dataset" for further analysis, such as predicting customer buying behaviors or understanding customer sentiments towards Air India's services.


## **Data Preprocessing**
Data preprocessing is crucial in the data mining process, involving cleaning, transforming, and integrating data for analysis. 
Its goal is to enhance data quality and suitability for specific tasks

### **Data Cleaning**
Data cleaning is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset.
- Removal of sentences before '|' in dataframe
- Removal of all special characters from the dataframe

### **Tokenization**
- Tokenization is the process of dividing text into a set of meaningful pieces.
- Tokens converted to tuples using POS Tagging, grouped into words through lemmatization.


## **Sentiment Analysis**
Sentiment analysis is the process of analyzing digital text to determine if the emotional tone of the message is positive, negative, or neutral.

### **VADER**
- VADER( Valence Aware Dictionary for Sentiment Reasoning) is an NLTK module that provides sentiment scores based on the words used.
- It is a rule-based sentiment analyzer in which the terms are generally labeled as per their semantic orientation as either positive, negative or neutral.


## **Data Visualization**
Data visualization uses graphics like charts, plots, infographics, and animations to represent complex data relationships and provide easy-to-understand insights.

### **via. Matplotlib**
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

<img src="https://github.com/nilayhangarge/IBM-CSRBOX-Internship-Project/assets/88373687/03e1d670-39bb-4c64-aedd-ccdeb2c39755" width="300">

### **via. WordCloud**
Wordcloud is basically a visualization technique to represent the frequency of words in a text where the size of the word represents its frequency.

<img src="https://github.com/nilayhangarge/IBM-CSRBOX-Internship-Project/assets/88373687/d3770498-5ab5-4707-a44d-5482123565ec" width="450">


## **Libraries Utilized**
- BeautifulSoup (bs4)
- Matplotlib → Pyplot (plt)
- Natural Language Toolkit (nltk)
  - Corpus
    - Stopwords
    - Wordnet
  - Stem → Lemmatization (WordNetLemmatizer)
  - POS Tagging (pos_tag)
  - Tokenize (word_tokenize)
- Pandas (pd)
- Requests (re)
- VaderSentiment (SentimentIntensityAnalyzer)
- WordCloud → stopwords
