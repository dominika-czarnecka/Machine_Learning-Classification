from Backend.Word2Vec.Code.Doc2VecModel import Doc2VecModel
from Backend.Word2Vec.Code.PrecisionTests import PrecisionTests

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
            # Trenowanie modelu na dokumentach we wskazanej w input lokalizacji
            print("Funkcjonalność nie została jeszcze zaimplementowana")
            raise NotImplementedError
        else:
            MyTests = PrecisionTests(self.model)
            wynik1 = MyTests.test1()
            wynik2 = MyTests.test2()
            s = str()
            s = "Wynik testu 1: " + str(wynik1) + '\n' + "Wynik testu 2: " + str(wynik2)
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
