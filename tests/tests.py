import unittest
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from ..src.main import *


# Sample data for testing
df_test = pd.DataFrame({
    'Sentence': ['This is a test sentence with some symbols!', 'Another sentence.'],
    'Sentiment': [1, 0]
})

class TestDataProcessing(unittest.TestCase):

    def test_data_clean(self):
        self.assertEqual(data_clean('Test!@#$'), 'test')
        self.assertEqual(data_clean('UPPERCASE'), 'uppercase')

    def test_remove_stopwords(self):
        tokens = ['this', 'is', 'a', 'test', 'sentence']
        expected = ['test', 'sentence']
        self.assertEqual(remove_stopwords(tokens), expected)

    def test_lemmatize_words(self):
        tokens = ['running', 'mice', 'better']
        expected = ['running', 'mouse', 'better']
        self.assertEqual(lemmatize_words(tokens), expected)

    def test_tfidf_vectorizer(self):
        corpus = ['This is the first document.', 'This document is the second document.']
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(corpus)
        self.assertEqual(X.shape[0], 2)  

    def test_cosine_similarity(self):
        vec1 = np.array([1, 2, 3])
        vec2 = np.array([4, 5, 6])
        similarity = cosine_similarity(vec1, vec2)
        self.assertTrue(0 <= similarity <= 1)  


if __name__ == '__main__':
    unittest.main()