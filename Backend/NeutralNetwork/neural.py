import p1
import numpy as np
import tensorflow as tf
import random

def NeuralNetworkTraining(gradient=0.5, steps=1500, target="tfidf", vocabulary_len=300, FromFile=False):
    if FromFile == True:
        Xp = np.load("1_train_Xs.npy").tolist()
        yp = np.load("1_train_ys.npy").tolist()
    else:
        p1.target = target
        p1.vocabulary_len = vocabulary_len
        crp = p1.corpus()
        (Xp, yp) = crp.get_svm_vectors(Train=1)

    x = tf.placeholder(tf.float32, [None, vocabulary_len])
    W = tf.Variable(tf.zeros([vocabulary_len, 90]))
    b = tf.Variable(tf.zeros([90]))
    y = tf.matmul(x, W) + b

    y_ = tf.placeholder(tf.float32, [None, 90])

    cross_entropy = tf.reduce_mean(
      tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
    train_step = tf.train.GradientDescentOptimizer(gradient).minimize(cross_entropy)

    #sess = tf.InteractiveSession()
    init = tf.global_variables_initializer()
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    saver = tf.train.Saver()

    if FromFile == True:
        XT = np.load("1_test_Xs.npy").tolist()
        yt = np.load("1_test_ys.npy").tolist()
    else:
        (XT, yt) = crp.get_svm_vectors(Test=1)

    with tf.Session() as sess:
        sess.run(init)
        for i in range(steps):
            batch_x = []
            batch_y = []
            for r in range(100):
                ranInt = random.randint(0, len(Xp) - 1)
                batch_x.append(Xp[ranInt])
                batch_y.append(yp[ranInt])
            if i % 100 == 0:
                acc_tst, loss_tst = sess.run([accuracy, cross_entropy], feed_dict={x: XT, y_: yt})
                print("#{}, Tst acc={} , Tst loss={}".format(i, acc_tst, loss_tst))
            sess.run(train_step, feed_dict={x: batch_x, y_: batch_y})

        print("Train Done")
        result = sess.run(accuracy, feed_dict={x: XT, y_: yt})
        print(result)
        save_path = saver.save(sess, "./models/model_gradient-" + str(gradient)
                               + "_steps-" + str(steps)
                               + "_target-" + target
                               + "_vocabulary_len" + str(vocabulary_len)
                               + ".ckpt")
        print("Zapisano model sieci neuronowych do: %s" % save_path)
        print("Test done")

NeuralNetworkTraining(1,300,"tfidf", 300,True)