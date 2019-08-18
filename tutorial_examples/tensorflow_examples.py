import tensorflow as tf
import numpy as np

X_train = np.arange(10).reshape((10, 1))

class TfLinreg(object):

    def __init__(self, x_dim, learning_rate=0.01, random_seed=None):
        self.x_dim = x_dim
        self.learning_rate = learning_rate
        self.g = tf.Graph()

        with self.g.as_default():
            tf.set_random_seed(random_seed)
            self.build()
            self.init_op = tf.global_variables_initializer()


    def build(self):