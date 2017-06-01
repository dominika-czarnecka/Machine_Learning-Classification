import gensim
from nltk.corpus import reuters




class Doc:
    def __init__(self, text, categories, docid):
        self.docid = docid
        self.text = text
        self.categories = categories

class PrecisionTests:
    def __init__(self, MyModel):
        self.model = MyModel
        self.test_documents = self.getTestDocuments()

    def getTestDocuments(self):
        documents = list()
        for docId in reuters.fileids():
            if docId.startswith("test"):
                text = reuters.raw(docId)
                categories = reuters.categories(docId)
                documents.append(Doc(text,categories, docId))
        return documents

    #TODO zmienić nazwę
    def test1(self):
        """
        Dp - dokumenty sklasyfikowane pozytywnie
        D - wszystkie dokumenty
        CR - kategorie danego dokumentu z korpusu Reuters
        
        test1 = |Dp|/|D|, gdzie |Dp| to moc zbioru takich dokumentów, że najbardziej prawdopodobna 
        kategoria uzyskana z klasyfikacji(doc2vec) danego dokumentu znajduje się w zbiorze CR
        """
        pozytywne = 0
        wszystkie = 0
        for doc in self.test_documents:
            infered_category = self.model.classify(
                args={"number-of-categories": 1, "get-similarity": False},text=doc.text)
            for cat in infered_category:
                if cat in doc.categories:
                    pozytywne += 1
            wszystkie += 1
        return (float(pozytywne)/float(wszystkie))

   #TODO zmienić nazwę
    def test2(self):
        """
        Dp - dokumenty pozytywne
        D - wszystkie dokumenty
        CR - kategorie danego dokumentu z korpusu Reuters
        CC - kategorie, do których został sklasyfikowany dokument
        test2 = |Dp|/|D|, gdzie |Dp| to moc zbioru takich dokumentów, że kategorie CR tego dokumentu są jednocześnie 
        najbardziej prawdopodobnymi katagoriami ze zbioru CC i nie istnieje klasa spoza zbioru CR, która jest
        bardziej prawdopodobna.
        Np. jeżeli mamy dokument z 3 kategoriami, to jeżeli każda z tych trzech znajduje się w zbiorze 3 kategorii z
        klasyfikatora, to zaliczamy jako pozytywny.
        """
        pozytywne = 0
        wszystkie = 0
        for doc in self.test_documents:
            number_of_categories = len(doc.categories)
            infered_categories = self.model.classify(
                args={"number-of-categories": number_of_categories, "get-similarity": False},text=doc.text)
            add_positive=True
            for cat in doc.categories:
                if cat not in infered_categories:
                    #Jeżeli jest choć jedna kategoria wśród kategorii dokumentu, której nie ma
                    # w zbiorze infered_categories, to nie można tago zaliczyć jako test pozytywny.
                    add_positive = False
            if add_positive:
                pozytywne += 1
            wszystkie += 1
        return (float(pozytywne)/float(wszystkie))
