# **Web Scraping for Company Insights & Predicting Customer Buying Behaviours**


## Table of Contents
* [Web Scraping](#web-scraping)
* [Data Preprocessing](#data-preprocessing)
* [Sentiment Analysis](#sentiment-analysis)
* [Data Visualization](#data-visualization)
* [Exploratory Data Analysis](#exploratory-data-analysis)
* [Mutual Information graphs](#mutual-information-graphs)
* [Test and Train Model](#test-and-train-model)
* [Validate Model](#validate-model)
* [Conclusion](#conclusion)
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


## **Predictive Modelling on Customers Data**
Predictive models are machine learning algorithms trained on high-quality customer data, requiring manipulation and preparation to accurately predict target outcomes.

### **Exploratory Data Analysis**
- Exploratory Data Analysis is a crucial step in the data analysis process, where the primary goal is to understand the data, gain insights, and identify patterns or relationships between variables.
- Imported Chardet library(Universal Character Encoding Detector) for UTF-8 encoded code, applied to CSV, checked for null values.

### **Mutual Information graphs**
- MI score graphs visualize feature relevance to target variable, measuring dependency and aiding feature selection.
- Scikit-learn(sklearn) library calculates MI_score correlation between attributes, and a graph is plotted for visualization purposes.

<img src="https://github.com/adityabasanti/IBM-CSRBOX-Internship-Project/assets/102895768/9206150b-b50a-4197-9957-0d917629a928" width="450">

### **Test and Train Model**
- Test and train split is a crucial step in building and evaluating machine learning models, dividing dataset into training and test sets.
- Training sets contain 70-80% of data, while test sets allocate 20-30%.
- The code splits data into training, validation, and testing sets, ensuring model training, validation, and testing on different subsets, preventing overfitting and providing a reliable evaluation.

**MinMaxScaler**
Min-Max Scaling is a preprocessing technique for scaling numerical features to a fixed range, ensuring consistent scaling across all features.

#### **via. Random Forest Classifier**
Random Forest is an ensemble learning method combining multiple decision trees, capturing complex relationships and interactions for more accurate and robust models.
- For top-6 features (Accuracy = 71.1864)
- For all features (Accuracy = 72.8813)

#### **via. XGB(Extreme Gradient Booster) Classifier**
XGBoost is a popular machine learning algorithm utilizing gradient boosting to optimize model performance and computational efficiency.
- For top-6 features (Accuracy = 71.1864)
- For all features (Accuracy = 71.1864)

### **Validate Model**
Validating the model on the test dataset is an essential step in the machine learning workflow to assess how well the model performs on unseen data.
- Accuracy = 71.1864


## **Conclusion**
**The Random Forest classifier with top 6 features showed slightly higher accuracy than XGBoost. It can predict customer satisfaction or other target variables in datasets. Performance may vary depending on data quality and representativeness.**


## **Libraries Utilized**
- BeautifulSoup (bs4)
- Chardet
- Matplotlib → Pyplot (plt)
- Natural Language Toolkit (nltk)
  - Corpus
    - Stopwords
    - Wordnet
  - Stem → Lemmatization (WordNetLemmatizer)
  - POS Tagging (pos_tag)
  - Tokenize (word_tokenize)
- Numpy (np)
- Pandas (pd)
- Requests (re)
- Seaborn (sns)
- Scikit-learn (sklearn)
  - Ensemble → Random Forest Classifier
  - Feature Selection → Mutual Information Classifier
  - Model Selection → train_test_split
  - Preprocessing → MinMaxScaler    
- VaderSentiment (SentimentIntensityAnalyzer)
- Warnings
- WordCloud → stopwords
  
