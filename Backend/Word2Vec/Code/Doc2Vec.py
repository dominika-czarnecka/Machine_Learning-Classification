from Backend.Word2Vec.Code.Doc2VecModel import Doc2VecModel


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
        print("Funkcjonalność nie została jeszcze zaimplementowana")
        raise NotImplementedError

    #Klasyfikacja dokumentu
    def single(self, text, args, name):
        if name:
            #Klasyfikacja dokumentu ze wskazanego pliku
            return self.model.classify(fileName=name, args=args)
        else:
            #Klasyfikacja dokumentu przekazanego jako tekst
            return self.model.classify(text=text, args=args)
