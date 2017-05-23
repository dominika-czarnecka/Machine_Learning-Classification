import gensim
import nltk.data
import re
from nltk.corpus import stopwords, reuters
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
import os.path
import math
import operator
import numpy as np
from Backend.Integration.ClassificatiorInterface import ClassificatorInterface
cachedStopWords = stopwords.words("english")
#from scipy.spatial.distance import cosine

def cosine2(v1, v2):
    v1v2 = 0
    for i in range(100):
        v1v2 += v1[i] * v2[i]
    v1norm = 0
    for i in range(100):
        v1norm += v1[i] * v1[i]
    v1norm = math.sqrt(v1norm)
    v2norm = 0
    for i in range(100):
        v2norm += v2[i] * v2[i]
    v2norm = math.sqrt(v2norm)
    return v1v2/(v1norm*v2norm)

def tokenize(text):
    min_length = 3
    words = map(lambda word: word.lower(), word_tokenize(text));
    words = [word for word in words if word not in cachedStopWords]
    tokens = (list(map(lambda token: PorterStemmer().stem(token), words)));
    p = re.compile('[a-zA-Z]+');
    filtered_tokens = list(filter(lambda token: p.match(token) and len(token) >= min_length, tokens));
    return filtered_tokens


class ReutersDoc2VecModel:
    def __init__(self, fname = 'd2vModel', preprocessing_function = gensim.utils.simple_preprocess):
        self.documents = list()
        self.preprocessing_function = preprocessing_function
        if(os.path.isfile(fname)):
            self.model =  gensim.models.Doc2Vec.load(fname)
        else:
            #trenujemy model
            self.documents = self.getTeggedDocuments()
            self.model = gensim.models.Doc2Vec(self.documents, size=100, min_count=2, iter=55)
            self.model.save(fname)

    def getTeggedDocuments(self):
        documents = list()
        for docid in reuters.fileids():
            if docid.startswith("train"):
                text = reuters.raw(docid)
                tags = reuters.categories(docid)
                documents.append(gensim.models.doc2vec.TaggedDocument(self.preprocessing_function(text), [docid] + tags))
        return documents

    def getDocVector(self,id):
        return self.model.docvecs[id]

    def similar_by_vec(self,vector):
        return self.model.similar_by_vector(vector)

    def similar_by_text(self, text):
        vector = self.model.infer_vector(self.preprocessing_function(text))
        return self.model.similar_by_vector(vector)

    """
    The closer to 1, the more similar. 
    """
    def cosine_similarity(self, v1, v2):
        return cosine2(v1, v2)

    def get_tags_for_text(self, text):
        tags = {}
        vectors = []
        for i in range(20):
            vector = self.model.infer_vector(self.preprocessing_function(text))
            vectors.append(vector)
        average_infered_vector = np.array(np.mean([v for v in vectors], axis=0))
        for c in reuters.categories():
            cvec = self.model.docvecs[c]
            tags[c] = self.cosine_similarity(average_infered_vector, cvec)
        sorted_tags = sorted(tags.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_tags

    def classify(self, text, number_of_categories, get_similarity=False):
        tags = self.get_tags_for_text(text)
        categories_for_text = []
        iter = 0
        for t in tags:
            if iter < number_of_categories:
                iter += 1
                if get_similarity:
                    categories_for_text.append(t)
                else:
                    categories_for_text.append(t[0])
        return categories_for_text



"""
Przykładowe użycie:
"""
MyModel = ReutersDoc2VecModel(preprocessing_function= tokenize)
raw_text = reuters.raw('test/14828')
#Jeżeli chcemy otrzymać dwie najbardziej prawdopodobne kategorie dla danego tekstu, to number_of_categories=2:
infered_categories = MyModel.classify(raw_text, number_of_categories= 3)
print("Kategorie z klasyfikacji dla \'test/14828\':")
print(infered_categories)
#print(MyModel.classify(raw_text, number_of_categories= 3, get_similarity=True))
print("Kategorie z korpusu dla \'test/14828\':")
print(reuters.categories('test/14828'))
