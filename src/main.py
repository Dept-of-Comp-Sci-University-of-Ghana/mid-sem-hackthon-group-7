# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c1CCuaMURFlQaSPBdr2nr2UMaGUBXf2n
"""

#importing the neccesary packages
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
import nltk
import re
import torch
from transformers import BertTokenizer, BertModel
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from transformers import BertTokenizer, BertForSequenceClassification, pipeline,BertModel
from bs4 import BeautifulSoup
import torch
import numpy as np
import pandas as pd
import spacy
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

#instantiating our dataset
df = pd.read_csv('/content/drive/MyDrive/data.csv')

#printing the first five rows of the dataset
print(df.head())

#getting the descriptive statistics of the data
print(df.describe())

print(df.info())

#finding the missing values
print(df.isnull().sum())

#function to clean text by removing symbols
def data_clean(text):
  text = re.sub('r[^\w\s]', '', text)
  text = text.lower()
  return text

df['clean_data'] = df['Sentence'].apply(data_clean)

#converting the data into tokens
df['tokenized'] = df['clean_data'].apply(word_tokenize)

stop_words = set(stopwords.words('english'))

#defining a function to remove stopwords
def remove_stopwords(tokens):
    return [word for word in tokens if word not in stop_words]

df['headline_no_stopwords'] = df['tokenized'].apply(remove_stopwords)

lemmatizer = WordNetLemmatizer()

def lemmatize_words(tokens):
    return [lemmatizer.lemmatize(word) for word in tokens]

df['lemmatized'] = df['headline_no_stopwords'].apply(lemmatize_words)

df['final_headline'] = df['lemmatized'].apply(lambda x: ' '.join(x))

vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['final_headline'])

# Convert the labels to a numpy array
y = df['Sentiment'].values

print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Load FinBERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')
model = BertModel.from_pretrained('yiyanghkust/finbert-tone')

# Load spaCy for POS tagging
nlp = spacy.load("en_core_web_sm")

# Sentence to analyze
sentence = list(df['Sentence'])


# Define a set of financial terms for each noun
financial_terms_bear_market = [
    "downturn", "recession", "decline", "slump", "bearish trend", "negative market",
    "market dip", "market crash", "economic downturn", "depressed market"
]

financial_terms_stocks = [
    "equities", "shares", "securities", "holdings", "equity securities", "common stock",
    "preferred stock", "corporate stock", "public stock", "trading shares"
]

financial_terms_market = [
    "exchange", "bourse", "trading floor", "marketplace", "securities market",
    "stock market", "equity market", "bond market", "commodities market",
    "forex", "financial market", "capital market", "derivatives market",
    "futures market", "options market", "OTC market", "primary market", "secondary market"
]

financial_terms = {
    "bear": financial_terms_bear_market,
    "market": financial_terms_market,
    "stocks": financial_terms_stocks
}

# Perform POS tagging to identify potential target words
for i in sentence:
  doc = nlp(i)
  target_words = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]

# Tokenize and get the embeddings for the sentence
  inputs = tokenizer(i, return_tensors="pt", add_special_tokens=True)
  outputs = model(**inputs)
  token_embeddings = outputs.last_hidden_state[0]
  tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

# Function to compute cosine similarity
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# Tokenize and get the embeddings for financial terms
financial_embeddings = {}
for key, term_list in financial_terms.items():
    for term in term_list:
        term_inputs = tokenizer(term, return_tensors="pt", add_special_tokens=False)
        term_outputs = model(**term_inputs)
        term_embedding = term_outputs.last_hidden_state[0][0].detach().numpy()
        financial_embeddings[term] = term_embedding

ambiguity_flags = {}
for target_word in target_words:
    if target_word in tokens:
        target_idx = tokens.index(target_word)
        target_embedding = token_embeddings[target_idx].detach().numpy()

        # Calculate similarity with all financial terms
        similarity_scores = {}
        for term, embedding in financial_embeddings.items():
            similarity_scores[term] = cosine_similarity(target_embedding, embedding)

        # Check for ambiguity (high similarity to terms from different categories)
        max_similarity = max(similarity_scores.values())
        if max_similarity > 0.7:  # Set a threshold for high similarity
            similar_terms = [term for term, score in similarity_scores.items() if score == max_similarity]
            if len(set([term.split()[0] for term in similar_terms])) > 1:  # Check if similar terms belong to different categories
                ambiguity_flags[target_word] = similar_terms

# Print potential ambiguities
if ambiguity_flags:
    print("Potential ambiguities detected:")
    for word, terms in ambiguity_flags.items():
        print(f"- '{word}' is similar to: {', '.join(terms)}")
else:
    print("No potential ambiguities detected.")

# Compute similarities
similarities = {}
for term in term_list:
    embedding = financial_embeddings[term]
    similarity = cosine_similarity(target_embedding, embedding)
    similarities[term] = similarity

# Sort terms by similarity
sorted_terms = sorted(similarities.items(), key=lambda item: item[1], reverse=True)

# Print the top similar terms
print(f"Top words similar to '{target_word}' in the financial context:")

for term, similarity in sorted_terms:
    print(f"{term}: {similarity:.4f}")