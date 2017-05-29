import gensim
import re
from nltk.corpus import stopwords, reuters
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
import os.path
import math
import operator
import numpy as np
cachedStopWords = stopwords.words("english")

"""
Input: v1, v2 - two vectors, they must be of the same length.
Output: It returns a cosine similarity between vectors v1 and v2.
"""
def cosine2(v1, v2):
    v1v2 = 0
    for i in range(len(v1)):
        v1v2 += v1[i] * v2[i]
    v1norm = 0
    for i in range(len(v1)):
        v1norm += v1[i] * v1[i]
    v1norm = math.sqrt(v1norm)
    v2norm = 0
    for i in range(len(v1)):
        v2norm += v2[i] * v2[i]
    v2norm = math.sqrt(v2norm)
    return v1v2/(v1norm*v2norm)

"""
Input:  text - raw text.
Output: A list of tokens.
    This function is used for tokenizing raw text. It includes Stemming and deleting Stop Words.
It was copied from the first PZ laboratories.
"""
def tokenize(text):
    min_length = 3
    words = map(lambda word: word.lower(), word_tokenize(text));
    words = [word for word in words if word not in cachedStopWords]
    tokens = (list(map(lambda token: PorterStemmer().stem(token), words)));
    p = re.compile('[a-zA-Z]+');
    filtered_tokens = list(filter(lambda token: p.match(token) and len(token) >= min_length, tokens));
    return filtered_tokens

"""
A class, that builds a doc2vec model and provides methods for classification.
"""
class ReutersDoc2VecModel:
    def __init__(self, args, fname = 'd2vModel', preprocessing_function = gensim.utils.simple_preprocess):
        self.documents = list()
        self.preprocessing_function = preprocessing_function
        if(os.path.isfile(fname)):
            #Loading the doc2vec model:
            self.model =  gensim.models.Doc2Vec.load(fname)
        else:
            #Creating and training doc2vec model:
            self.documents = self.getTeggedDocuments()
            size = args['size']
            min_count = args['min-count']
            iter = args['iter']
            self.model = gensim.models.Doc2Vec(self.documents,size=size,min_count=min_count,iter=iter)
            #Saving the model:
            self.model.save(fname)

    """
    Output: It returns a list of Tegged Documents, that are needed to build a doc2vec model.
        A gensim.models.doc2vec.TaggedDocument contains a collection of words(tokens) of the document and 
    a collection of tags( docid and cetegories) of the document.
    """
    def getTeggedDocuments(self):
        documents = list()
        for docid in reuters.fileids():
            if docid.startswith("train"):
                text = reuters.raw(docid)
                tags = reuters.categories(docid)
                documents.append(gensim.models.doc2vec.TaggedDocument(self.preprocessing_function(text), [docid] + tags))
        return documents
    """
    def getDocVector(self,id):
        return self.model.docvecs[id]

    def similar_by_vec(self,vector):
        return self.model.similar_by_vector(vector)

    def similar_by_text(self, text):
        vector = self.model.infer_vector(self.preprocessing_function(text))
        return self.model.similar_by_vector(vector)

    
    #The closer to 1, the more similar. 
    def cosine_similarity(self, v1, v2):
        return cosine2(v1, v2)
    """
    """
    Input: text - raw text of a document we want to classify
    Output: A collection of 90 (category, similarity) pairs sorted descending by similarity to given text.
    """
    def get_categories_for_text(self, text):
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
    """
    Input: text - raw text for classification,
        number_of_categories - an integer value, which tells as how many (of the most similar) categories are to be return,
        get_similarity - a boolean value which indicates whether or not to include similarity in the method's output.
    Output: a collection of categories into which the text is classified.
    """
    def classify(self, text, number_of_categories, get_similarity=False):
        tags = self.get_categories_for_text(text)
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
#MyModel = ReutersDoc2VecModel(preprocessing_function= tokenize)
#raw_text = reuters.raw('test/14828')
#print(raw_text)
#Jeżeli chcemy otrzymać dwie najbardziej prawdopodobne kategorie dla danego tekstu, to number_of_categories=2:
#infered_categories = MyModel.classify(raw_text, number_of_categories= 3)
#print("Kategorie z klasyfikacji dla \'test/14828\':")
#print(infered_categories)
#print(MyModel.classify(raw_text, number_of_categories= 3, get_similarity=True))
#print("Kategorie z korpusu dla \'test/14828\':")
#print(reuters.categories('test/14828'))
