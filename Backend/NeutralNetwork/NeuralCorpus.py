from os import listdir
from sklearn import svm
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords, reuters
import re
import math
import numpy as np
from operator import itemgetter

cachedStopWords = stopwords.words("english")
min_lenght = 3
vocabulary_len = 1500
target = "tfidf"

# UP target,
    # frequency - slownik najczesciej występujących slow w dokumentach
    # entrophy - slownik slow majacych najwieksza entropie

class corpus:
    def __init__(self):
        print("Initialize corpus...")
        self.documents = []
        self.categories = reuters.categories()
        self.cat_dict = {}
        self.tfidf = tf_idf()
        iterator = 0

        for category in self.categories:
            iterator += 1
            self.cat_dict[iterator] = category
        for docid in reuters.fileids():
            doc_cat = [0 for i in range(0, 90)]
            for i in range(90):
                if self.categories[i] in reuters.categories(docid):
                    doc_cat[i] = 1
            if docid.startswith("train"):
                train = 1
            elif docid.startswith("test"):
                train = 0
            else:
                raise
            text = reuters.raw(docid)
            doc = document(text, doc_cat, train)
            self.tfidf.add_document(doc)
            self.add_document(doc)

        self.vocabulary_entrophy = {}
        self.initialize_vocabulary(target)

    def add_document(self, document):
        self.documents.append(document)

    def get_train_documents(self):
        train = []
        for doc in self.documents:
            if doc.train == 1:
                train.append(doc.text)
        return train

    def initialize_vocabulary(self, type):
        self.vocabulary = {}
        self.inverse_vocabulary = {}
        print(target)
        if type == "frequency":
            vocabulary = {}
            inverse_vocabulary = {}

            vocabulary_sizes = {}
            iterator = 0
            for i, doc in enumerate(self.documents):
                if i % 1000 == 0:
                    print(i)
                for word in doc.get_unique_words():

                    if word not in vocabulary.values():
                        vocabulary_sizes[iterator] = 0
                        vocabulary[iterator] = word
                        inverse_vocabulary[word] = iterator
                        iterator = iterator + 1
                    else:
                        vocabulary_sizes[inverse_vocabulary[word]] += 1

            sorted_sizes = sorted(vocabulary_sizes.items(), key=itemgetter(1), reverse=True)
            keys_sorted = sorted_sizes[:vocabulary_len]

            for i in range(len(vocabulary)):
                for value in keys_sorted:
                    if i == value[0]:
                        self.vocabulary[i] = vocabulary[i]
                        self.inverse_vocabulary[vocabulary[i]] = i

        if type == "entrophy":
            self.vocabulary_entrophy = {}
            vocabulary = {}
            inverse_vocabulary = {}

            vocabulary_entrophy = {}
            iterator = 0
            for i, doc in enumerate(self.documents):
                if i % 1000 == 0:
                    print(i)
                for word in doc.get_unique_words():
                    probability = doc.get_probability_of_word(word)
                    if word not in vocabulary.values():
                        vocabulary_entrophy[iterator] = -probability * math.log2(probability)
                        vocabulary[iterator] = word
                        inverse_vocabulary[word] = iterator
                        iterator += 1
                    else:
                        vocabulary_entrophy[inverse_vocabulary[word]] -= probability * math.log2(probability)

            sorted_sizes = sorted(vocabulary_entrophy.items(), key=itemgetter(1), reverse=True)
            keys_sorted = sorted_sizes[:vocabulary_len]

            for i in range(len(vocabulary)):
                for value in keys_sorted:
                    if i == value[0]:
                        self.vocabulary[i] = vocabulary[i]
                        self.vocabulary_entrophy[i] = vocabulary_entrophy[i]
                        self.inverse_vocabulary[vocabulary[i]] = i

        if type == "tfidf":
            self.vocabulary_tfidf = {}
            vocabulary = {}
            inverse_vocabulary = {}
            vocabulary_tfidf = {}

            iterator = 0
            for i, doc in enumerate(self.documents):
                if i % 1000 == 0:
                    print(i)
                for word in doc.get_unique_words():
                    probability = doc.get_probability_of_word(word)
                    if word not in vocabulary.values():
                        vocabulary_tfidf[iterator] = self.tfidf.tfidf(word, doc)
                        vocabulary[iterator] = word
                        inverse_vocabulary[word] = iterator
                        iterator += 1
                    else:
                        vocabulary_tfidf[inverse_vocabulary[word]] += self.tfidf.tfidf(word, doc)

            sorted_sizes = sorted(vocabulary_tfidf.items(), key=itemgetter(1), reverse=True)
            keys_sorted = sorted_sizes[:vocabulary_len]

            for i in range(len(vocabulary)):
                for value in keys_sorted:
                    if i == value[0]:
                        self.vocabulary[i] = vocabulary[i]
                        self.vocabulary_tfidf[i] = vocabulary_tfidf[i]
                        self.inverse_vocabulary[vocabulary[i]] = i

    def get_svm_vectors(self, Train=0, Test=0):
        Xs = []
        ys = []
        itt = 0

        doc_number = len(self.documents)
        for doc in self.documents:
            itt += 1
            if itt % 100 == 0:
                print(itt, '|', doc_number)
            if Train == 1 and doc.train == 0:
                continue
            if Test == 1 and doc.train == 1:
                continue
            x = doc.get_vector("frequency", self.inverse_vocabulary, self.vocabulary_entrophy)
            y = doc.doc_class
            Xs.append(x)
            ys.append(y)
        return (Xs, ys)


class document:
    def __init__(self, text, doc_class, train=1):
        self.doc_class = doc_class
        self.train = train
        self.text = text
        self.preprocessed_text = self.preprocessing(self.text.split())

    def preprocessing(self, raw_tokens):

        p = re.compile('[a-zA-Z]+')
        pattern_checked = []
        for stem in raw_tokens:
            result = stem.replace('.', '')
            result = result.replace(',', '')
            result = result.replace(chr(39), '')
            result = result.replace(chr(34), '')

            if p.match(result) and len(result) >= min_lenght:
                pattern_checked.append(result)

        stemmed_tokens = []
        stemmer = PorterStemmer()
        for token in pattern_checked:
            stemmed_tokens.append(stemmer.stem(token))

        no_stopwords = [token for token in stemmed_tokens if token not in cachedStopWords]
        return no_stopwords

    def get_unique_words(self):
        self.inverse_vocabuary = {}
        self.vocabulary_sizes= {}
        inverse_vocabulary = {}
        vocabulary_sizes = {}
        vocabulary = {}
        iterator = 0

        for word in self.preprocessed_text:
            if word not in vocabulary.values():
                vocabulary_sizes[iterator] = 1
                vocabulary[iterator] = word
                inverse_vocabulary[word] = iterator
                iterator += 1
            else:
                vocabulary_sizes[inverse_vocabulary[word]] += 1
        self.inverse_vocabuary = inverse_vocabulary
        self.vocabulary_sizes = vocabulary_sizes
        return vocabulary.values()

    def get_probability_of_word(self, word):
        propability = self.vocabulary_sizes[self.inverse_vocabuary[word]] / len(self.preprocessed_text)
        return propability

    def get_vector(self, type, inverse_vocabulary, vocabulary_entrophy = {}):
        if type == "frequency":
            vector = [0 for i in range(vocabulary_len)]
            iterator = 0
            preprocessed_text = self.preprocessed_text
            for i in inverse_vocabulary.keys():
                if i in preprocessed_text:
                    vector[iterator] = self.vocabulary_sizes[self.inverse_vocabuary[i]]
                    #vector[iterator] = 1
                iterator += 1
            return vector
        if type == "entrophy":
            vector = [0 for i in range(vocabulary_len)]
            iterator = 0
            preprocessed_text = self.preprocessed_text
            for i in inverse_vocabulary.keys():
                if i in preprocessed_text:
                    vector[iterator] = vocabulary_entrophy[inverse_vocabulary[i]]
                iterator += 1
            return vector

class tf_idf:
    def __init__(self):
        self.D = 0.0
        self.df = {}

    def add_document(self, document):
        self.D += 1.0
        for token in document.get_unique_words():
            if token not in self.df.keys():
                self.df[token] = 1.0
            else:
                self.df[token] += 1.0

    def idf(self, token):
        return math.log(self.D / self.df[token])

    def tf(self, token, document):
        liczba_wystapien_tokenu = 0.0
        liczba_tokenow = 0.0
        for t in document.preprocessed_text:
            liczba_tokenow += 1.0
            if t == token:
                liczba_wystapien_tokenu += 1.0
        return liczba_wystapien_tokenu / liczba_tokenow

    def tfidf(self, token, document):
        return self.tf(token, document) * self.idf(token)
