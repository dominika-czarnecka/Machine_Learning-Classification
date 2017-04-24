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

class corpus:
    def __init__(self):
        self.documents = []
        self.categories = reuters.categories()
        self.cat_dict = {}
        iterator = 0
        for category in self.categories:
            iterator = iterator + 1
            self.cat_dict[iterator] = category
            for docid in reuters.fileids(category):
                doc_class = iterator
                if docid.startswith("train"):
                    train = 1
                elif docid.startswith("test"):
                    train = 0
                else:
                    raise
                text = reuters.raw(docid)
                doc = document(text, doc_class, train)
                self.add_document(doc)
        self.initialize_vocabulary()

    def add_document(self, document):
        self.documents.append(document)

    def get_train_documents(self):
        train = []
        for doc in self.documents:
            if doc.train == 1:
                train.append(doc.text)
        return train

    def initialize_vocabulary(self):
        self.vocabulary = {}
        self.inverse_vocabulary = {}

        for line in open('vocabulary.txt'):
            tokens = line.split()
            self.vocabulary[int(tokens[0])] = tokens[1]
            self.inverse_vocabulary[self.vocabulary[int(tokens[0])]] = tokens[0]

            # vocabulary = {}
            # inverse_vocabulary = {}

            # vocabulary_sizes = {}
            # iterator = 0
            # for i,doc in enumerate(self.documents):
            #     if i % 1000 == 0:
            #         print(i)
            #     for word in doc.get_unique_words():
            #
            #         if word not in vocabulary.values():
            #             vocabulary_sizes[iterator] = 0
            #             vocabulary[iterator] = word
            #             inverse_vocabulary[word] = iterator
            #             iterator = iterator + 1
            #         else:
            #             vocabulary_sizes[inverse_vocabulary[word]] += 1
            # #print("Vocabulary: ")
            # #print(vocabulary)
            #
            # sorted_sizes = sorted(vocabulary_sizes.items(), key=operator.itemgetter(1), reverse=True)
            #
            # #print("Sorted Sizes: ")
            # #print(sorted_sizes)
            #
            # keys_sorted = sorted_sizes[:300]
            # #print("Keys Sorted: ")
            # #print(keys_sorted)
            #
            # for i in range(len(vocabulary)):
            #     for value in keys_sorted:
            #         if i == value[0]:
            #             self.vocabulary[i] = vocabulary[i]
            #             self.inverse_vocabulary[vocabulary[i]] = i
            #
            # plik = open('vocabulary.txt', 'w')
            # for v in self.vocabulary.values():
            #     plik.write(str(self.inverse_vocabulary[v]) + "\t" + v + "\t" + str(
            #         vocabulary_sizes[self.inverse_vocabulary[v]]) + "\n")
            #
            # print("Zapisano do pliku")
            # plik.close()

    def get_svm_vectors(self,Train = 0, Test = 0):
        Xs = []
        ys = []
        itt=0
        step=20
        for doc in self.documents:
            itt +=1
            if itt%20 == 0:
                print(itt)
            if Train == 1 and doc.train == 0:
                continue
            if Test == 1 and doc.train == 1:
                continue
            if(itt % step != 0):
                continue
            x = doc.get_vector(self.inverse_vocabulary)
            cat_vec = [0 for i in range(1, 91)]
            cat_vec[doc.doc_class-1] = 1
            y = cat_vec
            #print(y)
            Xs.append(x)
            ys.append(y)
        print("Saving...")
        if Train == 1:
            np.save(str(step)+"_train_Xs.npy", Xs)
            np.save(str(step)+"_train_ys.npy", ys)
            print("Saved to .npy")
        if Test == 1:
            np.save(str(step)+"_test_Xs.npy", Xs)
            np.save(str(step)+"_test_ys.npy", ys)
            print("Saved to .npy")
        return (Xs,ys)

class document:
    def __init__(self, text, doc_class = 1, train = 1):
        self.doc_class = doc_class
        self.train = train
        self.text = text

    def preprocessing(self, raw_tokens):
        no_stopwords = [token for token in raw_tokens if token not in cachedStopWords]
        stemmed_tokens = []
        stemmer = PorterStemmer()
        for token in no_stopwords:
            stemmed_tokens.append(stemmer.stem(token))
        p = re.compile('[a-zA-Z]+')
        pattern_checked = []
        for stem in stemmed_tokens:
            result = stem.replace('.', '')
            result = result.replace(',', '')
            result = result.replace(chr(39), '')
            result = result.replace(chr(34), '')

            if p.match(result) and len(result) >= min_lenght:
                pattern_checked.append(result)

        return pattern_checked

    def get_unique_words(self):
        word_list = []

        for word in self.preprocessing(self.text.split()):
            if word not in word_list:
                word_list.append(word)
        return word_list

    def get_vector(self,inverse_vocabulary):
        lng = len(inverse_vocabulary)
        vector = [0 for i in range(300)]
        iterator = 0
        for i in inverse_vocabulary.keys():
            if i in self.preprocessing(self.text.split()):
                vector[iterator] = 1
            iterator += 1
        return vector


class tf_idf:

    def __init__(self):
        self.D = 0.0
        self.df = {}

    def add_document(self, document):
        self.D += 1.0
        for token in set(document):
            self.df[token] += 1.0

    def idf(self,token):
        return math.log(self.D/self.df[token])

    def tf(self,token,document):
        liczba_wystapien_tokenu = 0.0
        liczba_tokenow = 0.0
        for t in document:
            liczba_tokenow += 1.0
            if t == token:
                liczba_wystapien_tokenu += 1.0
        return liczba_wystapien_tokenu/liczba_tokenow

    def tfidf(self,token, document):
        return self.tf(token,document) * self.idf(token)


# klasyfikator = svm.SVC(kernel="linear")
# crp = corpus()
# (X,y) = crp.get_svm_vectors(Train = 1)
# print("starting fitting procedure")
# klasyfikator.fit(X,y)
# (XT,yt) = crp.get_svm_vectors(Test = 1)
# pozytywne = 0
# wszystkie = 0
# for i,x in enumerate(XT):
#     wszystkie += 1
#     klasa = klasyfikator.predict(x)
#     if klasa == yt[i]:
#         pozytywne = pozytywne + 1
#
# print(pozytywne)
# print(wszystkie)
