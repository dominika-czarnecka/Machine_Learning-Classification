from Backend.Word2Vec.Code.Doc2VecModel import Doc2VecModel
from Backend.Word2Vec.Code.Evaluation import EffectivenessTests

class Doc2Vec:
    def __init__(self):
        self.model = any

    #Trenowanie modelu
    def train(self, fromFile, input, args, name):
        if fromFile:
            #Trenowanie modelu na dokumentach we wskazanej w input lokalizacji
            print("Funkcjonalność nie została jeszcze zaimplementowana")
            raise NotImplementedError
        else:
            #Trenowanie nowego modelu na dokumentach z korpusu Reutersa i zapisanie go do pliku o wskazanej w name nazwie
            self.model = Doc2VecModel(args, modelFileName=name)

    #Testowanie modelu
    def test(self, fromFile, input, args, name):
        if fromFile:
            # Testowanie modelu na dokumentach we wskazanej w input lokalizacji
            print("Funkcjonalność nie została jeszcze zaimplementowana")
            raise NotImplementedError
        else:
            threshold = args["threshold"]
            categories = args["categories"]
            MyTests = EffectivenessTests(self.model)
            print("Starting tests...\n")
            wynik1 = MyTests.tolerantAccuracyTest()
            print("tolerantTest:" + str(wynik1))
            wynik2 = MyTests.strictAccuracyTest()
            print("strictTest: " + str(wynik2))
            wynik3 = MyTests.thresholdAccuracyTest(threshold)
            print("thresholdTest:" + str(wynik3))
            #wynik4 = MyTests.doPresisionAndRecallTests(reuters.categories)
            wynik4 = MyTests.doPresisionAndRecallTests(categories)

            s = str("Wyniki testów:\n" + "tolerantTest:" + str(wynik1) + '\n' + "strictTest: " + str(wynik2) + '\n'
                 + "thresholdTest:" + str(wynik3) + '\n' + wynik4)
            return s


    #Klasyfikacja dokumentu
    def single(self, text, args, name):
        if name:
            #Klasyfikacja dokumentu ze wskazanego pliku
            return self.model.classify(text = "", fileName=name, args=args)
        else:
            #Klasyfikacja dokumentu przekazanego jako tekst
            return self.model.classify(text=text, args=args)
