from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
import re


class DataTransformer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(tokenizer=self.tokenize)
        self.mlb = MultiLabelBinarizer()
        self.cachedStopWords = stopwords.words("english")

    # Method for tokenize (used in tf-idf)
    def tokenize(self, text):
        min_length = 3

        words = map(lambda word: word.lower(), word_tokenize(text))
        words = [word for word in words if word not in self.cachedStopWords]
        tokens = (list(map(lambda token: PorterStemmer().stem(token), words)))

        p = re.compile('[a-zA-Z]+')
        filtered_tokens = list(filter(lambda token: p.match(token) and len(token) >= min_length, tokens))

        return filtered_tokens

    # Tokenizer - using tf-idf vectorizer to transformate array of documents into vectors
    def transform_documents(self, train_docs, test_docs):
        vectorised_train_documents = self.vectorizer.fit_transform(train_docs)
        vectorised_test_documents = self.vectorizer.transform(test_docs)

        return vectorised_train_documents, vectorised_test_documents

    # Label binarizer - using MultiLabelBinarizer to transform array of labels into vectors
    def transform_labels(self, train_labels, test_labels):
        binarized_train_labels = self.mlb.fit_transform(train_labels)
        binarized_test_labels = self.mlb.transform(test_labels)

        return binarized_train_labels, binarized_test_labels
