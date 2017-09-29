from Backend.Word2Vec.Code.Doc2Vec import Doc2Vec
from Backend.Word2Vec.Code.Evaluation import EffectivenessTests
from nltk.corpus import reuters

#Inicjalizacja modułu
doc2Vec = Doc2Vec()
sampleDocument = reuters.raw('test/14828')
#print(sampleDocument)
#Wytrenowanie nowego modelu na korpusie Reuters
doc2Vec.train(False, "", {"size": 100, "iter": 55, "min_count": 6, "window": 1},"NewModelMinCount6")

#Wytrenowanie nowego modelu na wskazanym w lokalizacji korpusie (Jeszcze nie gotowe)
#doc2Vec.train(True,"/SomeFileDirectory",{"size": 100, "iter": 55, "min-count": 2},"NewModelName")

#Klasyfikacja dokumentu z pliku
#categories = doc2Vec.single("", {"number-of-categories": 3, "get-similarity": True}, "FileDirectory")
#print(categories)

#Klasyfikacja dokumentu z tekstu
#categories = doc2Vec.single(sampleDocument, {"number-of-categories": 5, "get-similarity": True}, name='')
#print(categories)
#print(doc2Vec.test(fromFile=False, input="", args={}, name=""))
cat = ['earn', 'acq', 'money-fx', 'grain', 'crude']
#cat = reuters.categories()
#result = doc2Vec.test(fromFile=False,input='',args={"threshold": 0.7, "categories": cat},name='')
#print(result)
t = EffectivenessTests(doc2Vec.model)
print(t.doPresisionRecallAndF1Tests(cat))
"""Window 2, Min-Count 2
Wynik testu 1: 0.5147399801258695
Wynik testu 2: 0.4660483603842332
"""

""""" dla {"size": 100, "iter": 55, "min-count": 5, "window": 1}
Wynik testu 1: 0.7360052997681351
Wynik testu 2: 0.667770785028155
"""
""""{"size": 100, "iter": 55, "min-count": 6, "window": 1}
Wynik testu 1: 0.7535607817158
Wynik testu 2: 0.6863199735011594
"""