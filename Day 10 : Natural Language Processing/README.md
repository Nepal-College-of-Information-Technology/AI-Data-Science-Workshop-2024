# Day 10: Natural Language Processing (NLP)

## Goal:
The goal of this session is to introduce students to the basics of **Natural Language Processing (NLP)**, focusing on text processing techniques and building a **Sentiment Analysis Model**. By the end of the session, students will be able to preprocess text data and train a model to classify text sentiment.

---

## Topics Covered:

### 1. **Text Processing**:
   - **Tokenization**: Breaking text into individual words or tokens.
   - **Stopwords Removal**: Removing common words that do not contribute much to the meaning of the text (e.g., "is", "the").
   - **Lemmatization**: Reducing words to their base or dictionary form (e.g., "better" to "good").
   - **Real-world example**: Analyzing customer feedback or movie reviews.

### 2. **Sentiment Analysis**:
   - **Sentiment Analysis**: Classifying text as either positive or negative.
   - **Text Classification**: Using machine learning to categorize text.
   - **Real-world application**: Classifying movie reviews or product reviews into positive or negative sentiments.

### 3. **Hands-on Activity: Building a Sentiment Analysis Model**:
   - Preprocessing text using tokenization, stopwords removal, and lemmatization.
   - Converting text into numerical format using **CountVectorizer**.
   - Training a **Naive Bayes** classifier to predict the sentiment of text data.

---

## Notebooks:

1. **Part1_Text_Processing_Basics.ipynb**:
   - Covers the basics of text preprocessing using NLTK.
   - Introduces **tokenization**, **stopwords removal**, and **lemmatization** with real-world examples.

2. **Part2_Sentiment_Analysis_Model.ipynb**:
   - Step-by-step guide to building a **Sentiment Analysis Model**.
   - Preprocessing a small dataset of movie reviews and using **Naive Bayes** for text classification.
   - Hands-on example for predicting the sentiment of new reviews.

---

## Key Learning Outcomes:

- Understand the key steps involved in **text preprocessing**.
- Learn to use **tokenization**, **stopwords removal**, and **lemmatization** to clean text data.
- Build a simple **Sentiment Analysis Model** using **Naive Bayes**.
- Apply these techniques to real-world text datasets like movie reviews or customer feedback.

---

## Resources:

- [NLTK Documentation](https://www.nltk.org/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Sentiment Analysis Guide](https://monkeylearn.com/sentiment-analysis/)
- [Naive Bayes for Text Classification](https://scikit-learn.org/stable/modules/naive_bayes.html)

---

### Activity:

**Build a Sentiment Analysis Model**:
- In this activity, you will preprocess a small dataset of movie reviews.
- You will build and train a **Naive Bayes** model to classify each review as positive or negative.
- Test your model with new reviews to see if it can accurately predict sentiment.

---

**Important Notes:**
- Ensure that **NLTK** and **scikit-learn** are installed in your environment.
- You can experiment with different datasets (e.g., product reviews, tweets) and text processing techniques.