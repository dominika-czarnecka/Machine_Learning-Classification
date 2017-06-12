from Backend.Word2Vec.Code.Doc2VecModel import Doc2VecModel
from Backend.Word2Vec.Code.Evaluation import AccuracyTests

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
            MyTests = AccuracyTests(self.model)
            print("Starting tests...\n")
            wynik1 = 0#MyTests.tolerantTest()
            wynik2 = 0#MyTests.strictTest()
            wynik3 = MyTests.thresholdTest(0.4)
            s = str()
            s = ("Wyniki testów:\n" + "tolerantTest:" + str(wynik1) + '\n' + "strictTest: " + str(wynik2) + '\n'
                 + "thresholdTest:" + str(wynik3))
            return s

        #Wynik testu 1: 0.5147399801258695
        #Wynik testu 2: 0.4660483603842332

        #print("Funkcjonalność nie została jeszcze zaimplementowana")
        #raise NotImplementedError

    #Klasyfikacja dokumentu
    def single(self, text, args, name):
        if name:
            #Klasyfikacja dokumentu ze wskazanego pliku
            return self.model.classify(text = "", fileName=name, args=args)
        else:
            #Klasyfikacja dokumentu przekazanego jako tekst
            return self.model.classify(text=text, args=args)
