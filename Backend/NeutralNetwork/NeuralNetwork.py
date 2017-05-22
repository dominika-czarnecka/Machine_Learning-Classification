import NeuralCorpus
import numpy as np
import tensorflow as tf
import random
import os


# NeuralNetworkTraining(FromFile:bool, Input:string, args:{}, output:string)
# Fromfile==true -> input to nazwa pliku
# Fromfile == false -> input nazwa korpusu
# output -> nazwa pliku - gdzie zapisac model
# args - lista argumentow (gradient,steps...)
#
# NeuralNetworkTesting(FromFile, Input, args:{}, klasyfikator:bin)
#
# Single(Text:string, klasyfikator:bin, args:{})
#
# info_text = "opis param"
#
# //za pomoca exceptions !
# if len(args) != 5:
# 	print info_text
# 	return
#
# Zapis parametorw klasyfiaktora do pliku np .json a nie w folderze

# args {gradient:0.5, steps:1500, target:"tfidf:, vocabulary_len:300}

class NeuralNetwork:
    def normalization(self, tab):
        minimum = tab[0]
        maximum = tab[0]

        for value in tab:
            if value < minimum:
                minimum = value
            if value > maximum:
                maximum = value

        table = [0 for i in range(len(tab))]
        iter = 0

        if minimum < 0:
            for value in tab:
                table[iter] = value + abs(minimum)
                iter += 1
            maximum += abs(minimum)
            minimum = 0
        else:
            table = tab

        norm_tab = [0 for i in range(len(tab))]
        iter = 0

        for value in table:
            if value - minimum == 0 and maximum - minimum == 0:
                norm_tab[iter] = 0
            else:
                if ((value - minimum) / (maximum - minimum)) > 0.95:
                    norm_tab[iter] = 1
                else:
                    norm_tab[iter] = 0
            iter += 1

        return norm_tab

    def correctPrediction_equal(self, y, y_):
        table = [False for i in range(len(y))]

        for i in range(len(y)):
            if self.normalization(y[i]) == self.normalization(y_[i]):
                table[i] = True
        return table

    def correctPrediction_partial(self, yy, yy_):
        positive_sum = 0
        multilabelCount = 0
        multilabelAllCount = 0

        for i in range(len(yy_)):
            doc_positive_count = 0
            doc_cat_count = 0
            isBraked = False
            y_ = self.normalization(yy_[i])
            y = self.normalization(yy[i])
            for j in range(len(y_)):
                if y_[j] == 1 and y[j] == 1:
                    doc_positive_count += 1
                    doc_cat_count += 1
                elif y_[j] == 1 and y[j] == 0:
                    doc_cat_count += 1
                elif y_[j] == 0 and y[j] == 1:
                    isBraked = True
                    # break
            if not isBraked:
                positive_sum += (doc_positive_count / doc_cat_count)
                if doc_cat_count > 1 and doc_positive_count > 1:
                    # print("{} / {}".format(doc_positive_count, doc_cat_count))
                    multilabelCount += 1
                    multilabelAllCount += 1
                elif doc_cat_count > 1:
                    multilabelCount += 1
                    multilabelAllCount += 1
            else:
                if doc_cat_count > 1:
                    multilabelAllCount += 1

        # print("MultiLabel: {} / {}".format(multilabelCount, multilabelAllCount))
        # print("{} / {}".format(positive_sum, len(yy_)))
        return positive_sum / len(yy_)

    def Train(self, FromFile, Input, args, output):
        path = "./models/" + str(output)
        info_text = "FromFile:bool, Input:string, args{gradient: 0-1, steps:int, target:tfidf,entrophy,frequency, vocabulary_len:int}, output:string"
        if len(args) != 4:
            print(info_text)
            return

        gradient = args['gradient']
        steps = args['steps']
        target = args['target']
        vocabulary_len = args['vocabulary_len']

        x = tf.placeholder(tf.float32, [None, vocabulary_len])
        W = tf.Variable(tf.zeros([vocabulary_len, 90]))
        b = tf.Variable(tf.zeros([90]))
        y = tf.matmul(x, W) + b
        y_ = tf.placeholder(tf.float32, [None, 90])

        cross_entropy = tf.reduce_mean(
            tf.nn.sigmoid_cross_entropy_with_logits(labels=y_, logits=y))
        train_step = tf.train.GradientDescentOptimizer(gradient).minimize(cross_entropy)
        saver = tf.train.Saver()

        if FromFile == True:
            # input - nazwa pliku z ktorego wczytujemy
            print("FromFile == True")
            # Xp = np.load("1_train_Xs.npy").tolist()  # input
            # yp = np.load("1_train_ys.npy").tolist()  # input
        else:
            # input - nazwa korpusu
            NeuralCorpus.target = target
            NeuralCorpus.vocabulary_len = vocabulary_len
            crp = NeuralCorpus.corpus()
            (Xp, yp) = crp.get_svm_vectors(Train=1)
            (XT, yt) = crp.get_svm_vectors(Test=1)

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            for i in range(steps):
                batch_x = []
                batch_y = []
                for r in range(100):
                    ranInt = random.randint(0, len(Xp) - 1)
                    batch_x.append(Xp[ranInt])
                    batch_y.append(yp[ranInt])
                if i % 100 == 0:
                    yy, yy2 = sess.run([y, y_], feed_dict={x: XT, y_: yt})
                    print("#{}, Tst acc={}".format(i, self.correctPrediction_partial(yy, yy2)))

                sess.run(train_step, feed_dict={x: batch_x, y_: batch_y})
            print("Train Done")

            # Zapis klasyfikatora
            if not os.path.exists(path):
                os.makedirs(path)
            save_path = saver.save(sess, path + '/model.ckpt')
            print("Model saved to: %s" % save_path)

    def Test(self, FromFile, Input, args, classifier):
        path = "./models/" + str(classifier)
        # classifier - sciezka do klasyfikatora
        target = args['target']
        vocabulary_len = args['vocabulary_len']

        x = tf.placeholder(tf.float32, [None, vocabulary_len])
        W = tf.Variable(tf.zeros([vocabulary_len, 90]))
        b = tf.Variable(tf.zeros([90]))
        y = tf.matmul(x, W) + b
        y_ = tf.placeholder(tf.float32, [None, 90])

        saver = tf.train.Saver()

        if FromFile == True:
            # input - nazwa pliku z ktorego wczytujemy
            print("FromFile == True")
            # XT = np.load("1_test_Xs.npy").tolist()  # input
            # yt = np.load("1_test_ys.npy").tolist()  # input
        else:
          #input - nazwa korpusu kotry wczytujemy
          NeuralCorpus.target = target
          NeuralCorpus.vocabulary_len = vocabulary_len
          crp = NeuralCorpus.corpus()
          (XT, yt) = crp.get_svm_vectors(Test=1)

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            ckpt = tf.train.get_checkpoint_state(path)
            if ckpt and ckpt.model_checkpoint_path:
                saver.restore(sess, ckpt.model_checkpoint_path)
            else:
                print("Klasyfikator nie istnieje")

            yy, yy2 = sess.run([y, y_], feed_dict={x: XT, y_: yt})
            print(self.correctPrediction_partial(yy, yy2))

    def Single(self, Text, classifier, args):
        return



args = {"gradient": 1, "steps": 10000, "target": "tfidf", "vocabulary_len": 1500}

neural = NeuralNetwork()
neural.Train(False,"input",args,"Model2")
# neural.Test(False, "input", args, "Model2")
