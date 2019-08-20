import os
from pathlib import Path

import tensorflow as tf
import tensorflow.contrib.keras as keras
import numpy as np

from utils import load_mnist

cwd = os.getcwd()
cwd = Path(cwd).parent
path = os.path.join(cwd, 'data', 'mnist')

X_train, y_train = load_mnist(path, kind='train')
X_test, y_test = load_mnist(path, kind='t10k')


# center around mean and normalize
mean_vals = np.mean(X_train, axis=0)
std_val = np.std(X_train)

X_train_centered = (X_train - mean_vals)/std_val
X_test_centered = (X_test - mean_vals)/std_val

del X_train, X_test

print('Zeilen: %d, Spalten: %d' %(X_train_centered.shape[0], X_train_centered.shape[1]))
print('Zeilen: %d, Spalten: %d' %(X_test_centered.shape[0], X_train_centered.shape[1]))

np.random.seed(123)
tf.set_random_seed(123)

# convert to one hot
y_train_onehot = keras.utils.to_categorical(y_train)
y_test_onehot = keras.utils.to_categorical(y_test)
