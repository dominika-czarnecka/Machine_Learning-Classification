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
        Dp - dokumenty pozytywne
        D - wszystkie dokumenty
        test = |Dp|/|D|, gdzie |Dp| to moc zbioru takich dokumentów, że najbardziej prawdopodobna 
        kategoria z doc2vec dla danego dokumentu znajduje się wśród zbioru jego kategorii
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
        test = |Dp|/|D|, gdzie |Dp| to moc zbioru takich dokumentów, że kategorie tego dokumentu są jednocześnie 
        najbardziej prawdopodobnymi katagoriami, do których został sklasyfikowany i nie istnieje klasa z poza sbioru 
        jego klas, która jest bardziej prawdopodobna.
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
                    #Jeżeli jest choć jedna kategoria wźród kategorii dokumentu, której nie ma
                    # w zbiorze infered_vectors, to nie można tago zaliczyć jako test pozytywny.
                    add_positive = False
            if add_positive:
                pozytywne += 1
            wszystkie += 1
        return (float(pozytywne)/float(wszystkie))
