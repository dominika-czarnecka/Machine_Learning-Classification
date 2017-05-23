from Backend.Word2Vec.ReutersDoc2VecModel import ReutersDoc2VecModel
from nltk.corpus import stopwords, reuters
import os.path
class Doc2Vec:
    def __init__(self):
        self.model = any

    def train(self,fromFile, input, args, name):
        if fromFile:
            self.model = ReutersDoc2VecModel(args, fname=input)
        else:
            self.model = ReutersDoc2VecModel(args, fname=name)

    def test(self,fromFile, input, args, name):
        print("test")

    def single(self,text, args, name):
        if name:
            text = reuters.raw(name)
        number_of_categories = args["number-of-categories"]
        get_similarity = args["get-similarity"]
        categories = self.model.classify(text = text,number_of_categories = number_of_categories,get_similarity = get_similarity)
        return categories


doc = Doc2Vec()
doc.train(False,"",{"size": 100, "iter": 55, "min-count": 2},"NewModel2")
categories = doc.single("",{"number-of-categories":3, "get-similarity":True},'test/14828')
print(categories)