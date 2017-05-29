from Backend.Word2Vec.Code.Doc2Vec import Doc2Vec
from nltk.corpus import reuters

#Inicjalizacja modułu
doc2Vec = Doc2Vec()
sampleDocument = reuters.raw('test/14828')
print(sampleDocument)
#Wytrenowanie nowego modelu na korpusie Reuters
doc2Vec.train(False, "", {"size": 100, "iter": 55, "min-count": 2, "window": 2},"NewModel")

#Wytrenowanie nowego modelu na wskazanym w lokalizacji korpusie (Jeszcze nie gotowe)
#doc2Vec.train(True,"/SomeFileDirectory",{"size": 100, "iter": 55, "min-count": 2},"NewModelName")

#Klasyfikacja dokumentu z pliku
#categories = doc2Vec.single("", {"number-of-categories": 3, "get-similarity": True}, "FileDirectory")
#print(categories)

#Klasyfikacja dokumentu z tekstu
categories = doc2Vec.single(sampleDocument, {"number-of-categories": 5, "get-similarity": True}, name='')
print(categories)
