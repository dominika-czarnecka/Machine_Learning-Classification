#Tutaj umieścić wszystkie testy jednostokowe
from Backend.Word2Vec.Code.Doc2Vec import Doc2Vec
import unittest
from unittest import TestCase

class Doc2VecTests(TestCase):
    def Doc2Vec_Single_Returned3CategoriesWithoutSimilarities(self):
        doc = Doc2Vec()
        doc.train(False, "", {"size": 100, "iter": 55, "min-count": 2}, "NewModel2")
        categories = doc.single("", {"number-of-categories": 3, "get-similarity": True}, 'test/14828')
        self.assertEqual(len(categories), 3)

    def Doc2Vec_Single_ReturnedNot3CategoriesWithoutSimilarities(self):
        doc = Doc2Vec()
        doc.train(False, "", {"size": 100, "iter": 55, "min-count": 2}, "NewModel2")
        categories = doc.single("", {"number-of-categories": 3, "get-similarity": True}, 'test/14828')
        self.assertFalse(len(categories).__eq__(2))


    def runTest(self):
        self.Doc2Vec_Single_Returned3CategoriesWithoutSimilarities()
        self.Doc2Vec_Single_ReturnedNot3CategoriesWithoutSimilarities()







def main():
    suite = unittest.TestSuite()
    suite.addTest(Doc2VecTests())

    runner = unittest.TextTestRunner()
    test_suite = suite
    runner.run(test_suite)

if __name__ == '__main__':
    main()