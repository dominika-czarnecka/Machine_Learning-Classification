import argparse
import sys
import p1
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import tensorflow as tf

FLAGS = None
FromFile = True

def main(_):
  crp = p1.corpus()
  if FromFile == True:
    Xp = np.load("1_train_Xs.npy").tolist()
    yp = np.load("1_train_ys.npy").tolist()
  else:
    (Xp, yp) = crp.get_svm_vectors(Train=1)

  tf.device("/gpu:0")
  x = tf.placeholder(tf.float32, [None, 300])
  W = tf.Variable(tf.zeros([300, 90]))
  b = tf.Variable(tf.zeros([90]))
  y = tf.matmul(x, W) + b

  y_ = tf.placeholder(tf.float32, [None, 90])

  cross_entropy = tf.reduce_mean(
      tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
  train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

  #sess = tf.InteractiveSession()
  init = tf.global_variables_initializer()
  correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
  accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

  if FromFile == True:
    XT = np.load("1_test_Xs.npy").tolist()
    yt = np.load("1_test_ys.npy").tolist()
  else:
    (XT, yt) = crp.get_svm_vectors(Test=1)

  with tf.Session() as sess:
      sess.run(init)

      for i in range(5000):
          if i % 100 == 0:
              acc_tst, loss_tst = sess.run([accuracy, cross_entropy], feed_dict={x: XT, y_: yt})

              print("#{}, Tst acc={} , Tst loss={}".format(i, acc_tst, loss_tst))
          sess.run(train_step, feed_dict={x: Xp, y_: yp})

      print("Train Done")
      print(sess.run(accuracy, feed_dict={x: XT, y_: yt}))
      print("test done")

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--data_dir', type=str, default='/tmp/tensorflow/mnist/input_data',
                      help='Directory for storing input data')
  FLAGS, unparsed = parser.parse_known_args()
tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)