import gensim
from nltk.corpus import stopwords, reuters
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
import os.path
import math
import operator
import re
import numpy as np
cachedStopWords = stopwords.words("english")

def tokenize(text):
    """
    Input:  text - raw text.
    Output: A list of tokens.
        This function is used for tokenizing raw text. It includes Stemming and deleting Stop Words.
    It was copied from the first PZ laboratories.
    """
    min_length = 3
    words = map(lambda word: word.lower(), word_tokenize(text));
    words = [word for word in words if word not in cachedStopWords]
    tokens = (list(map(lambda token: PorterStemmer().stem(token), words)));
    p = re.compile('[a-zA-Z]+');
    filtered_tokens = list(filter(lambda token: p.match(token) and len(token) >= min_length, tokens));
    return filtered_tokens

class Doc2VecModel:
    def __init__(self, args, modelFileName, input='', preprocessing_function=tokenize):
        #Inicjalizacja modułu
        self.documents = list()
        self.preprocessing_function = preprocessing_function
        self.cachedStopWords = stopwords.words("english")

        #Wczytanie istniejącego modelu z pliku
        if(os.path.isfile(modelFileName)):
            self.model = gensim.models.Doc2Vec.load(modelFileName)

        #Trenujemy nowy model
        else:
            #Wczytanie otagowanych dokumentów z korpusu Reuters
            self.documents = self.getDocumentsWithTags()

            #Wczytanie parametrów dla tworzonego modelu

            #Ilość wymiarów wektorów dla features
            size = args['size']
            #Wielkość okna
            window = args["window"]
            #Minimalna ilość wystąpień słowa, aby było brane pod uwagę
            min_count = args['min-count']
            #Liczba iteracji treningowych modelu
            iter = args['iter']

            #Stworzenie modelu dla otagowanych dokumentów i podanych parametrów
            #To jest implementacja Paragraph2Vec w bibliotece Gensim
            self.model = gensim.models.Doc2Vec(self.documents, size=size, window=window, min_count=min_count, iter=iter)

            #Zapisanie modelu do pliku o podanej nazwie
            self.model.save(modelFileName)

    #Ocena podobieństwa za pomocą funkcji Cosine
    def cosine_similarity(self, v1, v2):
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
        return v1v2 / (v1norm * v2norm)

    #Pobranie dokumentów treningowych z korpusu Reuters wraz z tagami
    def getDocumentsWithTags(self):
        documents = list()

        for docId in reuters.fileids():
            if docId.startswith("train"):
                text = reuters.raw(docId)
                tags = reuters.categories(docId)
                #Konwersja dokumentu na tokeny
                documents.append(gensim.models.doc2vec.TaggedDocument(self.preprocessing_function(text), [docId] + tags))
        return documents

    #Klasyfikacja dokumentu
    def classify(self, args, text, fileName=""):

        #Wczytanie argumentów

        #Czy zwracać wartość liczbową podobieństwa dokumentu do kategorii
        get_similarity = args["get-similarity"]
        #Ilość kategorii dla których podobieństwo mamy wyświetlić
        number_of_categories = args["number-of-categories"]

        #Klasyfikacja dokumentu - zwrócenie listy kategorii
        if (os.path.isfile(fileName)):
            document = open(fileName)
            categories = self.getCategoriesForText(document)
        else:
            categories = self.getCategoriesForText(text)

        #Obróbka wyniku
        resultCategories = []
        iter = 0
        for c in categories:
            if iter < number_of_categories:
                iter += 1
                if get_similarity:
                    resultCategories.append(c)
                else:
                    resultCategories.append(c[0])
        return resultCategories

    #Pobranie kategorii dla dokumentu
    def getCategoriesForText(self, text):
        vectors = []
        categories = {}

        #Pobranie dwudziestu wektorów dla dokumentu
        for i in range(20):
            vector = self.model.infer_vector(self.preprocessing_function(text))
            vectors.append(vector)

        #Uśrednienie wektorów
        average_infered_vector = np.array(np.mean([v for v in vectors], axis=0))

        #Porównywanie dokumentu z kategoriami
        for c in reuters.categories():
            cvec = self.model.docvecs[c]
            categories[c] = self.cosine_similarity(average_infered_vector, cvec)

        # Posortowanie kategorii po stopniu podobieństwa
        sorted_categories = sorted(categories.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_categories