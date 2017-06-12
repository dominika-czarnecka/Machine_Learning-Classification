from unittest import TestCase
import NeuralNetwork

class Test(TestCase):

    def test1(self):
        neural = NeuralNetwork.NeuralNetwork()
        self.assertEqual(neural.normalization([0.9, 0.96, 0, 1, 0.2, 0.3]), [0, 1, 0, 1, 0, 0])

    def test1_b(self):
        neural = NeuralNetwork.NeuralNetwork()
        self.assertEqual(neural.normalization([0, 1, 0, 1, 0, 0]), [0, 1, 0, 1, 0, 0])

    def test2(self):
        neural = NeuralNetwork.NeuralNetwork()
        self.assertNotEqual(neural.normalization([0.9, 0.96, 0, 1, 0.2, 0.3]), [0, 1, 1, 1, 0, 0])

    def test3(self):
        neural = NeuralNetwork.NeuralNetwork()
        y =  [[0.9, 0.96, 0, 1, 0.2, 0.3], [0.9, 0.96, 0, 1, 0.2, 0.3], [0.9, 0.96, 0, 1, 0.2, 0.3]]
        y_ = [[0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0]]
        self.assertEqual(neural.correctPrediction_partial(y, y_), 1)

    def test4(self):
        neural = NeuralNetwork.NeuralNetwork()
        args = {"gradient": 1, "steps": 5000, "target": "tfidf", "vocabulary_len": 1500}
        self.assertIsInstance(obj=neural.Test(False, "input", args, "Model2"), cls=float)

    def test5(self):
        neural = NeuralNetwork.NeuralNetwork()
        args = {"gradient": 1, "steps": 5000, "target": "tfidf"}
        with self.assertRaises(Exception):
            neural.Train(False, "input", args, "Model2")

    def test6(self):
        neural = NeuralNetwork.NeuralNetwork()
        args = {"gradient": 1, "steps": 5000, "target": "tfidf"}
        with self.assertRaises(Exception):
            neural.Test(False, "input", args, "Model2")

    def test7(self):
        neural = NeuralNetwork.NeuralNetwork()


