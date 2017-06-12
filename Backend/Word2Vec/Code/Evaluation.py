from nltk.corpus import reuters




class Doc:
    def __init__(self, text, categories, docid):
        self.docid = docid
        self.text = text
        self.categories = categories





class EffectivenessTests:
    def __init__(self, MyModel):
        self.model = MyModel
        self.test_documents = self.getTestDocuments()

    def tolerantAccuracyTest(self):
        """
        Dp - dokumenty sklasyfikowane pozytywnie
        D - wszystkie dokumenty
        CR - kategorie danego dokumentu z korpusu Reuters

        tolerantTest = |Dp|/|D|, gdzie |Dp| to moc zbioru takich dokumentów, że najbardziej prawdopodobna 
        kategoria uzyskana z klasyfikacji(doc2vec) danego dokumentu znajduje się w zbiorze CR
        """
        pozytywne = 0
        wszystkie = 0
        for doc in self.test_documents:
            infered_category = self.model.classify(
                args={"number-of-categories": 1, "get-similarity": False}, text=doc.text)
            for cat in infered_category:
                if cat in doc.categories:
                    pozytywne += 1
            wszystkie += 1
        s = str((float(pozytywne) / float(wszystkie)) * 100.00) + '%'
        return s

    def strictAccuracyTest(self):
        """
        Dp - dokumenty pozytywne
        D - wszystkie dokumenty
        CR - kategorie danego dokumentu z korpusu Reuters
        CC - kategorie, do których został sklasyfikowany dokument
        strictTest = |Dp|/|D|, gdzie |Dp| to moc zbioru takich dokumentów, że kategorie CR tego dokumentu są jednocześnie 
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
                args={"number-of-categories": number_of_categories, "get-similarity": False}, text=doc.text)
            add_positive = True
            for cat in doc.categories:
                if cat not in infered_categories:
                    # Jeżeli jest choć jedna kategoria wśród kategorii dokumentu, której nie ma
                    # w zbiorze infered_categories, to nie można tago zaliczyć jako test pozytywny.
                    add_positive = False
            if add_positive:
                pozytywne += 1
            wszystkie += 1
        s = str((float(pozytywne) / float(wszystkie)) * 100.00) + '%'
        return s

    def thresholdAccuracyTest(self, threshold):
        """
        Dp - dokumenty sklasyfikowane pozytywnie
        D - wszystkie dokumenty
        t - threshold(próg)

        thresholdTest = |Dp|/|D|, gdzie |Dp| to moc zbioru takich dokumentów, że podobieństwo między danym dokumentem,
        a kategorią jest większe od t
        """
        pozytywne = 0
        wszystkie = 0
        for doc in self.test_documents:
            infered_category = self.model.classify(
                args={"number-of-categories": 1, "get-similarity": True}, text=doc.text)
            for cat in infered_category:
                if cat[1] > threshold:
                    pozytywne += 1
            wszystkie += 1
        s = str((float(pozytywne) / float(wszystkie)) * 100.00) + '%'
        return s

    def precision(self, categoryName):
        truePositives = 0
        falsePositives = 0

        for doc in self.test_documents:
            number_of_categories = len(doc.categories)
            infered_categories = self.model.classify(
                args={"number-of-categories": number_of_categories, "get-similarity": False},text=doc.text)
            if categoryName in infered_categories:
                if categoryName in doc.categories:
                    #Jeżeli doc został zaklasyfikowany do danej kategorii i powinien być do niej zaklasyfikowany
                    truePositives += 1
                else:
                    #Jeżeli doc został zaklasyfikowany do danej kategorii, a nie powinien być do niej zaklasyfikowany
                    falsePositives += 1

        s = float((float(truePositives) / float(truePositives + falsePositives)) * 100.00)
        return s

    def recall(self, categoryName):
        truePositives = 0
        relevantItems  = 0 # <- wszystkie dokumenty, które powinny być zaklasyfikowane do danej kategorii
        test_documents = self.getRelevantTestDocuments(categoryName= categoryName)

        for doc in test_documents:
            number_of_categories = len(doc.categories)
            infered_categories = self.model.classify(
                args={"number-of-categories": number_of_categories, "get-similarity": False}, text=doc.text)
            if categoryName in infered_categories:
                #if categoryName in doc.categories: <- zawsze prawdziwe
                # Jeżeli doc został zaklasyfikowany do danej kategorii i powinien być do niej zaklasyfikowany
                truePositives += 1
        relevantItems += 1

        s = float((float(truePositives) / float(relevantItems)) * 100.00)
        return s

    def doPresisionAndRecallTests(self, categories):
        s = "\t\t precision:\t\t recall:\n"
        for cat in categories:
            precision = self.precision(cat)
            recall = self.recall(cat)
            s += str(str(cat) + '\t' + '|' + '\t' + precision + "\t\t" + '|' + '\t' + recall + '\n')
        return s

    def f1(self, categories):
        s = "f1:\n"
        for cat in categories:
            precision = self.precision(cat)
            recall = self.recall(cat)
            s += str(str(cat) + '\t' + "f1 score is: " + 2*(precision*recall)/(precision+recall) + '\n')
        return s

    def getTestDocuments(self):
        documents = list()
        for docId in reuters.fileids():
            if docId.startswith("test"):
                text = reuters.raw(docId)
                categories = reuters.categories(docId)
                documents.append(Doc(text, categories, docId))
        return documents

    def getRelevantTestDocuments(self, categoryName):
        documents = list()
        for docId in reuters.fileids(categoryName):
            if docId.startswith("test"):
                text = reuters.raw(docId)
                categories = reuters.categories(docId)
                documents.append(Doc(text, categories, docId))
        return documents