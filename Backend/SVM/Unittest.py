from SVM import SVM
from Corpus import Corpus
from ParametersParser import ParametersParser
from unittest import TestCase
import unittest
from DataTransformer import DataTransformer
from ResultDataTransformer import ResultDataTransformer
from nltk.corpus import reuters
from SavedClassifiersManager import SavedClassifiersManager


class TestSVM(TestCase):
    def test_parser(self):
        # missing argument
        args = {
            'c': 0.0,
            'kernel': 'linear',
            'degree': 0,
            'gamma': 'auto',
            'coef0': 0.0,
            'shrinking': True,
            'tol': 0.001,
        }
        with self.assertRaises(ValueError):
            ParametersParser.assert_args(args)

        args['max_iter'] = -1
        ParametersParser.assert_args(args)

        args['gamma'] = -1
        with self.assertRaises(ValueError):
            ParametersParser.assert_args(args)

        args['invalid arg'] = 0
        with self.assertRaises(ValueError):
            ParametersParser.assert_args(args)

    def test_corpus(self):
        with self.assertRaises(ValueError):
            Corpus('some invalid arg')

        corp = Corpus('reuters')
        self.assertEqual(len(corp.train_docs_id), 7769)
        self.assertEqual(len(corp.train_docs), 7769)
        self.assertEqual(len(corp.train_labels), 7769)
        self.assertEqual(len(corp.test_docs_id), 3019)
        self.assertEqual(len(corp.test_docs), 3019)
        self.assertEqual(len(corp.test_labels), 3019)

        #check if indices match
        i = 0
        while i < 7769:
            self.assertEqual(reuters.categories(corp.train_docs_id[i]), corp.train_labels[i])
            self.assertEqual(reuters.raw(corp.train_docs_id[i]), corp.train_docs[i])
            i += 200

    def test_transformer(self):
        trans = DataTransformer()
        self.assertEqual(
            trans.tokenize('ab ab12 abcd,efgh 12345'),
            ['ab12', 'abcd', 'efgh']
        )

    def test_result_transformer(self):
        test_labels = [0, 1, 0, 1]
        prediction = [0, 1, 0, 1]
        f1_weighted, f1_macro, f1_micro = ResultDataTransformer.transform_result_data(test_labels, prediction)
        self.assertEqual(f1_weighted, 1.0)
        self.assertEqual(f1_macro, 1.0)
        self.assertEqual(f1_micro, 1.0)

    def test_classifier(self):

        args = {
            'c': 10000.0,
            'kernel': 'rbf',
            'degree': 2,
            'gamma': 'auto',
            'coef0': 0.5,
            'shrinking': True,
            'tol': 0.0001,
            'max_iter': -1,
        }
        SavedClassifiersManager.delete_all()
        SVM.train(False, 'reuters', args, '')
        # should find the file
        SVM.test(False, 'reuters', args, '')

if __name__ == '__main__':
    unittest.main()
