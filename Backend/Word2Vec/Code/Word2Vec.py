import gensim
import nltk.data
import re
from nltk.corpus import stopwords, reuters
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
import os.path

cachedStopWords = stopwords.words("english")


class ReutersW2VModel:
    def __init__(self, fname = 'w2vClassificator'):
        self.sentences = []
        if(os.path.isfile(fname)):
            self.model =  gensim.models.Word2Vec.load(fname)
            #print(self.model.wv.vocab)

        else:
            #trenujemy model
            self.getTrainSentences()
            #print(self.sentences[5])
            self.model = gensim.models.Word2Vec(self.sentences, min_count=1)
            #print(self.model.wv.vocab)
            self.model.save("../../Bin/Classificators/" + fname)

    def getWordVector(self,word):
        return self.model.wv[word]
    def getTrainSentences(self):
        #test:
        texts = self.getReutersTrainTexts()
        for text in texts:
            sentences = self.doc2sentences(text)
            for s in sentences:
                self.sentences.append(self.tokenize(s))


    def getReutersTrainTexts(self):
        texts = []
        for docid in reuters.fileids():
            if docid.startswith("train"):
                texts.append(reuters.raw(docid))
        return texts

    def doc2sentences(self,text):
        sentences = []
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        s = tokenizer.tokenize(text)
        for sen in s:
            sentences.append(sen)
        return sentences

    def tokenize(self, text):
        min_length = 3
        words = map(lambda word: word.lower(), word_tokenize(text));
        words = [word for word in words if word not in cachedStopWords]
        tokens = (list(map(lambda token: PorterStemmer().stem(token), words)));
        p = re.compile('[a-zA-Z]+');
        filtered_tokens = list(filter(lambda token: p.match(token) and len(token) >= min_length, tokens));
        return filtered_tokens




MyModel = ReutersW2VModel()
vec = MyModel.getWordVector('bag')
print("Vector for \'bag\':")
print(vec)
sim = MyModel.model.similarity('bag', 'pack')
print("Similarity between \'bag\' and \'pack\':")
print(sim)

